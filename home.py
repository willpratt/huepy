import requests
import json

class Home:
    def __init__(self):
        with open("config.json") as json_file:
            self.config = json.load(json_file)
            self.ip = self.config["ip_addr"] 
            self.key = self.config["key"]

        with open("states.json") as json_file:
            self.states = json.load(json_file)

    def set_state(self, state):
        for i in self.states[state]:
            # This is ugly - consider changing format of states json
            light_number = list(i.keys())[0]
            requests.put("http://" + self.ip + "/api/" + self.key + "/lights/" + light_number + "/state", json.dumps(i[str(light_number)]))