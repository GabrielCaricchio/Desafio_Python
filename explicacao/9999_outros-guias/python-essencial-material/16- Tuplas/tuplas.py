estudante = ("joão", "joão", 16, "masculino")

print(estudante.count("joão"))
print(estudante.index("masculino"))

for x in estudante:
    print(x)

if "joão" in estudante:
    print("existe")