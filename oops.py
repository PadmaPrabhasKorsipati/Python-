

class Animals:

    def __init__(self,name):

        self.name=name

        self.is_alive=True


    def eat(self):

        print(f"{self.name} is eating")
    
    def sleep(self):

        print(f"{self.name} is sleeping")





class Dog(Animals):
    pass


class Cat(Animals):
    pass

class Mouse(Animals):
    pass


dog=Dog("Shiro")
cat=Cat("Garfield")
mouse=Mouse("Jerry")


print(cat.name)
print(cat.is_alive)

cat.eat()
cat.sleep()


        











