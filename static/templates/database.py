import sqlite3

conn = sqlite3.connect('bus.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS location (
    bus_id TEXT,
    lat REAL,
    lon REAL,
    speed REAL
)
''')

conn.commit()
conn.close()

print("Database Created")
