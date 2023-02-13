#!/usr/bin/env python
# coding: utf-8

# # Imersão Dados 2 - Educação no Brasil

# ### Importação da Base de Dados

# In[3]:


import pandas as pd

# adicionar a fonte de dados a uma variável
fonte = "https://github.com/alura-cursos/imersao-dados-2-2020/blob/master/MICRODADOS_ENEM_2019_SAMPLE_43278.csv?raw=true"

# ler a fonte de dados
dados = pd.read_csv(fonte)

# função para poder escolher a quantidade de linhas que quer visualizar (padrão 5 linhas)
dados.head()


# In[4]:


# descobrindo a quantidade de linhas e colunas
dados.shape


# In[5]:


# selecionando uma coluna específica
dados['SG_UF_RESIDENCIA']


# In[6]:


# retornar o nome das colunas
dados.columns.values


# In[7]:


# selecionando mais de uma coluna
dados[['SG_UF_RESIDENCIA', 'Q025']]


# In[16]:


# descobrindo quais são os estados distintos na base de dados
dados['SG_UF_RESIDENCIA'].unique()


# In[12]:


# descobrindo a quantidade de estados
qtde_estados = len(dados['SG_UF_RESIDENCIA'].unique())

print(f'A base de dados possui {qtde_estados} estados cadastrados.')


# In[21]:


# descobrindo quantas vezes o estado apareceu na base de dados
dados['SG_UF_RESIDENCIA'].value_counts()


# In[22]:


# descobrindo a quantidade de pessoas inscritas por idade
dados['NU_IDADE'].value_counts()


# In[23]:


# mesmo exemplo anterior mas dessa vez ordenando pela idade e não pela quantidade máxima de pessoas
dados['NU_IDADE'].value_counts().sort_index()


# In[26]:


# criando um histograma
dados['NU_IDADE'].hist()


# In[29]:


# criando um histograma mais detalhado
dados['NU_IDADE'].hist(bins = 20, figsize = (10, 8))


# In[34]:


# retornando a quantidade de treineiros
treineiros = len(dados.query('IN_TREINEIRO == 1'))
print(f'{treineiros} pessoas participaram desta edição do ENEM como treineiros')


# In[35]:


# retornando a quantidade de treineiros por idade (do maior para o menor)
dados.query('IN_TREINEIRO == 1')['NU_IDADE'].value_counts()


# In[36]:


# retornando a quantidade de treineiros por idade (ordenando por idade, do menor para o maior)
dados.query('IN_TREINEIRO == 1')['NU_IDADE'].value_counts().sort_index()


# In[37]:


# histograma com as notas da redação
dados['NU_NOTA_REDACAO'].hist(bins = 20)


# In[42]:


# retornando a média e desvio padrão das notas de uma determinada prova
media_redacao = dados['NU_NOTA_REDACAO'].mean()
print(f'A média das notas da prova de redação foi de {media_redacao:.2f}')

desvio_padrao_redacao = dados['NU_NOTA_REDACAO'].std()
print(f'O desvio padrão é de {desvio_padrao_redacao:.2f}')


# In[44]:


provas = ['NU_NOTA_CN', 'NU_NOTA_CH', 'NU_NOTA_MT', 'NU_NOTA_LC', 'NU_NOTA_REDACAO']

dados[provas].describe()


# In[47]:


# 10% das pessoas que tiraram nota mais alta
qtde_pessoas_10 = int(dados['NU_NOTA_LC'].quantile(0.9))
print(f'{qtde_pessoas_10} pessoas aproximadamente tiraram a nota mais alta na prova de Linguagens e Código')


# In[48]:


dados['NU_NOTA_LC'].plot.box(grid = True, figsize = (8, 6))


# In[53]:


dados[provas].boxplot(grid = True, figsize = (10, 5))


# In[ ]:




