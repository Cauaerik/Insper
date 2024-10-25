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
            #adiciona um novo valor caso o navio ja esteja no dicionário
            frota[nome_navio] += [define_posicoes(linha,coluna,orientacao,tamanho)]
      else:
            #adiciona um novo navio e o seu novo valor 
            frota[nome_navio] = [define_posicoes(linha,coluna,orientacao,tamanho)]
      return frota
def faz_jogada(tabuleiro, linha, coluna):
    if tabuleiro[linha][coluna] == 1:
          #caso a coordenada enviada esteja ocupada: X (acerto)
        tabuleiro[linha][coluna] = 'X'
    elif tabuleiro[linha][coluna] == 0:
          #caso a coordenada enviada NAO esteja ocupada: - (erro)
        tabuleiro[linha][coluna] = '-'
    return tabuleiro
