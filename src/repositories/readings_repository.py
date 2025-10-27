from typing import Optional, Dict

class ReadingsRepository:
    def __init__(self, conn_factory):
        self.conn_factory = conn_factory
    
    def insert_reading(self, data: Dict):
        query = "INSERT INTO readings (sensorId, temperature, humidity, timestamp) VALUES (?,?,?,?)"
        param = (data["sensorId"], data["temperature"], data["humidity"], data["timestamp"])

        with self.conn_factory.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(query, param)
            conn.commit()
            return True

    def has_sensor_readings(self, sensorId):
        query = "SELECT EXISTS(SELECT * FROM readings WHERE sensorId = ?)"
        param = (sensorId,)
        
        with self.conn_factory.get_connection() as conn:
            cursor = conn.cursor()
            check_sensor_id = cursor.execute(query, param)
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
    
    def fetch_stats_from_sensor_readings(self, sensorId: str):
        query = """
            SELECT AVG(temperature) as avg_temperature, AVG(humidity) as avg_humidity,
            MAX(temperature) as max_temperature, MIN(temperature) as min_temperature
            FROM readings WHERE sensorId = ?
        """

        params = [sensorId]

        with self.conn_factory.get_connection() as conn:
            cursor = conn.cursor()
            cursor = cursor.execute(query, params)
            stats = cursor.fetchone()
            return {
                "sensorId": sensorId,
                "avg_temperature": stats[0],
                "avg_humidity": stats[1],
                "max_temperature": stats[2],
                "min_temperature": stats[3]
            }


        
