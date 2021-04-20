"""Teste para os exercícios do Python Para Zumbis."""


# F. busca
# Verifique quantas ocorrências de uma palavra há numa frase
# frase = 'ana e mariana gostam de banana'
# palavra = 'ana'
# busca ('ana e mariana gostam de banana', 'ana') == 4


def busca(frase, palavra):
    return len([k for k in range(len(frase)) if frase[k:k+len(palavra)] == palavra])

print(busca('ana e mariana gostam de banana', 'ana'))
  
