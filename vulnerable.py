import sqlite3

# Exemple de vulnérabilité flagrante
def vulnerable_function():
    user_input = input("Entrez votre nom d'utilisateur : ")
    query = f"SELECT * FROM users WHERE username = '{user_input}'"  # Injection SQL ici
    print("Requête SQL :", query)
    conn = sqlite3.connect('database.db')
    conn.execute(query)  # Exécute une requête SQL avec une entrée non sécurisée
    conn.close()
