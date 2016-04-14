# Startsequenz / Einlesen relevanter Daten und Parameter

# Einlesen der eigen IP Adresse
# Setzen der eigenen IP Adresse im Rechner

# Einlesen der Datenpfades
DatenPfad = 199.199.199.1

# Einlesen der Zeit
if Netzwerkverbindung vorhanden:
	AktZeit=10:00:00
# Starte Zeitabfrage via Menü

# Einlesen der AnlagenNummer

AnlagenNummer = Z0

if AnlagenNummer[0]="Z":
	
	# Einlesen der Zentralstationsparameter
	
	TitelTextString=DatenPfad Tabelle BasisParameter Feld 
	AdminName=DatenPfad Tabelle BasisParameter Feld AdminName
	Passwort=DatenPfad Tabelle BasisParameter Feld Passwort
	AutoLogOff=DatenPfad Tabelle BasisParameter Feld AutoLogOff
	LichtAus=DatenPfad Tabelle BasisParameter Feld LichtAus
	AlarmschwelleKF=DatenPfad Tabelle BasisParameter Feld AlarmschwelleKF
	AlarmschwelleHeu=DatenPfad Tabelle BasisParameter Feld AlarmschwelleHeu
	
	VerteilZeit=DatenPfad Tabelle BasisParameter Feld VerteilZeit
	ZyklusStart=DatenPfad Tabelle BasisParameter Feld ZyklusStart
	ZeitOErkennung=DatenPfad Tabelle BasisParameter Feld ZeitOErkennung
	SchutzZeit=DatenPfad Tabelle BasisParameter Feld SchutzZeit
	MaximaleMengeKF=DatenPfad Tabelle BasisParameter Feld MaximaleMengeKF
	
	InklusiveTor=DatenPfad Tabelle BasisParameter Feld InklusiveTor
	InklusiveNachlauf=DatenPfad Tabelle BasisParameter Feld InklusiveNachlauf
	InklusiveFutterVorrat=DatenPfad Tabelle BasisParameter Feld InklusiveFutterVorrat
	InklusiveFutter2=DatenPfad Tabelle BasisParameter Feld InklusiveFutter2
	InklusiveFutter3=DatenPfad Tabelle BasisParameter Feld InklusiveFutter3
	InklusiveFutter4=DatenPfad Tabelle BasisParameter Feld InklusiveFutter4
	
	Futter1Name=DatenPfad Tabelle BasisParameter Feld Futter1Name
	Futter1Gewicht=DatenPfad Tabelle BasisParameter Feld Futter1Gewicht
	Motor1blockiert=DatenPfad Tabelle BasisParameter Feld Motor1blockiert
	if InklusiveFutterVorrat = true:
		Futter1VorratMin=DatenPfad Tabelle BasisParameter Feld Futter1VorratMin
		
	if InklusiveFutter2= true:
		Futter2Name=DatenPfad Tabelle BasisParameter Feld Futter2Name
		Futter2Gewicht=DatenPfad Tabelle BasisParameter Feld Futter2Gewicht
		Motor2blockiert=DatenPfad Tabelle BasisParameter Feld Motor2blockiert
		if InklusiveFutterVorrat = true:
			Futter2VorratMin=DatenPfad Tabelle BasisParameter Feld Futter2VorratMin
		
	elif InklusiveFutter3 = true:
		Futter3Name=DatenPfad Tabelle BasisParameter Feld Futter3Name
		Futter3Gewicht=DatenPfad Tabelle BasisParameter Feld Futter3Gewicht
		Motor3blockiert=DatenPfad Tabelle BasisParameter Feld Motor3blockiert
		if InklusiveFutterVorrat = true:
			Futter3VorratMin=DatenPfad Tabelle BasisParameter Feld Futter3VorratMin
		
	elif InklusiveFutter4 = true:
		Futter4Name=DatenPfad Tabelle BasisParameter Feld Futter4Name
		Futter4Gewicht=DatenPfad Tabelle BasisParameter Feld Futter4Gewicht
		Motor4blockiert=DatenPfad Tabelle BasisParameter Feld Motor4blockiert
		if InklusiveFutterVorrat = true:
			Futter4VorratMin=DatenPfad Tabelle BasisParameter Feld Futter4VorratMin
		
	elif InklusiveNachlauf = true:
		Motor5Ablockiert=DatenPfad Tabelle BasisParameter Feld Motor5Ablockier
		Motor5Zblockiert=DatenPfad Tabelle BasisParameter Feld Motor5Zblockiert
		
	elif InklusiveTor = true:
		Motor6Ablockiert=DatenPfad Tabelle BasisParameter Feld Motor6Ablockiert
		Motor6Zblockiert=DatenPfad Tabelle BasisParameter Feld Motor6Zblockiert
	
