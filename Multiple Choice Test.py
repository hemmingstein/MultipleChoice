
# coding: utf-8

# # Multiple Choice Test

import random

# Definition of questions

# Question 1
q1 = "Sample question 1"
# Answers (the first answer is the right answer)
s11 = "Answer 1"
s12 = "Answer 2"
# Concatenate answers
s1 = [s11,s12]
# Random answer order
s1r = random.sample(s1, len(s1))
# Create task containing the question, the answers, and the right answer
t1 = [q1,s1r,s11]

# Question 2
q2 = "Sample question 2"
s21 = "Answer 1"
s22 = "Answer 2"
s23 = "Answer 3"
s2 = [s21,s22,s23]
s2r = random.sample(s2, len(s2))
t2 = [q2,s2r,s21]

# Question 3
q3 = "Sample question 3"
s31 = "Answer 1"
s32 = "Answer 2"
s3 = [s31,s32]
s3r = random.sample(s3, len(s3))
t3 = [q3,s3r,s31]

# Add further questions

# Create the full set of questions
tasksFullSet = [t1,t2,t3]

# questionsset = [[q1,[s11,s12],s11],t2,t3]

# Pick a random sample of n questions
n = 2
tasksSampleSet = random.sample(tasksFullSet,n)

print("Multiple Choice Test")
print(" ")

# Create student version
print("Student version")
for i in range(0, n):
    # print question
    print(i+1,".", tasksSampleSet[i][0])
    # print answers
    for j in range(0, len(tasksSampleSet[i][1])):
        print(" O",tasksSampleSet[i][1][j])
    
print("End student version")
print(" ")

# Create solved version
print("Solution")
for i in range(0, n):
    print(i+1,".", tasksSampleSet[i][0])
    print(tasksSampleSet[i][2])
    
print("End solution")

