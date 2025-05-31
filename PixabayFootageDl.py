import requests
import os
import re

# Constants
API_KEY = '43529795-d21fe74cdc76676c2f16c2424'
BASE_URL = 'https://pixabay.com/api/videos/'
SAVE_PATH = 'D:/TEST 2/Data/Pixel/Footage'

# Ensure the save path exists
os.makedirs(SAVE_PATH, exist_ok=True)

# List of video URLs
video_urls = [
    'https://pixabay.com/videos/sunset-nature-sky-dubai-111204/',
    'https://pixabay.com/videos/cliff-precipice-sea-coastal-nature-22619/',
    'https://pixabay.com/videos/sea-ocean-seagulls-birds-sunset-140111/',
    'https://pixabay.com/videos/field-lavender-flowers-garden-205923/',
    'https://pixabay.com/videos/waterfall-river-water-drone-nature-158229/',
    'https://pixabay.com/videos/fogging-landscape-forest-grasslands-164360/',
    'https://pixabay.com/videos/flower-water-lilies-lake-163869/',
    'https://pixabay.com/videos/river-stream-waterfall-trees-174860/'
]

def extract_video_id(url):
    match = re.search(r'(\d+)/$', url)
    if match:
        return match.group(1)
    return None

def download_video(video_url, filename):
    response = requests.get(video_url, stream=True)
    if response.status_code == 200:
        with open(filename, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        print(f'Downloaded {filename}')
    else:
        print(f'Failed to download {filename}')

def fetch_video_info(video_id):
    params = {
        'key': API_KEY,
        'id': video_id
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    if data['total'] > 0:
        return data['hits'][0]
    return None

def main():
    for url in video_urls:
        video_id = extract_video_id(url)
        if video_id:
            video_info = fetch_video_info(video_id)
            if video_info:
                video_name = video_info['tags'][0] if video_info['tags'] else 'unknown'  # Get the first tag as the video name
                video_url = video_info['videos']['small']['url']  # You can choose different resolutions
                filename = os.path.join(SAVE_PATH, f"{video_name}_{video_id}.mp4")
                download_video(video_url, filename)

if __name__ == '__main__':
    main()
