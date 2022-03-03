class Person:

    # class variable: every instance will inherit this value
    nationality = "italy" 

    def __init__(self, name, job=None, pay=0):
        """Constructor. It runs every instance is created"""
        self.name = name
        self.job = job
        self.pay = pay

    # Behaviour Methods
    def lastName(self):
        """Extract object's last name"""
        return self.name.split()[-1]  # self is implied subject

    def giveRaise(self, percent):
        """Give this object a raise"""
        self.pay = int(self.pay * (1 + percent))  # much change here only

    def __repr__(self):
        """"
        If you don't overload __str__ when running:
        >>> print(sue) # will show something like
        <__main__.Person object at 0x7fa3288ed9d0> 
        __repr__ and __str__ are run automatically everytime an instance is converted to its print string.
        o __str__ are used for more user friedly info
        o __repr__ is used to provide extra details to developers
        """
        return "[Person: %s, %s]" % (self.name, self.pay)  # string to print
    

class Manager(Person):
    # Inherit Person attrs
    def giveRaise(self, percent, bonus=0.10):  # Redefine method
        Person.giveRaise(self, percent+bonus)  # GOOD way: augment original

if __name__ == "__main__":  # when run for testing only

    # create object instances
    bob = Person("Bob Smith")
    sue = Person("Sue Jones", job='dev', pay=100)
    tom = Manager("Tom Jonen", 'mgr', 1000)
    for obj in (bob, sue, tom):
        obj.giveRaise(0.10)
        print(obj)

    # show special class attribute
    print(bob.__class__)                # Show bob's class and his name
    print(bob.__class__.__bases__)

    # show attribute (the one defined in __init__)
    for key in bob.__dict__:
        print(key, "=>", bob.__dict__[key]) # 1st way
        print(key, "=>", getattr(bob,key))  # 2nd way useful to catch exception