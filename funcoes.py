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
  frotac = frota.copy()
  for nick, coord in frota.items():
    if nome_navio not in nick:
      frotac[nome_navio] = [define_posicoes(linha, coluna, orientacao, tamanho)]
    if nome_navio in nick:
      frotac[nome_navio] = coord + [define_posicoes(linha, coluna, orientacao, tamanho)]
  if frota == {}:
    frotac[nome_navio] = [define_posicoes(linha, coluna, orientacao, tamanho)]
  return frotac

a = {'porta-aviões': [[[1, 2], [2, 2], [3, 2], [4, 2]], [[0, 4], [1, 4], [2, 4], [3, 4]]]}
nome_navio = 'contratorpedeiro'
linha = 5
coluna = 4
orientacao = 'vertical'
tamanho = 2
print(preenche_frota(a, nome_navio, linha, coluna, orientacao, tamanho))