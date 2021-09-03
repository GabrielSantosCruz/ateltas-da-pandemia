'''*******************************************************************************
Autor: Gabriel Santos Cruz
Componente Curricular: Algoritmos I
Concluido em: xx/xx/2021
Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
trecho de código de outro colega ou de outro autor, tais como provindos de livros e
apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.
O própio e sua evolução pode ser encontrado em: https://github.com/GabrielSantosCruz/atletas-na-pandemia
******************************************************************************************/'''

# Entrada de dados:
print('=' * 30)
print("Sistema UEFS pelos atletas")
print('=' * 30)
print("\nInicio do cadastramento dos atletas!\n")
rep = 's' # para dar inicio ao loop
symptom = 'n'
quant = age = symptom_age = symp_quant = assymptom_age = assymptom_quant = total_age = temperature = temperature1 = symp_age_middle = assymptom_age_middle = 0
max_age = kit_covid = masculine = feminine = masc_kit = fem_kit = masc_not_kit = masc_kit_symp = fem_kit_symp = masc_kit_assymp = fem_kit_assymp = 0
masc_symp = fem_symp = masc_assymp = fem_assymp = medal_masc = medal_fem = medal_masc_symp = medal_fem_symp = medal_masc_assymp = medal_fem_assymp = 0
min_age = 1000
masc_gold = masc_silver = masc_bronze = 0
fem_gold = fem_silver = fem_bronze = 0
masc_symp_gold = masc_symp_silver = masc_symp_bronze = 0 # medalhas dos homens sintomáticos
masc_assymp_gold = masc_assymp_silver = masc_assymp_bronze = 0 # medalhas dos homens assintomáticos
fem_symp_gold = fem_symp_silver = fem_symp_bronze = 0 # medalhas das mulheres sintomáticas
fem_assymp_gold = fem_assymp_silver = fem_assymp_bronze = 0 # medalhas das mulheres assintomáticas

