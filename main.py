#/*******************************************************************************
#Autor: Gabriel Santos Cruz
#Componente Curricular: Algoritmos I
#Concluido em: xx/xx/2021
#Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
#trecho de código de outro colega ou de outro autor, tais como provindos de livros e
#apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
#de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
#do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.
# O própio e sua evolução pode ser encontrado em: https://github.com/GabrielSantosCruz/atletas-na-pandemia
#******************************************************************************************/

# Entrada de dados:
print('=' * 30)
print("Sistema UEFS pelos atletas")
print('=' * 30)
print("\nInicio do cadastramento dos atletas!\n")
rep = 's'
symptom = 'n'
quant = 0
age = 0
symptom_age = 0
symp_quant = 0
assymptom_age = 0
assymptom_quant = 0
total_age = 0
temperature = 0
temperature1 = 0
symp_age_middle = 0
assymptom_age_middle = 0
max_age = 0
min_age = 1000
kit_covid = 0
masculine = 0
feminine = 0
masc_kit = 0
fem_kit = 0
masc_symp = 0
fem_symp = 0
masc_assymp = 0
fem_assymp = 0
medal_masc = 0
medal_fem = 0
medal_masc_symp = 0
medal_fem_symp = 0
medal_masc_assymp = 0
medal_fem_assymp = 0
masc_gold = 0
fem_gold = 0
masc_silver = 0
fem_silver = 0
masc_bronze = 0
fem_bronze = 0

while rep.lower() == 's':
    quant += 1

    age = input("Digite a idade do atleta: ")
    while not age.isdigit() or (int(age) < 10 or int(age) > 100): # valida se é um número
        print("Erro! Digite uma idade válida")
        age = input("Digite a idade do atleta: ")

    total_age += age


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
        symptom = str(input("Teve algum sintoma (S/N): ")).lower()
        while symptom not in 'sn':
            symptom = str(input("Erro! Digite S ou N: ")).lower()
        if symptom == 's':
            symp_quant += 1
            symptom_age += age
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

    medal = input("Ganhou alguma medalha? (S/N): ").lower()
    while medal not in 'sn':
        medal = str(input("Erro! Digite S ou N: ")).lower()
    
# Calcular a quantidade de medalhas e qual o seu tipo (Ouro, Prata, Bronze)

    if medal == 's':
        print("Digite a quantidade de medalhas em números. Caso não tenha ganhado nenhuma de um tipo apenas digite 0!")
        # quantidade de homens e mulheres que ganharam medalhas:
        if gender == 'm': 
            medal_masc += 1
        if medal == 'f':
            medal_fem += 1
        
        if symptom == 's':
            if gender == 'm': 
                medal_masc_symp += 1
            if medal == 'f':
                medal_fem_symp += 1 

        else:
            if gender == 'm': 
                medal_masc_assymp += 1
            if medal == 'f':
                medal_fem_assymp += 1 

        try:
            gold = int(input("Quantas medalhas de ouro?: "))
        except:
            gold = int(input("Erro! Quantas medalhas de ouro?: "))
        while gold < 0:
            gold = int(input("Erro! Quantas medalhas de ouro?: "))
            if gender == 'm': 
                masc_gold += 1
            if medal == 'f':
                fem_gold += 1             

        try:
            silver = int(input("Quantas medalhas de prata?: "))
        except:
            silver = int(input("Erro! Quantas medalhas de prata?: "))
        while silver < 0:
            silver = int(input("Erro! Quantas medalhas de prata?: "))
            if gender == 'm': 
                masc_silver += 1
            if medal == 'f':
                fem_silver += 1 

        try:
            bronze = int(input("Quantas medalhas de bronze?: "))
        except:
            bronze = int(input("Erro! Quantas medalhas de bronze?: "))
        while bronze < 0:
            bronze = int(input("Erro! Quantas medalhas de bronze?: "))
            if gender == 'm': 
                masc_bronze += 1
            if medal == 'f':
                fem_bronze += 1 

    rep = str(input("Deseja cadastrar um novo atleta?(S/N): ")).lower()
    while rep not in 'sn':
        rep = str(input("Erro! Digite S ou N: "))
    if rep.lower() == 'n':

        print("O cadastramento foi encerrado!!!")

