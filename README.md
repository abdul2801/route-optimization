# Route Optimization (India-aware)

This project provides a simulation and optimization toolkit , with support for city-specific scenarios and real-world constraints such as traffic zones, festivals, and weather events.

## Features

- **Configurable city scenarios**: Delhi Dussehra, Kolkata Puja, Mumbai Ganesh, Mumbai Monsoon, and more via YAML configs.
- **Zone-aware routing**: Models traffic multipliers for active zones and time bands.
- **Order and rider simulation**: Generates realistic orders and rider start positions.
- **Route planning**: Optimizes rider routes using heuristics.
- **API and CLI**: Run optimizations via command line or REST API.
- **Metrics**: Summarizes key performance indicators for planned routes.


### Installation

```sh
pip install -e .