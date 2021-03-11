

user_list = [
    "Dylan|Reinhold|M|43", 
    "Bob|Jones|M|16", 
    "Sally|Smith|F|33", 
    "Nancy|Jones|F|15"
    ]

class Person:
    def __init__(self, first, last, sex, age):
        self.first = first
        self.last = last
        self.sex = sex
        self.age = age

    def formal_gretting(self):
        # Return title than first and last name
        if self.sex == 'F':
            return 'Ms {} {}'.format(self.first, self.last)
        if self.sex == 'M':
            return 'Mr {} {}'.format(self.first, self.last)

    def normal_geeting(self):
        # return First Name then Last Name
        pass

    def casual_greeting(self):
        # just return first name
        pass

    def last_first_greeting(self):
        # return "last name, first name"
        return('{}, {}'.format(self.first, self.last))

    def is_adult(self):
        # return True if adult 18 or over or False if not
        pass
        
    def is_male(self):
        # return True if male or False if female
        if self.sex == 'M':
            return True
        if self.sex == 'F':
            return False

for user in user_list:
    print('## User entry', user)
    u = user.split('|')
    person = Person(u[0], u[1], u[2], u[3])

    # Print Person with their fromal name
    print('### FORMAL ###')
    print(person.formal_gretting())

    # Print with normal name
    print('### Normal ###')
    print(person.normal_geeting())

    # Print a casual greeting of just the first name
    print('### Casual ###')
    print(person.casual_greeting())

    # Print Last Name then First Name
    print('### Last, First ###')
    print(person.last_first_greeting())

    # Print name of if an adult
    print('### Adult Check ###')
    if person.is_adult():
        print(person.normal_geeting(), 'Is an Adult aged', person.age)

    # Print first name if the person is male
    print('### Male check ###')
    if person.is_male():
        print(person.casual_greeting(), 'is a male')

