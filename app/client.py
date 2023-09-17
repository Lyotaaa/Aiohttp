import requests

"""Создать пользователя"""
# response = requests.post(
#     "http://127.0.0.1:5000/owner/",
#     json={
#         "email": "@yandex.com",
#         "password": "123",
#     },
# )
# print(response.status_code)
# print(response.text)

"""Найти пользователя"""
# response = requests.get("http://127.0.0.1:5000/owner/1", )
# print(response.status_code)
# print(response.text)

"""Обновить информацию"""
# response = requests.patch("http://127.0.0.1:5000/owner/1",
#                          json={
#                              "email": "@yandex.net",
#                              "password": "123",
#                          })
# print(response.status_code)
# print(response.text)
#
# response = requests.get("http://127.0.0.1:5000/owner/1", )
# print(response.status_code)
# print(response.text)

"""Удалить пользователя"""
# response = requests.delete("http://127.0.0.1:5000/owner/1")
# print(response.status_code)
# print(response.text)
#
# response = requests.get("http://127.0.0.1:5000/owner/1")
# print(response.status_code)
# print(response.text)

"""Создать объявление"""
# response = requests.post(
#     "http://127.0.0.1:5000/ads/",
#     json={
#         "title": "Test",
#         "description": "Check",
#         "owner_id": 1,
#     }
# )
#
# print(response.status_code)
# print(response.text)

"""Найти объявление"""
# response = requests.get("http://127.0.0.1:5000/ads/1")
# print(response.status_code)
# print(response.text)

"""Обновить объявление"""
# response = requests.patch(
#     "http://127.0.0.1:5000/ads/3",
#     json={
#         "title": "title",
#         "description": "description",
#         "owner_id": 1,
#     }
# )
# print(response.status_code)
# print(response.text)
# #
# response = requests.get("http://127.0.0.1:5000/ads/3")
# print(response.status_code)
# print(response.text)

"""Удалить объявление"""
# response = requests.delete("http://127.0.0.1:5000/ads/1")
# print(response.status_code)
# print(response.text)
#
# response = requests.get("http://127.0.0.1:5000/ads/1")
# print(response.status_code)
# print(response.text)
