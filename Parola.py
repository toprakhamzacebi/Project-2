import random
karakter1="+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
uzunluks = int(input("Şifremizin uzunluğu ne olsun?"))
parola= ""
for i in range (uzunluks):
    parola=parola+random.choice(karakter1)
print("Oluşturulan parola",parola)
