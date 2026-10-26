import pandas as pd
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
raw_path = os.path.join(current_dir, 'raw_survey_data.csv')
clean_path = os.path.join(current_dir, 'cleaned_survey_data.csv')

# Load
df = pd.read_csv(raw_path)

# Clean
df.loc[df['GPA'] > 4.0, 'GPA'] = pd.NA
df.loc[df['Study_Hours'] > 80, 'Study_Hours'] = pd.NA
df_clean = df.dropna()

# Save
df_clean.to_csv(clean_path, index=False)
print(f"Cleaned data saved to: {clean_path}")
print(f"Rows before: {len(df)} | Rows after: {len(df_clean)}")