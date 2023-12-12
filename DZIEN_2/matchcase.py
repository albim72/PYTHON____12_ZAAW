def provideAccess(user):
    return {
        "username":user,
        "password":"admin"
    }

def rumMatch():
    user = input("podaj nazwę użytkowmnika: ")

    match user:
        case "Olga":
            print("Olga nie ma dostępu do bazy danych SYSDB...., tylko do api code")
        case "Adam":
            print("Adam nie ma dostępu do bazy danych SYSDB...., tylko do fronted code")
        case "Adam":
            print("Adam jest kierownikiem projektu")
        case "Olaf":
            print("Olaf ma dostęp do bazy danych SYSDB.")
            print(provideAccess("Olaf"))
        case _:
            print("taki user nie istnieje!")

if __name__ == '__main__':
    for _ in range(3):
        rumMatch()
