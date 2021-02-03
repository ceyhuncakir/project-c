def caesarcijfer():

    decrypted = input("Geef een tekst: ").lower().split()
    rotatie = int(input("Geef een rotatie: "))

    alpha = "abcdefghijklmnopqrstuvwxyz"
    encrypt_all = ""
    shift = alpha[rotatie:] + alpha[:rotatie]
    all_words = []

    for word in decrypted:
        for i in range(len(word)):
            shift_letter = shift[alpha.index(word[i])]
            encrypt_all += shift_letter

        all_words.append(encrypt_all)
        encrypt_all = ""

    print("Caesarcode:", " ".join(all_words))

caesarcijfer()
