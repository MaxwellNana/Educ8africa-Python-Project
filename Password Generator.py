import random
import string

def generate_password(length):
    password = ""
    character_sets = [string.ascii_lowercase, string.ascii_uppercase, string.digits, string.punctuation]
    for i in range(length):
        password += random.choice(random.choice(character_sets))
    return password

password = generate_password(12)
print(password)
