string = "Exemplo de string"

def inverter_string(s):
    invertida = ""
    for i in range(len(s) - 1, -1, -1):
        invertida += s[i]
    return invertida

resultado = inverter_string(string)
print(f"String original: {string}")
print(f"String invertida: {resultado}")
