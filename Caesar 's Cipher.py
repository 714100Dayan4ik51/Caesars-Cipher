def encrypt_caesar(text, shift):
    if text.isalpha():
        num = ord(text) + shift % 32
        if num > 1103:
            num -= 32
        return chr(num)
    return text


def decrypt_caesar(encrypted, shift):
    shift %= 26
    return encrypt_caesar(encrypted, -shift)
