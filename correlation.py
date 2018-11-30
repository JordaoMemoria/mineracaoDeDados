from pandas import read_csv

dataset = read_csv("reading_habits.csv", sep=';')

matrix = dataset.corr()

print(matrix)
print(matrix.values)

