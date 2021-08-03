class Parent:
    def __init__(self):
        self.num = 100

    def first_method(self):
        print("First Function")


class Parent2(Parent):
    def second_metod(self):
        super().first_method()


p = Parent2()
p.first_method()
