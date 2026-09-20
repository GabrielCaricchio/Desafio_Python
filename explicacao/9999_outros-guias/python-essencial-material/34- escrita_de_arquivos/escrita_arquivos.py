texto = "Se inscreva\n\n\nAtive a notificação!\nBrazilian Dev\n"
texto_append = "Sou um append!!!" # usar com o argumento "a" em vez de "w"

with open("teste.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write(texto)
