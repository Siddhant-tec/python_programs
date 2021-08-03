class Myparty:
    x = 0
    name = ''

    def __init__(self, nam):
        self.name = nam
        print(self.name, 'Constructed')

    def party(self):
        self.x = self.x + 1
        print(self.name, "Party count", self.x)


s = Myparty('Siddhant')
t = Myparty('Timmy')
s.party()
t.party()
s.party()


