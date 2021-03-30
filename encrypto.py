import numpy as np
import more_itertools


__authors__ = ["Lukaeaeap", "Donkere-vader"]
__version__ = "0.1"


KEY = np.matrix([
    [4, 3, 6, 9],
    [4, 5, 6, -3],
    [6, 9, 7, 2],
    [2, -1, -9, 8]])


def print_w_label(print_label, printable_thing):
    print(f"{print_label}:" )
    print(printable_thing)


class Encryptor:
    def __init__(self, message, key, ence_array, matrix_to_decrypt, encrypted_list):
        self.message = message
        self.key = key 
        self.ence_array = ence_array
        self.matrix_to_decrypt = matrix_to_decrypt
        self.encrypted_list = encrypted_list

    def encrypt(self, message, key,matrix_to_decrypt,ence_array, encrypted_list):
        message_mat = list([ord(char) for char in self.message])
        output = [list(group) for group in more_itertools.grouper(message_mat, 4, 0)]  # [[1, 2, 3, 4], [5, 6, 0, 0]]
        out = np.rot90(np.matrix(output), k=1)
        self.matrix_to_decrypt = self.key*out
        turnedenc = np.rot90(np.matrix(self.matrix_to_decrypt), k=-1)
        enc_carray = np.rint(turnedenc)
        enc_list =  enc_carray.astype(int)
        str_list = enc_list.reshape(-1)
        self.ence_array = np.squeeze(np.asarray(str_list))

        """===| List with encrypted characters |==="""
        self.encrypted_list = ' '.join(map(str, self.ence_array))


class Decryptor:
    def __init__(self, key, decrypted_message):
        self.key = key
        self.decrypted_message = decrypted_message
    
    def decrypt(self, inpu, key, decrypted_message):
        print_w_label("Input matrix",inpu.matrix_to_decrypt)
        dec_mat = np.linalg.inv(key) * inpu.matrix_to_decrypt
        turned = np.rot90(np.matrix(dec_mat), k=-1)
        dec_carray = np.rint(turned)
        dec_list =  dec_carray.astype(int)
        done = dec_list.reshape(-1)
        dece_array = np.squeeze(np.asarray(done))

        decrypted_mes = [chr(num) for num in dece_array]
        self.decrypted_message = ''.join(map(str, decrypted_mes))


class Inpute:
    def __init__(self, encryptable_txt, show_list, decryptable_msg):
        self.encryptable_txt = encryptable_txt
        self.decryptable_msg = decryptable_msg
        self.show_list = show_list

    def get(self, encryptable_txt, show_list):
        self.encryptable_txt = input("Enter the message you want to encrypt: ")

        self.show_list = 'answer'
        while not self.show_list in ['yes', 'no','y', 'n']:
            self.show_list = input("Do you want to show the encryption number list (y/n): ")

    def after(self, show_list, encryptin):
        if self.show_list in ['yes', 'y']:
            print_w_label("Encrypted list",encryptin.encrypted_list)
        print_w_label("Encrypted matrix", encryptin.matrix_to_decrypt)

    def getdec(self, decryptable_msg):
        self.decryptable_msg = input("What is the code that needs to be decrypted?: ")
    
    def afterdec(self, decryptin):
        print_w_label("Decrypted message", decryptin.decrypted_message)


def _main():  # _ at start of name to hint that this should be treated as a private function
    key = KEY  # something
    enc_txt = 'soon text'
    decbl_msg = None
    show_list = None

    input_thing = Inpute(enc_txt, show_list, decbl_msg)
    input_thing.get(enc_txt, show_list)
    encrypting = Encryptor(input_thing.encryptable_txt, key, None, None, None)
    encrypting.encrypt(input_thing.encryptable_txt, key, None, None, None)
    input_thing.after(show_list, encrypting)
    
    decrypting = Decryptor(key, None)
    decrypting.decrypt(encrypting, key, None)
    # With input:
    """
    decrypting = Decrypt(key, None)
    decrypting.decryption(input_thing, key, None)
    """
    input_thing.afterdec(decrypting)


if __name__ == "__main__":
    _main()