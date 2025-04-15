import requests
import json

while True:
    base_url = ('http://www.omdbapi.com/?apikey=505480d7&s=') # основной адрес
    command = input("Введите название (на английском языке) или exit чтобы выйти): ") # вводим команду
    
    if command.lower() == "exit": # если exit == exit то программа завершается
        print("Goodbye!")
        break
    else:
        print(f"You entered: {command}") # показывает какую команду ввели
        full_url = requests.get(f"{base_url}{command}") # подставляет к адресу команду
        data = full_url.json() # чпоньк
        if full_url.status_code == 404: # нашел ли страницу
            print("Error: Not Found")
        elif full_url.status_code == 200: # есть ли коннект
            print("Success:")
        elif base_url.status_code == 401: # коннект с апи
            print("Unauthorized")
        try:
            
           for movie in data.get("Search"): #  для фильмов в список вытащить поиск
                print(f"🎬 {movie['Title']} ({movie['Year']})") # выводим пользователю его результаты
        except Exception as e:
            print(f"Введенное название не найдена: {e}") # обработка ошибок 
