import sqlite3

def get_user_input():
    user_input = input("Entrez votre nom d'utilisateur : ")
    return user_input

def query_database(user_input):
    conn = sqlite3.connect("example.db")
    cursor = conn.cursor()
    # Requête SQL vulnérable
    cursor.execute(f"SELECT * FROM users WHERE name = '{user_input}'")
    print(cursor.fetchall())

if __name__ == "__main__":
    user_input = get_user_input()
    query_database(user_input)