vetor=list(range(3))
print("Informe 3 números diferentes!")
for i in range(0,3):
    numero=float(input("Informe o número:"))  
    vetor[i]= numero
if vetor[2]>vetor[1] and vetor[1]>vetor[0]:
    print("O maior é:",vetor[2],"\nO do meio é:",vetor[1],"\nO menor é:",vetor[0])
if vetor[2]>vetor[0] and vetor[0]>vetor[1]:
    print("O maior é:",vetor[2],"\nO do meio é:",vetor[0],"\nO menor é:",vetor[1])
if vetor[1]>vetor[2] and vetor[2]>vetor[0]:
    print("O maior é:",vetor[1],"\nO do meio é:",vetor[2],"\nO menor é:",vetor[0])
if vetor[1]>vetor[0] and vetor[0]>vetor[2]:
    print("O maior é:",vetor[1],"\nO do meio é:",vetor[0],"\nO menor é:",vetor[2])
if vetor[0]>vetor[1] and vetor[1]>vetor[2]:
    print("O menor é:",vetor[0],"\nO do meio é:",vetor[1],"\nO menor é:",vetor[2])
if vetor[0]>vetor[2] and vetor[2]>vetor[1]:
    print("O maior é:",vetor[0],"\nO do meio é:",vetor[2],"\nO menor é:",vetor[1])