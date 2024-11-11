
Этот файл `README.md` содержит всю необходимую информацию для запуска и работы с приложением, включая установку зависимостей, описание и структуру проекта.


# Приложение Hacker_Groups

## Описание проекта

Данное приложение с использованием библиотеки NiceGUI предоставляет форму для сбора и хранения данных о хакерских группировках, атакующих организации. Приложение использует базу данных SQLite для сохранения введенной информации, что позволяет структурировать и анализировать данные по каждой группировке.

### Функциональные возможности

1. Ввод информации о хакерских группировках, включая:
  - Название группировки
  - Атакуемые организации
  - Метод атаки
  - Дата атаки
  - Алиасы группировки
2. Сохранение данных в локальную базу данных SQLite (`hackers.db`)
3. Уведомления об успешной записи данных в базу
4. Обновление таблицы с данными
5. Удаление записей из таблицы и базы данных

## Структура проекта

1. main.py # Основной файл приложения
2. hackers.db # База данных SQLite (создается автоматически)
3. requirements.txt # Файл с зависимостями для проекта
4. README.md # Документация к приложению

### Создаем виртуальное окружение (например, с использованием venv)

python -m venv venv

### Активируем виртуальное окружение

Для Windows:
venv\Scripts\activate

Для macOS/Linux:
source venv/bin/activate


### Подготовка и запуск

1. Клонируйте репозиторий или создайте директорию для проекта и скопируйте файлы.
2. Установите зависимости с помощью `requirements.txt`:

```bash
pip install -r requirements.txt
```

Проект требует Python 3.7 или выше. Зависимости в requirements.txt:

nicegui



3. Запустите приложение с помощью команды:

```bash
python main.py
```

### Использование
После запуска приложения откройте браузер и перейдите по адресу http://localhost:8080. Вы увидите форму для ввода информации о хакерских группировках. После заполнения и нажатия кнопки "Сохранить" данные будут добавлены в базу данных SQLite (hackers.db), и появится уведомление об успешной записи. Есть таблица с данными о хакерских группировках, для обновления данных в таблице есть кнопка "Обновить данные". Также можно удалить запись из таблицы и базы данных по номеру ID с помощью кнопки "Удалить запись".


### Структура базы данных

В базе данных hackers.db создается таблица groups со следующими полями:

Поле	         Тип	    Описание
id	           INTEGER  Первичный ключ, автоматически увеличивается
group_name	   TEXT	    Название хакерской группировки
target_orgs	   TEXT	    Атакуемые организации
attack_method	 TEXT	    Метод атаки (например, фишинг, DDoS)
attack_date	   TEXT	    Дата атаки
aliases	       TEXT	    Алиасы группировки


### Автор проекта

ФИО: Пивовар Денис Александрович, Telegram: @Densh1