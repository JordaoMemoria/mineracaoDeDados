import seaborn as sns
from pandas import read_csv
import matplotlib.pyplot as plt

sns.set(style="ticks", color_codes=True)
df = read_csv("reading_habits.csv",sep=";")
sns.catplot(x="Do you happen to read any magazines or journals?", y="How many books did you read during last 12 months?", data=df, legend=True)
plt.show()