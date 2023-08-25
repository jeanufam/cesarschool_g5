from src.models.store import Store
from src.models.user import User
from src.service.service_user import ServiceUser

s1 = ServiceUser()

print("##############################")
s = Store()
result = s1.add_user("Fabricio", "Engenheiro")
print(result)
for i in s1.store.bd:
    print(i.name," - ", i.job)
print("##############################")

s = Store()
result = s1.update_user("Fabricio", "Desenvolvedor")
print(result)
for i in s1.store.bd:
    print(i.name," - ", i.job)
print("##############################")

s = Store()
result = s1.get_user_by_name("Fabricio")
print(result.name,"-",result.job)
print("##############################")


s = Store()
result = s1.remove_user("Fabricio")
print(result)
for i in s1.store.bd:
    print(i.name," - ", i.job)
print("##############################")

'''
print(result)
print("##########")
print(result2)

u1 = User("Fabricio", "Engenheiro")
print(u1.name)
print(u1.job)
print("##########")

u2 = User("Torquato", "Eng")
print(u2.name)
print(u2.job)
print("##########")

s1 = Store()
s1.bd.append(u1)
s1.bd.append(u2)

print(s1.bd[0].name)
'''

'''
print(result)
result = s1.add_user("Torquato", "Eng")
print(result)
print(s1.store.bd[0].name)
print(s1.store.bd[1].job)
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
'''