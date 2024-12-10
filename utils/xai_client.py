import os
from openai import OpenAI
from dotenv import load_dotenv

# Загрузка переменных окружения
load_dotenv()

# Настройка API-ключа и базового URL
XAI_API_KEY = os.getenv("XAI_API_KEY")
client = OpenAI(
    api_key=XAI_API_KEY,
    base_url="https://api.x.ai/v1",
)

def chat_with_grok(user_message: str) -> str:
    """
    Отправляет сообщение пользователю в xAI Grok и возвращает ответ.
    
    Args:
        user_message (str): Ввод пользователя.
    
    Returns:
        str: Ответ модели или сообщение об ошибке.
    """
    try:
        # Формирование запроса к API
        response = client.chat.completions.create(
            model="grok-beta",
            messages=[
                {"role": "system", "content": "You are Grok, a chatbot inspired by the Hitchhikers Guide to the Galaxy."},
                {"role": "user", "content": user_message},
            ],
        )
        # Возвращаем текст ответа
        return response.choices[0].message['content']
    except Exception as e:
        return f"Произошла ошибка: {e}"

if __name__ == "__main__":
    print("Добро пожаловать в чат-бот xAI.")
    print("Напишите 'выход', чтобы завершить работу.")
    
    while True:
        user_input = input("Вы: ")
        if user_input.lower() == "выход":
            print("Чат-бот: До свидания.")
            break
        response = chat_with_grok(user_input)
        print(f"Чат-бот: {response}")
