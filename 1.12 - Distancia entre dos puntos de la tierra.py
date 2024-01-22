from math import radians, cos, sin, asin, acos, sqrt

print("Introduce la latitud y longitud :")
lat1 = float(input(" Latitud 1:        "))
lon1 = float(input(" Longitud 1:       "))
lat2 = float(input(" Latitud 2:        "))
lon2 = float(input(" Longitud 2:       "))
 
lon1 = radians(lon1)
lon2 = radians(lon2)
lat1 = radians(lat1)
lat2 = radians(lat2)
 
dlon = lon2 - lon1 
dlat = lat2 - lat1 
a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
c = 2 * asin(sqrt(a)) 
r = 6371 
 

print('La distancia es:      %.2f.' %(c*r),'Kilometros')