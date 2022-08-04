from unittest import TestCase
from ..models import Person


class TestPerson(TestCase):
    def setUp(self) -> None:
        self.expected_values()

    def expected_values(self):
        self.person_id = 1
        self.name = "test_name"
        self.surname = "test_surname"
        self.email = "test@mail.com"

    def test_create_person_empty_fields(self) -> None:
        person = Person()
        self.assertIsNone(person.person_id)
        self.assertIsNone(person.name)
        self.assertIsNone(person.surname)
        self.assertIsNone(person.email)

    def test_create_person_with_all_fields(self) -> None:
        person = Person(self.person_id, self.name, self.surname, self.email)
        self.assertEqual(self.person_id, person.person_id)
        self.assertEqual(self.name, person.name)
        self.assertEqual(self.surname, person.surname)
        self.assertEqual(self.email, person.email)
