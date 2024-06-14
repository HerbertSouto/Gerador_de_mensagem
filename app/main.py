import csv
from collections import defaultdict

# Caminho para o arquivo CSV
desconto_dados = r"C:\Users\herbe\Desktop\MsgAut\src\desconto.csv"

# Dicionário para armazenar os dados agrupados por motorista
dados_por_motorista = defaultdict(list)

# Lendo os dados do arquivo CSV e agrupando por motorista
with open(desconto_dados, mode="r") as dados:
    leitor = csv.DictReader(dados)
    for linha in leitor:
        motorista = linha["MOTORISTA"]
        dados_por_motorista[motorista].append(
            {
                "ID": linha["ID"],
                "PLACA": linha["PLACA"],
                "SPX TRACKING NUMBER": linha["SPX TRACKING NUMBER"],
                "DATA DA COLETA": linha["DATA DA COLETA"],
                "VALOR": float(linha["VALOR"]),
                "TELEFONE": linha["TELEFONE"],
            }
        )

# Iterando sobre os dados agrupados e gerando mensagem para cada motorista
for motorista, pacotes in dados_por_motorista.items():
    # Formatando a mensagem para cada motorista
    mensagem = f"Prezado(a) {motorista},\n"
    mensagem += "Gostaríamos de informar que, devido a eventos ocorridos durante a prestação de serviços de transporte realizada por você, será necessário realizar um desconto nos seus fretes futuros. Esse desconto visa cobrir o prejuízo decorrente dos referidos eventos. Abaixo estão os detalhes das entregas afetadas:\n\n"

    # Adicionando detalhes de cada pacote do motorista
    for pacote in pacotes:
        mensagem += f"SPX TRACKING NUMBER: {pacote['SPX TRACKING NUMBER']}\n"
        mensagem += f"Data da Coleta: {pacote['DATA DA COLETA']}\n"
        mensagem += f"Valor do Prejuízo: R$ {pacote['VALOR']:.2f}\n\n"

    # Calculando o total do prejuízo para o motorista
    total_prejuizo = sum(pacote["VALOR"] for pacote in pacotes)
    mensagem += f"Total do Prejuízo: R$ {total_prejuizo:.2f}\n\n"
    mensagem += "Valor do Desconto por Frete (%): 25\n"
    mensagem += "Início do Desconto: No próximo dia útil\n\n"
    mensagem += "Caso haja descontinuidade na prestação de serviços, ou impossibilidade de parcelamento dos descontos, fica a DHL expressamente autorizada a reter o valor total ou remanescente do prejuízo compensando-os de fretes e demais pagamentos devidos.\n\n"
    mensagem += "Atenciosamente,\n"
    mensagem += "Equipe de Suporte ao Cliente\n\n"

    # Imprimindo a mensagem para o motorista atual
    print(mensagem)
