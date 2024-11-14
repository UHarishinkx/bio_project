import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# Sample data mutation frequencies in different samples
data = {
    'Sample': ['Sample1', 'Sample2', 'Sample3', 'Sample4', 'Sample5'],
    'Mutation_A': [10, 15, 7, 20, 5],
    'Mutation_B': [5, 8, 12, 3, 6],
    'Mutation_C': [20, 5, 15, 10, 18]
}
df = pd.DataFrame(data)
df.set_index('Sample', inplace=True)
plt.figure(figsize=(10, 6))
df.plot(kind='bar', stacked=True)
plt.title('Team 702I Presents:\nMutation Frequencies in Different Samples')
plt.xlabel('Samples')
plt.ylabel('Frequency')
plt.xticks(rotation=45)
plt.legend(title='Mutations')
plt.tight_layout()
plt.show()
