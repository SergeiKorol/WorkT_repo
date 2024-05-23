import requests
import allure

def test_get_deleted_task():
    with allure.step("Создать новую задачу"):
        body = {"title":"generated","completed":False}
        response = requests.post("https://todo-app-sky.herokuapp.com/", json=body)
        id = response.json()["id"]

    with allure.step("Удалить созданную задачу"):
        response = requests.delete(f'https://todo-app-sky.herokuapp.com/{id}')

    with allure.step("получить удаленную задачу"):
        response = requests.get(f'https://todo-app-sky.herokuapp.com/{id}')
    
    with allure.step("Проверить, что приходит статус-код 404"):
        assert response.status_code == 404



