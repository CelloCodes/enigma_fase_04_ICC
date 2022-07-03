frase = input("Insira a frase que será trabalhada: ")
chave = int(input("Digite a chave (dica: 1000): "))
opt = input("Digite C para criptografar ou D para descriptografar: ")
alfabeto = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def criptografar(chave, frase, alfabeto):
    novaFrase = ""
    for i in range(len(frase)):
        if frase[i] == " ":
            novaFrase += " "
        else:
            for j in range(len(alfabeto)):
                if frase[i].lower() == alfabeto[j]:
                    index = (j + chave) % len(alfabeto)
                    print(f"chave = {chave} | substituindo {frase[i]} [{j}] por {alfabeto[index]} [{index}]")
                    novaFrase += alfabeto[index]
                    if alfabeto[j] in ["a", "e", "i", "o", "u"]:
                        chave -= 1
                    else:
                        chave += 3
    print("--------------------------- frase: ", novaFrase)

def descriptografar(chave, frase, alfabeto):
    novaFrase = ""
    for i in range(len(frase)):
        if frase[i] == " ":
            novaFrase += " "
        else:
            for j in range(len(alfabeto)):
                if frase[i].lower() == alfabeto[j]:
                    index = abs((j - chave) % len(alfabeto))
                    print(f"chave = {chave} | substituindo {frase[i]} [{j}] por {alfabeto[index]} [{index}]")
                    novaFrase += alfabeto[index]
                    if alfabeto[index] in ["a", "e", "i", "o", "u"]:
                        chave -= 1
                    else:
                        chave += 3
    print("--------------------------- frase: ", novaFrase)

if opt == "C":
    criptografar(chave, frase, alfabeto)
elif opt == "D":
    descriptografar(chave, frase, alfabeto)
