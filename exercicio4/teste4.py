import xml.etree.ElementTree as ET

# diário a partir do XML
def calcular_faturamento(dados):
    faturamentos = [float(dia.find('valor').text) for dia in dados if float(dia.find('valor').text) > 0]
    if not faturamentos:  # Verifica se a lista está vazia
        return None, None, 0
    media = sum(faturamentos) / len(faturamentos)
    return min(faturamentos), max(faturamentos), sum(1 for f in faturamentos if f > media)

# XML
try:
    tree = ET.ElementTree(ET.fromstring('''<root>
    <row>
        <dia>1</dia>
        <valor>31490.7866</valor>
    </row>
    <row>
        <dia>2</dia>
        <valor>37277.9400</valor>
    </row>
    <row>
        <dia>3</dia>
        <valor>37708.4303</valor>
    </row>
    <row>
        <dia>4</dia>
        <valor>0.0000</valor>
    </row>
    <row>
        <dia>5</dia>
        <valor>0.0000</valor>
    </row>
    <row>
        <dia>6</dia>
        <valor>17934.2269</valor>
    </row>
    <row>
        <dia>7</dia>
        <valor>0.0000</valor>
    </row>
    <row>
        <dia>8</dia>
        <valor>6965.1262</valor>
    </row>
    <row>
        <dia>9</dia>
        <valor>24390.9374</valor>
    </row>
    <row>
        <dia>10</dia>
        <valor>14279.6481</valor>
    </row>
    <row>
        <dia>11</dia>
        <valor>0.0000</valor>
    </row>
    <row>
        <dia>12</dia>
        <valor>0.0000</valor>
    </row>
    <row>
        <dia>13</dia>
        <valor>39807.6622</valor>
    </row>
    <row>
        <dia>14</dia>
        <valor>27261.6304</valor>
    </row>
    <row>
        <dia>15</dia>
        <valor>39775.6434</valor>
    </row>
    <row>
        <dia>16</dia>
        <valor>29797.6232</valor>
    </row>
    <row>
        <dia>17</dia>
        <valor>17216.5017</valor>
    </row>
    <row>
        <dia>18</dia>
        <valor>0.0000</valor>
    </row>
    <row>
        <dia>19</dia>
        <valor>0.0000</valor>
    </row>
    <row>
        <dia>20</dia>
        <valor>12974.2000</valor>
    </row>
    <row>
        <dia>21</dia>
        <valor>28490.9861</valor>
    </row>
    <row>
        <dia>22</dia>
        <valor>8748.0937</valor>
    </row>
    <row>
        <dia>23</dia>
        <valor>8889.0023</valor>
    </row>
    <row>
        <dia>24</dia>
        <valor>17767.5583</valor>
    </row>
    <row>
        <dia>25</dia>
        <valor>0.0000</valor>
    </row>
    <row>
        <dia>26</dia>
        <valor>0.0000</valor>
    </row>
    <row>
        <dia>27</dia>
        <valor>3071.3283</valor>
    </row>
    <row>
        <dia>28</dia>
        <valor>48275.2994</valor>
    </row>
    <row>
        <dia>29</dia>
        <valor>10299.6761</valor>
    </row>
    <row>
        <dia>30</dia>
        <valor>39874.1073</valor>
    </row>
</root>'''))

    root = tree.getroot()
    dados_faturamento = root.findall('row')
except ET.ParseError:
    print("Erro ao decodificar o arquivo XML.")
    exit()

# faturamento diário
menor, maior, dias_acima_media = calcular_faturamento(dados_faturamento)

if menor is not None and maior is not None:
    print(f"Menor faturamento diário: R${menor:.2f}")
    print(f"Maior faturamento diário: R${maior:.2f}")
    print(f"Dias com faturamento acima da média: {dias_acima_media}")
else:
    print("Não há faturamentos para calcular.")

# faturamento por estado
faturamento_por_estado = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

faturamento_total = sum(faturamento_por_estado.values())

print("\nPercentual de faturamento por estado:")
for estado, valor in faturamento_por_estado.items():
    percentual = (valor / faturamento_total) * 100
    print(f"{estado}: {percentual:.2f}%")
