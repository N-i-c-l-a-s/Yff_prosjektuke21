import os
from dotenv import find_dotenv, load_dotenv, set_key
from cryptography.fernet import Fernet
import random
import string

# Generer Fernet krypteringsnøkkel
encryption_key = Fernet.generate_key().decode()
fernet_instance = Fernet(encryption_key.encode())
dotenv_path = find_dotenv()

# Be brukeren om brukernavn og passord/ generer tilfeldig passord
input_username1 = input("Skriv inn brukernavnet ditt: ")
Valg=input("vil du bruke et tilfeldig genrert sterkt passord? ja/nei: ")

if Valg == "nei":
    input_password = input("Skriv inn passordet ditt: ")

if Valg == "ja":
    characters = string.ascii_letters + string.digits
    input_password = ''.join(random.choices(characters, k=16))


# Lagre brukernavn og passord til .env-fil
set_key(dotenv_path, "USERNAME1", input_username1)
set_key(dotenv_path, "PASSWORD", input_password)
set_key(dotenv_path, "SECRET_KEY", encryption_key)

# Last inn verdier fra .env-fil etter at vi har lagret dem
load_dotenv(dotenv_path)

# Hent verdier fra .env-fil
env_username1 = os.getenv("USERNAME1")
env_password = os.getenv("PASSWORD")

# Krypter brukernavnet
encrypted_username_bytes = fernet_instance.encrypt(env_username1.encode())
encrypted_username_str = encrypted_username_bytes.decode()
decrypted_username = fernet_instance.decrypt(encrypted_username_bytes).decode()

# Lagre kryptert brukernavn i .env-fil
set_key(dotenv_path, "ENCRYPTED_USERNAME1", encrypted_username_str)

# Krypter passordet
encrypted_password_bytes = fernet_instance.encrypt(env_password.encode())
encrypted_password_str = encrypted_password_bytes.decode()
decrypted_password = fernet_instance.decrypt(encrypted_password_bytes).decode()

# Lagre kryptert passord i .env-fil
set_key(dotenv_path, "ENCRYPTED_PASSWORD", encrypted_password_str)

# Vis de krypterte og deretter dekrypterte verdiene
print(f"\n Dekrypterte verdier fra kryptert data:")
print(f"Brukernavn: {decrypted_username}")
print(f"Passord: {decrypted_password}")
