# Household Tasks Card

A custom Lovelace card for the Household Tasks integration.

## Installation

1. Copy `household-tasks-card.js` to your Home Assistant `www` folder
2. Add the resource in your Lovelace configuration:

```yaml
resources:
  - url: /local/household-tasks-card.js
    type: module
```

Or via UI: Settings → Dashboards → Resources → Add Resource

## Usage

Add the card to your dashboard:

```yaml
type: custom:household-tasks-card
show_completed: false
default_room: all
```

## Options

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `show_completed` | boolean | `false` | Show completed chores for the week |
| `default_room` | string | `all` | Default room filter (room ID or "all") |

## Features

- **Weekly View**: See all chores due this week, grouped by day
- **Room Filter**: Filter chores by room
- **Quick Complete**: Check the box to mark a chore done
- **User Attribution**: Select who completed the chore (for shared devices)
- **Skip**: Skip to next occurrence without completing
- **Add Forms**: Add new chores and custom rooms directly from the card
- **Overdue Highlighting**: Visual indicator for past-due chores
