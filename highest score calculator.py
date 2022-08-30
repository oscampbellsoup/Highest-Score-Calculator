# Ask for list of student scores as separate string values.
student_scores = input("Input a list of student scores ").split()
# Determine a range of the values stored in student_scores variable.
for n in range(0, len(student_scores)):
# Change list values from str to int.
  student_scores[n] = int(student_scores[n])
# Print a list of the scores inputted by the user to confirm their trust in the outcome.
print(student_scores)
# Max_score variable is created. Set at 0 until scores among the list are compared in value.
max_score = 0
# Determine a range of the values stored in student_scores variable.
for n in range(0, len(student_scores)):
# Pick the first of two numbers to compare.
    number_one = int(student_scores[n])
# Determine a range of the values stored in student_scores variable.
    for n in range(0, len(student_scores)):
# Avoid index out of range error when comparing value of scores.
        if n == len(student_scores) - 1:
# Create an output listing the highest score in the class.
            print(f"The highest score in the class is: {max_score}")
            exit()
# If there are scores to be compared:
        else:
            number_two = int(student_scores[n+1])
# Score comparison
            if number_one > number_two:
# Comparing greater score with the current max score.
                if number_one > max_score:
# If max score is less than number_one, number_one becomes new max score.
                    max_score = 0
                    max_score += number_one
            else:
# Comparing greater score with the current max score.                
                if number_two > max_score:
# If max score is less than number_two, number_two becomes new max score.
                    max_score = 0
                    max_score += number_two