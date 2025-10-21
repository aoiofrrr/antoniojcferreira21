#!/usr/bin/env python3
"""
Growth Hacking Project Manager - Web Application
A Flask-based web interface for managing growth hacking projects.
"""

from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from growth_hacker import GrowthHackingManager
from datetime import datetime
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

# Initialize the manager
manager = GrowthHackingManager()


@app.route('/')
def index():
    """Dashboard showing all projects."""
    projects = manager.list_projects()

    # Calculate statistics
    total_projects = len(projects)
    active_projects = len([p for p in projects if p['status'] == 'active'])
    completed_projects = len([p for p in projects if p['status'] == 'completed'])

    stats = {
        'total': total_projects,
        'active': active_projects,
        'completed': completed_projects,
        'paused': total_projects - active_projects - completed_projects
    }

    return render_template('index.html', projects=projects, stats=stats)


@app.route('/project/create', methods=['GET', 'POST'])
def create_project():
    """Create a new project."""
    if request.method == 'POST':
        name = request.form.get('name')
        description = request.form.get('description', '')
        goal = request.form.get('goal', '')
        target_metric = request.form.get('target_metric', '')
        target_value = float(request.form.get('target_value', 0) or 0)

        project_id = manager.create_project(
            name=name,
            description=description,
            goal=goal,
            target_metric=target_metric,
            target_value=target_value
        )

        flash(f'Project "{name}" created successfully!', 'success')
        return redirect(url_for('view_project', project_id=project_id))

    return render_template('create_project.html')


@app.route('/project/<project_id>')
def view_project(project_id):
    """View project details."""
    project = manager.get_project(project_id)

    if not project:
        flash('Project not found', 'error')
        return redirect(url_for('index'))

    # Get unique metric names for the dropdown
    metric_names = list(set(m['name'] for m in project['metrics']))

    # Calculate growth for each metric
    growth_data = {}
    for metric_name in metric_names:
        growth = manager.calculate_growth(project_id, metric_name)
        if growth:
            growth_data[metric_name] = growth

    return render_template('view_project.html',
                         project=project,
                         metric_names=metric_names,
                         growth_data=growth_data)


@app.route('/project/<project_id>/edit', methods=['GET', 'POST'])
def edit_project(project_id):
    """Edit project details."""
    project = manager.get_project(project_id)

    if not project:
        flash('Project not found', 'error')
        return redirect(url_for('index'))

    if request.method == 'POST':
        name = request.form.get('name')
        description = request.form.get('description')
        goal = request.form.get('goal')
        status = request.form.get('status')
        target_metric = request.form.get('target_metric')
        target_value = request.form.get('target_value')

        if target_value:
            target_value = float(target_value)

        manager.update_project(
            project_id,
            name=name,
            description=description,
            goal=goal,
            status=status,
            target_metric=target_metric,
            target_value=target_value
        )

        flash('Project updated successfully!', 'success')
        return redirect(url_for('view_project', project_id=project_id))

    return render_template('edit_project.html', project=project)


@app.route('/project/<project_id>/delete', methods=['POST'])
def delete_project(project_id):
    """Delete a project."""
    success = manager.delete_project(project_id)

    if success:
        flash('Project deleted successfully', 'success')
    else:
        flash('Project not found', 'error')

    return redirect(url_for('index'))


@app.route('/project/<project_id>/add-metric', methods=['POST'])
def add_metric(project_id):
    """Add a metric to a project."""
    metric_name = request.form.get('metric_name')
    value = float(request.form.get('value'))
    note = request.form.get('note', '')
    date = request.form.get('date')

    if not date:
        date = None

    success = manager.add_metric(project_id, metric_name, value, date, note)

    if success:
        flash(f'Metric "{metric_name}" added successfully!', 'success')
    else:
        flash('Failed to add metric', 'error')

    return redirect(url_for('view_project', project_id=project_id))


@app.route('/project/<project_id>/add-note', methods=['POST'])
def add_note(project_id):
    """Add a note to a project."""
    note = request.form.get('note')

    success = manager.add_note(project_id, note)

    if success:
        flash('Note added successfully!', 'success')
    else:
        flash('Failed to add note', 'error')

    return redirect(url_for('view_project', project_id=project_id))


@app.route('/api/project/<project_id>/metrics/<metric_name>')
def get_metric_data(project_id, metric_name):
    """API endpoint to get metric data for charts."""
    metrics = manager.get_metrics(project_id, metric_name)

    data = {
        'labels': [m['date'][:10] for m in metrics],
        'values': [m['value'] for m in metrics],
        'notes': [m.get('note', '') for m in metrics]
    }

    return jsonify(data)


@app.route('/filter/<status>')
def filter_by_status(status):
    """Filter projects by status."""
    if status == 'all':
        projects = manager.list_projects()
    else:
        projects = manager.list_projects(status=status)

    # Calculate statistics
    all_projects = manager.list_projects()
    total_projects = len(all_projects)
    active_projects = len([p for p in all_projects if p['status'] == 'active'])
    completed_projects = len([p for p in all_projects if p['status'] == 'completed'])

    stats = {
        'total': total_projects,
        'active': active_projects,
        'completed': completed_projects,
        'paused': total_projects - active_projects - completed_projects
    }

    return render_template('index.html', projects=projects, stats=stats, filter=status)


if __name__ == '__main__':
    print("\n" + "="*60)
    print("🚀 Growth Hacking Project Manager - Web Interface")
    print("="*60)
    print("\n📊 Starting server...")
    print("🌐 Open your browser and go to: http://localhost:5000")
    print("\n💡 Press CTRL+C to stop the server\n")
    app.run(debug=True, host='0.0.0.0', port=5000)
