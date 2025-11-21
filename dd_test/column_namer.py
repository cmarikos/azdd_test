import pandas as pd
import re

# Read the xlsx file
input_path = "statistics.xlsx"     
sheet_name = "Gender Party & Age"          

raw = pd.read_excel(input_path, sheet_name=sheet_name, header=None)


    # generic logic for Status / Party & Status / district tabs
    HEADER_STATUS_ROW = 1   # e.g. Active / Inactive / Prereg
    HEADER_PARTY_ROW  = 2   # e.g. DEM / REP / UAF / ...
    DATA_START_ROW    = 3

    header_status = raw.iloc[HEADER_STATUS_ROW].copy()
    header_party  = raw.iloc[HEADER_PARTY_ROW].copy()

    header_status_ffill = header_status.ffill()

    combined_headers = []
    for i, (status_val, party_val) in enumerate(zip(header_status_ffill, header_party)):
        status_str = str(status_val).strip() if pd.notna(status_val) else ""
        party_str  = str(party_val).strip() if pd.notna(party_val) else ""

        if i == 0:
            base = status_str or party_str or f"col_{i}"
        else:
            if status_str and party_str:
                base = f"{status_str}_{party_str}"
            elif status_str:
                base = status_str
            elif party_str:
                base = party_str
            else:
                base = f"col_{i}"

        base = base.lower()
        base = re.sub(r"[^a-z0-9_]+", "_", base)
        base = re.sub(r"_+", "_", base).strip("_")

        combined_headers.append(base)

# ensure uniqueness by appending suffixes if duplicate
seen = {}
final_headers = []
for name in combined_headers:
    if name not in seen:
        seen[name] = 1
        final_headers.append(name)
    else:
        seen[name] += 1
        final_headers.append(f"{name}_{seen[name]}")

# drop the header rows, apply new names
clean = raw.iloc[DATA_START_ROW:].copy()
clean.columns = final_headers


# 3. save as a CSV
output_path = "gender_party_age_clean.csv"
clean.to_csv(output_path, index=False)

print("Wrote cleaned file:", output_path)
print("Columns:", clean.columns.tolist())
