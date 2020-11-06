def chiffrement(m,k): # m : message - k : clé
	crypted = ""
	m = m.upper() #on passe le message en majuscule
	for l in m:
		# le code ascii doit rester entre 65 & 90
		cl = ( ord(l) - 65 + k )%26 + 65
		crypted += chr(cl)
	return crypted


def dechiffrement(m):
	m = m.upper()
	decrypted = []
	for i in range(0,26):
		word = ""		
		for l in m:
			dl = (ord(l) - 65 - i)%26 + 65
			word += chr(dl)
		decrypted.append(word)
	return decrypted



s = chiffrement("POLYTECHANGERS",14)
print("Message chiffré : ",s)

tos = dechiffrement("MILOBCOMZYVIDOMRKXQOBC")
print("BruteForce : \n",tos)