import json
from app import STORE_PATH



class JsonManager(object):
    
    def __init__(self, filename: str) -> None:
        self.fullpath = STORE_PATH + filename
    
    def getData(self):
        with open(self.fullpath, "r", encoding='utf-8') as file:
            return json.loads(file.read())
    
    def setData(self, new_data):
        data = self.getData()
        data["data"].append(new_data)
        with open(self.fullpath, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)