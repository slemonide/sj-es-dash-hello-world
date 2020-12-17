import requests

url = "http://prod:8000"
api_url = url + "/_dash-update-component"

## Test Helpers

def make_request(state):
    pass


## Tests

def test_main_page_status_code_equals_200():
    response = requests.get(url)
    assert response.status_code == 200

def test_count():
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Content-Type': 'application/json'
    }

    # click count button
    json = {
        "output": "store.data",
        "outputs":
            {
                "id": "store",
                "property": "data"
            },
        "inputs": [
            {
                "id": "count",
                "property": "n_clicks", "value": 1
            },
            {
                "id": "clear",
                "property": "n_clicks"
            }
        ],
        "changedPropIds": ["count.n_clicks"],
        "state":
        [{
            "id":"store",
            "property": "data",
            "value": None
        }]
    }

    response = requests.post(api_url, json=json, headers=headers)

    expected_response = {
        'response':
            {
                'store': {'data': {'clicks': 1}} # increment number of clicks!
            },
        'multi': True # meaning there's more callbacks comming
    }
    
    assert response.json() == expected_response
