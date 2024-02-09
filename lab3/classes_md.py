#Exercises 1;
class stringmd:
    def getstring(self):
       s = input()
       return s
    def printstring(self, s):
        print(s.upper())

#Exercises 2;
class Shape:
    def __init__(self):
       pass
       def area (self):
           return 0
class Square(Shape):
    def __init__(self,length):
        super().__init__()
        self.length = length
        def area (self)
           return self.length ** 2
    
# Пример использования:
shape = Shape()
print("Площадь фигуры:", shape.area())

square = Square(4)
print("Площадь квадрата:", square.area())

#Exercises 3;
class Shape:
    def __init__(self)
        pass
    def area(self):
        return 0
    class Rectangle(Shape):
            def __init__(self, length, width):
                self.length = length
                self.width = width
                def area (self):
                    return  length * width
                
shape = Shape()
print("Площадь фигуры:" shape.area)


#Exercises 4;
class Point:
    def __init__(self, x , y):
        self.x = x
        self.y = y
    def show(self):
        return (x, y)
    def move(self):
        self.end_x = int(input())
        self.end_y = int(input())
def distance (self):
    return math.sqrt((x - end_x)**2+(y - end_y)**2)
x=int(input())
y=int(input())
point1 = Point(x, y)
point1.move()
print(point1.distance )

#Exercises 5;
class Account:
   def __init__(self, owner, balance):
    self.owner = owner
    self.balance = balance 
    def deposit(self, amount)
        self.amount = amount
        if amount > 0:
            self.balance +=amount
            print("New balance:", self.balance)
        else :
           print("Old balance:", self.balance)

    def withdraw(self, money)
        self.money = money 
        if money > 0:
           if money < self.balance:
               self.balance -=money
               print("new balance:", self balance)
        else:
          print("old balance:", self balance)
account = Account(owner="Dinmukhamed Sairambayev", balance=1000)

account.deposit(500)
account.withdraw(200)

#Exercises 6;
class Prime:
    def __init__(self, integer):
        self.integer = integer
        
    def is_prime(self):
        if self.integer < 2:
            return False
        for i in range(2, self.integer):
            if self.integer % i == 0:
                return False
        return True 
    
    @staticmethod
    def filter_integer(integers):
        return list(filter(lambda x: Prime(x).is_prime(), integers))

# Example usage:
integers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
prime_numbers = Prime.filter_integer(integers)
print("Prime numbers:", prime_numbers)


