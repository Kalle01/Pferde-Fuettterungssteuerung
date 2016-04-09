#Ausgangszustand: Station ist leer, Nachlaufsperre befindet sich in Stellung offen

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

#Identifiziere Pferd und Anlage
If AnweSensor1 = 0:
Schau nach dem RFIDLeser

#Einlesen der Transpondernummer im Futtergang 
Input (RFIDNr)
Input (AnlagenNummer)
RFIDNr=1234567890123456
AnlagenNummer=Z0

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

#Schaue via SQL Statement in der DB Tabelle Fuetterungsprotokoll nach, wieviel Futter das Pferd heute und in den letzten 60 Minuten schon bekommen hat und fülle die Pferde Variablen

LetztesFutterDatum=01.01.2016
LetzteFutterZeit=00:00:00
MengeStd=0
ZuteilungFutter1aufgelaufen=0
ZuteilungFutter2aufgelaufen=0
ZuteilungFutter3aufgelaufen=0
ZuteilungFutter4aufgelaufen=0
ZuteilungHeuZeitaufgelaufen=0

#Zentrale Fütterungslogik

#Zuerst das Heu

if Heu-J-N=True:
	print ("Pferd ", PferdeName, " bekommt Heu")
	FunkHeuTuer(AnlagenNummer)# hier folgt die Function FunkHeuTuer öffnen mit Parameter Anlage in dem das Pferd steht
	
elif HeuZeit/VerteilZeit*(ZyklusStart-AktZeit) >ZuteilungHeuZeit and AnlagenNummer = H1-9:
	print ("Pferd ", PferdeName, " bekommt ", Futter2Name)
	FunkHeuSchieber(AnlagenNummer)# hier folgt die Function FunkHeuSchieber 1 füttern mit Parameter Anlage in dem das Pferd steht
else:
	print ("Pferd ", PferdeName, " bekommt zur Zeit kein Heu ")	
	
	
#Jetzt das Kraftfutter	

if AnlagenNummer = (Z0, K0-K9) and MengeStd <= MaximaleMengeKF:
	if MengeFutter1/VerteilZeit*(ZyklusStart-AktZeit) + Futter1Gewicht >=ZuteilungFutter1aufgelaufen and AktZeit - LetzteFutterZeit >= Fresspause:
		# Schließen der Nachlaufsperre
		FunkNachlauf(AnlagenNummer) # hier folgt die Function FunkNachlauf mit Parameter Anlage in dem das Pferd steht
		print ("Pferd ", PferdeName, " bekommt ", Futter1Name, "Fütterung läuft")
		FunkMotor(Motor1, AnlagenNummer) # hier folgt die Function FunkMotor füttern mit Parameter Anlage in dem das Pferd steht und Ansteuerung Motor1
		# Datensatz Datum, Uhrzeit, Menge Schneckenumdrehung Futter1, Futterart in DB Tabelle Fütterungsprotokoll speichern
		save to DB AktZeit PferdeID Futter1Gewicht Futter1Name
		
	elif MengeFutter2/VerteilZeit*(ZyklusStart-AktZeit) + Futter2Gewicht >=ZuteilungFutter2aufgelaufen and AktZeit - LetzteFutterZeit >= Fresspause:
		# Schließen der Nachlaufsperre
		FunkNachlauf(AnlagenNummer) # hier folgt die Function FunkNachlauf mit Parameter Anlage in dem das Pferd steht
		print ("Pferd ", PferdeName, " bekommt ", Futter2Name, "Fütterung läuft")
		FunkMotor(Motor2, AnlagenNummer)# hier folgt die Function FunkMotor füttern mit Parameter Anlage in dem das Pferd steht und Ansteuerung Motor2
		# Datensatz Datum, Uhrzeit, Menge Schneckenumdrehung Futter2, Futterart in DB Tabelle Fütterungsprotokoll speichern
		save to DB AktZeit PferdeID Futter2Gewicht Futter2Name
		
	elif MengeFutter3/VerteilZeit*(ZyklusStart-AktZeit) + Futter3Gewicht >=ZuteilungFutter3aufgelaufen and AktZeit - LetzteFutterZeit >= Fresspause:
		# Schließen der Nachlaufsperre
		FunkNachlauf(AnlagenNummer) # hier folgt die Function FunkNachlauf mit Parameter Anlage in dem das Pferd steht
		print ("Pferd ", PferdeName, " bekommt ", Futter3Name, "Fütterung läuft")
		FunkMotor(Motor3, AnlagenNummer)# hier folgt die Function FunkMotor füttern mit Parameter Anlage in dem das Pferd steht und Ansteuerung Motor3
		# Datensatz Datum, Uhrzeit, Menge Schneckenumdrehung Futter3, Futterart in DB Tabelle Fütterungsprotokoll speichern
		save to DB AktZeit PferdeID Futter3Gewicht Futter3Name
	
	# Futter 4 ist besonders. Dieses wird immer „zeitgleich“ zu einem anderen Futter gefüttert. Hier ist, wenn vorhanden, der Mineralfutterbehälter anzuschließen
	elif MengeFutter4/VerteilZeit*(ZyklusStart-AktZeit) + Futter4Gewicht >=ZuteilungFutter4aufgelaufen:
		# Schließen der Nachlaufsperre
		FunkNachlauf(AnlagenNummer) # hier folgt die Function FunkNachlauf mit Parameter Anlage in dem das Pferd steht
		print ("Pferd ", PferdeName, " bekommt ", Futter4Name, "Fütterung läuft")
		FunkMotor(Motor4, AnlagenNummer)# hier folgt die Function FunkMotor füttern füttern mit Parameter Anlage in dem das Pferd steht und Ansteuerung Motor4
		# Datensatz Datum, Uhrzeit, Menge Schneckenumdrehung Futter4, Futterart in DB Tabelle Fütterungsprotokoll speichern
		save to DB AktZeit PferdeID Futter4Gewicht Futter4Name
		
	else:
		print ("Pferd ", PferdeName, " hat keinen Anspruch auf Kraftfutter")	
else:
	print ("Pferd ", PferdeName, " hat keinen Anspruch auf Kraftfutter")	
function OeffneNachlaufsperre(AnlagenNummer) 