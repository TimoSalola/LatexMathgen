
from mathgen_fraction import *
from abc import ABC, abstractmethod

from decimal import *


#contains exercises and exercise groups

#tuner variables
exercises_per_part = 4
decimal_to_fraction_tuner_variable = 100

#exercise type enumerators
fraction_fraction_enum = 1
decimal_to_fraction_enum = 2
text_question_enum = 3
fraction_fraction_mixed_enum = 4

#score given for text questions
text_question_score = 4


#   Mathgen exercise classes and their containers
#   Every exercise should be of abstract class mathgen_exercise
#   Mathgen exercises should be stored within exercise groups even if
#   group would contain only one exercise.
#
#   mathgen_exercise classes
#   text_question()
#   exercise_operation_between_fractions()
#   exercise_decimal_to_fraction()
#   All of these should be stored within mathgen_exercise_group()
#
#   Groups and exercises should have
#   get_latex() for fletching latex for the math problem
#   get_latex_solution() for fletching latex for the solution
#   get_instructions for flethcing instructions



#abstract class which allows exercise groups and other aid structures to work
class mathgen_exercise(ABC):
    def __str__(self):
        pass
    def get_latex(self):
        pass
    def get_latex_solution(self):
        pass
    def get_instructions(self):
        pass

#store one type of exercises within one exercise group as instructions don't work otherwise
class mathgen_exercise_group():
    def __init__(self, type_enumerator):
        self.exercises = []
        self.type_enumerator = type_enumerator

    #Add either one exercise or a list of them
    def add_exercise(self, given_new_exercise):
        if(isinstance(given_new_exercise, mathgen_exercise)):
            self.exercises.append(given_new_exercise)
        elif(isinstance(given_new_exercise, list)):
            for item in given_new_exercise:
                self.exercises.append(item)

    #returns a list of exercises
    def get_exercises(self):
        return self.exercises

    #returns text instructions for the exercise group
    def get_instructions(self):
        return self.exercises[0].get_instructions()
        #might be a bit of a nasty hack
        #We are assuming that one exercise group contains only one type of exercise
        #sking the first exercise what it's instructions are should work



    def __len__(self):
        return len(self.exercises)

    #Returns exercise count, used for scoring
    def get_score_from_group(self):
        #text questions are special and worth more points
        if(self.type_enumerator == text_question_enum):
            return text_question_score

        #othrwise 1 point for each exercise
        return len(self.exercises)

    #Returns generated latex for the exercise group.
    def get_latex(self):


        if(self.type_enumerator == fraction_fraction_enum or self.type_enumerator == decimal_to_fraction_enum or self.type_enumerator == fraction_fraction_mixed_enum):
            output = r'''
        \renewcommand*{\arraystretch}{1.6}
        %this handles vertical margins for the table

        \begin{tabularx}{0.9\textwidth}{X X X X}
        %tabularx allows us to choose table width via  {x.x\textwidth}
        %important as answer space is needed.

        %{X X X X}  marks column count. 4 or 3 seem to work best for fractions
        %With 4 table columns, we need to format our latex to resemble "1 & 2 & 3 & 4 \\ 5 & 6 & 7...."
        %Instead of a single row, separate rows for every fraction exercise are used to make things a bit neater.

        %\large

            '''

            #loops every list item and fletches their latex
            atIndex = 0
            for index in range(0, len(self.exercises)):
                item = self.exercises[index]
                output += "$"+ item.get_latex() + '''$'''

                if(((index+1) % 4)  == 0):
                    output += r'''  \\

            '''
                else:
                    output += r'''  &
            '''


            #adds the end part of our exercise
            output += r'''
        \end{tabularx}
        \begin{flushright}
            /''' + str(self.get_score_from_group()) + r'''
            %^Total score for this exercise goes here
        \end{flushright}
            '''

            #returns our whole latex thing


            return output

        elif(self.type_enumerator == text_question_enum):


            output = str(self.exercises[0].get_latex())
            output += r'''
        \begin{flushright}
            /''' + str(self.get_score_from_group()) + r'''
            %^Total score for this exercise goes here
        \end{flushright}
            '''

            return output

    #Returns generated latex for the exercise group. Including the answer
    def get_latex_solution(self):

        if(self.type_enumerator == fraction_fraction_enum or self.type_enumerator == decimal_to_fraction_enum):
            output = r'''
        \renewcommand*{\arraystretch}{1.6}
        %this handles vertical margins for the table

        \begin{tabularx}{0.9\textwidth}{X X X X}
        %tabularx allows us to choose table width via  {x.x\textwidth}
        %important as answer space is needed.

        %{X X X X}  marks column count. 4 or 3 seem to work best for fractions
        %With 4 table columns, we need to format our latex to resemble "1 & 2 & 3 & 4 \\ 5 & 6 & 7...."
        %Instead of a single row, separate rows for every fraction exercise are used to make things a bit neater.

        %\large

            '''

            #loops every list item and fletches their latex
            atIndex = 0
            for index in range(0, len(self.exercises)):
                item = self.exercises[index]
                output += "$"+ item.get_latex_solution() + '''$'''

                if(((index+1) % 4)  == 0):
                    output += r'''  \\

            '''
                else:
                    output += r'''  &
            '''


            #adds the end part of our exercise
            output += r'''
        \end{tabularx}
        \begin{flushright}
            /''' + str(self.get_score_from_group()) + r'''
            %^Total score for this exercise goes here
        \end{flushright}
            '''

            #returns our whole latex thing


            return output
        elif(self.type_enumerator == text_question_enum):
            text_ex = self.exercises[0]
            print(text_ex)

            return self.exercises[0].get_latex_solution()

