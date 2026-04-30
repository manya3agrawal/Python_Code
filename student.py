import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(0)

students = ['Student_' + str(i) for i in range(1, 21)]

data = {
    'Name': students,
    'Math': np.random.randint(40, 100, 20),
    'Science': np.random.randint(40, 100, 20),
    'English': np.random.randint(40, 100, 20),
    'Computer': np.random.randint(40, 100, 20)
}

df = pd.DataFrame(data)


df['Total'] = df.iloc[:, 1:5].sum(axis=1)
df['Average'] = df.iloc[:, 1:5].mean(axis=1)


print("\n--- Statistical Analysis ---")
print(df.describe())


print("\nMean:\n", df.mean(numeric_only=True))
print("\nMedian:\n", df.median(numeric_only=True))
print("\nStandard Deviation:\n", df.std(numeric_only=True))


topper = df.loc[df['Total'].idxmax()]
low_performer = df.loc[df['Total'].idxmin()]

print("\nTopper:\n", topper)
print("\nLow Performer:\n", low_performer)


subject_means = df.iloc[:, 1:5].mean()
print("\nSubject-wise Average:\n", subject_means)


subject_means.plot(kind='bar', title='Average Marks per Subject')
plt.ylabel('Marks')
plt.show()


df.set_index('Name')[['Math','Science','English','Computer']].plot()
plt.title('Student-wise Performance')
plt.ylabel('Marks')
plt.show()


df['Total'].plot(kind='hist', bins=10)
plt.title('Distribution of Total Marks')
plt.xlabel('Total Marks')
plt.show()

# 4. Pie Chart (Subject Contribution for Topper)
topper_subjects = topper[['Math','Science','English','Computer']]
topper_subjects.plot(kind='pie', autopct='%1.1f%%', title='Topper Subject Contribution')
plt.ylabel('')
plt.show()