# Processamento de dados:

    # procentagem dos sintomáticos
middle_age = float(total_age / quant) # Idade média dos atletas

    # se o atleta tiver febre e não forem preenchidos estes dados da erro de ZerodivisionError (corrigido)
if (fever == 'n') and (symp_quant > 0) and (symptom == 's'):
    symp_age_middle = float(symptom_age / symp_quant) # Idade média dos sintomáticos

if symptom == 'n':    
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
print(f"A quantidade de atletas monitorados é de {quant}!")

    # A quantidade e a porcentagem de atletas que apresentaram sintomas;

print(f"A quantidade de atletas que apresentam sintomas é de {symp_quant}.\nO que equivale a {round(percent_symp, 2)}% do total!" )

    # Idade média de todos os atletas, dos atletas sem sintomas, e dos atletas sintomáticos;
print(f"A idade média dos atletas cadastrados é {round(middle_age, 2)}!\nSendo {round(symp_age_middle, 2)} a media dos sintomáticos\nE {round(assymptom_age_middle, 2)} a dos assintomáticos")

    # A temperatura corporal mais alta relatada;
if temperature > 0:
    print(f"A maior temperatura registrada foi de {temperature1}!")
elif temperature == 0:
    print("Não houveram atletas com febre!")

    # Dentre os que apresentaram sintomas, a idade do atleta mais novo e do atleta mais velho;
if symptom == 's':
    print(f"Dentre os sintomáticos, a idade do atleta mais novo foi de {min_age} e do atleta mais velho {max_age}!") 
    # caso só tenha um atleta a idade digitada vai para o mais novo e o mais velho fica com 0
else:
    print("Não houveram atletas com sintomas!")
    
    '''Um recorte por gênero dos atletas que tomaram o “kit COVID”, indicando ainda, dentre estes, a  
    quantidade de homens e mulheres que tiveram ou não sintomas;'''
    # quantos homens e mulheres tomaram o kit covid;
        # destes, quantos homens e mulheres tiveram sintomas. E quantos não tiveram;
if kit_covid > 0:
    print(f"A quantidade de homens que tomaram o Kit Covid foi de {masc_kit} e a de mulheres {fem_kit}! ")
    if symp_quant > 0:
        print(f"Dentre estes, {masc_symp} homens e {fem_symp} mulheres tiveram sintomas!")
    if assymptom_quant > 0:    
        print(f"Dentre estes, {masc_assymp} homens e {fem_assymp} mulheres não tiveram sintomas!")
else: 
    print("Nenhum atleta tomou o kit covid! ")

    '''Um recorte por gênero (M/F) e por sintomas (S/N) dos atletas que 
    trouxeram medalhas para casa, especificando a quantidade de medalhas de ouro, prata e bronze.'''
    # Dos que trouxeram medalhas, a quantidade de homens e mulheres;
        # quantos destes tiveram ou não sintomas 
        # especificar a quantidade de medalhas por gênero

    # Homens: X homens, X com sintomas e X sem sintomas. Um total de X medalhas de ouro, X de prata e X de bronze
    # Mulheres: X mulheres, X com sintomas e X sem sintomas. Um total de X medalhas de ouro, X de prata e X de bronze

if medal == 's':
    print(f"Dos atletas que ganharam medalhas {medal_masc} eram homens e {medal_fem} eram mulheres! ")
    print(f"Destes {medal_masc_symp} homens tiveram sintomas e {medal_masc_assymp} não tiveram")
    print(f"Das mulheres, {medal_fem_symp} tiveram e {medal_fem_assymp} não tiveram")
    print(f"Os homens ganharam: {masc_gold} medalhas de ouro, {masc_silver} medahas de prata e {masc_bronze} medalhas de bronze! ")
    print(f"As mulheres ganharam: {fem_gold} medalhas de ouro, {fem_silver} medalhas de prata e {fem_bronze} medalhas de bronze! ")
else:
    print("Nenhum atleta ganhou medalha! ")

    # organizar melhor as saídas de dados
    # conferir possíveis erros
    # conferir a verificação de dados
        # as strings estão deixando passar se apenas digitar enter
        # não consegui as de numeros ainda
    # adicionar opção de voltar a pergunta anterior?    