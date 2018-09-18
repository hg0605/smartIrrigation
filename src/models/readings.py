import datetime
import uuid


from src.common.database import Database


class Readings(object):

    def __init__(self,temperature,moisture,humidity,_id=None,printdata="Yes"):
        self.temperature=temperature
        self.moisture=moisture
        self.humidity=humidity
        self._id=uuid.uuid4().hex if _id is None else _id
        self.printdata=printdata

    @classmethod
    def get(cls):
        data=Database.find("readings",{})
        if data is not None:
            return data


    @classmethod
    def push(cls,temperature,moisture,humidity):       
            new_data=cls(temperature,moisture,humidity)
            new_data.save_to_mongo()
            return True


    
    def json(self):
        return {
            "temperature":self.temperature,
            "_id":self._id,
            "printdata":self.printdata,
        "moisture":self.moisture,
        "humidity":self.humidity
        }

    def save_to_mongo(self):
        Database.insert("readings",self.json())