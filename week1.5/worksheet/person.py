# Worksheet 1.5: Person class

from datetime import date

class Person:
    """
    A Person, with a name and a date of birth.
    """

    # Write a constructor here to create and initialize name and
    # birth fields (see README.md for further details)
    
    def __init__(self, name, birth):

        if not isinstance(name,str):
            raise TypeError("Nmae must be a string")

        if name == '':
            raise ValueError("Name must have a value")

        if not isinstance(birth, date):
            raise TypeError("birthday must be a date")


        self.name = name
        self.birth = birth

    # Implement methods initials() and is_birthday() here
    # (see README.md for further details)

    def initials(self):
        '''
        Returns the initials of the name of the person.
        '''
        names = self.name.split()
        initial = ""
        for name in names:
            initial += name[0].upper()
        return initial


    def is_birthday(self):
        '''
        Returns True if the person's birthday matches the current date and False if not.
        '''
        if date.today().month == self.birth.month and date.today().day == self.birth.day:
            return True
        return False


