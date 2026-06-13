

class Animals:

    def __init__(self,name):

        self.name=name

        self.is_alive=True


    def eat(self):

        print(f"{self.name} is eating")
    
    def sleep(self):

        print(f"{self.name} is sleeping")



class Dog(Animals):
    def speak(self):
        print("Bow!")


class Cat(Animals):
    def speak(self):
        print("Meow!")


class Mouse(Animals):
    def speak(self):
        print("Squeek!")


dog=Dog("Shiro")
cat=Cat("Garfield")
mouse=Mouse("Jerry")


print(cat.name)
print(cat.is_alive)

cat.eat()
cat.sleep()
cat.speak()


        











