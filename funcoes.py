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

def afundados(frota,tabuleiro):
      #declarar a variavel de embarcacoes afundadas
      embarcacoes_afundadas = 0
      #percorrer listas de posicoes nos valores do dicionario
      for lista_posicoes in frota.values():
          #percorrer as listas de coordenadas dentro da lista de posicoes
          for lista_coordenadas in lista_posicoes:
              #declarar uma variavel auxiliar que conta quantas coordenadas que a embarcacao ocupa foram atingidas
              cont = 0
              #percorrer as cordenadas (x,y) dentro das listas de coordenadas
              for coordenada in lista_coordenadas:
                  x = coordenada[0]
                  y = coordenada[1]
                  if tabuleiro[x][y] == 'X':
                      #atualiza a variavel auxiliar para cada coordenada atingida (X)
                      cont += 1
                      if cont == len(lista_coordenadas):
                          #conta as embarcacoes afundadas sempre que a variavel auxiliar atinge o numero total de coordenadas que a embarcacao ocupa 
                          embarcacoes_afundadas += 1
      return embarcacoes_afundadas
def posicao_valida(frota,linha,coluna,orientacao,tamanho):
      navio_novo = define_posicoes(linha,coluna,orientacao,tamanho)
      if orientacao == "vertical":
            if (linha + tamanho) > 10:
                  return False
      if orientacao == "horizontal":
            if (coluna + tamanho) > 10:
                  return False
      #percorrer listas de posicoes nos valores do dicionario
      for lista_posicoes in frota.values():
          #percorrer as listas de coordenadas dentro da lista de posicoes
          for lista_coordenadas in lista_posicoes:
              #percorrer as cordenadas (x,y) dentro das listas de coordenadas
              for coordenada in lista_coordenadas:
                  x = coordenada[0]
                  y = coordenada[1]
                  for coord_novo in navio_novo:
                        if coord_novo[0] == x and coord_novo[1] == y:
                            return False

      return True
    