from affine import euclide

def phi_n(p,q):
	return (p-1) * (q-1)


def ClePublique(p,q,e):
	n = p*q
	public = [n,e]
	return public

def ClePrivee(phi_n,e):
	d = euclide(e,phi_n)[1]
	return d


def Chiffrement(m,clepublique):
	m = m.upper()
	trame = []

	B = []
	C = []

	for c in m:
		idx = ord(c) - 65
		if idx < 10:
			trame.append(0)
			trame.append(idx)
		else:
			trame.append(int(idx/10))
			trame.append(idx%10)
	print("Chiffres isoles : " + str(trame))



	for i in reversed(range(0,len(trame),3)):
		if i > 2:
			B.append(trame[i-2]*100 + trame[i-1]*10 + trame[i])
		elif i > 1:
			B.append(trame[i-1]*10 + trame[i])
		else:
			B.append(trame[i])
	B.reverse()
	print("Triplets : " + str(B))

	for b in B:
		C.append( (b**clepublique[1])%clepublique[0] )

	print("Crypted : " + str(C))

	return C



def Dechiffrement(m, cleprivee,clepublique):
	D = []
	for c in m:
		D.append( (c**cleprivee)%clepublique[0] )
	print("Decrypted : " + str(D))

	trame = []
	for d in D:
		if d in range(0,10):
			trame.append(0)
			trame.append(0)
			trame.append(d)
		elif d in range(10,100):
			trame.append(0)
			trame.append(int(d/10))
			trame.append(d%10)
		else:
			trame.append(int(d/100))
			trame.append( int((d%100)/10) )
			trame.append((d%100)%10)
	

	print("Trame :" + str(trame))

	message = []
	for i in reversed(range(0,len(trame),2)):
		if i > 1:
			message.append(trame[i]*10 + trame[i+1])
	message.reverse()
	print("Rang lettre : " + str(message))
	
	final = ""
	for m in message:
		final += chr(m+65)

	return final


p = 53
q = 11
e = 3
 
Cpu = ClePublique(p,q,e)
#print("Cle Publique : " + str(Cpu))
Cpr  = ClePrivee(phi_n(p,q),e)
#print("Cle Privee : " + str(Cpr))

s = "POLYTECHANGERS"
C = Chiffrement(s,Cpu)
D = Dechiffrement(C,Cpr,Cpu)
print("Décrypté : " + D)