falsy1 = []       #Empty lists []
falsy2 = ()       #Empty tuples ()
falsy3 = {}       #Empty dictionaries {}
falsy4 = set()    #Empty sets set()
falsy5 = ""       #Empty strings ""
falsy6 = range(0) #Empty ranges range(0)
falsy7 = 0

if not(falsy1):
    print("falsy1 " + str(falsy1) + " do tipo " + str(type(falsy1)) + " é falso")
if not(falsy2):
    print("falsy2 " + str(falsy2) + " do tipo " + str(type(falsy2)) + " é falso")
if not(falsy3):
    print("falsy3 " + str(falsy3) + " do tipo " + str(type(falsy3)) + " é falso")
if not(falsy4):
    print("falsy4 " + str(falsy4) + " do tipo " + str(type(falsy4)) + " é falso")
if not(falsy5):
    print("falsy5 " + str(falsy5) + " do tipo " + str(type(falsy5)) + " é falso")
if not(falsy6):
    print("falsy6 " + str(falsy6) + " do tipo " + str(type(falsy6)) + " é falso")
if not(falsy7):
    print("falsy7 " + str(falsy7) + " do tipo " + str(type(falsy7)) + " é falso")
    


truthy1 = "uma string"
truthy2 = 10
truthy3 = ['item']

    
if truthy1 and truthy2 and truthy3:
    print("Esses valores são verdadeiros: " + str(truthy1) + ", " + str(truthy2) + ", " + str(truthy3) )

if truthy1 and falsy1:
    print("Isso não irá aparecer")
    
if truthy1 or falsy1:
    print("Isso vai aparecer")