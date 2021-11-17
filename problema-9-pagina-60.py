A=set(input("Introduceti elementele multimii A formate din litere mari ale alfabetului latin  :" ).split())
LT=True
for a in A:
    if ((ord(a)<65)or(ord(a)>90)):
        LT=False
if LT==True:
    B=set(input('Introduceti elemnetele multimii B: ').split())
    LT2=True
    for b in B:
        if ((ord(b)<65)or(ord(b)>90)):
            LT2=False
    if LT2==True:        
        print('Diferenta multimilor  A si B :', A.difference(B)) 
        print('Diferenta multimilor  B si A :', B.difference(A)) 
        print('Intersectia multimilor A si B: ',A.intersection(B) )
        print('Reuniunea multimilor A si B :', A.union(B))
    else:
        print("Multimea trebuie sa includa doar litere mari ale alfabetului latin ")
else:
    print("Multimea trebuie sa includa doar litere mari ale alfabetului latin")