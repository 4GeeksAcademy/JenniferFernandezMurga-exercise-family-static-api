
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
        self._members = []

    # read-only: Use this method to generate random members ID's when adding members into the list
    # read-only: Utilice este método para generar ID de miembros aleatorios al agregar miembros a la lista
    def _generate_id(self):
        generated_id = self._next_id
        self._next_id += 1
        return generated_id

    def add_member(self, member):
        member["last_name"] = self.last_name
        member["id"] = self._generate_id()
        member["lucky_numbers"] = list(member.get("lucky_numbers", set()))
        self._members.append(member)

        return member
        # if member not in self._members:  # Verifica si el miembro ya existe
        #     self._members.append(member)  # Agrega el miembro a la lista
        #     return f'Miembro {member} añadido.'
        # else:
        #     return f'El miembro {member} ya existe en la lista.'

   
    def delete_member(self, id):
        # Busca el miembro por id y lo elimina
        for member in self._members:
            if member['id'] == id:
                self._members.remove(member)
                return f'Miembro con id {id} ha sido eliminado.'
        return f'Miembro con id {id} no encontrado.'
        # fill this method and update the return
        

    def get_member(self, id):
        for member in self._members:
            if member['id'] == id:
                return member 
        return None

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