#generator functions for random exercises of the supported exercise types

#classes for containing supported exercise types
class exercise_operation_between_fractions(mathgen_exercise):
    def __init__(self, fraction1, fraction2, operation):
        self.fraction1 = fraction1
        self.fraction2 = fraction2
        self.operation = operation
        self.solution = self.solve()

    def solve(self):
        if(self.operation =="*"):
            return self.fraction1*self.fraction2
        if(self.operation == "+"):
            return self.fraction1 + self.fraction2
        if(self.operation =="-"):
            return self.fraction1 - self.fraction2
        if(self.operation == ":"):
            return self.fraction1 / self.fraction2


    def __str__(self):
        return str(self.fraction1) + self.operation + str(self.fraction2) + "=" + str(self.solution)

    def get_latex(self):
        return self.fraction1.get_latex_mixed_fraction() + self.operation + self.fraction2.get_latex_mixed_fraction() + "="

    def get_latex_solution(self):
        return self.get_latex() + str(self.solution.get_latex())

    def get_instructions(self):
        return r'''Suorita murtolukujen laskutoimitus ja ilmoita tulos supistetussa muodossa.
        '''

class exercise_decimal_to_fraction(mathgen_exercise):

    def __init__(self, decimal):
        self.decimal = decimal
        self.solution = self.solve()

    def __str__(self):
        return str(self.decimal) + "=" + str(self.solution)

    def solve(self):
        return fraction_from_decimal(self.decimal)

    def get_latex(self):
        return  str(self.decimal) + "="

    def get_latex_solution(self):
        return self.get_latex()  + self.solution.get_latex()

    def get_instructions(self):
        return "Muuta desimaaliluku supistetuksi murtoluvuksi."

