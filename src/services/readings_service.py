from typing import Dict, Optional, List

class ReadingsService:
    def __init__(self, repo):
        self.repo = repo
    
    def create_reading(self, data: Dict):
        required = ["sensorId", "temperature", "humidity", "timestamp"]
        missing = [param for param in required if param not in data]

        if missing:
            return {"error": "A parameter is missing"}, 400
        
        new_reading = self.repo.insert_reading(data)
        return {"message": "Reading created successfully"}, 200