elif AnlagenNummer[0] = "K":

	# Einlesen der Kraftfutterparameter
	
	VerteilZeit=DatenPfad Tabelle BasisParameter Feld VerteilZeit
	ZyklusStart=DatenPfad Tabelle BasisParameter Feld ZyklusStart
	ZeitOErkennung=DatenPfad Tabelle BasisParameter Feld ZeitOErkennung
	SchutzZeit=DatenPfad Tabelle BasisParameter Feld SchutzZeit
	MaximaleMengeKF=DatenPfad Tabelle BasisParameter Feld MaximaleMengeKF
	
	InklusiveNachlauf=DatenPfad Tabelle KFParameter Feld InklusiveNachlauf where Datensatz = AnlagenNummer
	InklusiveFutterVorrat=DatenPfad Tabelle KFParameter Feld InklusiveFutterVorrat where Datensatz = AnlagenNummer
	InklusiveFutter2=DatenPfad Tabelle KFParameter Feld InklusiveFutter2 where Datensatz = AnlagenNummer
	InklusiveFutter3=DatenPfad Tabelle KFParameter Feld InklusiveFutter3 where Datensatz = AnlagenNummer
	InklusiveFutter4=DatenPfad Tabelle KFParameter Feld InklusiveFutter4 where Datensatz = AnlagenNummer
	
	Futter1Name=DatenPfad Tabelle KFParameter Feld Futter1Name where Datensatz = AnlagenNummer
	Futter1Gewicht=DatenPfad Tabelle KFParameter Feld Futter1Gewicht where Datensatz = AnlagenNummer
	Motor1blockiert=DatenPfad Tabelle KFParameter Feld Motor1blockiert where Datensatz = AnlagenNummer
	if InklusiveFutterVorrat = true:
		Futter1VorratMin=DatenPfad Tabelle KFParameter Feld Futter1VorratMin where Datensatz = AnlagenNummer
		
	if InklusiveFutter2= true:
		Futter2Name=DatenPfad Tabelle KFParameter Feld Futter2Name where Datensatz = AnlagenNummer
		Futter2Gewicht=DatenPfad Tabelle KFParameter Feld Futter2Gewicht where Datensatz = AnlagenNummer
		Motor2blockiert=DatenPfad Tabelle KFParameter Feld Motor2blockiert where Datensatz = AnlagenNummer
		if InklusiveFutterVorrat = true:
			Futter2VorratMin=DatenPfad Tabelle KFParameter Feld Futter2VorratMin where Datensatz = AnlagenNummer
		
	elif InklusiveFutter3 = true:
		Futter3Name=DatenPfad Tabelle KFParameter Feld Futter3Name where Datensatz = AnlagenNummer
		Futter3Gewicht=DatenPfad Tabelle KFParameter Feld Futter3Gewicht where Datensatz = AnlagenNummer
		Motor3blockiert=DatenPfad Tabelle KFParameter Feld Motor3blockiert where Datensatz = AnlagenNummer
		if InklusiveFutterVorrat = true:
			Futter3VorratMin=DatenPfad Tabelle KFParameter Feld Futter3VorratMin where Datensatz = AnlagenNummer
		
	elif InklusiveFutter4 = true:
		Futter4Name=DatenPfad Tabelle KFParameter Feld Futter4Name where Datensatz = AnlagenNummer
		Futter4Gewicht=DatenPfad Tabelle KFParameter Feld Futter4Gewicht where Datensatz = AnlagenNummer
		Motor4blockiert=DatenPfad Tabelle KFParameter Feld Motor4blockiert where Datensatz = AnlagenNummer
		if InklusiveFutterVorrat = true:
			Futter4VorratMin=DatenPfad Tabelle KFParameter Feld Futter4VorratMin where Datensatz = AnlagenNummer
		
	elif InklusiveNachlauf = true:
		Motor5Ablockiert=DatenPfad Tabelle KFParameter Feld Motor5Ablockier where Datensatz = AnlagenNummer
		Motor5Zblockiert=DatenPfad Tabelle KFParameter Feld Motor5Zblockiert where Datensatz = AnlagenNummer
	
