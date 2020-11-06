import math
def chiffrement(m,a,b):
	m = m.upper()
	crypted = ""
	for l in m:
		cl = (a * ( ord(l) - 65 ) + b)%26 + 65
		crypted += chr(cl)
	return crypted


def euclide(a,b):
	r = a
	u = 1
	v = 0

	rp = b
	up = 0
	vp = 1

	while rp != 0:
		q = r//rp

		i = r
		j = u
		k = v

		r = rp
		u = up
		v = vp

		rp = i - q*rp
		up = j - q*up
		vp = k - q*vp
	if u < 0:
		u = u + b

	return r,u




def dechiffrement(m,a,b):
	m = m.upper()
	word = ""
	pgcd, inv_a = euclide(a,26)
	if pgcd == 1:
		for y in m:
			x = (inv_a*((ord(y)-65)-b)%26)+65
			word += chr(x)
	else:
		word = "Dechiffrement impossible"
	return word 


# a = 17
# b = 56

# crypted = chiffrement("POLYTECHANGERS",a,b)
# decrypted = dechiffrement(crypted,a,b)

# print("Message chiffre : " + crypted)
# print("Message dechiffre : " + decrypted)