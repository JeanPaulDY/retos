
import json
from pprint import pprint
#{"Sangria": 24, "Brandi": 23, "Cerveza": 26, "Ron": 23}#
compra = input("Alcohol a comprar: ")
total = 0

string=''.join([str(item) for item in compra])
print(string)

data = '''{
    "alcohols":{"Vodka":30, "Ron":20, "Whisky":32, "Vino":15, "Cerveza":11, "Tequila":28, "Aguardiente":22, "Brandi":29, "Sangria":23}
    }'''

D = json.loads(data)

print(compra)


