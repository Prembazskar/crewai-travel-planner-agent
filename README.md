# CrewAI Travel Planner Agent

A CrewAI agent that takes a city name and produces a travel plan.

> Part of my Gen AI course practice work (Week 4, Day 3).

## Tech stack

- Python 3
- CrewAI
- OpenAI

## Features

- Prompts for a city
- Travel planner agent and task run through a Crew

## Getting started

1. Clone the repository:
   ```bash
   git clone https://github.com/Prembazskar/crewai-travel-planner-agent.git
   cd crewai-travel-planner-agent
   ```
2. Install and configure:
   ```bash
   pip install -r requirements.txt
   cp .env.example .env   # then add your OpenAI key
   ```

Environment variables (set in `.env`, never commit it):

- `OPENAI_API_KEY`

## Usage

```bash
python travel_planner.py
```

## License

MIT, see [LICENSE](LICENSE).
