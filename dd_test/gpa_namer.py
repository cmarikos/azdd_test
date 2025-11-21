import pandas as pd
import re

input_path = "statistics.xlsx"
sheet_name = "Gender Party & Age"

raw = pd.read_excel(input_path, sheet_name=sheet_name, header=None, dtype=str)

if sheet_name == "Gender Party & Age":
    # rows 0 = title, 1 = party/total row, 2 = blank, 3 = age bands, 4+ = data
    PARTY_ROW = 1
    AGE_ROW = 3
    DATA_START_ROW = 4

    party_row = raw.iloc[PARTY_ROW]          # don't fillna yet
    age_row   = raw.iloc[AGE_ROW].fillna("")

    # treat "AGE" as missing so ffill propagates ACN/APV/DEM/... across the block
    party_clean = party_row.replace("AGE", pd.NA)
    party_ffill = party_clean.ffill().fillna("")

    combined_headers = []
    for i, (party_val, age_val) in enumerate(zip(party_ffill, age_row)):
        party_str = (str(party_val) if pd.notna(party_val) else "").strip().lower()
        age_str   = (str(age_val)   if pd.notna(age_val)   else "").strip().lower()

        # normalize age band "<18" to "lt18", "18-24" to "18_24", "75+" to "75"
        if age_str:
            age_str = age_str.replace("<", "lt")
            age_str = re.sub(r"[^a-z0-9]+", "_", age_str).strip("_")

        # normalize party "ACN Total" to "acn_total", "Dem" to "dem", etc.
        if party_str:
            party_str = re.sub(r"[^a-z0-9]+", "_", party_str).strip("_")

        if i == 0:
            base = "county"
        elif i == 1:
            base = "gender"
        else:
            if party_str and age_str:
                base = f"{party_str}_{age_str}"
            elif party_str:
                base = party_str
            elif age_str:
                base = age_str
            else:
                base = f"col_{i}"

        combined_headers.append(base)

    # ensure uniqueness
    seen = {}
    final_headers = []
    for name in combined_headers:
        if name not in seen:
            seen[name] = 1
            final_headers.append(name)
        else:
            seen[name] += 1
            final_headers.append(f"{name}_{seen[name]}")

    clean = raw.iloc[DATA_START_ROW:].copy()
    clean.columns = final_headers


# ffill the county name so FEMALE/MALE/UNK rows get the right county
    clean["county"] = clean["county"].ffill()

# make a version without the " Total" suffix for later use
    clean["county"] = clean["county"].str.replace(r"\s+total$", "", case=False, regex=True)

# drop the county total / subtotal rows
    clean = clean[clean["gender"].notna()]

    output_path = "gender_party_age_clean.csv"
    clean.to_csv(output_path, index=False)

    print("columns:", clean.columns.tolist())
    print("rows:", clean.shape[0], "Cols:", clean.shape[1])
    print("select column values:")
    print(clean.iloc[:, 1].tolist())