# You have access to a database of student_scores in the format of a dictionary. The keys in student_scores are the names of the students and the values are their exam scores.
#write a program that converts their scores to grads. by the end of the program, you should have a new dictionaru called student_grades tha should contain student names for keys
#and their grades for values. the final version of the student_grades dictionary will be checked. 

#do no modify the existing student_scores dictionary
#do not write any print statements. 
#scores 91-100 grade= 'outstanding'
#scores 81-90 grade='exceeds expctations
#scores 71-80 grade ='acceptable'

student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇
for names in student_scores:
    if (student_scores[names] >= 91 and student_scores[names] >= 100 ):
        student_grades[names] =  "Outstanding"
    elif (student_scores[names] >= 81 and student_scores[names] <= 90):
        student_grades[names] = "Exceeds Expctations"
    elif (student_scores[names] >= 71 and student_scores[names] <= 80):
        student_grades[names] = "Acceptable"
    elif (student_scores[names] <= 70):
        student_grades[names] = "Fail"
    

# 🚨 Don't change the code below 👇
print(student_grades)