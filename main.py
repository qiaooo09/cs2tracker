import sqlite3
from datetime import datetime

# Подключение (файл автоматически создастся, если его нет)
conn = sqlite3.connect('db/stats.db')
cursor = conn.cursor()

# Создание таблицы (если не существует)
cursor.execute('''
CREATE TABLE IF NOT EXISTS games (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    kda REAL NOT NULL,
    avg_damage INTEGER NOT NULL,
    grenade_damage INTEGER NOT NULL,
    match_date TEXT DEFAULT CURRENT_TIMESTAMP
)
''')
conn.commit()

# Функция добавления записи после игры
def add_game(player, kda, dmg, g_dmg):
    cursor.execute('''
                   INSERT INTO games (name, kda, avg_damage, grenade_damage)
                   VALUES (?, ?, ?, ?)
                   ''', (player, kda, dmg, g_dmg))
    conn.commit()
    print(f"{player} - запись добавлена!")
    
add_game("Rina", 2.4, 215, 45)