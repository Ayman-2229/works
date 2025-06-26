import pandas as pd
from io import StringIO

def merge_uploaded_files(files) -> pd.DataFrame:
    all_dfs = []

    for file in files:
        stringio = StringIO(file.getvalue().decode("utf-8"))
        df = pd.read_csv(stringio)
        df.columns = [col.lower().strip() for col in df.columns]
        all_dfs.append(df)

    merged = pd.concat(all_dfs, ignore_index=True)
    merged["amount"] = merged["amount"].astype(float)
    return merged
