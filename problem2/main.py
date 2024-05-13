def caesar(offset, input_str):
    encrypted_str = ''
    for char in input_str:
        if char.isalpha():
            shifted = ord(char) + offset
            if char.islower():
                shifted = (shifted - ord('a')) % 26 + ord('a')
            encrypted_str += chr(shifted)
        else:
            encrypted_str += char
    return encrypted_str

if __name__ == '__main__':
    print(caesar(3, "abc"))  # def
    print(caesar(2, "alta"))  # cnvc
    print(caesar(10, "alterraacademy"))  # kvdobbkkmknowi
    print(caesar(1, "abcdefghijklmnopqrstuvwxyz"))  # bcdefghijklmnopqrstuvwxyza
    print(caesar(1000, "abcdefghijklmnopqrstuvwxyz"))  # mnopqrstuvwxyzabcdefghijkl
