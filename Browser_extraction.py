import os
import io
import zipfile
import requests
import shutil
from tqdm import tqdm
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("DadosGovBR").getOrCreate()

download_url = "https://anatel.gov.br/dadosabertos/paineis_de_dados/acessos/acessos_banda_larga_fixa.zip"

current_dir = os.getcwd()
extract_dir = os.path.join(current_dir, "broadband_access_data_temp")
os.makedirs(extract_dir, exist_ok=True)

response = requests.get(download_url, stream=True)
response.raise_for_status()
print("HTTP Response Status:", response.status_code)

total_size = int(response.headers.get("content-length", 0))
chunk_size = 1024

print("Download in progress...")
zip_bytes = io.BytesIO()
with tqdm(total=total_size, unit="B", unit_scale=True, desc="Download") as pbar:
    for chunk in response.iter_content(chunk_size=chunk_size):
        if chunk:
            zip_bytes.write(chunk)
            pbar.update(len(chunk))

zip_bytes.seek(0)

with zipfile.ZipFile(zip_bytes, "r") as z:
    z.extractall(extract_dir)

extracted_files = os.listdir(extract_dir)
print("Extracted files:", extracted_files)
print(f"Number of extracted files: {len(extracted_files)}")

repo_data_dir = os.path.join(current_dir, "dados")
os.makedirs(repo_data_dir, exist_ok=True)

for file_name in os.listdir(extract_dir):
    src_file = os.path.join(extract_dir, file_name)
    dst_file = os.path.join(repo_data_dir, file_name)
    if os.path.isfile(src_file):
        shutil.copy2(src_file, dst_file)

print(f"Files successfully updated in GitHub repository at: {repo_data_dir}")
