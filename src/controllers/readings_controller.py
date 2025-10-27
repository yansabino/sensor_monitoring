from flask import request, jsonify

class ReadingsController:
    def __init__(self, service):
        self.service = service
    
    def create_reading(self):
        data = request.get_json()
        result, status = self.service.create_reading(data)
        return jsonify(result), status
    
    def fetch_sensor_readings(self, sensorId: str):
        start = request.args.get("start")
        end = request.args.get("end")

        data, status = self.service.fetch_readings(sensorId, start, end)
        return jsonify(data), status
