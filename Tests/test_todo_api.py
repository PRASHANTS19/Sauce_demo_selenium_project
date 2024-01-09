# import requests
#
# ENDPOINT = "https://todo.pixegami.io/"
#
#
# def test_call_api():
#     response = requests.get(ENDPOINT)
#     assert response.status_code==200
#
# def create_task(payload):
#     return requests.put(ENDPOINT+"/create-task",json=payload)
#
# def get_task(task_id):
#     return requests.get(ENDPOINT+f"/get-task/{task_id}")
#
# def get_task_list(user_id):
#     return requests.get(ENDPOINT+f"/list-tasks/{user_id}")
#
# def update_task(updated_payload):
#     return  requests.put(ENDPOINT + "/update-task", json=updated_payload)
#
# def delete_task(task_id):
#     return requests.delete(ENDPOINT+f"/delete-task/{task_id}")
#
# def test_api():
#     payload = {
#             "content": "automation",
#             "user_id": "007",
#             "is_done": False
#         }
#     response = create_task(payload)
#     assert response.status_code==200, f"Something went wrong and status code is: {response.status_code}"
#     data = response.json()
#
#     # check if task is created or not
#     task_id = data['task']['task_id']
#     response = get_task(task_id)
#     assert response.status_code==200, f"Something went wrong and status code is: {response.status_code}"
#     # print(response.json())
#
#     #get task list
#     user_id = data['task']['user_id']
#     response = get_task_list(user_id)
#     # print("Task list is: ",response.json())
#
# # update task
#     updated_payload = {
#         "content": "new task",
#         "user_id": "007",
#         "task_id": task_id,
#         "is_done": False
#         }
#     response = update_task(updated_payload)
#     assert response.status_code == 200, f"Updation is incomplete and status code is: {response.status_code}"
#
#     response = requests.get(ENDPOINT+f"/list-tasks/{user_id}")
#     # print("Task list is: ",response.json())
#
#     delete_task(task_id)
#     response = get_task(task_id)
#     print(response.status_code)