class Person:
    def __init__(self, age, license): # initialise with built in method called __init__(self) - self refers to current class
        # we declare attributes in our methods
        self.vote_age = 18
        self.age = age
        self.driver_license = license

    def drink(self):
        if self.age >= 18:
            return "You can legally drink."
        elif self.age >= 16 and self.age < 18:
            return "You can only drink with an adult supervision."
        return "You are not old enough to drink."

    def drive(self):
        if self.driver_license == "yes":
            return "Time to ride!"
        return "Go pass your driving test first."

    def can_i_vote(self):
        if self.age == self.vote_age:
            return "Go to the voting booth."
        return "Maybe better luck next year."

    def again(self):
        if self.age == self.vote_age:
            return "Go to the voting booth."
        return "Maybe better luck next year."

stop = ""
#  as a user I should be able to keep being prompted for input until I say 'exit'
while True:
    if stop == "exit":
        break
    age = int(input("What is your age? >> "))
    license = str(input("Do you have a driving license?  yes/no >> ").lower())
    student = Person(age, license)

    # - You can vote
    print(student.drink())
    # # - You can drive
    print(student.drive())
    # - You can vote
    print(student.can_i_vote())
    stop = input("Shall we try again? Write exit to stop >>")





