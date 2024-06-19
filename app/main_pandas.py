import pandas as pd
import chardet

# Caminho para o arquivo CSV
desconto_dados = "src/desconto.csv"

# Detectando a codificação do arquivo CSV
with open(desconto_dados, 'rb') as f:
    result = chardet.detect(f.read(10000))
    encoding = result['encoding']
    print(f"Codificação detectada: {encoding}")

# Lendo os dados do arquivo CSV usando a codificação detectada
df = pd.read_csv(desconto_dados, encoding=encoding)

# Agrupando os dados por motorista
dados_por_motorista = df.groupby("ID")

# Iterando sobre os dados agrupados e gerando mensagem para cada motorista
for motorista_id, pacotes in dados_por_motorista:
    # Pegando o nome do motorista a partir do primeiro pacote
    motorista_nome = pacotes.iloc[0]["MOTORISTA"]

    # Formatando a mensagem para cada motorista
    mensagem = f"Prezado(a) {motorista_nome},\n"
    mensagem += "Gostaríamos de informar que, devido a eventos ocorridos durante a prestação de serviços de transporte realizada por você, será necessário realizar um desconto nos seus fretes futuros. Esse desconto visa cobrir o prejuízo decorrente dos referidos eventos. Abaixo estão os detalhes das entregas afetadas:\n\n"

    # Adicionando detalhes de cada pacote do motorista
    for _, pacote in pacotes.iterrows():
        mensagem += f"SPX TRACKING NUMBER: {pacote['SPX TRACKING NUMBER']}\n"
        mensagem += f"Data da Coleta: {pacote['DATA DA COLETA']}\n"
        mensagem += f"Valor do Prejuízo: R$ {pacote['VALOR']:.2f}\n\n"

    # Calculando o total do prejuízo para o motorista
    total_prejuizo = pacotes["VALOR"].sum()
    mensagem += f"Total do Prejuízo: R$ {total_prejuizo:.2f}\n\n"
    mensagem += "Valor do Desconto por Frete (%): 25\n"
    mensagem += "Início do Desconto: No próximo dia útil\n\n"
    mensagem += "Caso haja descontinuidade na prestação de serviços, ou impossibilidade de parcelamento dos descontos, fica a DHL expressamente autorizada a reter o valor total ou remanescente do prejuízo compensando-os de fretes e demais pagamentos devidos.\n\n"
    mensagem += "Atenciosamente,\n"
    mensagem += "Equipe de Suporte ao Cliente\n\n"

    # Imprimindo as mensagens
    print(mensagem)
