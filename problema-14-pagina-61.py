z = set(input("Introduceti sirul  de caractere z: "))
k = set(input("Introduceti  sirul de caractere: "))
print("Caracterele care se  intalnesc cel putin in unul din sirui :", z.intersection(k))
print(" Caracterele care apar  in ambele siruri: ", z.union(k))
print("Caracterele care apar in primul si nu apar in sirul al doilea: ", z.difference(k))