elif AnlagenNummer[0] = "T":
	
	# Einlesen der Torparameter
	
	VerteilZeit=DatenPfad Tabelle BasisParameter Feld VerteilZeit
	ZyklusStart=DatenPfad Tabelle BasisParameter Feld ZyklusStart
	ZeitOErkennung=DatenPfad Tabelle BasisParameter Feld ZeitOErkennung
	SchutzZeit=DatenPfad Tabelle BasisParameter Feld SchutzZeit
	MaximaleMengeKF=DatenPfad Tabelle BasisParameter Feld MaximaleMengeKF
	
	Motor5Ablockiert=DatenPfad Tabelle TorParameter Feld Motor5Ablockier where Datensatz = AnlagenNummer
	Motor5Zblockiert=DatenPfad Tabelle TorParameter Feld Motor5Zblockiert where Datensatz = AnlagenNummer
	
	Motor6Ablockiert=DatenPfad Tabelle TorParameter Feld Motor6Ablockiert where Datensatz = AnlagenNummer
	Motor6Zblockiert=DatenPfad Tabelle TorParameter Feld Motor6Zblockiert where Datensatz = AnlagenNummer
	
elif AnlagenNummer[0] = "H":
	
	# Einlesen der Heuparameter
	
	VerteilZeit=DatenPfad Tabelle BasisParameter Feld VerteilZeit
	ZyklusStart=DatenPfad Tabelle BasisParameter Feld ZyklusStart
	ZeitOErkennung=DatenPfad Tabelle BasisParameter Feld ZeitOErkennung
	SchutzZeit=DatenPfad Tabelle BasisParameter Feld SchutzZeit
	MaximaleMengeKF=DatenPfad Tabelle BasisParameter Feld MaximaleMengeKF
	
	HeuTyp=DatenPfad Tabelle HeuParameter Feld HeuTyp where Datensatz = AnlagenNummer
	
	InklusiveNachlauf=DatenPfad Tabelle HeuParameter Feld InklusiveNachlauf where Datensatz = AnlagenNummer
	
	Motor5Ablockiert=DatenPfad Tabelle HeuParameter Feld Motor5Ablockier where Datensatz = AnlagenNummer
	Motor5Zblockiert=DatenPfad Tabelle HeuParameter Feld Motor5Zblockiert where Datensatz = AnlagenNummer
	
	if InklusiveNachlauf = true:
		Motor7Ablockiert=DatenPfad Tabelle HeuParameter Feld Motor7Ablockiert where Datensatz = AnlagenNummer
		Motor7Zblockiert=DatenPfad Tabelle HeuParameter Feld Motor7Zblockiert where Datensatz = AnlagenNummer
	
	
	
# Ausgangszustand: Station ist leer, Nachlaufsperre befindet sich in Stellung offen


# Identifiziere Pferd und ermittle Pferddaten


If AnweSensor1 = 0:
Schau nach dem RFIDLeser

# Einlesen der Transpondernummer im Futtergang 
Input (RFIDNr)
RFIDNr=1234567890123456

# Schaue in der DB Tabelle Pferdenamen nach welches Pferd der RFIDNr entspricht und fülle die Pferde Variablen

