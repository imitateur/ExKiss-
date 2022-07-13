print("hello !")
name = input("saisie ton nom: ")
mnom = input("saisie mon future nom: ")

dwl = open("config.txt", "a")
dwl.write(name+mnom)
dwl.close()
print("les données vocal sont envoyer pour amiloré vorte IA")
