import os
from utils.xai_client import chat_with_grok
from dotenv import load_dotenv

# Загрузка переменных окружения из .env
load_dotenv()

def main():
    print("Добро пожаловать в чат-бот xAI.")
    print("Напишите 'выход', чтобы завершить работу.")
    
    while True:
        user_input = input("Вы: ")
        if user_input.lower() == 'выход':
            print("Чат-бот: До свидания.")
            break

        # Получение ответа от модели
        response = chat_with_grok(user_input)
        print(f"Чат-бот: {response}")

if __name__ == "__main__":
    main()
