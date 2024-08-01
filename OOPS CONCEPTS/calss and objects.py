class Dog:
    def __init__ (self,name,age):
        self.name=name
        self.age=age
    def bark(self):
        print(f"{self.name}says Woof!")
dog1=Dog("Buddy",3)
dog2=Dog("Molly",2)
print(f"{dog1.name}is {dog1.age}years old.")
dog2.bark()
        
