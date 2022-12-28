import random
n = 5


class Field:
    def __init__(self, *characters):
        self.matrix = []
        self.list = [*characters]

    def render(self):
        for i in range(n):
            self.matrix.append([0] * n)

        for i in range(len(self.list)):
            self.matrix[self.list[i].y][self.list[i].x] = self.list[i].sign

        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                print(self.matrix[i][j], end=' ')
            print()


class Character:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        self.__sign = 1

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def sign(self):
        return self.__sign

    @sign.setter
    def sign(self, sign):
        if sign == 1:
            self.__sign = sign
        else:
            print("Here can be only 1")

    def move(self, matrix, obstacle):
        direction = input(f'Choose direction where you want to go, Player {self.sign}: ')
        if direction == 'w' and self.y != 0 and matrix[self.y-1][self.x] != obstacle.sign:
            self.__y -= 1
        elif direction == 's' and self.y != n-1 and matrix[self.y+1][self.x] != obstacle.sign:
            self.__y += 1
        elif direction == 'a' and self.x != 0 and matrix[self.y][self.x-1] != obstacle.sign:
            self.__x -= 1
        elif direction == 'd' and self.x != n-1 and matrix[self.y][self.x+1] != obstacle.sign:
            self.__x += 1
        elif ((self.y == 0 or matrix[self.y-1][self.x] == obstacle.sign) and direction == 'w') or \
                ((self.y == n-1 or matrix[self.y+1][self.x] == obstacle.sign) and direction == 's') or \
                ((self.x == 0 or matrix[self.y][self.x-1] == obstacle.sign) and direction == 'a') or \
                ((self.x == n-1 or matrix[self.y][self.x+1] == obstacle.sign) and direction == 'd'):
            print('In front of you is an obstacle.')
        else:
            print('I didn\'t understand what you said.')


class Outsider(Character):
    def __init__(self, x, y):
        super(Outsider, self).__init__(x, y)
        self.__sign = 2

    @property
    def sign(self):
        return self.__sign

    @sign.setter
    def sign(self, sign):
        if sign == 2:
            self.__sign = sign
        else:
            print("Here can be only 2")


def main():
    human = Character(random.randint(0, 1), random.randint(0, 1))
    outsider = Outsider(random.randint(3, 4), random.randint(3, 4))
    field = Field(human, outsider)
    field.render()
    print('*************************')
    while True:
        human.move(field.matrix, outsider)
        field = Field(human, outsider)
        field.render()
        print('*************************')
        outsider.move(field.matrix, human)
        field = Field(human, outsider)
        field.render()
        print('*************************')


main()
