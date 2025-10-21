# Growth Hacking Manager - Web Version Guide

A beautiful, modern web interface for managing your growth hacking projects.

## Quick Start

### Option 1: Using the Start Script (Easiest)

```bash
./start_web.sh
```

Then open your browser to: **http://localhost:5000**

### Option 2: Manual Start

```bash
# Install dependencies
pip3 install -r requirements.txt

# Start the server
python3 web_app.py
```

Then open your browser to: **http://localhost:5000**

## Features

### Dashboard
- **Overview Statistics**: See total, active, paused, and completed projects at a glance
- **Project Cards**: Visual cards showing all your projects with status badges
- **Filtering**: Filter projects by status (all, active, paused, completed)
- **Quick Actions**: Create, edit, view projects with one click

### Project Management
- **Create Projects**: Easy-to-use forms with example suggestions
- **Edit Projects**: Update any project detail including status
- **View Details**: Comprehensive project view with all information
- **Delete Projects**: Remove projects you no longer need

### Metrics Tracking
- **Add Metrics**: Quick form to add metric data points
- **Multiple Metrics**: Track unlimited metrics per project
- **Historical Data**: View all metrics with dates and notes
- **Visual Charts**: Interactive line charts powered by Chart.js
- **Growth Calculations**: Automatic growth rate calculations

### Visualizations
- **Interactive Charts**: View metrics trends over time
- **Growth Analysis**: See start/end values, growth rate, and absolute growth
- **Metric Tables**: Tabular view of all historical data
- **Notes Timeline**: Track important observations and changes

## Using the Web Interface

### Creating Your First Project

1. Click **"+ New Project"** in the navigation bar
2. Fill in the form:
   - **Name**: e.g., "Email Campaign A/B Test"
   - **Description**: What this project is about
   - **Goal**: What you want to achieve
   - **Target Metric**: The metric you're tracking (e.g., "conversion_rate")
   - **Target Value**: Your goal number (e.g., 0.05 for 5%)
3. Click **"Create Project"**

### Adding Metrics

1. Open a project by clicking on it
2. In the **"Add Metric"** section:
   - **Metric Name**: Choose from existing or create new (e.g., "users", "revenue")
   - **Value**: The numeric value
   - **Note** (optional): Context about this data point
   - **Date** (optional): Defaults to today
3. Click **"Add Metric"**

The chart will automatically update to show your new data point!

### Viewing Growth

Growth is calculated automatically when you have 2+ data points for a metric:
- **Start Value**: First recorded value
- **Current Value**: Most recent value
- **Growth Rate**: Percentage change
- **Absolute Growth**: Numeric change

### Adding Notes

Document insights, changes, or observations:
1. Open a project
2. In the **"Add Note"** section, type your note
3. Click **"Add Note"**

Notes appear with timestamps on the project page.

### Updating Project Status

1. Click **"Edit Project"**
2. Change the **Status** dropdown:
   - **Active**: Currently running
   - **Paused**: Temporarily stopped
   - **Completed**: Finished
3. Click **"Save Changes"**

## Real-World Workflow Examples

### Example 1: A/B Testing Campaign

**Day 1: Create Project**
```
Name: Homepage CTA Button Test
Description: Testing Blue vs Orange button
Goal: Increase signup rate to 5%
Target: signup_rate = 0.05
```

**Day 1-7: Track Metrics**
- Add baseline: `signup_rate = 0.032` (Blue variant)
- Add test result: `signup_rate = 0.047` (Orange variant)
- Add final: `signup_rate = 0.051` (Orange winner)

**View Results**
- Chart shows upward trend
- Growth analysis shows 59% improvement
- Update status to "Completed"

### Example 2: Product Launch

**Week 1: Setup**
```
Name: Q4 Premium Tier Launch
Description: New premium subscription offering
Goal: Get 500 premium subscribers
Target: premium_users = 500
```

