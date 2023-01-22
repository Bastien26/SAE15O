import csv
import matplotlib.pyplot as plt

#Seuils de connexion
CONNECTION_THRESHOLD = 1000
IP_THRESHOLD = 50

ip_count = {}

#ouverture de Tableau.csv
with open('Tableau.csv') as csvfile :
     #mise en place d'un lecteur csv
     reader = csv.DictReader(csvfile)
     #Boucle qui va regarder 1 a 1 les ligne du tableau
     for row in reader:
          #Extraction de l'ip source
          source_ip = row['SOURCE']
          #verifie si l'ip existe dans le dictionnaire
          if source_ip in ip_count:
               ip_count[source_ip] +=1
               #Si c'est le cas le compteur ajoute 1
          else :
               #sinon il l'ajoute au dictionnaire
               ip_count[source_ip] = 1
#Creation d'une variable qui va stockerle totale de connexion
connection_count = 0
#crée une boucle des ip comptés au préalable
for ip, count in ip_count.items():
     #Ajoute 1 au compteur de connexion
     connection_count += count

     #Vérifie si le compte d'ip a dépasser le seuil
     if count > IP_THRESHOLD:
          print(f"Possible attaque DDOS de {ip} avec {count} connexions")
#verifie que le compte totale n'est pas dépassé le seuil
if connection_count > CONNECTION_THRESHOLD:
     print(f"Possible attaque DDOS: {connection_count} connexions")
else :
     print("Pas de connexion anormale détecté")

# Tracage des données
ips = [ip for ip, count in ip_count.items() if count > IP_THRESHOLD]
counts = [count for count in ip_count.values() if count > IP_THRESHOLD]
plt.bar(ips, counts)
plt.xlabel('Adresse IP')
plt.ylabel('Nombre de connexion')
plt.show()