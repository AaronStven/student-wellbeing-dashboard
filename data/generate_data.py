import pandas as pd
import numpy as np
import os

# Ensure we save in the current directory
current_dir = os.path.dirname(os.path.abspath(__file__))

np.random.seed(42)
n = 500

data = {
    'Student_ID': [f'S{1000+i}' for i in range(n)],
    'Year': np.random.choice(['Freshman', 'Sophomore', 'Junior', 'Senior'], n),
    'Faculty': np.random.choice(['CS', 'Engineering', 'Arts', 'Business'], n),
    'Sleep_Hours': np.random.normal(6.5, 1.5, n).round(1),
    'Stress_Level': np.random.randint(1, 11, n), # 1-10 scale
    'Study_Hours': np.random.normal(15, 5, n).round(1),
    'GPA': np.random.uniform(2.0, 4.0, n).round(2)
}

df = pd.DataFrame(data)

# Introduce missing values and outliers for cleaning practice
df.loc[10:15, 'Sleep_Hours'] = np.nan
df.loc[20, 'GPA'] = 5.0 
df.loc[25, 'Study_Hours'] = 100 

# Save to csv
file_path = os.path.join(current_dir, 'raw_survey_data.csv')
df.to_csv(file_path, index=False)
print(f"Raw data generated at: {file_path}")