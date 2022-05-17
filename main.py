from secretpy import Beaufort, Autokey, Caesar, Vigenere, Scytale


Finish = False
while not Finish:
    plaintext = input("Please enter the plain text: ")
    choice = input("Please select one: \n"
                   "a.Beaufort b.Autokey c.Caesar d.Vigenere e.Scytale "
                   " \n")
    if choice == "a":
        key = input("Please enter the key: ")
        cipher = Beaufort()
        print(plaintext)
        enc = cipher.encrypt(plaintext, key)
        print(enc)
        dec = cipher.decrypt(enc, key)
        print(dec)
    elif choice == "b":
        key = input("Please enter the key: ")
        cipher = Autokey()
        print(plaintext)
        enc = cipher.encrypt(plaintext, key)
        print(enc)
        dec = cipher.decrypt(enc, key)
        print(dec)
    elif choice == "c":
        shiftKey = int(input("Please enter shifting size: "))
        cipher = Caesar()
        print(plaintext)
        enc = cipher.encrypt(plaintext, shiftKey)
        print(enc)
        dec = cipher.decrypt(enc, shiftKey)
        print(dec)
    elif choice == "d":
        key = input("Please enter the key: ")
        cipher = Vigenere()
        print(plaintext)
        enc = cipher.encrypt(plaintext, key)
        print(enc)
        dec = cipher.decrypt(enc, key)
        print(dec)
    elif choice == "e":
        shiftKey = int(input("Please enter shifting size: "))
        cipher = Scytale()
        print(plaintext)
        enc = cipher.encrypt(plaintext, shiftKey)
        print(enc)
        dec = cipher.decrypt(enc, shiftKey)
        print(dec)
    restart = input("Please type Yes if you want to try again. Otherwise type No \n")
    if restart == "no":
        Finish = True
        print("Goodbye")
