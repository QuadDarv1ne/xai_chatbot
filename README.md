# xAI Chatbot

![grok](img/grok.png)

Добро пожаловать в проект `xAI Chatbot`

Это чат-бот, использующий `API xAI` для взаимодействия с моделью `Grok`

Проект позволяет пользователю общаться с искусственным интеллектом в терминале.

---

## Функционал

- Общение с моделью xAI Grok через терминал.
- Возможность получения ответов на запросы пользователя.
- Обработка ошибок и исключений.

---

## Установка и запуск

### 1. Клонирование репозитория
Склонируйте проект на ваш локальный компьютер:
```bash
git clone https://github.com/your-username/xai_chatbot.git
cd xai_chatbot
```

### 2. Установка зависимостей

**Создайте виртуальное окружение и установите необходимые библиотеки:**

```bash
python -m venv venv
source venv/bin/activate  # Для Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Настройка переменных окружения

**Создайте файл .env в корне проекта и добавьте в него ваш API-ключ xAI:**

```plaintext
XAI_API_KEY=your_xai_api_key_here
```

### 4. Запуск проекта

**Запустите приложение:**

```bash
python main.py
```

---

### Пример работы

```plaintext
Добро пожаловать в чат-бот xAI.
Напишите 'выход', чтобы завершить работу.
Вы: Что ты умеешь?
Чат-бот: Я могу отвечать на вопросы и помогать вам с различными задачами.
```

---

## Структура проекта

```
xai_chatbot/
├── main.py             # Главный скрипт для запуска чат-бота
├── .env                # Переменные окружения (API-ключ)
├── .gitignore          # Игнорируемые файлы и папки
├── requirements.txt    # Список зависимостей проекта
└── utils/
    ├── __init__.py     # Инициализация пакета utils
    └── xai_client.py   # Логика работы с API xAI
```

---

### Требования

- **Python 3.9 или выше**

- **Установленные библиотеки:**

    - openai
    - python-dotenv

---

**Автор:** Дуплей Максим Игоревич

**Дата:** 10.12.2024