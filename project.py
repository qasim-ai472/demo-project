import random
chars = "abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()ABCDEFGHIJKLMNOPQRSTUVWXYZ"

print("Welcome to the Password Generator!")

length = int(input("Enter the desired password length: "))
password = "".join(random.sample(chars, length))
print("Generated password:", password)
print("Thank you for using the Password Generator!")


