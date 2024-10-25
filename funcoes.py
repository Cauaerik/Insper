#Esse é o nosso mapa
'''grid = [
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
  ]'''

#essa definição define sempre a posição do navio
def define_posicoes(linha, coluna, orientacao, tamanho):
  #posicoes sempre em ordem crescente
  posicao = []
  if orientacao == 'horizontal':
    i = 0
    while i < tamanho:
      posicaox = linha 
      posicaoy = coluna + i
      posicao.append([posicaox, posicaoy])
      i += 1
  if orientacao == 'vertical':
    i = 0
    while i < tamanho:
      posicaox = linha + i
      posicaoy = coluna
      posicao.append([posicaox, posicaoy])   
      i += 1 
  return posicao

#essa definição tem que guardar as posições do navio
def preenche_frota(frota, nome_navio, linha, coluna, orientacao, tamanho):
  if nome_navio in frota.values():
    frota[nome_navio] = coord + [define_posicoes(linha, coluna, orientacao, tamanho)]
  else:
    frota[nome_navio] = [define_posicoes(linha, coluna, orientacao, tamanho)]
  return frota

frota ={'porta-aviões': [[[9, 3], [9, 4], [9, 5], [9, 6]], [[4, 5], [5, 5], [6, 5], [7, 5]], [[6, 6], [6, 7], [6, 8], [6, 9]], [[4, 1], [5, 1], [6, 1], [7, 1]]],
'submarino': [[[6, 0]]]}
nome_navio= 'navio-tanque'
linha= 3
coluna= 4
orientacao= 'horizontal'
tamanho= 3
print(preenche_frota(frota,nome_navio,linha,coluna,orientacao,tamanho))
'''
  Era esperado {'navio-tanque': [[[3, 4], [3, 5], [3, 6]]],
   'porta-aviões': [[[9, 3], [9, 4], [9, 5], [9, 6]],
                    [[4, 5], [5, 5], [6, 5], [7, 5]],
                    [[6, 6], [6, 7], [6, 8], [6, 9]],
                    [[4, 1], [5, 1], [6, 1], [7, 1]]],
   'submarino': [[[6, 0]]]}. 

  Porém, foi obtido {'porta-aviões': [[[9, 3], [9, 4], [9, 5], [9, 6]],
                    [[4, 5], [5, 5], [6, 5], [7, 5]],
                    [[6, 6], [6, 7], [6, 8], [6, 9]],
                    [[4, 1], [5, 1], [6, 1], [7, 1]]],
   'submarino': [[[6, 0]]]}.'''
   