class MojaMeta(type):
    def __new__(cls,clasname,superclasses,attrs):
        print(f"_____________ {cls.__class__.__name__} _________________")
        print(f"nazwa klasy: {clasname}")
        print(f"dziedziczone klasy: {superclasses}")
        print(f"zbiór atrybutów klasy: {attrs}")
        return type.__new__(cls,clasname,superclasses,attrs)

    def jedynka(cls):
        return 1


class S:
    pass

class F:
    pass

class Specjalna(S,metaclass=MojaMeta):
    pass

class B(Specjalna):
    pass

class C(F,B):
    pass

cf = C
print(cf.jedynka())

# cf = C()
# print(cf.jedynka())
