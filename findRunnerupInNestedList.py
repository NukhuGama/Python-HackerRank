if __name__ == '__main__':
    student = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        
        # Create  Student List and adding names and their scores
        student.append([name,score])
    
    # Make a list of score for all students
    all_score = []
    
    for i in range(len(student)):
        all_score.append(student[i][1])
        # print(student[i][1])
    
    all_score.sort()
    min_num = min(all_score)
    # Create New Student list
    new_student = []
    for i in range(len(student)):
        if (student[i][1]!=min_num):
            new_student.append([student[i][0], student[i][1]])   
    
    # print(new_student)
    # Runnerup Student
    minVal_student = min(new_student, key=lambda x: x[1])
    min_score = minVal_student[1]
    # print(min_score)
    # Sorting Students List
    new_student.sort()
    for i in range(len(new_student)):
        if (min_score==new_student[i][1]):
            # Print the name of runnerup students
            print(new_student[i][0])







# Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

# Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

# Example

# The ordered list of scores is , so the second lowest score is . There are two students with that score: . Ordered alphabetically, the names are printed as:

# alpha
# beta
# Input Format

# The first line contains an integer, , the number of students.
# The  subsequent lines describe each student over  lines.
# - The first line contains a student's name.
# - The second line contains their grade.

# Constraints

# There will always be one or more students having the second lowest grade.
# Output Format

# Print the name(s) of any student(s) having the second lowest grade in. If there are multiple students, order their names alphabetically and print each one on a new line.

# Sample Input 0

# 5
# Harry
# 37.21
# Berry
# 37.21
# Tina
# 37.2
# Akriti
# 41
# Harsh
# 39
# Sample Output 0

# Berry
# Harry
# Explanation 0

# There are  students in this class whose names and grades are assembled to build the following list:

# python students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]

# The lowest grade of  belongs to Tina. The second lowest grade of  belongs to both Harry and Berry, so we order their names alphabetically and print each name on a new line.