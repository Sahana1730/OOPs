class ceo():
    a=20
    @classmethod
    def show(cls):
        print(f"the attribute class is:{cls.a}")

m=ceo()
m.a=45
m.show()