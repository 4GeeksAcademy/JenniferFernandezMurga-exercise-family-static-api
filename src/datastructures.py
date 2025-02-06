
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._next_id = 1
       

        # example list of members
        self._members = [
               {
                "id": self._generate_id(),
                "first_name": "John",
                "last_name": self.last_name,
                "age": 33,
                "Lucky Numbers": [7, 13, 22]
            },
            {
                "id": self._generate_id(),
                "name": "Jane",
                "last_name": self.last_name,
                "age": 35,
                "Lucky Numbers": [10, 14, 3]
            },
            {
               "id": self._generate_id(),
                "name": "Jimmy",
                "last_name": self.last_name,
                "age": 5,
                "Lucky Numbers": [1]
            }
        ]

    # read-only: Use this method to generate random members ID's when adding members into the list
    # read-only: Utilice este método para generar ID de miembros aleatorios al agregar miembros a la lista
    def _generate_id(self):
        generated_id = self._next_id
        self._next_id += 1
        return generated_id

    def add_member(self, member):
        #Agrega un nuevo miembro a la lista de miembros.
        if member not in self.members:  # Verifica si el miembro ya existe
            self.members.append(member)  # Agrega el miembro a la lista
            return f'Miembro {member["name"]} añadido.'
        else:
            return f'El miembro {member["name"]} ya existe en la lista.'
        # fill this method and update the return
        # rellene este método y actualice la declaración
        pass

    def delete_member(self, id):
        # Busca el miembro por id y lo elimina
        for member in self.members:
            if member['id'] == id:
                self.members.remove(member)
                return f'Miembro con id {id} ha sido eliminado.'
        return f'Miembro con id {id} no encontrado.'
        # fill this method and update the return
        pass

    def get_member(self, id):
        for member in self.members:
            if member['id'] == id:
                return member 

        # fill this method and update the return
        pass

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
