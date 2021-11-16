A=set(input("Introduceti elementele multimii A formate din numere intregi :" ))
B=set(input("Introduceti elementele multimii B formate di numere intregi :"))
if isinstance(A,int):
    print('int')
if isinstance(B,int):
    print('int')    
print('Diferenta multimilor  A si B :', A.difference(B)) 
print('Diferenta multimilor  B si A :', B.difference(A)) 
print('Intersectia multimilor A si B: ',A.intersection(B) )
print('Reuniunea multimilor A si B :', A.union(B))