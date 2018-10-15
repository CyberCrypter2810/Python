#binarystring.py gbpm
def bincon(decimal):
	print(decimal)
	print("**********")
	binstr = "" # binstr is a string
	for i in range(8):
		bin = decimal % 2
		decimal = decimal // 2
		#print(bin)
		binstr = binstr + str(bin)
		print(binstr)
	print("------------")
	#binstr = "".join(reversed(binstr))
	print(binstr)

def main():
	print("IMPUT -1 TO EXIT THE PROGRAM")
	print("IMPUT A POSITIVE INTEGER LESS THAN 256")
	done = 0
	while (done >= 0):
		dec = input("INPUT AN INTEGER : ")
		bincon(dec)
		print("done",done)
		done = dec

main()
