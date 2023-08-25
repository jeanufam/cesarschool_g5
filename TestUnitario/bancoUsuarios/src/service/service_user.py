from src.models.store import Store
from src.models.user import User

"""
Escopo:
1- Desenvolver o método add_user
- Verificar se os parametros é Str e diferente de None; OK
- Verificar se o nome não existe para adicionar; OK

2- Desenvolver o metodo remove_user
- Verificar se os parametros é Str e diferente de None; OK
- Verificar se o nome já existe para remover; OK

3- Desenvolver o método update_user
- Verificar se os parametros é Str e diferente de None;
- Verificar se o nome já existe para atualizar;

4- Desenvolver o método get_user_by_name
- Verificar se os parametros é Str e diferente de None;
- Verificar se o nome já existe para atualizar;

Fora de escopo:
1 – Desenvolver testes unitarios
"""

class ServiceUser:
    def __init__(self):
        self.store = Store()

    def busca_user(self, name):
        for user in self.store.bd:
            if user.name == name:
                return user
        return None

    def add_user(self, name, job):
        if isinstance(name, str) and isinstance(job, str):
            if name is not None and job is not None:
                if self.busca_user(name) is None:
                    u1 = User(name, job)
                    self.store.bd.append(u1)
                    return "Usuário Cadastrado"
                else:
                    return "Usuário já existe"
            else:
                return "Parâmetros inválidos"
        else:
            return "Parâmetros inválidos"

    def update_user(self, name, newjob):
        if isinstance(name, str) and isinstance(newjob, str) and name is not None and newjob is not None:
            for user in self.store.bd:
                if user.name == name:
                    user.job = newjob
                    return "Usuario Atualizado"
        else:
            return "Parâmetros inválidos"
        return "Usuario não cadastrado"

    def remove_user(self, name):
        resp = self.busca_user(name)
        if resp is not None:
            self.store.bd.remove(resp)
            return "Usuário removido"
        else:
            return "Usuário não encontrado"

    def get_user_by_name(self, name):
        if isinstance(name, str) and name is not None:
            resp = self.busca_user(name)
            if resp is not None:
                return resp
            else:
                return "Usuario não encontrado"
        else:
            return "Parâmetros inválidos"


