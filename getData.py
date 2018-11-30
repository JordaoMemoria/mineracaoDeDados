from pandas import read_csv


df = read_csv("reading_habits.csv", sep=';')
print(df.columns)
print(df["Do you happen to read any magazines or journals?"].unique())

for value in df["Employement"].unique():
    feature = "Employement"


    print(value)
    newDf = df.loc[(df[feature] == value) & (df['How many books did you read during last 12 months?'] > 0) & (df['How many books did you read during last 12 months?'] <= 20)]
    a1 = len(newDf.values)

    newDf = df.loc[(df[feature] == value) & (df['How many books did you read during last 12 months?'] > 20) & (df['How many books did you read during last 12 months?'] <= 40)]
    a2 = len(newDf.values)

    newDf = df.loc[(df[feature] == value) & (df['How many books did you read during last 12 months?'] > 40) & (df['How many books did you read during last 12 months?'] <= 60)]
    a3 = len(newDf.values)

    newDf = df.loc[(df[feature] == value) & (df['How many books did you read during last 12 months?'] > 60) & (df['How many books did you read during last 12 months?'] <= 80)]
    a4 = len(newDf.values)

    newDf = df.loc[(df[feature] == value) & (df['How many books did you read during last 12 months?'] > 80) & (df['How many books did you read during last 12 months?'] <= 100)]
    a5 = len(newDf.values)

    sum = a1+a2+a3+a4+a5

    print(a1,a1/sum*100)
    print(a2, a2 / sum * 100)
    print(a3, a3 / sum * 100)
    print(a4, a4 / sum * 100)
    print(a5, a5 / sum * 100)








