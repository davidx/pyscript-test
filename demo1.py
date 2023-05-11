import random


students = ['Tomas', 'Sher', 'Sal', 'Jose', 'Ryan', 'Lawrence', 'Mel', 'Senay', 'Christie', 'Vincent', 'Caitlyn', 
            'Adeline', 'Ray', 'Mike']


def pick(my_students):
    my_students.remove(student := random.choice(my_students))
    return student


def main():
    choice = 'y'
    while students and choice[0] not in 'nN':
        winner = pick(students)
        print("And the winner is: " + winner + "!")
        choice = input("More? [y]/n: ") or 'y'

    print('Thanks for playing!')


if __name__ == '__main__':
    main()
