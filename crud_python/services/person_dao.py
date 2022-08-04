"""Data Access Object"""
from lessons_310.others.crud_python.database import Postgresql
from lessons_310.others.crud_python.models import Person
from lessons_310.others.crud_python.config import log


class PersonDAO:
    """
    Perform CRUD operations on the db
    CRUD (Create, Read, Update, Delete)
    """
    _TABLE_NAME = "persona"
    _DELETE_SENTENCE = f"DELETE FROM {_TABLE_NAME} WHERE id=%s"
    _INSERT_SENTENCE = f"INSERT INTO {_TABLE_NAME}(name, surname, email) VALUES(%s, %s, %s)"
    _SELECT_SENTENCE = f"SELECT * FROM {_TABLE_NAME} ORDER BY id"
    _UPDATE_SENTENCE = f"UPDATE {_TABLE_NAME} SET name=%s, surname=%s, email=%s WHERE id=%s"

    @classmethod
    def select(cls):
        with Postgresql.get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(cls._SELECT_SENTENCE)
                rows = cursor.fetchall()
                people = map(lambda x: Person(*x), rows)
                return people

    @classmethod
    def insert(cls, person: Person):
        with Postgresql.get_connection():
            with Postgresql.get_cursor() as cursor:
                values = (person.name, person.surname, person.email)
                cursor.execute(cls._INSERT_SENTENCE, values)
                n_inserted = cursor.rowcount
                log.info(f"{n_inserted} person(s) created: {person}")
                return n_inserted

    @classmethod
    def update(cls, person: Person):
        with Postgresql.get_connection():
            with Postgresql.get_cursor() as cursor:
                values = (person.name, person.surname, person.email, person.person_id)
                cursor.execute(cls._UPDATE_SENTENCE, values)
                n_updated = cursor.rowcount
                log.info(f"{n_updated} person(s) updated: {person}")
                return n_updated

    @classmethod
    def delete(cls, person: Person):
        with Postgresql.get_connection():
            with Postgresql.get_cursor() as cursor:
                values = (person.person_id, )
                cursor.execute(cls._DELETE_SENTENCE, values)
                n_deleted = cursor.rowcount
                log.info(f"Person with id: {person}. {n_deleted} people have been deleted.")
                return n_deleted


if __name__ == '__main__':
    # -- insert a record
    # person1 = Person(name="Diego", surname="Diogo", email="didi@mail.com")
    # PersonDAO.insert(person1)

    # -- Update a record
    # persona = Person(5, "Carlos", "Carrillo", "carlillo@mail.com")
    # PersonDAO.update(persona)

    # -- Delete a record
    persona = Person(person_id=22)
    PersonDAO.delete(persona)

    # -- select
    people = PersonDAO.select()
    for person in people:
        print(person)
    Postgresql.close()
