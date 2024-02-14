import xml.etree.ElementTree as ET


def ler_arquivo_xml(dados):
    try:

        tree = ET.parse(dados)
        root = tree.getroot()

        faturamento_diario = []

        for row in root.iter('row'):
            valor_faturamento = float(row.find('valor').text)
            faturamento_diario.append(valor_faturamento)

        return faturamento_diario

    except ET.ParseError as e:
        print(f"Erro ao parsear o arquivo XML: {e}")


def analisar_faturamento_anual():
    faturamento_diario = ler_arquivo_xml(dados)

    menor_valor = min(faturamento_diario)
    maior_valor = max(faturamento_diario)

    dias_sem_faturamento = len([f for f in faturamento_diario if f == 0])
    print(f"Quantidade de dias sem faturamento: {dias_sem_faturamento}")

    dias_com_faturamento = [f for f in faturamento_diario if f > 0]

    if dias_com_faturamento:
        media_anual = sum(dias_com_faturamento) / len(dias_com_faturamento)
        print(f"Media anual: R${media_anual:.2f}")
    else:
        media_anual = 0

    dias_acima_da_media = len([f for f in faturamento_diario if f > media_anual])

    return menor_valor, maior_valor, dias_acima_da_media


if __name__ == "__main__":
    dados = 'dados.xml'
    ler_arquivo_xml(dados)

    menor, maior, acima_media = analisar_faturamento_anual()

    print(f"Menor valor de faturamento diário: R$ {menor:.2f}")
    print(f"Maior valor de faturamento diário; R${maior:.2f}")
    print(f"Dias com faturamento acima da média: {acima_media}")
