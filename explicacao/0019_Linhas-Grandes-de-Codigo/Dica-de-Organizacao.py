# ### Listas

# In[ ]:


meses = ['janeiro', 
         'fevereiro', 
         'março', 
         'abril', 
         'maio', 
         'junho', 
         'julho', 
         'agosto', 
         'setembro', 
         'outubro', 
         'novembro',
         'dezembro']


# ### Dicionários

# In[ ]:


faturamento = {
    'janeiro': 1500, 
    'fevereiro': 2300, 
    'março': 2900, 
    'abril': 3100, 
    'maio': 2800, 
    'junho': 2500, 
    'julho': 4000, 
    'agosto': 4200, 
    'setembro': 4000, 
    'outubro': 2500, 
    'novembro': 7000,
    'dezembro': 2000}


# ### Linhas grandes

# In[ ]:


if (meses[0] == "janeiro" \
    and faturamento["janeiro"] > 1000 \
    and faturamento["fevereiro"] > faturamento["janeiro"]):
    print("Ganhou bônus")


# In[ ]:




