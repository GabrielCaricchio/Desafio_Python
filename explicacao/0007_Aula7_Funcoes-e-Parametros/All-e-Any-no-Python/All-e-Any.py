# ### All e Any

# In[26]:


saldo = [10, 100, 1500, 3000, 3000, 2900, 2800, 3000, 4500, -10, 13, 20, 50, 50, 50, 50, 50]

if any([item < 0 for item in saldo]):
    print("Teve saldo negativo")
else:
    print("Não teve saldo negativo")


# In[27]:



if all([item >= 0 for item in saldo]):
    print("Não teve negativo")
else:
    print("Teve negativo")


# In[ ]:




