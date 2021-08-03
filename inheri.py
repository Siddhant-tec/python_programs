class Myparty:
    x = 0
    name = ''

    def __init__(self, nam):
        self.name = nam
        print(self.name, 'Constructed')

    def party(self):
        self.x = self.x + 1
        print(self.name, "Party count", self.x)


class Cricket(Myparty):
    points = 0

    def six(self):
        self.points = self.points + 6
        self.party()
        print(self.name, "scores", self.points)


s = Myparty("Siddhant")
s.party()
t = Cricket("Timmy")
t.party()
t.six()
