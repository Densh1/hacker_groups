from nicegui import ui
import sqlite3
from datetime import datetime

# Инициализация базы данных SQLite и создание таблицы
def init_db():
    conn = sqlite3.connect('hackers.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS groups (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        group_name TEXT NOT NULL,
                        target_orgs TEXT,
                        attack_method TEXT,
                        attack_date TEXT,
                        aliases TEXT
                      )''')
    
    # Проверка на наличие данных и сброс автоинкремента, если таблица пуста
    cursor.execute("SELECT COUNT(*) FROM groups")
    if cursor.fetchone()[0] == 1:
        cursor.execute("DELETE FROM sqlite_sequence WHERE name='groups'")
    
    conn.commit()
    conn.close()

# Функция для записи данных в базу
def save_to_db(group_name, target_orgs, attack_method, attack_date, aliases):
    conn = sqlite3.connect('hackers.db')
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO groups (group_name, target_orgs, attack_method, attack_date, aliases) 
                      VALUES (?, ?, ?, ?, ?)''', 
                   (group_name, target_orgs, attack_method, attack_date, aliases))
    conn.commit()
    conn.close()

# Функция для получения данных из базы
def fetch_data():
    conn = sqlite3.connect('hackers.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM groups")
    data = cursor.fetchall()
    conn.close()
    return data

# Функция для удаления записи из базы данных
def delete_from_db(record_id):
    conn = sqlite3.connect('hackers.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM groups WHERE id = ?", (record_id,))
    conn.commit()
    conn.close()
    show_data()  # Обновление таблицы после удаления

# Инициализация базы данных
init_db()

# Функция для обработки данных формы и записи их в базу
def handle_submit():
    group_name = group_name_input.value
    target_orgs = target_orgs_input.value
    attack_method = attack_method_input.value
    attack_date = attack_date_input.value
    aliases = aliases_input.value
    
    save_to_db(group_name, target_orgs, attack_method, attack_date, aliases)
    ui.notify(f'Данные о группировке "{group_name}" сохранены в базе данных.')
    show_data()  # Обновление таблицы после добавления

# Функция для отображения данных в таблице
def show_data():
    data = fetch_data()
    table.rows.clear()  # Очистка таблицы перед добавлением новых данных

    # Вывод данных в консоль
    print("Данные о хакерских группировках:", data)

    for row in data:
        # Использование именованных полей для добавления строк
        table.add_row({
            "ID": row[0],
            "Название": row[1],
            "Цель": row[2],
            "Метод": row[3],
            "Дата": row[4],
            "Алиасы": row[5]
        })

# Функция для обработки удаления записи через выбранный ID
def handle_delete():
    record_id = int(delete_id_input.value)
    delete_from_db(record_id)

# Добавление глобального стиля для предотвращения горизонтальной прокрутки
ui.add_head_html("""
    <style>
        body {
            overflow-x: hidden; /* Отключает горизонтальную прокрутку */
        }
    </style>
""")

# Основной интерфейс
with ui.column().style('display: grid; place-items: center; height: 100vh; width: 100vw;'):
    with ui.column().style('width: 100%; max-width: 800px; text-align: center;'):
        ui.label("Форма для заполнения информации о хакерских группировках").style('text-align: center; width: 100%; font-size: 22px; font-weight: bold;')
        
        # Элементы формы
        group_name_input = ui.input(label="Название группировки", placeholder="Введите название группировки").style('text-align: center; width: 100%;')
        target_orgs_input = ui.input(label="Атакуемые организации", placeholder="Введите названия организаций").style('text-align: center; width: 100%;')
        
        
        attack_method_input = ui.input(label="Метод атаки", placeholder="Введите метод атаки").style('text-align: center; width: 100%;')
        
        # Поле ввода для даты атаки
        attack_date_input = ui.input(label="Дата атаки", placeholder="Введите дату атаки").style('text-align: center; width: 100%;')

        aliases_input = ui.input(label="Алиасы группировки", placeholder="Введите алиасы группировки").style('text-align: center; width: 100%;')
        submit_button = ui.button("Сохранить", on_click=handle_submit).style('text-align: center; width: 100%;')

        ui.label("Данные о хакерских группировках").style('font-size: 16px; font-weight: bold; margin-bottom: 5px; text-align: center;')
        
        # Таблица данных
        table = ui.table(columns=[
            {"name": "ID", "label": "ID", "field": "ID"},
            {"name": "Название", "label": "Название", "field": "Название"},
            {"name": "Цель", "label": "Цель", "field": "Цель"},
            {"name": "Метод", "label": "Метод", "field": "Метод"},
            {"name": "Дата", "label": "Дата", "field": "Дата"},
            {"name": "Алиасы", "label": "Алиасы", "field": "Алиасы"}
        ], rows=[]).style('text-align: center; width: 100%; max-height: 400px; overflow-y: auto;')
        
        ui.button("Обновить данные", on_click=show_data).style('margin-top: 10px; text-align: center;')

        # Поле ввода ID записи для удаления
        delete_id_input = ui.input(label="ID записи для удаления", placeholder="Введите ID записи").style('text-align: center; width: 100%;')
        ui.button("Удалить запись", on_click=handle_delete).style('text-align: center; width: 100%; margin-top: 5px;')

# Запуск приложения
ui.run()