#Enigme 1
#Trouver le premier nombre entier dont le sha512 de la représentation textuelle commence par 6 "a" consécutifs en représentation hexadécimale
#(Ressemble au principe de base du minage de bitcoin)
#Solution: 35318008
import hashlib

for i in range(1000000000):
	a=hashlib.sha512(bytes(str(i), encoding='utf8')).hexdigest()
	
	if a[0:6]=="aaaaaa":
		print(str(i))
		break	