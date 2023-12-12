import sys

try:
    f = open("waznedane.txt","r",encoding="utf-8")
    s = f.readline()
    i = int(s.strip())
    raise Exception(d=i/0)
except OSError as err:
    print(f"błąd systemowy: {err}")
except ValueError:
    print("nie można przekonwertować danych typu str na int...")
except Exception as exc:
    print(f"klasa błędu: {type(exc)}")
    print(exc.args)
    print(exc)
except:
    print(f'nieoczekiwany błąd: {sys.exc_info()}')
else:
    print("plik odczytany")
finally:
    print("koniec analizy błędów")
    f.close()
