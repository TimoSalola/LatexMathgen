# LatexMathgen
Python script for generating math exams with fractions in latex. Built with vocational schools in mind.

Consists of 4 files.
## mathgen.py
Master file. Run this with python 3 and it will print the latex code for your exam.

## mathgen_fraction.py
Fraction class and relevant methods for fractions.

## mathgen_exam.py
Container for mathgen exams.

## mathgen_exercises.py
Contains generators for mathgen exercises and exercise groups.


## Possible improvements
Tune exercises further. Exercises can be too difficult without a calculator. Currently exercises are generated with a random number generator and purely random questions may lack educational value.

Only 2 types of text questions are currently supported. Add more.

mathgen.py should ask for parameters for the exam. Add terminal configurator. Would allow script to be more useful to those without python skills.

