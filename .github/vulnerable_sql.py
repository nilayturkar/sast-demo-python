import sqlite3

def get_user_data(username):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    # 🚨 Vulnerable code (SQL Injection)
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    
    cursor.execute(query)
    result = cursor.fetchall()
    print(result)

# Example usage
get_user_data("admin' OR '1'='1")
