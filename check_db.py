import sqlite3

try:
    # Connect to database
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    # Get Users
    print("\n--- REGISTERED USERS ---")
    cursor.execute("SELECT id, username FROM user")
    users = cursor.fetchall()
    if not users:
        print("No users found.")
    for user in users:
        print(f"ID: {user[0]} | Name: {user[1]}")

    # Get Logs
    print("\n--- RECENT ACTIVITY ---")
    cursor.execute("SELECT activity_type, details, timestamp FROM activity_log ORDER BY timestamp DESC LIMIT 5")
    logs = cursor.fetchall()
    if not logs:
        print("No activity logs found.")
    for log in logs:
        print(f"[{log[2]}] {log[0]}: {log[1]}")

    conn.close()

except Exception as e:
    print(f"Error reading database: {e}")
    print("Make sure 'users.db' exists in this folder.")