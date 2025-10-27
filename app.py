from flask import Flask
from src.db.sqlite_connect import SQLiteConnectionFactory, init_db
from src.repositories.readings_repository import ReadingsRepository
from src.services.readings_service import ReadingsService
from src.controllers.readings_controller import ReadingsController
from src.routes.readings_routes import readings_blueprint 

def create_app(db_path: str = "sensor_readings.db") -> Flask:
    app = Flask(__name__)

    conn_factory = SQLiteConnectionFactory(db_path)
    init_db(conn_factory)

    readings_repo = ReadingsRepository(conn_factory)
    readings_service = ReadingsService(readings_repo)
    readings_controller = ReadingsController(readings_service)

    readings_bp = readings_blueprint(readings_controller)
    app.register_blueprint(readings_bp)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
