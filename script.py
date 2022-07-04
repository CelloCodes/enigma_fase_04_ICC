frase = input("Insira a frase que será trabalhada: ")
chave = int(input("Digite a chave (dica: 1000): "))
opt = input("Digite C para criptografar ou D para descriptografar: ")
alfabeto = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

if opt not in ["C", "D"]:
    print("Opção inválida")
    quit()

novaFrase = ""
for i in range(len(frase)):
    if frase[i] == " ":
        novaFrase += " ";
    else:
        for j in range(len(alfabeto)):
            if (frase[i].lower() == alfabeto[j]):
                if opt == "C":
                    index = (j + chave) % len(alfabeto)
                    letra = alfabeto[j]
                elif opt == "D":
                    index = abs((j - chave) % len(alfabeto))
                    letra = alfabeto[index]
                print(f"chave = {chave} | substituindo {frase[i]} [{j}] por {alfabeto[index]} [{index}]")
                novaFrase += alfabeto[index]
                if letra in ["a", "e", "i", "o", "u"]:
                    chave -= 1
                else:
                    chave += 3
print("--------------------------- frase: ", novaFrase)
