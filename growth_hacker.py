#!/usr/bin/env python3
"""
Growth Hacking Project Manager
A CLI tool to manage and track growth hacking projects, experiments, and metrics.
"""

import json
import os
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional
import argparse


class GrowthHackingManager:
    """Manages growth hacking projects and their metrics."""

    def __init__(self, data_file: str = None):
        """Initialize the manager with a data file."""
        if data_file is None:
            data_file = os.path.expanduser("~/.growth_hacking_projects.json")
        self.data_file = data_file
        self.data = self._load_data()

    def _load_data(self) -> Dict:
        """Load data from JSON file."""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r') as f:
                    return json.load(f)
            except json.JSONDecodeError:
                print(f"Warning: Could not parse {self.data_file}. Starting fresh.")
                return {"projects": {}, "next_id": 1}
        return {"projects": {}, "next_id": 1}

    def _save_data(self):
        """Save data to JSON file."""
        os.makedirs(os.path.dirname(self.data_file), exist_ok=True)
        with open(self.data_file, 'w') as f:
            json.dump(self.data, f, indent=2)

    def create_project(self, name: str, description: str = "", goal: str = "",
                      target_metric: str = "", target_value: float = 0) -> int:
        """Create a new growth hacking project."""
        project_id = str(self.data["next_id"])
        self.data["next_id"] += 1

        project = {
            "id": project_id,
            "name": name,
            "description": description,
            "goal": goal,
            "target_metric": target_metric,
            "target_value": target_value,
            "status": "active",
            "created_at": datetime.now().isoformat(),
            "updated_at": datetime.now().isoformat(),
            "metrics": [],
            "notes": []
        }

        self.data["projects"][project_id] = project
        self._save_data()
        return int(project_id)

    def list_projects(self, status: Optional[str] = None) -> List[Dict]:
        """List all projects, optionally filtered by status."""
        projects = list(self.data["projects"].values())
        if status:
            projects = [p for p in projects if p["status"] == status]
        return sorted(projects, key=lambda x: x["created_at"], reverse=True)

    def get_project(self, project_id: str) -> Optional[Dict]:
        """Get a specific project by ID."""
        return self.data["projects"].get(project_id)

    def update_project(self, project_id: str, **kwargs) -> bool:
        """Update project fields."""
        if project_id not in self.data["projects"]:
            return False

        project = self.data["projects"][project_id]
        allowed_fields = ["name", "description", "goal", "status",
                         "target_metric", "target_value"]

        for key, value in kwargs.items():
            if key in allowed_fields and value is not None:
                project[key] = value

        project["updated_at"] = datetime.now().isoformat()
        self._save_data()
        return True

    def delete_project(self, project_id: str) -> bool:
        """Delete a project."""
        if project_id in self.data["projects"]:
            del self.data["projects"][project_id]
            self._save_data()
            return True
        return False

    def add_metric(self, project_id: str, metric_name: str, value: float,
                   date: str = None, note: str = "") -> bool:
        """Add a metric data point to a project."""
        if project_id not in self.data["projects"]:
            return False

        if date is None:
            date = datetime.now().isoformat()

        metric = {
            "name": metric_name,
            "value": value,
            "date": date,
            "note": note
        }

        self.data["projects"][project_id]["metrics"].append(metric)
        self.data["projects"][project_id]["updated_at"] = datetime.now().isoformat()
        self._save_data()
        return True

    def add_note(self, project_id: str, note: str) -> bool:
        """Add a note to a project."""
        if project_id not in self.data["projects"]:
            return False

        note_entry = {
            "note": note,
            "date": datetime.now().isoformat()
        }

        self.data["projects"][project_id]["notes"].append(note_entry)
        self.data["projects"][project_id]["updated_at"] = datetime.now().isoformat()
        self._save_data()
        return True

    def get_metrics(self, project_id: str, metric_name: Optional[str] = None) -> List[Dict]:
        """Get metrics for a project, optionally filtered by metric name."""
        if project_id not in self.data["projects"]:
            return []

        metrics = self.data["projects"][project_id]["metrics"]
        if metric_name:
            metrics = [m for m in metrics if m["name"] == metric_name]

        return sorted(metrics, key=lambda x: x["date"])

    def calculate_growth(self, project_id: str, metric_name: str) -> Optional[Dict]:
        """Calculate growth rate for a specific metric."""
        metrics = self.get_metrics(project_id, metric_name)

        if len(metrics) < 2:
            return None

        first = metrics[0]
        last = metrics[-1]

        if first["value"] == 0:
            return None

        growth_rate = ((last["value"] - first["value"]) / first["value"]) * 100
        absolute_growth = last["value"] - first["value"]

        return {
            "metric_name": metric_name,
            "start_value": first["value"],
            "end_value": last["value"],
            "absolute_growth": absolute_growth,
            "growth_rate": growth_rate,
            "start_date": first["date"],
            "end_date": last["date"]
        }


