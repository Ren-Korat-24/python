class animal:
    def types(self):
        print("There are diiferent type of animals..")

    def bark(self):
        print("Animal bark..")

class dog(animal):
    def sound_dog(self):
        print("This sound is dog..")

A=dog()
A.types()
A.bark()
A.sound_dog()