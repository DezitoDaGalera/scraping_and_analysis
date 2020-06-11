import json
import os

json_dict = {}

class parser:
    def __init__(self):
        super().__init__()

    def parse(self):
        with open(os.path.abspath("pa_7/DadosRuasBairros.json")) as f:
            data = json.loads(f.read())
        data_trimmer = trimmer()
        trimmed_data = data_trimmer.trim(data)
        return trimmed_data

    

class trimmer:
    def __init__(self):
        super().__init__()

    def trim(self,data):
        for values in data:
            values["Value"].strip()
        return data