def format_project(project: Dict, detailed: bool = False) -> str:
    """Format project for display."""
    status_emoji = {
        "active": "🚀",
        "paused": "⏸️",
        "completed": "✅"
    }

    emoji = status_emoji.get(project["status"], "📊")
    output = [f"{emoji} [{project['id']}] {project['name']} ({project['status']})"]

    if detailed:
        output.append(f"  Description: {project['description']}")
        output.append(f"  Goal: {project['goal']}")

        if project['target_metric'] and project['target_value']:
            output.append(f"  Target: {project['target_metric']} = {project['target_value']}")

        output.append(f"  Created: {project['created_at'][:10]}")
        output.append(f"  Updated: {project['updated_at'][:10]}")

        if project['metrics']:
            output.append(f"  Metrics tracked: {len(project['metrics'])} data points")

            # Show unique metric names
            metric_names = set(m['name'] for m in project['metrics'])
            output.append(f"  Metric types: {', '.join(metric_names)}")

        if project['notes']:
            output.append(f"  Notes: {len(project['notes'])} notes")
    else:
        if project['description']:
            desc = project['description'][:60] + "..." if len(project['description']) > 60 else project['description']
            output.append(f"  {desc}")

    return "\n".join(output)


def main():
    """Main CLI interface."""
    parser = argparse.ArgumentParser(
        description="Growth Hacking Project Manager - Track your experiments and metrics",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    subparsers = parser.add_subparsers(dest="command", help="Commands")

    # Create project
    create_parser = subparsers.add_parser("create", help="Create a new project")
    create_parser.add_argument("name", help="Project name")
    create_parser.add_argument("-d", "--description", default="", help="Project description")
    create_parser.add_argument("-g", "--goal", default="", help="Project goal")
    create_parser.add_argument("-m", "--target-metric", default="", help="Target metric name")
    create_parser.add_argument("-v", "--target-value", type=float, default=0, help="Target metric value")

    # List projects
    list_parser = subparsers.add_parser("list", help="List all projects")
    list_parser.add_argument("-s", "--status", choices=["active", "paused", "completed"],
                            help="Filter by status")

    # View project
    view_parser = subparsers.add_parser("view", help="View project details")
    view_parser.add_argument("project_id", help="Project ID")

    # Update project
    update_parser = subparsers.add_parser("update", help="Update project")
    update_parser.add_argument("project_id", help="Project ID")
    update_parser.add_argument("-n", "--name", help="New name")
    update_parser.add_argument("-d", "--description", help="New description")
    update_parser.add_argument("-g", "--goal", help="New goal")
    update_parser.add_argument("-s", "--status", choices=["active", "paused", "completed"],
                              help="New status")
    update_parser.add_argument("-m", "--target-metric", help="Target metric name")
    update_parser.add_argument("-v", "--target-value", type=float, help="Target metric value")

    # Delete project
    delete_parser = subparsers.add_parser("delete", help="Delete a project")
    delete_parser.add_argument("project_id", help="Project ID")
    delete_parser.add_argument("-y", "--yes", action="store_true", help="Skip confirmation")

    # Add metric
    metric_parser = subparsers.add_parser("add-metric", help="Add a metric data point")
    metric_parser.add_argument("project_id", help="Project ID")
    metric_parser.add_argument("metric_name", help="Metric name (e.g., users, conversions, revenue)")
    metric_parser.add_argument("value", type=float, help="Metric value")
    metric_parser.add_argument("-n", "--note", default="", help="Optional note")
    metric_parser.add_argument("-d", "--date", help="Date (ISO format, default: now)")

    # Add note
    note_parser = subparsers.add_parser("add-note", help="Add a note to a project")
    note_parser.add_argument("project_id", help="Project ID")
    note_parser.add_argument("note", help="Note text")

    # View metrics
    metrics_parser = subparsers.add_parser("metrics", help="View project metrics")
    metrics_parser.add_argument("project_id", help="Project ID")
    metrics_parser.add_argument("-m", "--metric-name", help="Filter by metric name")

    # Calculate growth
    growth_parser = subparsers.add_parser("growth", help="Calculate growth rate")
    growth_parser.add_argument("project_id", help="Project ID")
    growth_parser.add_argument("metric_name", help="Metric name")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return

    manager = GrowthHackingManager()

    # Execute commands
    if args.command == "create":
        project_id = manager.create_project(
            name=args.name,
            description=args.description,
            goal=args.goal,
            target_metric=args.target_metric,
            target_value=args.target_value
        )
        print(f"✅ Created project #{project_id}: {args.name}")

    elif args.command == "list":
        projects = manager.list_projects(status=args.status)
        if not projects:
            print("No projects found.")
        else:
            print(f"\n📊 Growth Hacking Projects ({len(projects)}):\n")
            for project in projects:
                print(format_project(project))
                print()

    elif args.command == "view":
        project = manager.get_project(args.project_id)
        if not project:
            print(f"❌ Project #{args.project_id} not found.")
            sys.exit(1)

        print(f"\n{format_project(project, detailed=True)}\n")

        # Show recent metrics
        if project['metrics']:
            print("📈 Recent Metrics:")
            recent = project['metrics'][-5:]
            for m in recent:
                date = m['date'][:10]
                note = f" - {m['note']}" if m['note'] else ""
                print(f"  {date}: {m['name']} = {m['value']}{note}")
            print()

        # Show recent notes
        if project['notes']:
            print("📝 Recent Notes:")
            recent_notes = project['notes'][-3:]
            for n in recent_notes:
                date = n['date'][:10]
                print(f"  {date}: {n['note']}")
            print()

    elif args.command == "update":
        success = manager.update_project(
            args.project_id,
            name=args.name,
            description=args.description,
            goal=args.goal,
            status=args.status,
            target_metric=args.target_metric,
            target_value=args.target_value
        )
        if success:
            print(f"✅ Updated project #{args.project_id}")
        else:
            print(f"❌ Project #{args.project_id} not found.")
            sys.exit(1)

    elif args.command == "delete":
        if not args.yes:
            confirm = input(f"Delete project #{args.project_id}? (y/n): ")
            if confirm.lower() != 'y':
                print("Cancelled.")
                return

        success = manager.delete_project(args.project_id)
        if success:
            print(f"✅ Deleted project #{args.project_id}")
        else:
            print(f"❌ Project #{args.project_id} not found.")
            sys.exit(1)

    elif args.command == "add-metric":
        success = manager.add_metric(
            args.project_id,
            args.metric_name,
            args.value,
            date=args.date,
            note=args.note
        )
        if success:
            print(f"✅ Added metric to project #{args.project_id}: {args.metric_name} = {args.value}")
        else:
            print(f"❌ Project #{args.project_id} not found.")
            sys.exit(1)

    elif args.command == "add-note":
        success = manager.add_note(args.project_id, args.note)
        if success:
            print(f"✅ Added note to project #{args.project_id}")
        else:
            print(f"❌ Project #{args.project_id} not found.")
            sys.exit(1)

    elif args.command == "metrics":
        metrics = manager.get_metrics(args.project_id, args.metric_name)
        if not metrics:
            print(f"No metrics found for project #{args.project_id}")
            sys.exit(1)

        print(f"\n📈 Metrics for Project #{args.project_id}:\n")
        for m in metrics:
            date = m['date'][:10]
            note = f" - {m['note']}" if m['note'] else ""
            print(f"  {date}: {m['name']} = {m['value']}{note}")
        print()

    elif args.command == "growth":
        growth = manager.calculate_growth(args.project_id, args.metric_name)
        if not growth:
            print(f"❌ Cannot calculate growth. Need at least 2 data points for {args.metric_name}")
            sys.exit(1)

        print(f"\n📈 Growth Analysis for {growth['metric_name']}:\n")
        print(f"  Start: {growth['start_value']} ({growth['start_date'][:10]})")
        print(f"  End: {growth['end_value']} ({growth['end_date'][:10]})")
        print(f"  Absolute Growth: {growth['absolute_growth']:+.2f}")
        print(f"  Growth Rate: {growth['growth_rate']:+.2f}%")
        print()


if __name__ == "__main__":
    main()
