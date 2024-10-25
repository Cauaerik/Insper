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

def preenche_frota(frota, nome_navio, linha, coluna, orientacao, tamanho):
      #adicionar o novo navio ao dicionario e atribuir o seu valor com a sua posicao
      if nome_navio in frota:
            #caso o navio ja esteja no dicionario, adicionar o valor novo ao ja existente
            frota[nome_navio] += [define_posicoes(linha,coluna,orientacao,tamanho)]
      else:
            #caso o navio ainda nao esteja no dicionario, adicionar o navio como chave e o sua posicao como valor
            frota[nome_navio] = [define_posicoes(linha,coluna,orientacao,tamanho)]
      return frota
def faz_jogada(tabuleiro,linha,coluna):
      if tabuleiro[linha][coluna] == 1:
            tabuleiro[linha][coluna] = 'X'
      elif tabuleiro [linha][coluna] == 0:
            tabuleiro [linha][coluna] = '-'
      return tabuleiro
def posiciona_frota(frota):
      #tabuleiro referencia
      tabuleiro = [
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
  ]
      #percorrer listas de posicoes nos valores do dicionario
      for lista_posicoes in frota.values():
            #percorrer as listas de coordenadas dentro da lista de posicoes
            for lista_coordenadas in lista_posicoes:
                  #percorrer as cordenadas (x,y) dentro das listas de coordenadas
                  for coordenada in lista_coordenadas:
                        x = coordenada[0]
                        y = coordenada[1]
                        #atualizar a coordenada do tabuleiro para 1
                        tabuleiro[x][y] = 1
      return tabuleiro