class text_question(mathgen_exercise):
    def __init__(self):
        self.latex = ""
        self.solution =""
        self.fractions_used = []
        self.type_enumerator = 1

    def __str__(self):
        return self.latex

    def get_latex_solution(self):
        return self.solution

    def get_instructions(self):
        return "Sanallinen tehtävä"

    def set_type(self, type):
        #print("got type" + str(type))
        self.type_enumerator = type

    def give_fraction(self, fraction):
        self.fractions_used.append(fraction)


    def get_latex(self):
        output = ""
        if(self.type_enumerator == 1):




            output += r'''
Säilytystilasta '''
            output +=  str(self.fractions_used[0]) +" on täytetty ruokatarvikkeilla. " + str(self.fractions_used[1]) +" työkaluilla. Ja "
            output += str(self.fractions_used[2])+" vaatteilla. Kuinka suuri osuus tilasta on yhä käyttämättä?"
            output += " Ilmoita vastaus murtolukuna."

        elif(self.type_enumerator == 2):

            '''
            Kokeeseen osallistui{random int} opiskelijaa. Näistä opiskelijoista kokeen läpäisi {random fraction}.
            Kokeen läpäisseistä arvosanan {random grade} sai {random fraction}.
            Kuinka moni sai arvosanan {random fraction} ?
            '''

            possible_grade = random.randint(1,5)

            output += r'''

Kokeeseen osallistui '''  + str(int(self.fractions_used[0].absolute_value())) + " opiskelijaa."
            output += r''' Näistä opiskelijoista kokeen läpäisi $''' + self.fractions_used[1].get_latex() + "$."
            output += r''' Kokeen läpäisseistä arvosanan ''' + str(possible_grade) + " sai $" + self.fractions_used[2].get_latex() + "$."
            output += "Kuinka moni sai arvosanan " + str(possible_grade) + "?"

        return output


    def get_latex_solution(self):
        #print("called solution")
        output = r""
        if(self.type_enumerator == 1):
            #type 1, calculation is of type 1/1 - a/b - b/c -d/e=
            output += r'''

    Säilytystilan vapaa tila = ''' + str(fraction(1,1))
            sum_of_used_fractions = fraction(0, 1) # 0/1 works as a zero fraction

            #calculating the sum of fractions used
            for f in self.fractions_used:
                output += " - " + str(f)
                sum_of_used_fractions += f
            solution = fraction(1,1) - sum_of_used_fractions

            output += " = " + str(solution)

            #print(output)


        if (self.type_enumerator == 2):
            #got through
            students_who_passed = int(self.fractions_used[0].absolute_value() * self.fractions_used[1].absolute_value())
            output += r'''

Kokeen läpäisi $''' + self.fractions_used[0].get_latex() + "*" + self.fractions_used[1].get_latex() + "$=" +str(students_who_passed) + " opiskelijaa. "

            #got grade
            students_who_got_grade_x = int(students_who_passed * self.fractions_used[2].absolute_value())
            output += r'''

Kokeen läpäissestä ''' + str(students_who_passed)+ ''' kysytyn arvosanan sai $'''  + str(students_who_passed) + " * "+  self.fractions_used[2].get_latex() + " = "   + str(students_who_got_grade_x) + "$"




        return output

#generators for exercises
def generate_random_operation_between_fractions():
    typeEnum = random.randint(1,4)
    #will generate a  number from 1 to 4
    #4 operation types currently Supported
    fraction1 = generate_fraction()
    fraction2 = generate_fraction()

    operation = ""
    if(typeEnum == 1):
        operation = "*"
    elif(typeEnum ==2):
        operation = "+"
    elif(typeEnum == 3):
        operation = "-"
    elif(typeEnum == 4):
        operation = ":"
    #print("Generated:" + str(fraction1) + operation + str(fraction2))
    return exercise_operation_between_fractions(fraction1, fraction2, operation)

def generate_random_operation_between_mixed_fractions():
    #generates more complicated fraction exercises
    #eq 2 4/7 + 1/3

    typeEnum = random.randint(1,4)
    #will generate a  number from 1 to 4
    #4 operation types currently Supported
    fraction1 = generate_fraction() +random.randint(0,2)
    fraction2 = generate_fraction() +random.randint(0,2)

    if(fraction1.absolute_value() < 1 and fraction2.absolute_value() < 1):
        #both fractions were still less than 1
        fraction1 += 1 # this should fix it

    operation = ""
    if(typeEnum == 1):
        operation = "*"
    elif(typeEnum ==2):
        operation = "+"
    elif(typeEnum == 3):
        operation = "-"
    elif(typeEnum == 4):
        operation = ":"
    #print("Generated:" + str(fraction1) + operation + str(fraction2))
    return exercise_operation_between_fractions(fraction1, fraction2, operation)

    return

def generate_random_decimal_to_fraction():
    random_decimal = random.randint(1,decimal_to_fraction_tuner_variable) / 100
    return exercise_decimal_to_fraction(random_decimal)

