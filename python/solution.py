import numpy as np

def generate_key(key):
    key_list = []
    for char in key.upper():
        if char not in key_list:
            key_list.append(char)
    
    letters = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    for char in letters:
        if char not in key_list:
            key_list.append(char)
    
    return np.array(key_list).reshape(5, 5)

def find_position(char, key_matrix):
    pos = np.where(key_matrix == char)
    return pos[0][0], pos[1][0]

def decrypt_pair(pair, key_matrix):
    if len(pair) == 1:
        return pair
    
    row1, col1 = find_position(pair[0], key_matrix)
    row2, col2 = find_position(pair[1], key_matrix)
    
    if row1 == row2:
        return key_matrix[row1][(col1 - 1) % 5] + key_matrix[row1][(col2 - 1) % 5]
    elif col1 == col2:
        return key_matrix[(row1 - 1) % 5][col1] + key_matrix[(row2 - 1) % 5][col2]
    else:
        return key_matrix[row1][col2] + key_matrix[row2][col1]

def decrypt(message, key):
    message = message.upper().replace(" ", "")
    key_matrix = generate_key(key)
    decrypted = ""
    
    i = 0
    while i < len(message):
        pair = message[i:i+2]
        decrypted_pair = decrypt_pair(pair, key_matrix)
        if decrypted_pair[0] == "X":
            decrypted += decrypted_pair[1]
        elif decrypted_pair[1] == "X":
            decrypted += decrypted_pair[0]
        else:
            decrypted += decrypted_pair
        i += 2
    
    return decrypted

def main():
    encrypted_message = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
    key = "SUPERSPY"
    decrypted_message = decrypt(encrypted_message, key)
    print(decrypted_message, end="")

if __name__ == '__main__':
    main()
