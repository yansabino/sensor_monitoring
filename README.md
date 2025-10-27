# sensor_monitoring

A small Flask-based sensor readings service that stores sensor measurements in a SQLite database and exposes simple HTTP endpoints to insert and query readings and statistics.

## Features

- Insert sensor readings (sensorId, temperature, humidity, timestamp)
- Query readings for a sensor (optionally by time range)
- Retrieve basic statistics for a sensor (avg, max, min)
- Lightweight SQLite storage (no external DB required)

## Requirements

- Python 3.9+
- pip

The project includes a `requirements.txt` for Python dependencies.

## Quick setup

1. Create and activate a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app

The app uses SQLite and will create a file named `sensor_readings.db` by default in the current directory.

```bash
python app.py
```

By default the Flask app will be available at http://127.0.0.1:5000/ and will run with debug=True (as implemented in `app.py`).


## HTTP API

The service exposes the following endpoints (registered in `src/routes/readings_routes.py`):

- POST /readings
  - Create a new reading.
  - Expected JSON body:

```json
{
  "sensorId": "sensor-1",
  "temperature": 22.5,
  "humidity": 40.2,
  "timestamp": "2025-10-27"
}
```

- GET /readings/<sensorId>
  - Fetch all readings for `sensorId`.
  - Optional query params: `start` and `end` (timestamps in the same format stored).
  - Example: `/readings/sensor-1?start=2025-10-01&end=2025-10-31`

- GET /stats/<sensorId>
  - Returns aggregated statistics for the sensor (avg temperature/humidity, max/min temperature).


## Database

The SQLite schema is created automatically on startup by `src/db/sqlite_connect.py` and contains a `readings` table with columns:

- id (INTEGER PRIMARY KEY AUTOINCREMENT)
- sensorId (TEXT)
- temperature (REAL)
- humidity (REAL)
- timestamp (TEXT)

No manual migrations are required for this simple setup.

## Project layout

- `app.py` - app factory and entrypoint
- `src/db/sqlite_connect.py` - SQLite connection factory and DB init
- `src/repositories/readings_repository.py` - DB access layer
- `src/services/readings_service.py` - business logic and validation
- `src/controllers/readings_controller.py` - Flask view handlers
- `src/routes/readings_routes.py` - blueprint and routes

## License

This project includes a `LICENSE` file in the repository root.

## Contact

If you need help or want improvements (tests, CI, Dockerfile), open an issue or contact the repository owner.
