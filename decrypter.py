import os
import pyaes 

# abrindo o arquivo criptografado
file_name = "teste.txt"
file = open(file_name, "rb")
file_data = file.read()
file.close()

# chave para descriptografia
key = b"testeransomwares"
aes = pyaes.AESModeOfOperationCTR(key)
decrypt_data = aes.decrypt(file_data)

# removendo o arquivo que foi criptografado
os.remove(file_name)

# criando o arquivo que foi descriptografado
new_file = "teste.txt"
new_file = open(f'{new_file}', "wb")
new_file.write(decrypt_data)
new_file.close()
