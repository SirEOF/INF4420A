n = 103009
e = 449
cipher = [61038, 100123, 21665, 12728, 87116]
dico = {}

def breakRSA():
    # (message^e) mod n = C
    messageClair = ""
    for i in range(0, 26):
        caractereChiffre = (i ** e) % n
        lettreClaire = str(chr(i+65))
        print(lettreClaire + " = " + str(i) + " " + str(caractereChiffre))
        dico[caractereChiffre] = lettreClaire
    print(dico)
    print("Texte clair = ", end='')
    for c in cipher:
        print(dico.get(c), end='')
    print()

def main():
    breakRSA()


if __name__ == '__main__':
    main()

