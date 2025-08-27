import sqlite3

"""
Sqlite3 documentation: https://docs.python.org/3/library/sqlite3.html
"""

db = "server_inventory.db"

conn = sqlite3.connect(db)
cursor = conn.cursor()

create_table_query = """
CREATE TABLE IF NOT EXISTS servers (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    ip_address TEXT NOT NULL,
    os TEXT NOT NULL,
    status TEXT NOT NULL
)
"""
cursor.execute(create_table_query)

conn.commit()
conn.close()


def insert_server(name, ip_address, os, status):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()

    insert_query = (
        "INSERT INTO servers (name, ip_address, os, status) VALUES (?, ?, ?, ?)"
    )
    cursor.execute(insert_query, (name, ip_address, os, status))

    cursor.commit()
    cursor.close()


def get_server():
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    select_query = "SELECT * FROM servers"
    cursor.execute(select_query)

    servers = cursor.fetchall()
    conn.close()
    return servers
