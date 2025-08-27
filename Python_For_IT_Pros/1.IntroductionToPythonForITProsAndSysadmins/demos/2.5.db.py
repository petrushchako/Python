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

    conn.commit()
    conn.close()


def get_server():
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    select_query = "SELECT * FROM servers"
    cursor.execute(select_query)

    servers = cursor.fetchall()
    for server in servers:
        print(server)
        
    conn.close()
    return servers


def update_server(status, id):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    update_query = "UPDATE servers SET status = ? WHERE id = ?"

    cursor.execute(update_query, (status, id))
    print(cursor.fetchall())
    conn.commit()
    conn.close()


if __name__ == "__main__":
    # insert_server("Jenkins Server", "192.168.0.100", "RHEL", "UP")
    get_server()
    update_server("DOWN", 2)
    get_server()