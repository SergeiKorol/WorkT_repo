import requests

def test_add_and_edit():
    body = {"title":"generated","completed":False}
    resp = requests.post("https://todo-app-sky.herokuapp.com/", json=body)
    id = resp.json()["id"]
    
    body = {"completed": True}
    resp = requests.patch(f'https://todo-app-sky.herokuapp.com/{id}', json=body)
    resp_body = resp.json()
    
    assert resp_body['completed'] == True