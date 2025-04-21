def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

msg = input("Enter message: ")
s = int(input("Enter shift value: "))
encrypted = encrypt(msg, s)
print("Encrypted:", encrypted)
print("Decrypted:", decrypt(encrypted, s))