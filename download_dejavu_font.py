import os
import urllib.request

def download_dejavu_font(dest_folder: str = "components"):
    url = "https://github.com/dejavu-fonts/dejavu-fonts/raw/version_2_37/ttf/DejaVuSans.ttf"
    dest_path = os.path.join(dest_folder, "DejaVuSans.ttf")
    os.makedirs(dest_folder, exist_ok=True)
    if not os.path.exists(dest_path):
        print(f"Downloading DejaVuSans.ttf to {dest_path}...")
        urllib.request.urlretrieve(url, dest_path)
        print("Download complete.")
    else:
        print(f"DejaVuSans.ttf already exists at {dest_path}.")

if __name__ == "__main__":
    download_dejavu_font()
