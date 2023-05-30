
#Cinco candidatos representados por dicionários: 
candidato1 = {'nome': 'Andre', 'entrevista': 8, 'teste teórico': 7, 'teste prático': 6, 'avaliação Soft skills': 9}
candidato2 = {'nome': 'Bianca', 'entrevista': 6, 'teste teórico': 7, 'teste prático': 8, 'avaliação Soft skills': 7}
candidato3 = {'nome': 'Carlos', 'entrevista': 9, 'teste teórico': 5, 'teste prático': 8, 'avaliação Soft skills': 8}
candidato4 = {'nome': 'Daniel', 'entrevista': 4, 'teste teórico': 4, 'teste prático': 5, 'avaliação Soft skills': 4}
candidato5 = {'nome': 'Erica', 'entrevista': 7, 'teste teórico': 6, 'teste prático': 8, 'avaliação Soft skills': 8}

#Resultados dos candidatos armazenados em uma lista
lista_candidatos = [candidato1, candidato2, candidato3, candidato4, candidato5]

#Função que busca os candidatos de acordo com as notas do usuário
def buscar_candidatos_por_notas():
    notas_entrevista = int(input('Digite a nota mínima da entrevista: '))
    notas_teste_teórico = int(input('Digite a nota mínima do teste teórico: '))
    notas_teste_prático = int(input('Digite a nota mínima do teste prático: '))
    notas_avaliação_soft_skills = int(input('Digite a nota mínima da avaliação de soft skills: '))
    # Criada uma lista vazia para armazenar os candidatos que atendem aos critérios de notas mínimas.
    candidatos_compatíveis = []
    #Um loop for é utilizado para percorrer cada candidato na lista candidatos.
    for candidato in lista_candidatos:
       #Para cada candidato, é verificado se todas as notas são maiores ou iguais as notas mínimas pedidas pelo usuário. Se todas as notas forem maiores ou iguais, o candidato é considerado compatível e adicionado à lista candidatos compatíveis.
       if (candidato['entrevista'] >= notas_entrevista) and (candidato['teste teórico'] >= notas_teste_teórico) and (candidato['teste prático'] >= notas_teste_prático) and (candidato['avaliação Soft skills'] >= notas_avaliação_soft_skills):
            candidatos_compatíveis.append(candidato)
    # Depois de percorrer todos os candidatos a função retorna a lista candidatos compatíveis.
    return candidatos_compatíveis

#Exemplo de uso da função e atribuindo o resultado à variável candidatos compatíveis.
candidatos_compatíveis = (buscar_candidatos_por_notas())
if len(candidatos_compatíveis) > 0:
    #Se houver candidatos compatíveis na lista, um loop for é utilizado para repetir a execução em cada candidato e imprimir seu nome e suas notas individuais.
    for candidato in candidatos_compatíveis:
        print(f"{candidato['nome']} - e{candidato['entrevista']}_t{candidato['teste teórico']}_p{candidato['teste prático']}_s{candidato['avaliação Soft skills']}")
#Se não houver candidatos compatíveis, é exibida a mensagem "Nenhum candidato dentro do perfil.".
else:
    print('Nenhum candidato dentro do perfil.')

