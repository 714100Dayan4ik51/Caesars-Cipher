def caesar_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isupper():
            encrypted_text += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        elif char.islower():
            encrypted_text += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            encrypted_text += char
    return encrypted_text


def caesar_decrypt(encrypted_text, shift):
    shift %= 26
    return caesar_encrypt(encrypted_text, -shift)


def main():
    while True:
        try:
            text = input("Введите текст для шифрования: ")
            shift = int(input("Введите шаг сдвига: "))
            encrypted_text = caesar_encrypt(text, shift)
            print("Зашифрованный текст:", encrypted_text)
            decrypted_text = caesar_decrypt(encrypted_text, shift)
            print("Расшифрованый текст: ", decrypted_text)
            break
        except ValueError:
            print("Что-то пошло не так, попробуйте снова.")
main()