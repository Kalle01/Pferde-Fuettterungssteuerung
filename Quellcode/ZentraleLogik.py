#Variablen

VerteilZeit=20
ZyklusStart=00:00:00
AktZeit=10:00:00

Futter1Name="Hafer"
Futter1Gewicht=20
Futter2Name="Müsli"
Futter3Gewicht=40
Futter3Name="Kräuterfutter"
Futter3Gewicht=40
Futter4Name="Mineralfutter"
Futter4Gewicht=5

MaximaleMengeKF=500

#Identifiziere Pferd
#Einlesen der Transpondernummer im Futtergang 
Input (RFIDNr)
RFIDNr=1234567890123456

#Schaue in der DB Tabelle Pferdenamen nach welches Pferd der RFIDNr entspricht und fülle die Pferde Variablen

PferdeID =10
PferdeName="Donna"
Fresspause=20
PferdeBild=10
MengeFutter1=1000
MengeFutter2=1000
MengeFutter3=1000
MengeFutter4=10
Heu-J-N=True
HeuZeit=240

#Schaue in der DB Tabelle Fuetterungsprotokoll nach wieviel Futter das Pferd heute schon bekommen hat und fülle die Pferde Variablen

LetztesFutterDatum=01.01.2016
LetzteFutterZeit=00:00:00
ZuteilungFutter1=0
ZuteilungFutter2=0
ZuteilungFutter3=0
ZuteilungFutter4=0
HeuraumZutritt=False
ZuteilungHeuZeit=0

 
#Zentrale Fütterungslogik

#Zuerst das Heu

if Heu-J-N=True:
	print ("Pferd ", PferdeName, " bekommt Heu")
	FunkHeuTuer(1)# hier folgt die Function FunkHeuTuer 1 öffnen
	
elif HeuZeit/VerteilZeit*(ZyklusStart-AktZeit) >ZuteilungHeuZeit:
	print ("Pferd ", PferdeName, " bekommt ", Futter2Name)
	FunkHeuSchieber(1)# hier folgt die Function FunkHeuSchieber 1 füttern	

else:
	print ("Pferd ", PferdeName, " bekommt zur Zeit kein Heu ")	
	
	
#Jetzt das Kraftfutter	

if AktZeit - LetzteFutterZeit >= Fresspause and MengeStd <= MaximaleMengeKF:
	if MengeFutter1/VerteilZeit*(ZyklusStart-AktZeit) + Futter1Gewicht >=ZuteilungFutter1:
		print ("Pferd ", PferdeName, " bekommt ", Futter1Name)
		FunkMotor(Motor1) # hier folgt die Function FunkMotor füttern mit Ansteuerung Motor1
		save to DB AktZeit PferdeID Futter1Gewicht 
		# Datensatz Datum, Uhrzeit, Menge Schneckenumdrehung Futter1, Futterart in DB Tabelle Fütterungsprotokoll speichern
		
	elif MengeFutter2/VerteilZeit*(ZyklusStart-AktZeit) + Futter2Gewicht >=ZuteilungFutter2:
		print ("Pferd ", PferdeName, " bekommt ", Futter2Name)
		FunkMotor(Motor2)# hier folgt die Function FunkMotor füttern mit Ansteuerung Motor2
		save to DB AktZeit PferdeID Futter2Gewicht
		# Datensatz Datum, Uhrzeit, Menge Schneckenumdrehung Futter2, Futterart in DB Tabelle Fütterungsprotokoll speichern

	
	elif MengeFutter3/VerteilZeit*(ZyklusStart-AktZeit) + Futter3Gewicht >=ZuteilungFutter3:
		print ("Pferd ", PferdeName, " bekommt ", Futter3Name)
		FunkMotor(Motor3)# hier folgt die Function FunkMotor füttern mit Ansteuerung Motor3
		save to DB AktZeit PferdeID Futter3Gewicht
		# Datensatz Datum, Uhrzeit, Menge Schneckenumdrehung Futter3, Futterart in DB Tabelle Fütterungsprotokoll speichern

	
	elif MengeFutter4/VerteilZeit*(ZyklusStart-AktZeit) + Futter4Gewicht >=ZuteilungFutter4:
		print ("Pferd ", PferdeName, " bekommt ", Futter4Name)
		FunkMotor(Motor4)# hier folgt die Function FunkMotor füttern mit Ansteuerung Motor 4
		save to DB AktZeit PferdeID Futter1Gewicht
		# Datensatz Datum, Uhrzeit, Menge Schneckenumdrehung Futter4, Futterart in DB Tabelle Fütterungsprotokoll speichern


	else:
		print ("Pferd ", PferdeName, " hat keinen Anspruch auf Kraftfutter")	
else:
	print ("Pferd ", PferdeName, " hat keinen Anspruch auf Kraftfutter")	
