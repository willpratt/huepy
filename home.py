import requests
import json
import os

class Home:
    def __init__(self):
        with open(os.path.dirname(__file__) + "/config.json") as json_file:
            self.config = json.load(json_file)
            self.ip = self.config["ip_addr"] 
            self.key = self.config["key"]

        response = requests.get("http://" + self.ip + "/api/" + self.key + "/lights/")
        self.state = json.loads(response.content)

        with open(os.path.dirname(__file__) + "/states.json") as json_file:
            self.config_states = json.load(json_file)

    def set_state(self, state):
        for i in self.config_states[state]:
            # This is ugly - consider changing format of states json
            light_number = list(i.keys())[0]
            requests.put("http://" + self.ip + "/api/" + self.key + "/lights/" + light_number + "/state", json.dumps(i[str(light_number)]))

    def dim_the_lights(self):
        for light in self.state:
            print(light)
            bri = self.state[light]["state"]['bri'] - 100
            self.state[light]["state"]["bri"] = bri
            requests.put("http://" + self.ip + "/api/" + self.key + "/lights/" + light + "/state", json.dumps(self.state[light]["state"]) )