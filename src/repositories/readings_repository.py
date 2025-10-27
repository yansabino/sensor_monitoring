from typing import Optional, Dict

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

    def has_sensor_readings(self, sensorId):
        with self.conn_factory.get_connection() as conn:
            cursor = conn.cursor()
            check_sensor_id = cursor.execute("SELECT EXISTS(SELECT * FROM readings WHERE sensorId = ?)", (sensorId,))
            exists = cursor.fetchone()[0]

            return exists == 1

    
    def fetch_readings(self, sensorId: str, start: Optional[str] = None, end: Optional[str] = None):
        query = "SELECT * FROM readings WHERE sensorId = ?"
        params = [sensorId]

        if start and end:
            query += " AND timestamp BETWEEN ? AND ?"
            params += [start, end]

        with self.conn_factory.get_connection() as conn:
            cursor = conn.cursor()
            cursor = cursor.execute(query, params)
            return [dict(row) for row in cursor.fetchall()]


        
