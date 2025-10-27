from typing import List, Optional, Dict

class ReadingsRepository:
    def __init__(self, conn_factory):
        self.conn_factory = conn_factory
    
    def insert_reading(self, data: Dict):
        with self.conn_factory.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO readings (sensorId, temperature, humidity, timestamp) VALUES (?,?,?,?)",
                (data["sensorId"], data["temperature"], data["humidity"], data["timestamp"])
            )
            conn.commit()
            return True


        
