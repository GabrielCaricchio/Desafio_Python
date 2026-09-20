import time
# While Loops são ilimitados
# For Loops são limitados 

for i in range(10):
    print(i + 1)

for i in range(10, 30 + 1, 2):
    print(i)

for i in "Paulo Raoni":
    print(i)


for segundos in range(10, 0, -1):
    print(segundos)
    time.sleep(1)
    
print("Feliz Ano Novo!")