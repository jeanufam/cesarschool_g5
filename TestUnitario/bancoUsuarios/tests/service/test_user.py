from unittest import TestCase

from src.service.service_user import ServiceUser


class TestServiceUser(TestCase):

    def test_user_add_sucess(self):
        service = ServiceUser()
        user = service.add_user('GRUPO-ETA', 'QA-TESTING')
        self.assertEqual(user, 'Usuário Cadastrado')

    def test_user_name_not_string(self):
        service = ServiceUser()
        user = service.add_user(123, 'QA-TESTING')
        self.assertEqual(user, 'Parâmetros inválidos')

    def test_user_job_not_string(self):
        service = ServiceUser()
        user = service.add_user('GRUPO-ETA', 123)
        self.assertEqual(user, 'Parâmetros inválidos')

    def test_user_duplicated(self):
        service = ServiceUser()
        service.add_user('GRUPO-ETA', 'QA-TESTING')
        user = service.add_user('GRUPO-ETA', 'QA-TESTING')
        self.assertEqual(user, "Usuário já existe")

    def test_user_update_sucess(self):
        service = ServiceUser()
        service.add_user('GRUPO-ETA', 'QA-TESTING')
        user = service.update_user("GRUPO-ETA", "Desenvolvedores")
        self.assertEqual(user, 'Usuario Atualizado')

    def test_user_update_failure(self):
        service = ServiceUser()
        service.add_user('GRUPO-ETA', 'QA-TESTING')
        user = service.update_user("Grupo-5", "Desenvolvedores")
        self.assertNotEqual(user, 'Usuario Atualizado')

    def test_user_remove_sucess(self):
        service = ServiceUser()
        service.add_user('GRUPO-ETA', 'QA-TESTING')
        user = service.remove_user('GRUPO-ETA')
        self.assertEqual(user, 'Usuário removido')

    def test_user_remove_failure(self):
        service = ServiceUser()
        service.add_user('GRUPO-ETA', 'QA-TESTING')
        user = service.remove_user('Passaro')
        self.assertNotEqual(user, 'Usuário removido')

    def test_get_user_sucess(self):
        service = ServiceUser()
        service.add_user("Grupo5", "Testadores")
        user = service.get_user_by_name("Grupo5")
        self.assertEqual(user.name, 'Grupo5')

    def test_get_user_failure(self):
        service = ServiceUser()
        service.add_user("Grupo5", "Testadores")
        user = service.get_user_by_name("Grupo5")
        self.assertEqual(user.name, 'Usuario não encontrado')
