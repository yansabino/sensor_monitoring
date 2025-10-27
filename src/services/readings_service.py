from typing import Dict, Optional

class ReadingsService:
    def __init__(self, repo):
        self.repo = repo
    
    def create_reading(self, data: Dict):
        try:
            required = ["sensorId", "temperature", "humidity", "timestamp"]
            missing = [param for param in required if param not in data]

            if missing:
                return {"error": "A parameter is missing"}, 400
            
            new_reading = self.repo.insert_reading(data)
            return {"message": "Reading created successfully"}, 200
        except Exception as e:
            return {"error": e}, 500
    
    def fetch_readings(self, sensorId: str, start: Optional[str] = None, end: Optional[str] = None):
        try:
            if not sensorId:
                return {"error": "sensorId param is missing!"}, 400

            sensor_exists_on_readings = self.repo.has_sensor_readings(sensorId)

            if not sensor_exists_on_readings:
                return {"error": "sensorId not found!"}, 404
                
            readings = self.repo.fetch_readings(sensorId, start, end)

            return readings, 200
        except Exception as e:
            return {"error": e}, 500