import os 

os.system('cls')

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        class_name = self.__class__.__name__
        return f'{class_name}(x={self.x!r}, y={self.y!r})'  

    def __add__(self, other):
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Point(new_x, new_y)
    
    def __gt__(self, other):
        result_self = self.x + self.y
        result_other = other.x + other.y
        return result_self > result_other
    
if __name__ == '__main__':
    p1 = Point(4, 2)
    p2 = Point(6, 4)

    p3 = p1 + p2
    print(p3)

    print('p1 > p2?', p1 > p2)
    print('p2 > p1?', p2 > p1)