**Weekly Tracking**
- Week 1: Add `premium_users = 45` and `revenue = 4500`
- Week 2: Add `premium_users = 120` and `revenue = 12000`
- Week 3: Add `premium_users = 280` and `revenue = 28000`
- Week 4: Add `premium_users = 520` and `revenue = 52000`

**Monitor Progress**
- Use the chart selector to switch between metrics
- View growth rate for each metric
- Add notes when you make changes or observations

### Example 3: SEO Campaign

**Month 1: Create & Start**
```
Name: SEO Content Strategy 2025
Description: Publish optimized blog content
Goal: 200% increase in organic traffic
Target: organic_sessions = 15000
```

**Monthly Tracking**
```
Month 1: organic_sessions = 5000 (baseline)
Month 2: organic_sessions = 6500 (10 posts)
Month 3: organic_sessions = 9200 (25 posts)
Month 4: organic_sessions = 13500 (40 posts)
```

**Notes to Add**
- "Published 'Ultimate Guide to X' - best performer"
- "Long-tail keywords showing best ROI"
- "Increased publishing frequency to 3x/week"

## Tips for Best Results

### 1. Consistent Naming
Use the same metric names across projects:
- ✅ `conversion_rate`, `users`, `revenue`
- ❌ `conv rate`, `Users`, `REVENUE`

### 2. Regular Updates
Add metrics on a consistent schedule:
- Daily for fast-moving experiments
- Weekly for standard campaigns
- Monthly for long-term initiatives

### 3. Add Context with Notes
Always document:
- When you make changes
- Unexpected spikes or drops
- External factors (holidays, marketing campaigns)

### 4. Use Multiple Metrics
Don't just track vanity metrics:
- Track both volume AND quality
- Example: `signups` + `activated_users` + `revenue`

### 5. Archive Completed Projects
Mark projects as "Completed" when done:
- Keeps dashboard focused
- Can still view historical data
- Easy to filter and find

## Keyboard Shortcuts

- Click project name to view details
- Filter buttons at top of dashboard
- Forms auto-suggest existing metric names

## Customization

### Change Port
Edit `web_app.py`, line at the bottom:
```python
app.run(debug=True, host='0.0.0.0', port=5000)  # Change 5000 to your port
```

### Change Data File Location
Edit `web_app.py`, near the top:
```python
manager = GrowthHackingManager('/custom/path/to/data.json')
```

## Troubleshooting

### Port Already in Use
If port 5000 is taken:
```bash
# Find and kill process using port 5000
lsof -ti:5000 | xargs kill -9

# Or change port in web_app.py
```

### Flask Not Installed
```bash
pip3 install -r requirements.txt
```

### Can't Access from Another Device
The server runs on `0.0.0.0`, so you can access it from other devices on your network:
```
http://YOUR_IP_ADDRESS:5000
```

### Charts Not Showing
Make sure you have internet connection - Chart.js loads from CDN.

## Data Sharing with CLI

The web app uses the same data file as the CLI tool (`~/.growth_hacking_projects.json`), so:
- ✅ Create in web, view in CLI
- ✅ Create in CLI, view in web
- ✅ Switch between interfaces anytime

## Browser Compatibility

Works best in modern browsers:
- Chrome/Edge (recommended)
- Firefox
- Safari
- Opera

## Mobile Support

The interface is responsive and works on:
- Tablets (great experience)
- Phones (functional, best for viewing)

For data entry, desktop is recommended.

## Performance

- Handles hundreds of projects easily
- Charts render instantly
- No database required
- All data stored locally in JSON

## Security

⚠️ **Important**: This is designed for local use:
- Don't expose to public internet without authentication
- Runs on localhost by default
- No built-in user authentication

For production use, add:
- Authentication layer
- HTTPS
- Rate limiting
- Input validation

## Next Steps

Ready to grow? Start tracking your experiments:

1. **Launch the app**: `./start_web.sh`
2. **Create your first project**
3. **Add some metrics**
4. **Watch your growth**

Happy hacking! 🚀
