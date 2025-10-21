# Growth Hacking Project Manager - Usage Guide

A powerful CLI tool to manage and track your growth hacking projects, experiments, and metrics.

## Installation

1. Make the script executable:
```bash
chmod +x growth_hacker.py
```

2. (Optional) Create an alias for easier access:
```bash
# Add to your ~/.bashrc or ~/.zshrc
alias ghpm='python3 /path/to/growth_hacker.py'
```

## Quick Start

### Create Your First Project

```bash
./growth_hacker.py create "Email Campaign A/B Test" \
  -d "Testing subject line variations" \
  -g "Increase email open rate by 20%" \
  -m "open_rate" \
  -v 0.35
```

### List All Projects

```bash
./growth_hacker.py list
```

Filter by status:
```bash
./growth_hacker.py list --status active
./growth_hacker.py list --status completed
```

### View Project Details

```bash
./growth_hacker.py view 1
```

## Core Commands

### Project Management

#### Create a Project
```bash
./growth_hacker.py create "Project Name" [OPTIONS]

Options:
  -d, --description TEXT      Project description
  -g, --goal TEXT            Project goal
  -m, --target-metric TEXT   Target metric name (e.g., conversions, users)
  -v, --target-value FLOAT   Target metric value
```

**Example:**
```bash
./growth_hacker.py create "Referral Program Launch" \
  -d "Implement viral referral system" \
  -g "Get 1000 referrals in 30 days" \
  -m "referrals" \
  -v 1000
```

#### Update a Project
```bash
./growth_hacker.py update PROJECT_ID [OPTIONS]

Options:
  -n, --name TEXT              New name
  -d, --description TEXT       New description
  -g, --goal TEXT             New goal
  -s, --status {active|paused|completed}
  -m, --target-metric TEXT    Target metric name
  -v, --target-value FLOAT    Target metric value
```

**Example:**
```bash
./growth_hacker.py update 1 --status completed
./growth_hacker.py update 2 --target-value 2000
```

#### Delete a Project
```bash
./growth_hacker.py delete PROJECT_ID [-y]

Options:
  -y, --yes    Skip confirmation prompt
```

### Metrics Tracking

#### Add a Metric Data Point
```bash
./growth_hacker.py add-metric PROJECT_ID METRIC_NAME VALUE [OPTIONS]

Options:
  -n, --note TEXT    Optional note about this data point
  -d, --date TEXT    Date in ISO format (default: now)
```

**Examples:**
```bash
# Track daily active users
./growth_hacker.py add-metric 1 users 1250 -n "After feature launch"

# Track conversion rate
./growth_hacker.py add-metric 1 conversion_rate 0.034

# Add historical data
./growth_hacker.py add-metric 1 revenue 5420.50 -d "2025-10-15T00:00:00"

# Track with context
./growth_hacker.py add-metric 2 email_opens 450 -n "Monday morning send"
```

#### View Metrics
```bash
./growth_hacker.py metrics PROJECT_ID [OPTIONS]

Options:
  -m, --metric-name TEXT    Filter by specific metric
```

**Examples:**
```bash
# View all metrics for a project
./growth_hacker.py metrics 1

# View only conversion metrics
./growth_hacker.py metrics 1 --metric-name conversion_rate
```

#### Calculate Growth Rate
```bash
./growth_hacker.py growth PROJECT_ID METRIC_NAME
```

**Example:**
```bash
./growth_hacker.py growth 1 users
```

Output:
```
Growth Analysis for users:

  Start: 1000 (2025-10-01)
  End: 1250 (2025-10-15)
  Absolute Growth: +250.00
  Growth Rate: +25.00%
```

### Notes

#### Add a Note
```bash
./growth_hacker.py add-note PROJECT_ID "Your note text"
```

**Examples:**
```bash
./growth_hacker.py add-note 1 "Changed landing page copy"
./growth_hacker.py add-note 2 "Experiment paused due to holiday season"
./growth_hacker.py add-note 3 "Best performing variant was Option B"
```

## Real-World Examples

### Example 1: A/B Testing Campaign

```bash
# Create project
./growth_hacker.py create "Homepage Hero A/B Test" \
  -d "Testing CTA button colors: Blue vs Orange" \
  -g "Increase signup rate to 5%" \
  -m "signup_rate" \
  -v 0.05

# Track metrics over time
./growth_hacker.py add-metric 1 signup_rate 0.032 -n "Blue variant"
./growth_hacker.py add-metric 1 signup_rate 0.047 -n "Orange variant"
./growth_hacker.py add-metric 1 signup_rate 0.051 -n "Orange variant final"

# Add notes about findings
./growth_hacker.py add-note 1 "Orange button increased signups by 59%"

# Calculate growth
./growth_hacker.py growth 1 signup_rate

# Mark as completed
./growth_hacker.py update 1 --status completed
```

### Example 2: Product Launch

```bash
# Create project
./growth_hacker.py create "Q4 Product Launch" \
  -d "New premium tier launch campaign" \
  -g "Acquire 500 premium users" \
  -m "premium_users" \
  -v 500

# Track multiple metrics
./growth_hacker.py add-metric 2 premium_users 45 -n "Week 1"
./growth_hacker.py add-metric 2 premium_users 120 -n "Week 2"
./growth_hacker.py add-metric 2 premium_users 280 -n "Week 3"

./growth_hacker.py add-metric 2 revenue 4500 -n "Week 1"
./growth_hacker.py add-metric 2 revenue 12000 -n "Week 2"
./growth_hacker.py add-metric 2 revenue 28000 -n "Week 3"

# View progress
./growth_hacker.py view 2
./growth_hacker.py growth 2 premium_users
```

