import pandas as pd

input_path = "statistics.xlsx"     
sheet_name = "UAF Voter Preference Counts"             

# works for status, uocava, and precinct counts, for uaf change header=3
df = pd.read_excel(input_path, sheet_name=sheet_name, header=3)

# save as CSV
output_path = "uaf_voter_pref_counts_clean.csv"
df.to_csv(output_path, index=False)

print("Wrote:", output_path)
print("Columns:", df.columns.tolist())
