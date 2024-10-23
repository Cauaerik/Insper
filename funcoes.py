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
  for nick, coord in frota.items():
    if nome_navio not in nick:
      frota[nome_navio] = [define_posicoes(linha, coluna, orientacao, tamanho)]
    if nome_navio in nick:
      frota[nome_navio] = coord + [define_posicoes(linha, coluna, orientacao, tamanho)]
  if frota == {}:
    frota[nome_navio] = [define_posicoes(linha, coluna, orientacao, tamanho)]
  return frota
