from concurrent.futures import ThreadPoolExecutor
import requests
import os
import json
from tqdm import tqdm


def download(src):
    dest = os.path.join("images/", os.path.basename(src))
    response = requests.get(src)
    with open(dest, mode="wb") as file:
        file.write(response.content)


def download_all():
    base = "https://sam.nyc3.digitaloceanspaces.com/apartment-images/https___static.trulia-cdn.com_pictures_thumbs_6_zillowstatic"

    image_paths = []

    with open("./images.json", "r") as infile:
        data = json.load(infile)
        for d in data.values():
            d = [base + i for i in d]
            image_paths += d

    with ThreadPoolExecutor() as executor:
        res = list(tqdm(executor.map(download, image_paths), total=len(image_paths)))

if __name__ == "__main__":
    download_all()
