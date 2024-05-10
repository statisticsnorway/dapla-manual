import dapla as dp
import pandas as pd
from dapla.files import FileClient

from benchmark_code.timer import timing

bucket = "gs://ssb-prod-dapla-felles-data-delt"
folder = "tech-coach/parquet-test/concat/dataset-1000"
fs = FileClient().get_gcs_file_system()
files: list[str] = fs.glob(f"{bucket}/{folder}/*.parquet") # liste av 1000 filer

@timing
def concat_files_slow() -> pd.DataFrame:
    dfs = []
    for file in files:
        df = dp.read_pandas(gcs_path=file, file_format="parquet")
        dfs.append(df)
    df_all = pd.concat(dfs)
    return df_all

@timing
def concat_files_fast() -> pd.DataFrame:
    return dp.read_pandas(gcs_path=files, file_format="parquet")

print(concat_files_fast())