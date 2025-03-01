student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65]
totalExamScore = sum(student_scores)

sum = 0

for score in student_scores:
    sum += score

print(sum)

print(max(student_scores)) # function that finds the max
max = 0

for score in student_scores:
    if(score > max):
        max = score
print(max)