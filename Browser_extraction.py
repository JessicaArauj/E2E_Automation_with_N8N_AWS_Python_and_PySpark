import os
import io
import zipfile
import requests
import shutil
from tqdm import tqdm

current_dir = os.environ.get("GITHUB_WORKSPACE", os.getcwd())
extract_dir = os.path.join(current_dir, "broadband_access_data_temp")
repo_data_dir = os.path.join(current_dir, "data")

os.makedirs(extract_dir, exist_ok=True)
os.makedirs(repo_data_dir, exist_ok=True)

download_url = "https://anatel.gov.br/dadosabertos/paineis_de_dados/acessos/acessos_banda_larga_fixa.zip"
print(f"Downloading dataset from {download_url} ...")

try:
    response = requests.get(download_url, stream=True)
    response.raise_for_status()
except Exception as e:
    print("Error downloading file:", e)
    exit(1)

total_size = int(response.headers.get("content-length", 0))
chunk_size = 1024
zip_bytes = io.BytesIO()

with tqdm(total=total_size, unit="B", unit_scale=True, desc="Download") as pbar:
    for chunk in response.iter_content(chunk_size=chunk_size):
        if chunk:
            zip_bytes.write(chunk)
            pbar.update(len(chunk))

zip_bytes.seek(0)

with zipfile.ZipFile(zip_bytes, "r") as z:
    z.extractall(extract_dir)

extracted_files = [f for f in os.listdir(extract_dir) if f.endswith(".csv")]
if not extracted_files:
    print("No CSV files found in ZIP.")
else:
    print(f"{len(extracted_files)} CSV files extracted.")

for file_name in extracted_files:
    src_file = os.path.join(extract_dir, file_name)
    dst_file = os.path.join(repo_data_dir, file_name)
    shutil.copy2(src_file, dst_file)
    print(f"Copied {file_name} to {repo_data_dir}")

shutil.rmtree(extract_dir)
print(f"All CSV files saved in repository folder: {repo_data_dir}")
