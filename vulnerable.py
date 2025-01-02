import sqlite3

# Vulnérabilité : Injection SQL
def get_user_info(user_id):
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE id = {user_id}"  # Mauvaise pratique : concaténation directe
    cursor.execute(query)
    result = cursor.fetchall()
    conn.close()
    return result

# Vulnérabilité : Mot de passe en clair
def store_password(user, password):
    with open("passwords.txt", "a") as file:
        file.write(f"{user}:{password}\n")  # Mauvaise pratique : stockage en clair

# Fonction principale
if __name__ == "__main__":
    user_id = input("Entrez un ID utilisateur : ")
    print(get_user_info(user_id))
    store_password("admin", "password123")  # Exemple d'utilisation
