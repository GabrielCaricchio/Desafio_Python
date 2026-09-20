capitais = {'RJ': 'Rio de Janeiro',
            'SP': 'São Paulo',
            'MG': 'Belo Horizonte',
            'ES': 'Vitória'}

# print(capitais.get('BA'))

# print(capitais.keys())
# print(capitais.values())
# print(capitais.items())

# capitais.update({'RS': 'Porto Alegre'})
# capitais.update({'SC': 'Floripa'})
# capitais.pop('RS')
# capitais.clear()

for key, value in capitais.items():
    print(key, value)
