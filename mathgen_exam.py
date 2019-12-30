mathgen_exam_name = "Murtolukukoe"

#   Container class for mathgen exercise groups
#   Relevant functions
#   mathen_exam() __init__
#   add_exercise_group
#   get_latex()
#
#   Other functions are for internal usage
class mathgen_exam:
    def __init__(self):
        self.ex_groups = []

    def get_latex_end_of_exam(self):
        output = r'''
\end{document}'''
        return output

    #returns the latex code for the whole exam
    def get_latex(self):
        #add header
        output = self.generate_latex_exam_head(self.get_max_score())

        #then exercises
        for index in range(0, len(self.ex_groups)):
            groupAtIndex = self.ex_groups[index]
            #print("at index" + str(index))
            output += r'''
'''+str(index +1) +". "+ groupAtIndex.get_instructions()
            output += groupAtIndex.get_latex()


        #then page swap and solutions
        output += self.get_latex_solutions_page()

        #then end of document
        output += self.get_latex_end_of_exam()


        return output

    #use this to add exercise groups to the exam
    def add_exercise_group(self, new_group):
        self.ex_groups.append(new_group)

    #returns the first rows of a latex exam document.
    def generate_latex_exam_head(self, maxScore):
        #Formatted like this for the ease of editing.
        #contains the first n rows of a latex document
        #from document declaration to the last row before actual exercises
        outputLatex = r'''
\documentclass[12pt,a4paper]{article}
\usepackage[utf8]{inputenc}
\usepackage[a-1b]{pdfx}
\usepackage{hyperref}
\usepackage[finnish]{babel}
\usepackage{parskip}
\pagenumbering{gobble}
\usepackage{tabularx}

%Documentation
%   Tables are used to contain exercises
%   Second page has answers for the questions. If a question is modified, modify the answer as well
%   Update the date few lines below

%doc size
\usepackage{geometry}
    \geometry{
        a4paper,
        total={170mm,257mm},
        left=20mm,
        top=20mm,
    }

%header part
\begin{document}

\hline
    \vspace{0.2cm}
    \noindent
    \textsc{''' + mathgen_exam_name + r'''}
    \hfill
    21.12.2020
    %##################        UPDATE DATE HERE MANUALLY
    \vspace{0.2cm}
\hline

    \noindent
    \vspace{0.5cm}
    Nimi:
    \rule{60mm}{.1pt}
    \hfill
    [\hspace{0.5cm} / ''' + str(maxScore) +   r''']

%Exam begins
'''



        return outputLatex

    #returns max score for the exam
    def get_max_score(self):
        sum = 0
        for group in self.ex_groups:
            #could use len here
            sum += group.get_score_from_group()
        return sum

    #returns solutions page for the exam
    def get_latex_solutions_page(self):
        output = r'''
\newpage

\textsc{Vastaukset}

'''
        for index in range(0, len(self.ex_groups)):
            groupAtIndex = self.ex_groups[index]
            #print("at index" + str(index))
            output += r'''
'''+str(index +1) +". "+ groupAtIndex.get_instructions()
            output += groupAtIndex.get_latex_solution()

        return output
