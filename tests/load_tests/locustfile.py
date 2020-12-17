from locust import HttpUser, task, between
from copy import deepcopy
from random import randint

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Content-Type': 'application/json'
}

base_json = {
    "output": "store.data",
    "outputs": { "id": "store", "property": "data" },
    "inputs": [
        { "id": "count", "property": "n_clicks"},
        { "id": "clear", "property": "n_clicks"}
    ],
}

json_none = deepcopy(base_json)
json_none["changedPropIds"] = ["count.n_clicks"]
json_none["state"] = [{ "id":"store", "property": "data", "value": None }]

json_clear = deepcopy(base_json)
json_clear["changedPropIds"] = ["clear.n_clicks"]
json_clear["state"] = [{ "id":"store", "property": "data", "value": {"clicks": 52 }}]

json_render = {}
json_render["changedPropIds"] = ["store.data"]
json_render["outputs"] = {"id": "output", "property": "children"}
json_render["output"] = "output.children"

class MyUser(HttpUser):
    def render_helper(self):
      my_json_render = deepcopy(json_render)
      my_json_render["inputs"] = [{
        "id": "store",
        "property": "data",
        "value": { "clicks": randint(1,100000) }
      }]

      self.client.post("/_dash-update-component",
                 json=my_json_render,
                 headers=headers,
                 name="render")

    @task
    def get_homepage(self):
      self.client.get("/")
      self.render_helper()
    
    @task(2)
    def count_none(self):
      self.client.post("/_dash-update-component",
                       json=json_none,
                       headers=headers,
                       name="count_none")
      self.render_helper()
    
    @task(10)
    def count_increment(self):
      json_increment = deepcopy(json_none)
      json_increment["state"] = [{
        "id":"store",
        "property": "data",
        "value": {"clicks": randint(1,100000)}
      }]
      self.client.post("/_dash-update-component",
                       json=json_increment,
                       headers=headers,
                       name="count_increment")
      self.render_helper()

    @task(4)
    def count_clear(self):
      self.client.post("/_dash-update-component",
                       json=json_clear,
                       headers=headers,
                       name="count_clear")
      self.render_helper()
      
    wait_time = between(0.2, 10)
