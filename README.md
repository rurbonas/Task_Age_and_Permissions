# Control Flow Age and Permission

## Summary

Simple program to use control flow
(Create a class and function to achieve this.)
## Tasks

* rules of what the program to do are followed, see bellow

Starter code
```
age = 19
driver_license = True


# - You can vote and driver
# - You can vote
# - You can driver
# - you can't legally drink but your mates/unties might have your back (bigger 16)
# - Your too young, go back to school!


 #  as a user I should be able to keep being prompted for input until I say 'exit'

```

## Acceptance Criteria
* class created with required function/s 
* is a program that run continuously
* handles strings and integers
* has exist condition
* all business logic works

```python
class Person:
    def __init__(self): # initialise with built in method called __init__(self) - self refers to current class
        # we declare attributes in our methods
        self.vote_age = 18
        self.age = int(input("What is your age? >> "))
        self.driver_license = str(input("Do you have a driving license?  yes/no >> ").lower())

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

student = Person()
while True:
    stop = ""
    if stop == "exit":
        break
    # - You can vote
    print(student.drink())
    # # - You can drive
    print(student.drive())
    # - You can vote
    print(student.can_i_vote())
    stop = input("Would you like to try again? ")
```