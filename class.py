class Mystate:
    x = 10
    def state(self):
        self.x = self.x - 1
        print(self.x)
st = Mystate()
st.state()
st.state()
st.state()
###########
Mystate.state(st)
