import numpy as np
import more_itertools

__author__ = "Lukaeaeap"
__version__ = "0.1"

KEY = np.matrix([
    [4, 3, 6, 9],
    [4, 5, 6, -3],
    [6, 9, 7, 2],
    [2, -1, -9, 8]])

def prin(print_label, printable_thing):
    print(f"{print_label}:" )
    print(printable_thing)

class Encrypt:
    def __init__(self, message, key, ence_array, matrix_to_decrypt, encrypted_list):
        self.message = message
        self.key = key 
        self.ence_array = ence_array
        self.matrix_to_decrypt = matrix_to_decrypt
        self.encrypted_list = encrypted_list

    def encryption(self, message, key,matrix_to_decrypt,ence_array, encrypted_list):
        message_mat = list([ord(char) for char in self.message])
        #prin("Message matrix",message_mat)
        output = [list(group) for group in more_itertools.grouper(message_mat, 4, 0)]  # [[1, 2, 3, 4], [5, 6, 0, 0]]
        #prin("Grouped matrix",output)
        out = np.rot90(np.matrix(output), k=1)
        #prin("Text matrix", out)
        self.matrix_to_decrypt = self.key*out
        #prin("Encrypted matrix", oit)
        turnedenc = np.rot90(np.matrix(self.matrix_to_decrypt), k=-1)
        #prin("Turned back", turned)
        enc_carray = np.rint(turnedenc)
        #prin("Rounded",dec_carray)
        enc_list =  enc_carray.astype(int)
        #prin("As integer ist",dec_list)
        str_list = enc_list.reshape(-1)
        #prin("Straight line",done)
        self.ence_array = np.squeeze(np.asarray(str_list))
        #prin("Encrypted list",ence_array)
        """===| List with encrypted characters |==="""
        self.encrypted_list = ' '.join(map(str, self.ence_array))

class Decrypt:
    def __init__(self, key, decrypted_message):
        self.key = key
        self.decrypted_message = decrypted_message
    
    def decryption(self, inpu, key, decrypted_message):
        prin("Input matrix",inpu.matrix_to_decrypt)
        dec_mat = np.linalg.inv(key) * inpu.matrix_to_decrypt
        #prin("Decrypted matrix",dec_mat)
        turned = np.rot90(np.matrix(dec_mat), k=-1)
        #prin("Turned back", turned)
        dec_carray = np.rint(turned)
        #prin("Rounded",dec_carray)
        dec_list =  dec_carray.astype(int)
        #prin("As integer ist",dec_list)
        done = dec_list.reshape(-1)
        #prin("Straight line",done)
        dece_array = np.squeeze(np.asarray(done))
        #prin("Decrypted list",dece_array)

        # Translate the characters of the decrypted list in to a message, transform the list in to a steady string
        decrypted_mes = [chr(num) for num in dece_array]
        self.decrypted_message = ''.join(map(str, decrypted_mes))
        #return decrypted_message
        #prin("Output",decrypted_message)

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
            prin("Encrypted list",encryptin.encrypted_list)
        prin("Encrypted matrix", encryptin.matrix_to_decrypt)

    def getdec(self, decryptable_msg):
        self.decryptable_msg = input("What is the code that needs to be decrypted?: ")
    
    def afterdec(self, decryptin):
        prin("Decrypted message", decryptin.decrypted_message)

def _main():  # _ at start of name to hint that this should be treated as a private function
    key = KEY  # something
    enc_txt = 'soon text'
    decbl_msg = None
    show_list = None

    input_thing = Inpute(enc_txt, show_list, decbl_msg)
    input_thing.get(enc_txt, show_list)
    encrypting = Encrypt(input_thing.encryptable_txt, key, None, None, None)
    encrypting.encryption(input_thing.encryptable_txt, key, None, None, None)
    #print(encrypting.encrypted_list)
    #print(show_list)
    #print(encrypting.encrypted_list)
    input_thing.after(show_list, encrypting)
    #input_thing.getdec(None)
    #print(encrypting.matrix_to_decrypt)
    
    decrypting = Decrypt(key, None)
    decrypting.decryption(encrypting, key, None)
    #With input:
    """
    decrypting = Decrypt(key, None)
    decrypting.decryption(input_thing, key, None)
    """
    input_thing.afterdec(decrypting)

if __name__ == "__main__":
    _main()