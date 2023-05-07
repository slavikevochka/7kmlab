import requests
import json

# Список доступних категорій
categories = [
    "animal",
    "career",
    "celebrity",
    "dev",
    "explicit",
    "fashion",
    "food",
    "history",
    "money",
    "movie",
    "music",
    "political",
    "religion",
    "science",
    "sport",
    "travel"
]

# Запит к API
category = input("Введіть категорію: ")
if category not in categories:
    print("Невірна категорія!")
    exit()
url = f"https://api.chucknorris.io/jokes/random?category={category}"
response = requests.get(url)

# Парсинг відповіді
data = json.loads(response.text)

# Вивід результатів у консоль
print(f"Категорія: {category}")
print(f"Дата створення: {data['created_at']}")
print(f"Анекдот: {data['value']}")
