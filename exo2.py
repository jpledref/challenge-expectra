#Enigme 2
#Le code a été généré entre le 25 Juillet 2019 à 16h55 et 45s et le 26 Juillet 2019 à 18h26 et 50s à Paris.
#Il s'agit d'un md5 (en représentation hexadécimale) de l'heure à laquelle il a été généré - heure au format suivant : YYMMDDHHmmss exprimée dans l'heure locale.
#La première heure est ainsi : 190725165545
#Les 4 premières lettres de ce code ont la particularité d'être égales aux 4 dernières
#Solution: d5fc927dcdbb0a21e85e2759f6bbd5fc

import datetime
import hashlib

a = datetime.datetime.strptime('2019-07-25 16:55:45', '%Y-%m-%d %H:%M:%S')
b = datetime.datetime.strptime('2019-07-26 18:26:50', '%Y-%m-%d %H:%M:%S')

for i in range(int(a.strftime('%y%m%d%H%M%S')),int(b.strftime('%y%m%d%H%M%S'))):
	h=hashlib.md5(bytes(str(i), encoding='utf8')).hexdigest()	
	if(h[0:4]==h[-4:]):		
		try:
			v=datetime.datetime.strptime(str(i), '%y%m%d%H%M%S')
			print(h)
			exit(0)
		except:
			continue