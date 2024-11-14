###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 11 - No Man's Sky
# Nome: CAiky Pinheiro Foge de Sá
# RA: 204570
###################################################


PROTOTIPOS = ('PD', 'PA', 'PTR', 'PTE', 'PC', 'PR', 'PO', 'PV')
PAISAGENS = ('SOA', 'SVM', 'SCO', 'SF1', 'SF2', 'SF3', 'SL', 'SPC')
CONDICOES_CLIMATICAS = ('CC0', 'CC1', 'CC2', 'CN1', 'CN2', 'CN3', 'CN4', 'CV', 'CTA1', 'CTA2', 'CTE1')

TERRENO_PROTO = {
  'PD':  ('TD', 'TA2'),
  'PA':  ('TA1 TA2', 'TD TP TM'),
  'PTR': ('TP TM', 'TAR TO1 TO2'),
  'PTE': ('TP TM', 'TAR TO1 TO2 TC'),
  'PC':  ('TC TM', 'TO1 TO2 TP'),
  'PR':  ('TC TM', 'TO1 TO2'),
  'PO':  ('TO1 TO2', 'TAR TM'),
  'PV':  ('TM', 'TP TC')
}

TERRENO_ADJACENCIA = {
  'TAR': 'TAR TO1 TP TC TM',
  'TO1': 'TAR TO1 TO2 TM',
  'TO2': 'TO1 TO2',
  'TA1': 'TA1 TA2 TP TC TM',
  'TA2': 'TA1 TA2 TD TC TM',
  'TD': 'TA2 TD',
  'TP': 'TAR TA1 TA2 TP TC TM',
  'TC': 'TAR TA1 TA2 TP TC TM',
  'TM': 'TAR TO1 TA1 TA2 TP TC TM'
}

ELEMENTOS = {
  # Scenarios
  'SOA' : ('PA',               'TA1 TA2'),
  'SVM' : ('PTR PTE PR PO',    'TO1 TO2'),
  'SCO' : ('PTR PTE PR PO',    'TO1'),
  'SF1' : ('PTR PTE',          'TP TM'),
  'SF2' : ('PTR PTE',          'TP TM'),
  'SF3' : ('PA PTR PTE',       'TP TM'),
  'SL'  : ('PTR PTE',          'TP TM TC'),
  'SPC' : (PROTOTIPOS,         'TC TM'),
  # Weather conditions
  'CC0' : ('PTR PTE PC PR PO', 'TAR TO1 TO2 TP TC TM'),
  'CC1' : ('PTR PTE PR PO',    'TAR TO1 TO2 TP TC TM'),
  'CC2' : ('PTR PTE PR PO',    'TAR TO1 TO2 TP TC TM'),
  'CN1' : ('PTE PR PO',        'TAR TP TC TM'),
  'CN2' : ('PTE PC PR PO',     'TAR TP TC TM'),
  'CN3' : ('PTE PC',           'TAR TP TC TM'),
  'CN4' : ('PC',               'TAR TP TC TM'),
  'CV'  : ('PV',               'TP TC TM'),
  'CTA1': ('PD PA',            'TD'),
  'CTA2': ('PD PA PV',         'TD TA2 CV'),
  'CTE1': ('PR',               'TM TO1 TO2'),
  # Animals
  'AMA' : (PROTOTIPOS,         'TD TA2'),
  'AAV' : (PROTOTIPOS,         'TAR TP TA1 TC TM'),
  'AMM' : (PROTOTIPOS,         'TO1 TO2 TAR'),
  'APE' : (PROTOTIPOS,         'TO1 TO2 SL TAR'),
  'AAL' : (PROTOTIPOS,         'TAR TP SL TO1'),
  'ACR' : (PROTOTIPOS,         'TAR TO1'),
  'AHQ' : (PROTOTIPOS,         'TAR TA1 TP TM'),
  'ARO' : (PROTOTIPOS,         'TAR TA1 TA2 TD TC TM'),
  'AFE' : (PROTOTIPOS,         'TAR TA1 TP TC TM SF1'),
  'ACA1': (PROTOTIPOS,         'TP TC TM SF1'),
  'ACA2': (PROTOTIPOS,         'TP TC TM SF1'),
  'AHOT': (PROTOTIPOS,         'TP TC TM SF1 SF2 SF3')
}



#criar tabela o prototipo
p = input()
planeta = []
if p in PROTOTIPOS:
    x, y = input().split(" ")
    for i in range(int(x)):
        linhas = input().split(" ")
        linha = []
        for j in range(len(linhas)):
            if linhas[j] != '':
                linha.append(linhas[j])
        planeta.append(linha)

        
#verificar regra 1 - arrumar saída
erro1 = []
for i in range(len(planeta)):
    for j in range(len(planeta[i])):
        terreno = planeta[i][j].split(",")
        if p in TERRENO_PROTO and any(terreno[0] in item.split() for item in TERRENO_PROTO[p]):
            continue
        else: 
            posicao = str(i) +","+str(j)+":"+terreno[0]
            erro1.append(posicao)
print("regra 1")
if len(erro1)==0:
    print("ok")
else:
    for i in erro1:
        print(i)
    print("falha")

#verificar regra 2
erro2 = []
for i in range(len(planeta)):
    for j in range(len(planeta[i])):
        terreno = planeta[i][j].split(",")
        cima = planeta[(i-1)% len(planeta[i])][j].split(",")
        baixo = planeta[(i+1)% len(planeta[i])][j].split(",")
        esquerda = planeta[i][(j-1)% len(planeta[j])].split(",")
        direita = planeta[i][(j+1)% len(planeta[j])].split(",")
        vizinhos = TERRENO_ADJACENCIA.get(terreno[0], "").split()
        if (cima[0] in vizinhos) and  (baixo[0] in vizinhos) and (esquerda[0]  in vizinhos) and (direita[0]  in vizinhos):
            continue
        else:
            posicao = str(i) +","+str(j)+":"+terreno[0]
            erro2.append(posicao)
print("regra 2")
if len(erro2)==0:
    print("ok")
else:
    for i in erro2:
        print(i)
    print("falha")




#verificar regra 3
erro3 = []
for i in range(len(planeta)):
    for j in range(len(planeta[i])):
        terreno = planeta[i][j].split(",")
        if len(terreno)>1:
            print("\n",terreno, len(terreno))
            for k in range(1, len(terreno)):
                print(terreno[k])
                if terreno[k] in ELEMENTOS:
                    prototipo, terra = ELEMENTOS[terreno[k]]
                    print(prototipo,terra)
                    #se for paisagem
                    if terreno[k][0]=="S":
                        if p in prototipo or terreno[0] in terra.split():
                            pass
                        else:
                            posicao = str(i) +","+str(j)+":"+terreno[0]
                            erro3.append(posicao)
                    #se for clima
                    if terreno[k][0]=="C" or terreno[k][0]=="A":
                        if p in prototipo:
                            pass
                        else:
                            posicao = str(i) +","+str(j)+":"+terreno[0]
                            erro3.append(posicao)
                        #verificação dos terrenos/paisagens
                        for l in range(len(terreno)):
                            if any(terreno[0:l]) in terra.split():
                                pass
                            else:
                                posicao = str(i) +","+str(j)+":"+terreno[0]
                                erro3.append(posicao)

                    
print("regra 3")
if len(erro3)==0:
    print("ok")
else:
    for i in erro3:
        print(i)
    print("falha")
