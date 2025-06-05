import pandas as pd
# import openpyxl

#load the Excel file
student_data = pd.read_excel('student_scores.csv.xlsx')

#start row numbers from 1 instead of 0
student_data.index = range(1, len(student_data) + 1)

#display the student scores
print("Student Scores Data:")
print(student_data)

#calculate average score for each subject (only numeric columns)
average_scores = student_data.mean(numeric_only=True)
print("\nAverage Scores in Each Subject:")
print(average_scores)

#calculate total score for each student
student_data['Total'] = student_data.iloc[:, 1:].sum(axis=1)

#display updated data with Total scores
print("\nStudent Data with Total Scores:")
print(student_data)
