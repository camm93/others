from ..config import log


class Person:

    def __init__(self, person_id=None, name=None, surname=None, email=None):
        self._person_id = person_id
        self._name = name
        self._surname = surname
        self._email = email

    @property
    def person_id(self):
        return self._person_id

    @person_id.setter
    def person_id(self, person_id):
        self._person_id = person_id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def surname(self):
        return self._surname

    @surname.setter
    def surname(self, surname):
        self._surname = surname

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email

    def __str__(self):
        return f"Person[Id: {self._person_id}, name: {self._name}, surname: {self._surname}, email: {self._email}]"


if __name__ == '__main__':
    person = Person(1, "Juan", "Pérez", "jperez@mail.com")
    log.debug(f"Created {person}")
    # simulate an insert
    person1 = Person(name="Carmen", surname="Carmona", email="carmona@mail.com")
    log.debug(f"Created {person}")
    # simulate a delete
    person1 = Person(person_id=1)
    log.debug(f"Deleted {person1}")
