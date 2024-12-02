import os
os.system('clear')

def somaImposto(taxaImposto, custo):
    result = custo * (1 + (taxaImposto/100))
    return result