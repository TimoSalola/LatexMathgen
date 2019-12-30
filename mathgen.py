import random
import math
import re
import os

from decimal import *
from abc import ABC, abstractmethod

from mathgen_fraction import *
from mathgen_exercises import *
from mathgen_exam import *

__author__ = "Timo Salola https://github.com/TimoSalola"
__copyright__ = "Copyright (C) 2020 Timo Salola"
__license__ = "Public Domain"
__version__ = "1.0"


#Latex exam generator, this function contains an example use case
def main():

  #random.seed("kissa")
  #if random seed is used, the exam will be the same, could be useful
  example_exam = mathgen_exam()

  #generating question sets
  first_set_of_questions = generate_random_operation_group_between_fractions()
  second_set_of_questions = generate_random_operation_group_between_mixed_fractions()
  third_set_of_questions = generate_random_decimal_to_fraction_group()
  fourth_set_of_questions = generate_text_question_group()

  #adding them to our exam
  example_exam.add_exercise_group(first_set_of_questions)
  example_exam.add_exercise_group(second_set_of_questions)
  example_exam.add_exercise_group(third_set_of_questions)
  example_exam.add_exercise_group(fourth_set_of_questions)

  #providing output, contains solutions
  exam_in_latex = example_exam.get_latex()
  print(exam_in_latex)




if __name__ == "__main__":
    main()
