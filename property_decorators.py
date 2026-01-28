class ceo:
    @property
    def name(self):
        return self.ename

    @name.setter
    def name(self, value):
        self.ename = value

    def show(self):
        print(f"CEO name is: {self.name}")


e = ceo()
e.name = "sahana"
e.show()
