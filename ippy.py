#!/usr/bin/python

########################### <--Creado por MrRecoveryy-->

import os
import urllib2
import json


os.system("reset")

   

print "\033[93m  _____ _____  _______     __"
print "\033[93m |_   _|  __ \|  __ \ \   / / "
print "\033[93m   | | | |__) | |__) \ \_/ /"
print "\033[93m   | | |  ___/|  ___/ \   /"
print "\033[93m  _| |_| |    | |      | | - MrRecoveryy"
print "\033[93m |_____|_|    |_|      |_|\n"

while True:
	print "\033[93m --------------------------------------"
	print "\033[93m -> No me hago responsable del mal uso."
        print "\033[93m --------------------------------------"
        print "\033[93m                                     "
	ip=raw_input("\033[93m Direccion IP: ")
	url = "http://ip-api.com/json/"
	response = urllib2.urlopen(url + ip)
	datos = response.read()
	values = json.loads(datos)
	os.system("reset")
	
        print "\033[93m  _____ _____  _______     __"
        print "\033[93m |_   _|  __ \|  __ \ \   / /"
        print "\033[93m   | | | |__) | |__) \ \_/ /"
        print "\033[93m   | | |  ___/|  ___/ \   /"
        print "\033[93m  _| |_| |    | |      | |"
        print "\033[93m |_____|_|    |_|      |_|"

        print "\033[93m ---------------------------------"
	
	print("\033[93m" + "\n IP: \033[91m" + values['query'])
	print("\033[93m" + " Status: \033[92m" + values['status'])
	print("\033[93m" + " Region: \033[91m" + values['regionName'])
	print("\033[93m" + " Pais: \033[91m" + values['country'])
	print("\033[93m" + " Ciudad: \033[91m" + values['city'])
	print("\033[93m" + " ISP: \033[91m" + values['isp'])
	print("\033[93m" + " Lat,Lon: \033[91m" + str(values['lat']) + "," + str(values['lon']))
	print("\033[93m" + " Codigo Postal: \033[91m" + values['zip'])
	print("\033[93m" + " TimeZone: \033[91m" + values['timezone'])
	print("\033[93m" + " AS: \033[91m" + values['as'] + "\n")

	print("\033[93m \n")

	break