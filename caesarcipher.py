from collections import OrderedDict
import string

Dec_disk = OrderedDict(zip(range(2,28),string.ascii_uppercase ))
Enc_disk = OrderedDict(zip(range(0,26),string.ascii_uppercase ))
disk = OrderedDict(zip(string.ascii_uppercase,range(0,26) )) #disk to get the key index and the index of exach letter of plain text
key_index=0 

print("please input the text")
input_text = input().upper() #input the plain or 

print("input the encryption key or decryption key")
key = input().upper()
key_index = disk[key]

print("input the modee , encryption : mode 0 , decryption : mode 1")
mode=input()

sentence_index= []
Enc_text=[]
Dec_text=[]


for i in input_text:
	sentence_index.append(disk[i])



def Enc():
	for i in sentence_index:
		if i == ' ':
			Enc_text.append(' ')
		else:
			disk_i = (i + key_index) % 26
			Enc_text.append(ord(Enc_disk[disk_i]))
	for i in Enc_text:
		if i == ' ':
			Enc_text[Enc_text(i)] = ' '
		else:
			Enc_text[Enc_text.index(i)] = chr(i)	
	


def Dec():
	for i in sentence_index:
		if i == ' ':
			Dec_text.append(' ')
		else:
			disk_i = (i + key_index) % 26
			Dec_text.append(ord(Dec_disk[disk_i]))
	for i in Dec_text:
		Dec_text[Dec_text.index(i)] = chr(i)	


if __name__ == "__main__":
	if mode == '0':
		Enc()
		Enc_text = ''.join(Enc_text)
		print(Enc_text)
	elif mode == '1':
		Dec()
		Dec_text = ''.join(Dec_text)
		print(Dec_text)
	else:
		print("why")