while rep.lower() == 's':
    quant += 1

    age = input("Digite a idade do atleta: ")
    while not age.isdigit() or (int(age) < 10 or int(age) > 100): # valida se é um número
        print("Erro! Digite uma idade válida")
        age = input("Digite a idade do atleta: ")
    age = int(age)
    total_age += int(age)

    gender = str(input("Digite seu sexo (M/F): ")).lower().strip()
    while gender not in 'mf':
        gender = str(input("Erro! Digite M ou F: ")).lower()
    fever = str(input("Teve febre (S/N): ")).lower()
    while fever not in 'sn':
        fever = str(input("Erro! Digite S ou N: ")).lower()
        if gender == 'm':
            masculine += 1
        if gender == 'f':
            feminine += 1

    if fever.lower() == 's':

        temperature = float(input("Qual foi a maior temperatura detectada: "))
        while temperature < 0:
            print('Erro! digite uma temperatura válida!')
            temperature = float(input("Qual foi a maior temperatura detectada: "))
        if temperature < 37.7: # da erro na variavel symptom por conta do else na linha 96
            print('Isso não é considerado febre')
            fever = str(input("Teve febre (S/N): ")).lower()
            while fever not in 'sn':
                fever = str(input("Erro! Digite S ou N: ")).lower()
                if gender == 'm':
                    masculine += 1
                if gender == 'f':
                    feminine += 1
        else:
            if temperature > temperature1: # temperatura máxima
                temperature1 = temperature
            symptom = 's'

    else:
        symptom = str(input("Teve algum sintoma (S/N): ")).lower()
        while symptom not in 'sn':
            symptom = str(input("Erro! Digite S ou N: ")).lower()

    if symptom == 's': # calcular a maior e a menor idade dentre o sintomáticos   
        if min_age > age:
            min_age = age
        elif age > max_age: 
            max_age = age

        symp_quant += 1 # quantidade dos atletas sintomáticos
        symptom_age += age
        # Recorte por gênero dos atletas que tiveram sintomas
        if gender == 'm':
            masc_symp += 1
        if gender == 'f':
            fem_symp += 1
    else:
        assymptom_quant  += 1
        assymptom_age += age 
        if gender == 'm':
            masc_assymp += 1
        if gender == 'f':
            fem_assymp += 1    

    kit = str(input("Tomou o kit Covid ao retornar ao Brasil (S/N): ")).lower()
    while kit not in 'sn':
        kit = str(input("Erro! Digite S ou N: ")).lower()
    if kit == 's':
        kit_covid += 1
        # quantidade de homens e mulheres que tomaram o kit covid:
        if gender == 'm':
            masc_kit += 1
        if gender == 'f':
            fem_kit += 1
        # quantidade dos que tomaram o kit que tiveram sintomas
        if symptom == 's':
            if gender == 'm':
                masc_kit_symp +=1
            if gender == 'f':
                fem_kit_symp +=1
        # quantidade dos que tomaram o kit que não tiveram sintomas
        if symptom == 'n':
            if gender == 'm':
                masc_kit_assymp += 1
            if gender == 'f':
                fem_kit_assymp += 1

    # Calcular a quantidade de medalhas e qual o seu tipo (Ouro, Prata, Bronze) 
    medal = input("Ganhou alguma medalha? (S/N): ").lower()
    while medal not in 'sn':
        medal = str(input("Erro! Digite S ou N: ")).lower()
    
    if medal == 's':
        print("Digite a quantidade de medalhas em números. Caso não tenha ganhado nenhuma de um tipo apenas digite 0!")
        # quantidade de homens e mulheres que ganharam medalhas:
        if gender == 'm': 
            medal_masc += 1
        if gender == 'f':
            medal_fem += 1
        
        if symptom == 's':
            if gender == 'm': 
                medal_masc_symp += 1
            if gender == 'f':
                medal_fem_symp += 1 

        else:
            if gender == 'm': 
                medal_masc_assymp += 1
            if gender == 'f':
                medal_fem_assymp += 1 

        # Conferir as saídas de medalhas
        gold = input("Quantas medalhas de ouro?: ")
        while not gold.isdigit() or (int(gold) < 0):
            gold = input("Erro! Quantas medalhas de ouro?: ")
        gold = int(gold)
        if gender == 'm' and symptom == 's': 
            masc_gold += gold
            masc_symp_gold += gold
        if gender == 'm' and symptom == 'n':
            masc_gold += gold
            masc_assymp_gold += gold       
        if gender == 'f' and symptom == 's':
            fem_gold += gold           
            fem_symp_gold += gold
        if gender == 'f' and symptom == 'n':
            fem_god += gold
            fem_assymp_gold += gold

        silver = input("Quantas medalhas de prata?: ")
        while not silver.isdigit() or (int(silver) < 0):
            silver = input("Erro! Quantas medalhas de prata?: ")
        silver = int(silver)
        if gender == 'm' and symptom == 's':
            masc_silver += silver
            masc_symp_silver += silver
        if gender == 'm' and symptom == 'n':
            masc_silver += silver
            masc_assymp_silver += silver    
        if gender == 'f' and symptom == 's':
            fem_silver += silver
            fem_symp_silver += silver
        if gender == 'f' and symptom == 'n':
            fem_silver = silver
            fem_assymp_silver = silver

        bronze = input("Quantas medalhas de bronze?: ")
        while not bronze.isdigit() or (int(bronze) < 0):
            bronze = input("Erro! Quantas medalhas de bronze?: ")
        bronze = int(bronze)
        if gender == 'm' and symptom == 's': 
            masc_bronze += bronze
            masc_symp_bronze += bronze
        if gender == 'm' and symptom == 'n':
            masc_bronze += bronze
            masc_assymp_bronze += bronze
        if gender == 'f':
            fem_bronze += bronze

    rep = str(input("Deseja cadastrar um novo atleta?(S/N): ")).lower()
    while rep not in 'sn':
        rep = str(input("Erro! Digite S ou N: "))
    if rep.lower() == 'n':

        print("O cadastramento foi encerrado!!!")

# Processamento de dados:

    # procentagem dos sintomáticos
middle_age = float(total_age / quant) # Idade média dos atletas

    # se o atleta tiver febre e não forem preenchidos estes dados da erro de ZerodivisionError (corrigido)
if (symp_quant > 0): # and (symptom == 's'): #and (fever == 'n'):
    # caso alguem tenha tido febre acaba bugando a idade média dos sintomáticos
    symp_age_middle = float(symptom_age / symp_quant) # Idade média dos sintomáticos

if symptom == 'n' and (assymptom_age > 0 or assymptom_quant > 0):    
    assymptom_age_middle = float(assymptom_age / assymptom_quant) # Idade média dos assintomáticos

if temperature > temperature1: # temperatura máxima
    temperature1 = temperature

if symptom == 's':   
    if min_age > age: # sempre dando a maior
        min_age = age
    elif age > max_age: # sempre 0 
        max_age = age

percent_symp = float((100 * symp_quant) / quant) # procentagem dos sintomáticos

# Saída de dados:
print('=' * 30)
print("Relatório de dados: ")
print('=' * 30)
    # Quantidade de atletas monitorados;
print(f"A quantidade de atletas monitorados é: {quant}!")
print('-' * 10)

    # A quantidade e a porcentagem de atletas que apresentaram sintomas;
print(f"A quantidade de atletas que apresentam sintomas é: {symp_quant}\nO que equivale a {round(percent_symp, 1)}% do total!" )
print('-' * 10)

    # Idade média de todos os atletas, dos atletas sem sintomas, e dos atletas sintomáticos;
