dados = [
    ['Rodas de liga', 'Travas elétricas', 'Piloto automático', 'Bancos de couro',
        'Ar condicionado', 'Sensor de estacionamento', 'Sensor crepuscular', 'Sensor de chuva'],
    ['Central multimídia', 'Teto panorâmico', 'Freios ABS', '4 X 4', 'Painel digital',
        'Piloto automático', 'Bancos de couro', 'Câmera de estacionamento'],
    ['Piloto automático', 'Controle de estabilidade', 'Sensor crepuscular', 'Freios ABS',
        'Câmbio automático', 'Bancos de couro', 'Central multimídia', 'Vidros elétricos']
]
Acessorios = ['Rodas de liga',              
              'Travas elétricas',
              'Piloto automático',
              'Bancos de couro',
              'Ar condicionado',
              'Sensor de estacionamento',
              'Sensor crepuscular',
              'Sensor de chuva']

Carro_1 = ['Jetta Variant', 'Motor 4.0 Turbo', 2003, 44410.0, False, [
    'Rodas de liga', 'Travas elétricas', 'Piloto automático'], 88078.64]
Carro_2 = ['Passat', 'Motor Diesel', 1991, 5712.0, False, [
    'Central multimídia', 'Teto panorâmico', 'Freios ABS'], 106161.94]


def tratamento_de_dados(lista:str)->list:
    lista_tratada=[]
    for item in lista:
        lista_tratada.append(lista)
    print(lista_tratada)
    return(lista_tratada)
    
tratamento_de_dados(Acessorios)