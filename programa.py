import funcoes 
#hora de fazer o jogo de terminal!

#pergunta sobre horizontal e vertical
#horizontal = 2
#vertical = 1

frota = {
    "porta-aviões": [],
    "navio-tanque": [],
    "contratorpedeiro": [],
    "submarino": [],
} 

naviospossiveis = [
'porta-avioes', 'navio-tanque', 'navio-tanque 2', 
'contratorpedeiro', 'contratorpedeiro 2',
'contratorpedeiro 3','submarino', 'submarino 2', 'submarino 3',
'submarino 4'   
]

def tamanho(naviospossiveis):
    if naviospossiveis == 'submarino':
        return 1
    if naviospossiveis == 'contratorpedeiro':
        return 2
    if naviospossiveis == 'navio-tanque':
        return 3
    if naviospossiveis == 'porta-avioes':
        return 4
    
for n in naviospossiveis:
#posicionamento, linha e coluna
    t = tamanho(n)

    print(f'Insira as informações referentes ao navio {n} que possui tamanho {str(t)}')

    invalido = True 
    while invalido == True:

        posel = input(f'para {n} qual a linha?:\n ')
        posec = input(f'para {n} qual a coluna?:\n ')

        posel = float(posel)
        posec = float(posec)

        if n != "submarino":
            sentido = input(f'para {n} informe o sentido, vertical (1) ou horizontal (2):\n ')
            if sentido == '1' or  sentido =='vertical':
                orientacao = 'vertical'
            elif sentido == '2' or sentido == 'horizontal':
                orientacao = 'horizontal'
            else:
                print('Esta posição não está válida!')
        else:
            orientacao == 'vertical'
        
        if funcoes.posicao_valida(n,posel,posec,orientacao,t) == True:
            invalido == False
        else:
            print('Esta posição não está válida!')
    
    funcoes.define_posicoes(posel, posec, orientacao, t)
    funcoes.preenche_frota(frota, n, posel, posec, orientacao, t)
    
    
