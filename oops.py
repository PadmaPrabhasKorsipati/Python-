

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


print(dog.name)
print(dog.is_alive)

dog.eat()
dog.sleep()


        











