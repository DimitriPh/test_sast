import sqlite3
import os

# Mauvaise gestion des mots de passe
PASSWORD = "123456"  # Ne pas stocker les mots de passe en clair dans le code

# Injection SQL
def unsafe_query(user_input):
    conn = sqlite3.connect("example.db")
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE username = '{user_input}'"  # Vulnérabilité d'injection SQL
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results

# Exécution de commande arbitraire
def execute_command(cmd):
    os.system(cmd)  # Vulnérabilité d'exécution de commande

# Exemple d'utilisation
if __name__ == "__main__":
    print("Bienvenue dans l'application vulnérable.")

    # Requête avec injection SQL
    username = input("Entrez le nom d'utilisateur : ")
    print(unsafe_query(username))

    # Exécution de commande arbitraire
    command = input("Entrez une commande à exécuter : ")
    execute_command(command)
