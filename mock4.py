class Jumps:
    def __init__(self, size, my_list):
        self.size = size
        self.my_list = my_list

    def minimum_jump(self):
        jump = 0
        for i in range(0, self.size):
            while i <= self.size:
                try:
                    if self.my_list[i] == 0:
                        print("0 Encountered!")
                    elif self.my_list[i] != 0:
                        if self.my_list[i] < self.size:
                            i += self.my_list[i]
                            jump += 1
                            print("jumped to: ", self.my_list[i], "Jump: ", jump)
                        else:
                            print(jump)
                            exit()
                except IndexError:
                    print(jump)
                    exit()


size = int(input("Enter size: "))
list = [int(x) for x in input("Enter list: ").split()]
jp = Jumps(size, list)
jp.minimum_jump()
