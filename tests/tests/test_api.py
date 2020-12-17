import requests
from copy import deepcopy

url = "http://dev:8050"
api_url = url + "/_dash-update-component"

## Test Helpers

def make_json_request(json):
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Content-Type': 'application/json'
    }

    return requests.post(api_url, json=json, headers=headers)

# Basic data state to make it easier to construct other states on top of
base_json = {
    "output": "store.data",
    "outputs": { "id": "store", "property": "data" },
    "inputs": [
        { "id": "count", "property": "n_clicks"},
        { "id": "clear", "property": "n_clicks"}
    ],
}

## Tests

def test_main_page_status_code_equals_200():
    response = requests.get(url)
    assert response.status_code == 200

def test_count_store_increment_none_state():
    json = deepcopy(base_json)
    json["changedPropIds"] = ["count.n_clicks"]
    json["state"] = [{ "id":"store", "property": "data", "value": None }]

    response = make_json_request(json)

    expected_response = {
        'response': { 'store': {'data': {'clicks': 1}} },
        'multi': True
    }
    
    assert response.json() == expected_response

def helper_test_count_store_increment_non_null_state(value):
    json = deepcopy(base_json)
    json["changedPropIds"] = ["count.n_clicks"]
    json["state"] = [{ "id":"store", "property": "data", "value": {"clicks": value} }]

    response = make_json_request(json)

    expected_response = {
        'response': { 'store': {'data': {'clicks': value + 1}} },
        'multi': True
    }
    
    assert response.json() == expected_response

def test_count_store_increment_non_null_state():
  for value in range(1, 100):
    helper_test_count_store_increment_non_null_state(value)

def test_clear_count_store():
    json = deepcopy(base_json)
    json["changedPropIds"] = ["clear.n_clicks"]
    json["state"] = [{ "id":"store", "property": "data", "value": {"clicks": 64} }]

    response = make_json_request(json)

    expected_response = {
        'response': { 'store': {'data': {'clicks': 0}} },
        'multi': True
    }

    assert response.json() == expected_response

def test_render_store_data():
    counter_data = 64

    json = {}
    json["changedPropIds"] = ["store.data"]
    json["inputs"] = [{ "id": "store", "property": "data", "value": { "clicks": counter_data } }]
    json["outputs"] = {"id": "output", "property": "children"}
    json["output"] = "output.children"

    response = make_json_request(json)

    expected_response = {
        'response': { 'output': {'children': "The count is " + str(counter_data) }},
        'multi': True
    }

    assert response.json() == expected_response
