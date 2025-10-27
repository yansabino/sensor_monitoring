from flask import request, jsonify

class ReadingsController:
    def __init__(self, service):
        self.service = service
    
    def create_reading(self):
        data = request.get_json()
        print(data)
        result, status = self.service.create_reading(data)
        return jsonify(result), status