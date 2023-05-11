import random

students = ['Tomas','Sher','Sal','Jose','Ryan','Lawrence','Mel','Senay','Christie','Vincent','Caitlyn','Adeline','Ray','Mike']

def pick(my_students):
    """Removes and returns a random student from the list."""
    my_students.remove(student := random.choice(my_students))
    return student

def interact_with_user(students):
    """Interacts with the user to pick a winner."""
    more = 'y'
    while students and len(more) and not more[0] in 'nN':
        winner = pick(students)
        print("And the winner is: " + winner + ")
        more = input("More? [y]/n: ")
        if not len(more):
            more = 'y'

interact_with_user(students)
print('Thanks for playing!')
