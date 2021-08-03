class Jumps:
    def __init__(self, size, my_list):
        self.size = size
        self.my_list = my_list

    def minimum_jump(self):
        i = 0
        jump = 0
        for i in range(0, self.size):
            while i <= self.size:
                if self.my_list[i] == 0:
                    print("0 Encountered!")
                elif self.my_list[i] != 0:
                    i = self.my_list[i]
                    jump += 1
                    #print("Jumped to: ", self.my_list[i], "Jump: ", jump)
                elif self.my_list[i] >= self.my_list[size]:
                    print(jump)


size = int(input("Enter size: "))
list = [int(x) for x in input("Enter list: ").split()]
jp = Jumps(size, list)
jp.minimum_jump()