PferdeID =10
PferdeName="Donna"
Fresspause=20
PferdeBild=10
MengeFutter1=1000
MengeFutter2=1000
MengeFutter3=1000
MengeFutter4=10
TorT0Darf=True
TorT1Darf=True
TorT2Darf=True
TorT3Darf=True
HeuZeit1=240
HeuZeit2=240

# Schaue via SQL Statement in der DB Tabelle FuetterungsProtokoll nach, wieviel Futter das Pferd heute und in den letzten 60 Minuten schon bekommen hat und fülle die Pferde Variablen



LetzteKFFressZeit=00:00:00 30.06.2016
LetzteHeuFressZeit=00:00:00 30.06.2016
MengeStd=0
ZuteilungFutter1aufgelaufen=0
ZuteilungFutter2aufgelaufen=0
ZuteilungFutter3aufgelaufen=0
ZuteilungFutter4aufgelaufen=0
ZuteilungHeuZeit1aufgelaufen=0
ZuteilungHeuZeit2aufgelaufen=0



# Zentrale Fütterungslogik

# Zuerst die Selektionstore

if TorT0Darf=True and AnlagenNummer=Z0 and InklusiveTor=true:
	# Schließen der Nachlaufsperre
	if InklusiveNachlauf = true and Motor6AufKontakt = true
		FunkNachlauf() # hier folgt die Function FunkNachlauf
	print ("Pferd ", PferdeName, " bekommt Zugang Tor 0")
	FunkTorAuf() # hier folgt die Function FunkTorAuf öffnen
	
elif TorT1Darf=True and AnlagenNummer=T1:
	# Schließen der Nachlaufsperre
	if InklusiveNachlauf = true and Motor6AufKontakt = true
		FunkNachlauf() # hier folgt die Function FunkNachlauf
	print ("Pferd ", PferdeName, " bekommt Zugang Tor 1")
	FunkTorAuf() # hier folgt die Function FunkTorAuf öffnen
	
elif TorT2Darf=True and AnlagenNummer=T2:
	# Schließen der Nachlaufsperre
	if InklusiveNachlauf = true and Motor6AufKontakt = true
		FunkNachlauf() # hier folgt die Function FunkNachlauf
	print ("Pferd ", PferdeName, " bekommt Zugang Tor 2")
	FunkTorAuf() # hier folgt die Function FunkTorAuf öffnen
	
elif TorT3Darf=True and AnlagenNummer=T3:
	# Schließen der Nachlaufsperre
	if InklusiveNachlauf = true and Motor6AufKontakt = true
		FunkNachlauf() # hier folgt die Function FunkNachlauf
	print ("Pferd ", PferdeName, " bekommt Zugang Tor 3")
	FunkTorAuf() # hier folgt die Function FunkTorAuf öffnen	
	
else:
	print ("Pferd ", PferdeName, " bekommt keinen Zugang")


# Jetzt Heu und Silage	

if HeuZeit1/VerteilZeit*(ZyklusStart-AktZeit) >ZuteilungHeuZeit and AnlagenNummer = H1-9 and HeuTyp =1:
	# Schließen der Nachlaufsperre
	if InklusiveNachlauf = true and Motor6AufKontakt = true:
		FunkNachlauf() # hier folgt die Function FunkNachlauf
	print ("Pferd ", PferdeName, " bekommt ", Heu)
	LetzteHeu1FressZeit = AktZeit
	FunkHeuSchieber()# hier folgt die Function FunkHeuSchieber öffnen
else:
	print ("Pferd ", PferdeName, " bekommt zur Zeit kein Heu ")	
	
if HeuZeit2/VerteilZeit*(ZyklusStart-AktZeit) >ZuteilungHeuZeit and AnlagenNummer = H1-9 and HeuTyp =2:
	# Schließen der Nachlaufsperre
	if InklusiveNachlauf = true and Motor6AufKontakt = true:
		FunkNachlauf() # hier folgt die Function FunkNachlauf
	print ("Pferd ", PferdeName, " bekommt ", Silage)
	LetzteHeu2FressZeit = AktZeit
	FunkHeuSchieber()# hier folgt die Function FunkHeuSchieber öffnen
