import numpy as np

"""============| Encrypted output |=========="""
message = "&7nd"

message_mat = np.matrix([[ord(char)] for char in message])

Key = np.matrix([
    [-1, 3, 6, 9],
    [4, 5, 10, -11],
    [6, 9, 12, 2],
    [2, -1, -9, 8]
])

enc_mat = Key*message_mat

print("Input message: " + message)
print("Key: ")
print(Key)
print("Number message: ")
print(message_mat)
print("Encrypted matrix: ")
print(enc_mat)

"""============| Decrypted output |=========="""
# Multiply inverse of key with decrypted matrix
dec_mat = np.linalg.inv(Key) * enc_mat

# Make the vertical matrix filled with floats, in to a list with integers, that are rounded
dec_array = np.squeeze(np.asarray(dec_mat))
#print(dec_array)
dec_carray = np.rint(dec_array)
#print(dec_carray)
dec_list =  dec_carray.astype(int)
#print(dec_list)

# Translate the characters of the decrypted list in to a message, transform the list in to a steady string
decrypted_mes = [chr(num) for num in dec_list]
decrypted_message = ''.join(map(str, decrypted_mes))

print("\nDecrypted matrix: ")
print(dec_mat)
print("Decrypted output: " + decrypted_message)