def generate_text_question():
    #Generates a random text question




    text_question_type = random.randint(1,2)
    #generating

    tq = text_question()
    tq.set_type(text_question_type)

    if(text_question_type == 1):
        #generating storage space question

        #Fraction restrictions
        max_denominator = 8
        min_denominator = 3 #keep this at 3 or higher

        #generating random fractions
        fraction1 = generate_fraction()
        fraction2 = generate_fraction()
        fraction3 = generate_fraction()

        #making sure that fractions follow restrictions and they are unique
        while(True):
            denominator = fraction1.denominator
            numerator = fraction1.numerator

            if(numerator == 1 and denominator != 1):
                if(denominator <= max_denominator and denominator >= min_denominator):
                    break

            fraction1 = generate_fraction()
        while(True):
            denominator = fraction2.denominator
            numerator = fraction2.numerator

            if(numerator == 1 and denominator != 1):
                if(denominator <= max_denominator and denominator >= min_denominator):
                    if(fraction1 != fraction2):
                        break

            fraction2 = generate_fraction()
        while(True):
            denominator = fraction3.denominator
            numerator = fraction3.numerator

            if(numerator == 1 and denominator != 1):
                if(denominator <= max_denominator and denominator >= min_denominator):
                    if(fraction1 != fraction3 and fraction2 != fraction3):
                        break

            fraction3 = generate_fraction()

        #giving fractions to the question
        tq.give_fraction(fraction1)
        tq.give_fraction(fraction2)
        tq.give_fraction(fraction3)


    elif(text_question_type == 2):
        #generating exam grades question
        '''
        1. Kokeeseen osallistui {amount of students here} opiskelijaa.
        2. Kokeen läpäisyyn vaaditaan 1/2 pisteistä ja opiskelijoista {random fraction here} saa läpäisee kokeen.
        Kokeen läpäisseistä {random fraction here} saa arvosanan {insert possible grade here}.
        Kuinka moni sai arvosanan {insert possible grade}?
        '''

        #1. how many students in total?
        student_count = 24
        student_count_fraction = fraction(student_count,1)
        tq.give_fraction(student_count_fraction)
        #24 divides well and it's a nice number

        #2. how many passed the exam?
        # 12 +- 2 or 12 +- 3 would generate an interesting fraction
        students_who_passed = 12

        interesting_enum = random.randint(1,4)
        if(interesting_enum ==1):
            students_who_passed = 12 +2
        if(interesting_enum == 2):
            students_who_passed = 12- 2
        if(interesting_enum ==3):
            students_who_passed = 12 +3
        if(interesting_enum == 4):
            students_who_passed = 12- 3

        students_who_passed_fraction = fraction(students_who_passed, student_count)

        tq.give_fraction(students_who_passed_fraction)

        #3. how many got grade x?
        #12 factorizes well, but 10 and 14 don't
        #neither do 9 or 15

        #let's use 2 or 3 depending on if we got 10,14 or 9,15
        students_who_got_grade_x = 0

        if(students_who_passed % 2 == 0):
            #divides by 2, is 10 or 14
            students_who_got_grade_x = 2
        if(students_who_passed % 3== 0):
            students_who_got_grade_x = 3

        students_who_got_grade_x_fraction = fraction(students_who_got_grade_x, students_who_passed)

        tq.give_fraction(students_who_got_grade_x_fraction)



    return tq




#generators for exercise groups
def generate_random_operation_group_between_fractions():
    #this function should be tuned further

    output_group = mathgen_exercise_group(fraction_fraction_enum)

    for item in range(0, exercises_per_part):
        output_group.add_exercise(generate_random_operation_between_fractions())

    return output_group

def generate_random_operation_group_between_mixed_fractions():
    #this function should be tuned further

    output_group = mathgen_exercise_group(fraction_fraction_enum)

    for item in range(0, exercises_per_part):
        output_group.add_exercise(generate_random_operation_between_mixed_fractions())

    return output_group

def generate_random_decimal_to_fraction_group():

    output_group = mathgen_exercise_group(decimal_to_fraction_enum)

    for item in range(0, exercises_per_part):
        output_group.add_exercise(generate_random_decimal_to_fraction())

    return output_group

def generate_text_question_group():
    output_group = mathgen_exercise_group(text_question_enum)

    output_group.add_exercise(generate_text_question())
    return output_group







#class exercise_fractions_to_same_denominator(mathgen_exercise):