else:
	print ("Pferd ", PferdeName, " bekommt zur Zeit kein Heu ")	
	
	
# Jetzt das Kraftfutter	

if AnlagenNummer = (Z0, K0-K9) and MengeStd <= MaximaleMengeKF:
	if MengeFutter1/VerteilZeit*(ZyklusStart-AktZeit) + Futter1Gewicht >=ZuteilungFutter1aufgelaufen and AktZeit - LetzteFutterZeit >= Fresspause:
		# Schließen der Nachlaufsperre
		if InklusiveNachlauf = true and Motor6AufKontakt = true
			FunkNachlauf() # hier folgt die Function FunkNachlauf
		print ("Anlage ", AnlagenNummer, ": Pferd ", PferdeName, " bekommt ", Futter1Name, "Fütterung läuft")
		KFFresszeit = AktZeit
		FunkMotor(Motor1) # hier folgt die Function FunkMotor füttern mit Parameter Ansteuerung Motor1
		# Datensatz Datum, Uhrzeit, AnlagenNummer, PferdeID, Menge Schneckenumdrehung Futter1, Futter1Name in DB Tabelle FuetterungsProtokoll speichern
		save to DB Tabelle FuetterungsProtokoll AktZeit AnlagenNummer PferdeID Futter1Gewicht Futter1Name
		if InklusiveFutterVorrat = true and Futter1VorratMin > Futter1Vorrat: 
			print ("ACHTUNG ", Futter1Name, " in Anlage ", AnlagenNummer, " ist aufgebraucht" )
			# Datensatz Datum, Uhrzeit, AnlagenNummer print ("ACHTUNG ", Futter1Name, " in Anlage ", AnlagenNummer, " ist aufgebraucht" ) in DB Tabelle AnlagenProtokoll speichern
			save to DB Tabelle AnlagenProtokoll AktZeit AnlagenNummer (Futter1Name, " in Anlage ", AnlagenNummer, " ist aufgebraucht" ) 
	
	elif MengeFutter2/VerteilZeit*(ZyklusStart-AktZeit) + Futter2Gewicht >=ZuteilungFutter2aufgelaufen and AktZeit - LetzteFutterZeit >= Fresspause:
		# Schließen der Nachlaufsperre
		if InklusiveNachlauf = true and Motor6AufKontakt = true
			FunkNachlauf() # hier folgt die Function FunkNachlauf
		print ("Anlage ", AnlagenNummer, ": Pferd ", PferdeName, " bekommt ", Futter2Name, "Fütterung läuft")
		KFFresszeit = AktZeit
		FunkMotor(Motor2) # hier folgt die Function FunkMotor füttern mit Parameter Ansteuerung Motor2
		# Datensatz Datum, Uhrzeit, AnlagenNummer, PferdeID, Menge Schneckenumdrehung Futter2, Futter2Name in DB Tabelle FuetterungsProtokoll speichern
		save to DB Tabelle FuetterungsProtokoll AktZeit AnlagenNummer PferdeID Futter2Gewicht Futter2Name
		if InklusiveFutterVorrat = true and Futter2VorratMin > Futter2Vorrat: 
			print ("ACHTUNG ", Futter2Name, " in Anlage ", AnlagenNummer, " ist aufgebraucht" )
			# Datensatz Datum, Uhrzeit, AnlagenNummer print ("ACHTUNG ", Futter2Name, " in Anlage ", AnlagenNummer, " ist aufgebraucht" ) in DB Tabelle AnlagenProtokoll speichern
			save to DB Tabelle AnlagenProtokoll AktZeit AnlagenNummer (Futter2Name, " in Anlage ", AnlagenNummer, " ist aufgebraucht" ) 
		
	elif MengeFutter3/VerteilZeit*(ZyklusStart-AktZeit) + Futter3Gewicht >=ZuteilungFutter3aufgelaufen and AktZeit - LetzteFutterZeit >= Fresspause:
		# Schließen der Nachlaufsperre
		if InklusiveNachlauf = true and Motor6AufKontakt = true
			FunkNachlauf() # hier folgt die Function FunkNachlauf
		print ("Anlage ", AnlagenNummer, ": Pferd ", PferdeName, " bekommt ", Futter3Name, "Fütterung läuft")
		KFFresszeit = AktZeit
		FunkMotor(Motor3) # hier folgt die Function FunkMotor füttern mit Parameter Ansteuerung Motor3
		# Datensatz Datum, Uhrzeit, AnlagenNummer, PferdeID, Menge Schneckenumdrehung Futter3, Futter3Name in DB Tabelle FuetterungsProtokoll speichern
		save to DB Tabelle FuetterungsProtokoll AktZeit AnlagenNummer PferdeID Futter3Gewicht Futter3Name
		if InklusiveFutterVorrat = true and Futter3VorratMin > Futter3Vorrat: 
			print ("ACHTUNG ", Futter3Name, " in Anlage ", AnlagenNummer, " ist aufgebraucht" )
			# Datensatz Datum, Uhrzeit, AnlagenNummer print ("ACHTUNG ", Futter3Name, " in Anlage ", AnlagenNummer, " ist aufgebraucht" ) in DB Tabelle AnlagenProtokoll speichern
			save to DB Tabelle AnlagenProtokoll AktZeit AnlagenNummer (Futter3Name, " in Anlage ", AnlagenNummer, " ist aufgebraucht" ) 
		
	# Futter 4 ist besonders. Dieses wird immer „zeitgleich“ zu einem anderen Futter gefüttert. Hier ist, wenn vorhanden, der Mineralfutterbehälter anzuschließen
	elif MengeFutter4/VerteilZeit*(ZyklusStart-AktZeit) + Futter4Gewicht >=ZuteilungFutter4aufgelaufen:
		# Schließen der Nachlaufsperre
		if InklusiveNachlauf = true and Motor6AufKontakt = true	
			FunkNachlauf() # hier folgt die Function FunkNachlauf
		print ("Anlage ", AnlagenNummer, ": Pferd ", PferdeName, " bekommt ", Futter4Name, "Fütterung läuft")
		KFFresszeit = AktZeit
		FunkMotor(Motor4) # hier folgt die Function FunkMotor füttern füttern mit Parameter Ansteuerung Motor4
		# Datensatz Datum, Uhrzeit, AnlagenNummer, PferdeID, Menge Schneckenumdrehung Futter4, Futter4Name in DB Tabelle FuetterungsProtokoll speichern
		save to DB Tabelle FuetterungsProtokoll AktZeit AnlagenNummer PferdeID Futter4Gewicht Futter4Name
		if InklusiveFutterVorrat = true and Futter4VorratMin > Futter4Vorrat: 
			print ("ACHTUNG ", Futter4Name, " in Anlage ", AnlagenNummer, " ist aufgebraucht" )
			# Datensatz Datum, Uhrzeit, AnlagenNummer print ("ACHTUNG ", Futter4Name, " in Anlage ", AnlagenNummer, " ist aufgebraucht" ) in DB Tabelle AnlagenProtokoll speichern
			save to DB Tabelle AnlagenProtokoll AktZeit AnlagenNummer (Futter4Name, " in Anlage ", AnlagenNummer, " in Anlage ", AnlagenNummer, " ist aufgebraucht"  ) 
		
	else:
		print ("Pferd ", PferdeName, " hat keinen Anspruch auf Kraftfutter")	
else:
	print ("Pferd ", PferdeName, " hat keinen Anspruch auf Kraftfutter")


# Schließen Heuraumtür bzw. Selektionstor

if InklusiveTor = true and AktZeit - LetzteKFFressZeit >= SchutzZeit and Motor6ZuKontakt 0 false:
	
	FunkTorZu() # hier folgt die Function FunkTorZu


# Öffnen der Nachlaufsperre	
if InklusiveNachlauf = true and AktZeit - LetzteKFFressZeit > SchutzZeit or AktZeit - LetzteHeuFressZeit > SchutzZeitand and Motor5ZuKontakt = true and Motor6ZuKontakt 0 true
	
	OeffneNachlaufsperre() # hier folgt die Function OeffneNachlaufsperre