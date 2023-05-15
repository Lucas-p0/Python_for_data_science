# Acessando Listas
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

Lista_c = Acessorios[0:5]+Carro_1

print(Lista_c)
