# Weather Data Pipeline

A simple Python ETL (Extract, Transform, Load) pipeline that fetches live weather data from a public API, cleans it, and stores it for analysis.

## What it does
1. **Extract** — Calls the OpenWeatherMap API to get current weather for a city
2. **Transform** — Parses the raw JSON response into clean, readable fields (temperature, humidity, condition)
3. **Load** — Appends each reading as a new row in a CSV file, building a historical log over time

## Tech stack
- Python 3
- `requests` — API calls
- `python-dotenv` — secure environment variable management
- CSV — lightweight data storage

## How to run it
1. Clone this repo
2. Install dependencies:
3. Create a `.env` file in the project root with your own OpenWeatherMap API key:
4. Run the script:
python3 weather.py
## What I learned
- How to securely manage API keys using environment variables instead of hardcoding them
- How to parse nested JSON responses from a REST API
- The basics of an ETL pattern: extract data, transform it into a usable format, and load it into storage
- Git/GitHub workflow for version-controlling a project

## Next steps
- Automate this to run on a schedule (e.g. every hour) using cron or Airflow
- Track multiple cities at once
- Move storage from CSV to a proper database (PostgreSQL/SQLite)