print(f"A idade média dos atletas cadastrados é: {round(middle_age, 1)}!\nSendo {round(symp_age_middle, 2)} a media dos sintomáticos\nE {round(assymptom_age_middle, 2)} a dos assintomáticos")
print('-' * 10)

    # A temperatura corporal mais alta relatada;
if temperature > 0:
    print(f"A maior temperatura de febre registrada é: {temperature1}!")
elif temperature == 0:
    print("Não houveram atletas com febre!")
print('-' * 10)

    # Dentre os que apresentaram sintomas, a idade do atleta mais novo e do atleta mais velho;
if symp_quant > 0: # a condição não pode ser essa
    print(f"Dentre os sintomáticos, a idade do atleta mais novo foi: {min_age} e do atleta mais velho: {max_age}!")
    print('-' * 10)
else:
    print("Não houveram atletas com sintomas!")
    print('-' * 10)
    
    '''Um recorte por gênero dos atletas que tomaram o “kit COVID”, indicando ainda, dentre estes, a  
    quantidade de homens e mulheres que tiveram ou não sintomas;'''
    # quantos homens e mulheres tomaram o kit covid;
        # destes, quantos homens e mulheres tiveram sintomas. E quantos não tiveram;
if kit_covid > 0:
    print(f"Os {kit_covid} atletas que tomaram o Kit Covid são:\n{masc_kit} Homens\n{fem_kit} Mulheres")
    # print(f"A quantidade de homens que tomaram o Kit Covid foi de {masc_kit} e a de mulheres {fem_kit}! ")
    if symp_quant > 0:
        print(f"Dentre estes {kit_covid}, os sintomáticos são:\n{masc_kit_symp} Homens\n{fem_kit_symp} Mulheres")
    else:
        print(f"Dentre estes {kit_covid} não houveram sintomáticos!")
    if assymptom_quant > 0:    
        print(f"Dentre estes {kit_covid}, os assíntomáticos são:\n{masc_kit_assymp} Homens\n{fem_kit_assymp} Mulheres")
    else:
        print(f"Dentre estes {kit_covid} não houveram assintomáticos!")
    print('-' * 10)
else: 
    print("Nenhum atleta tomou o kit covid! ")
    print('-' * 10)
    
    '''Um recorte por gênero (M/F) e por sintomas (S/N) dos atletas que 
    trouxeram medalhas para casa, especificando a quantidade de medalhas de ouro, prata e bronze.'''
    # Dos que trouxeram medalhas, a quantidade de homens e mulheres;
        # quantos destes tiveram ou não sintomas 
        # especificar a quantidade de medalhas por gênero
    # Homens: X homens, X com sintomas e X sem sintomas. Um total de X medalhas de ouro, X de prata e X de bronze
    # Mulheres: X mulheres, X com sintomas e X sem sintomas. Um total de X medalhas de ouro, X de prata e X de bronze
if medal == 's' or (medal_masc > 0) or (medal_fem > 0):
    print(f"Os atletas que ganharam medalhas foram:\n{medal_masc} Homen(s)\n{medal_fem} Mulher(es)")
    print(f"Destes {medal_masc} Homem(ns): {medal_masc_symp} tiveram sintomas e {medal_masc_assymp} não tiveram")
    print(f"Destas {medal_fem} Mulher(es): {medal_fem_symp} tiveram sintomas e {medal_fem_assymp} não tiveram")
    print(f"Os {medal_masc_symp} Homem(ns) sintomático(s) ganharam: {masc_symp_gold} de ouro, {masc_symp_silver} de prata e {masc_symp_bronze} de bronze! ")
    print(f"Os {medal_masc_assymp} Homem(ns) assintomático(s) ganharam: {masc_assymp_gold} de ouro, {masc_assymp_silver} de prata e {masc_assymp_bronze} de bronze! ")
    #print(f"Os homens ganharam: {masc_gold} medalhas de ouro, {masc_silver} medalhas de prata e {masc_bronze} medalhas de bronze! ")
    print(f"As {medal_fem_symp} mulher(es) sintomáticas ganharam: {fem_symp_gold} medalhas de ouro, {fem_symp_silver} medalhas de prata e {fem_symp_bronze} medalhas de bronze! ")
    print(f"As {medal_fem_assymp} mulher(es) assintomáticas ganharam: {fem_assymp_gold} medalhas de ouro, {fem_assymp_silver} medalhas de prata e {fem_assymp_bronze} medalhas de bronze! ")
    
    print('-' * 10)
else:
    print("Nenhum atleta ganhou medalha! ")
    print('-' * 10)
print('=' * 30) 
rep = input("Pressione enter para sair!\n")