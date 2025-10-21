import random
import string

print("=== Password Generator ===")

# Step 1: Ask user for password length
length = int(input("Enter the length of password: "))

# Step 2: Define all possible characters
letters = string.ascii_letters  # a-z, A-Z
digits = string.digits          # 0-9
symbols = string.punctuation    # !, @, #, $, etc.

# Step 3: Combine all characters
all_characters = letters + digits + symbols

# Step 4: Generate password
password = ''.join(random.choice(all_characters) for i in range(length))

# Step 5: Display result
print("\nYour generated password is:", password)
print("=============================")



























