### Example 3: SEO Optimization

```bash
# Create project
./growth_hacker.py create "SEO Content Strategy" \
  -d "Publish 50 optimized blog posts" \
  -g "Increase organic traffic by 200%" \
  -m "organic_sessions" \
  -v 15000

# Track weekly progress
./growth_hacker.py add-metric 3 organic_sessions 5000 -n "Baseline"
./growth_hacker.py add-metric 3 organic_sessions 6200 -n "10 posts published"
./growth_hacker.py add-metric 3 organic_sessions 8500 -n "25 posts published"
./growth_hacker.py add-metric 3 organic_sessions 12000 -n "40 posts published"

./growth_hacker.py add-metric 3 blog_posts 0
./growth_hacker.py add-metric 3 blog_posts 10
./growth_hacker.py add-metric 3 blog_posts 25
./growth_hacker.py add-metric 3 blog_posts 40

# Add context notes
./growth_hacker.py add-note 3 "Focus on long-tail keywords showing best results"
./growth_hacker.py add-note 3 "Top performing post: 'Ultimate Guide to X'"
```

### Example 4: Viral Referral Program

```bash
# Create project
./growth_hacker.py create "Referral Program v2" \
  -d "Give $10, Get $10 referral campaign" \
  -g "Generate 2000 referrals" \
  -m "referrals" \
  -v 2000

# Track metrics
./growth_hacker.py add-metric 4 referrals 156 -n "Day 1"
./growth_hacker.py add-metric 4 referrals 425 -n "Day 3"
./growth_hacker.py add-metric 4 referrals 890 -n "Day 7"
./growth_hacker.py add-metric 4 referrals 1650 -n "Day 14"
./growth_hacker.py add-metric 4 referrals 2340 -n "Day 21"

./growth_hacker.py add-metric 4 viral_coefficient 1.8 -n "Calculated K-factor"

# Calculate growth
./growth_hacker.py growth 4 referrals
```

## Tips and Best Practices

1. **Consistent Metric Names**: Use consistent naming for metrics across projects
   - Good: `conversion_rate`, `signup_rate`, `users`
   - Avoid: `conv_rate`, `Conversion Rate`, `USERS`

2. **Regular Updates**: Add metrics regularly to track trends
   ```bash
   # Daily tracking
   ./growth_hacker.py add-metric 1 daily_active_users 1234
   ```

3. **Use Notes Effectively**: Document important changes and insights
   ```bash
   ./growth_hacker.py add-note 1 "Changed pricing - monitor impact"
   ```

4. **Track Multiple Metrics**: Don't just track vanity metrics
   ```bash
   # Track both quantity and quality
   ./growth_hacker.py add-metric 1 signups 500
   ./growth_hacker.py add-metric 1 activated_users 320
   ./growth_hacker.py add-metric 1 revenue 12500
   ```

5. **Status Management**: Keep projects organized
   ```bash
   # Pause experiments that aren't working
   ./growth_hacker.py update 1 --status paused

   # Mark successful ones as completed
   ./growth_hacker.py update 2 --status completed
   ```

## Data Storage

All data is stored in `~/.growth_hacking_projects.json`

To backup your data:
```bash
cp ~/.growth_hacking_projects.json ~/growth_hacking_backup.json
```

To use a custom data file:
```bash
# Edit the script or set a custom path in the GrowthHackingManager initialization
```

## Common Workflows

### Weekly Review
```bash
# List all active projects
./growth_hacker.py list --status active

# Review each project
./growth_hacker.py view 1
./growth_hacker.py view 2

# Check growth rates
./growth_hacker.py growth 1 users
./growth_hacker.py growth 2 conversion_rate
```

### Month-End Reporting
```bash
# List all projects
./growth_hacker.py list

# Get detailed metrics for each
./growth_hacker.py metrics 1
./growth_hacker.py metrics 2

# Calculate growth for key metrics
./growth_hacker.py growth 1 revenue
./growth_hacker.py growth 2 users
```

## Troubleshooting

**Issue**: Command not found
```bash
# Make sure the script is executable
chmod +x growth_hacker.py

# Use python3 directly
python3 growth_hacker.py list
```

**Issue**: Cannot find project
```bash
# List all projects to see IDs
./growth_hacker.py list
```

## Advanced Usage

### Scripting and Automation

You can integrate this tool into your automation scripts:

```bash
#!/bin/bash
# Daily metrics collection script

PROJECT_ID=1
USERS=$(curl -s https://api.yourapp.com/metrics/users | jq .count)

python3 growth_hacker.py add-metric $PROJECT_ID users $USERS -n "Automated daily update"
```

### Integration with Analytics

```bash
# Pull from Google Analytics and track
GA_SESSIONS=$(your_ga_script.sh)
./growth_hacker.py add-metric 1 sessions $GA_SESSIONS

# Track from multiple sources
STRIPE_MRR=$(stripe_mrr.sh)
./growth_hacker.py add-metric 2 mrr $STRIPE_MRR -n "Stripe data"
```
