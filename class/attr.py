# class Person:
#     no_of_people = 0

#     def __init__(self, name):
#         self.name = name
#         Person.add_person()

#     @classmethod    
#     def number_of_people(cls):
#         return cls.no_of_people

#     @classmethod
#     def add_person(cls):
#         cls.no_of_people += 1     

# p1 = Person("tim")
# p2 = Person("Jill")
# print(Person.number_of_people())


class Math:
    
    @staticmethod
    def add5(x):
        return x + 5
    @staticmethod
    def add10(x):
        return x + 10
    @staticmethod
    def pr():
        print("run")

        

Math.pr()     
print(Math.add10(5))        