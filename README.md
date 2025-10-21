# Growth Hacking Project Manager

A powerful tool to manage and track your growth hacking projects, experiments, and metrics.

**Available in two interfaces:**
- **Web Interface**: Beautiful browser-based dashboard with charts and visualizations
- **CLI Tool**: Command-line interface for terminal power users

## Features

- **Project Management**: Create, update, and organize growth hacking projects
- **Metrics Tracking**: Track multiple metrics over time (users, conversions, revenue, etc.)
- **Growth Analysis**: Calculate growth rates and trends automatically
- **Goal Setting**: Set targets and track progress
- **Notes**: Document insights and changes
- **Status Management**: Organize projects by status (active, paused, completed)

## Quick Start

### Web Interface (Recommended)

```bash
# Start the web server
./start_web.sh

# Then open your browser to:
# http://localhost:5000
```

**Features:**
- Interactive dashboard with statistics
- Visual charts and graphs
- Easy-to-use forms
- Real-time growth calculations
- No commands to memorize

See [WEB_GUIDE.md](WEB_GUIDE.md) for detailed web interface documentation.

### CLI Tool

```bash
# Make the script executable
chmod +x growth_hacker.py

# Create your first project
./growth_hacker.py create "My First Growth Project" \
  -d "Testing a new marketing channel" \
  -g "Acquire 1000 new users" \
  -m "users" \
  -v 1000

# List all projects
./growth_hacker.py list

# Add metrics
./growth_hacker.py add-metric 1 users 250 -n "Week 1"
./growth_hacker.py add-metric 1 users 520 -n "Week 2"

# Calculate growth
./growth_hacker.py growth 1 users

# View project details
./growth_hacker.py view 1
```

## Commands Overview

| Command | Description |
|---------|-------------|
| `create` | Create a new project |
| `list` | List all projects |
| `view` | View project details |
| `update` | Update project information |
| `delete` | Delete a project |
| `add-metric` | Add a metric data point |
| `metrics` | View project metrics |
| `growth` | Calculate growth rate |
| `add-note` | Add a note to a project |

## Documentation

- **[WEB_GUIDE.md](WEB_GUIDE.md)** - Complete web interface guide with screenshots and workflows
- **[USAGE.md](USAGE.md)** - CLI tool documentation, examples, and best practices

## Use Cases

- **A/B Testing**: Track experiment variants and results
- **Product Launches**: Monitor adoption and key metrics
- **Marketing Campaigns**: Measure campaign performance over time
- **SEO Projects**: Track organic traffic growth
- **Referral Programs**: Monitor viral growth and K-factors
- **Feature Rollouts**: Track activation and engagement metrics

## Data Storage

All data is stored locally in `~/.growth_hacking_projects.json` in JSON format.

## Requirements

- Python 3.6+
- Flask 3.0+ (for web interface only)
- CLI tool has no external dependencies

## Examples

### Track a Viral Referral Campaign

```bash
./growth_hacker.py create "Referral Program v2" \
  -d "Give $10, Get $10 campaign" \
  -g "Generate 2000 referrals" \
  -m "referrals" -v 2000

./growth_hacker.py add-metric 1 referrals 156 -n "Day 1"
./growth_hacker.py add-metric 1 referrals 425 -n "Day 3"
./growth_hacker.py add-metric 1 referrals 890 -n "Day 7"

./growth_hacker.py growth 1 referrals
```

### Monitor Product Launch

```bash
./growth_hacker.py create "Q4 Product Launch" \
  -d "Premium tier rollout" \
  -m "premium_users" -v 500

./growth_hacker.py add-metric 1 premium_users 45
./growth_hacker.py add-metric 1 revenue 4500
./growth_hacker.py add-metric 1 churn_rate 0.02

./growth_hacker.py view 1
```

## Author

António Ferreira

## License

MIT
