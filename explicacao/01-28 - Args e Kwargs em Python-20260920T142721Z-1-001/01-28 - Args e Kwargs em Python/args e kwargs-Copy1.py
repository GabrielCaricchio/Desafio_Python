#!/usr/bin/env python
# coding: utf-8

# ### Funções no Python
# 
# 1. Argumentos de Posição e Keyword
# 2. args e kwargs

# In[1]:


def calcular_imposto(valor):
    ir = valor * 0.275
    iss = valor * 0.05
    csll = valor * 0.0375
    pis = valor * 0.03
    return ir + iss + csll + pis

print(calcular_imposto(1000))

