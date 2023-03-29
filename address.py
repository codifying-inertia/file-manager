# create a new model object for class employee. generate 6 attributes
# create a from json as a class function
# create an instance method(NOT A FUNCTION) that will write employee to a serialized JSON file
# methods care about state.
# create a JSON project of my choosing. something that needs interoperability

import json

class Employee():
    def __init__(self, first_name, last_name, is_citizen, id_number, employee_number, position):
        self.first_name = first_name
        self.last_name = last_name
        self.is_citizen = is_citizen
        self.id_number = id_number
        self.employee_number = employee_number
        self.position = position
    
    def from_json(json_str):
        return Employee(json_str['FirstName'], json_str['LastName'], json_str['is_citizen'], json_str['id_number'], json_str['employee_number'], json_str['position'],)

    def to_json(self, employee_file):
        with open(employee_file, 'w') as e:
            json.dump(employee_file, e)

class Address():
    def __init__(self, address1, city, state, postal_code):
        self.address1 = address1
        self.city = city
        self.state = state
        self.postal_code = postal_code

    def from_json(json_str):
        return Address(json_str['Address1'], json_str['City'], json_str['State'], json_str['PostalCode'])
