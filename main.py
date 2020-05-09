print("""+---------------------------------------------------------+
| +----------------------------------------------------+  |
| |                                                    |  |
| |              CAESAR CIPHER DECRYPTOR               |  |
| |           DEVELOPED BY: JOURNEL CABRILLOS          |  |
| |       EMAIL: journelcabrillos@protonmail.com       |  |
| |                                                    |  |
| +----------------------------------------------------+  |
+---------------------------------------------------------+""")

#Libraries
import os
import sys
import time
from random import randint
#Declarations

dictionary = str.upper(open('words_alpha.txt', 'r').read())
x = []
key = 1
decipher = []
decipher_key = []
msg = str.upper(input("\n\nINPUT CIPHERTEXT: "))
msg_o = str()
decrypt = []
count = len(msg)
frequent_words = str.upper('the of and to at here cipher decryptor')
toolbar_width = 40
shift = int()
#PROGRAM STARTS HERE
sys.stdout.write("\n\n[BRUTEFORCE] PERFORMING DICTIONARY ATTACK: [%s]" % (" " * toolbar_width))
sys.stdout.flush()
sys.stdout.write("\b" * (toolbar_width + 1))

def findMaximum(word, pos):
    li=word.split()
    li=list(li)
    op=[]
    for i in li:
        op.append(len(i))
    if pos == 'max':
        l=op.index(max(op))
    elif pos == 'random':
        l  = randint(0, len(op) - 1)
    return (li[l])


for i in range(toolbar_width):
    time.sleep(0.1)
    while key < 26:
        for i in range(0, len(msg)):
            if msg[i].isupper() == True:
                shift = ord(msg[i]) - key
                if shift < 65:
                    shift += 26
                elif shift > 90:
                    shift -= 26
                x.append(shift)
            elif msg[i].isnumeric() == True:
                 x.append(ord(msg[i]))                         
            else:
                x.append(ord(msg[i]))
            msg_o = ''.join(map(chr,x))
            if len(msg_o) > count:
                msg_o = msg_o[-count:]
        decrypt.append(msg_o)
        key = key + 1
    sys.stdout.write("-")
    sys.stdout.flush()

sys.stdout.write("]\n")

for i in range(0, len(decrypt)):
    if dictionary.find(findMaximum(decrypt[i], "max")) != -1:
        decipher.append(decrypt[i])
        decipher_key.append(i + 1)
    else:
        if frequent_words.find(findMaximum(decrypt[i], "max")) != -1:
            decipher.append(decrypt[i])
            decipher_key.append(i + 1)        

if not decipher:
    print("\n\nSorry, No possible key combination found.")
else:
    for z in range (len(decipher)):
        if dictionary.find(findMaximum(decipher[z], "random")) != -1:
            print("\n" + " POSSIBLE PLAINTEXT ".center(50, "=") + "\nTEXT: " + str(decipher[z]) + "\nKEY: " + str(decipher_key[z]) + "\n" + "".center(50, "="))
        else:
            print("\n\nFound some " + str(len(decipher)) + " matched strings in the dictionary...\nConsidering that the decrpytion is not 100% accurate, repeat the decrpytion process? [y/n]")
            ch = input()
            if ch == "y" or "Y":
                while False:
                    if dictionary.find(findMaximum(decipher[z], "random")) != -1:
                        print("\nPOSSIBLE PLAINTEXT: " + str(decipher[z]) + "\n\nKEY: " + str(decipher_key[z]))

                    else:
                        if count > 1500:
                            print("\n\nSorry, No possible key combination found.")
                    count += 1
            elif ch == "n" or "N":
                print("\n\nSorry, No possible key combination found.")

delay = input("Enter any key to exit...")

