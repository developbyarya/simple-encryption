from gacrypt import GAcrypt

string = "arya123"

gacrypt = GAcrypt()

encrypt = gacrypt.encrypt(string)
print(encrypt)
print(gacrypt.decrypt(encrypt))