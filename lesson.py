# interoperability

from address import Address

import json

with open('address.json') as input_file:
    address = json.load(input_file)
    chris_address = Address.from_json(address)
print(chris_address)
