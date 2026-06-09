import mysql.connector

conn = mysql.connector.connect(
    host="127.0.0.1",
    user="ninja",
    password="ninja",
    database="ninja",
    port=3307,  # 🔥 THIS IS THE FIX
)

print("Connected!", conn.is_connected())
conn.close()
