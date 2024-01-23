import subprocess
from pytube import YouTube
import requests
import re
import datetime
import time
from concurrent.futures import ThreadPoolExecutor

def is_link_available(link):
    try:
        response = requests.get(link)
        return response.status_code == 200
    except requests.RequestException:
        return False

def get_valid_filename(title):
    valid_chars = '-_() abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    clean_title = ''.join(char if char in valid_chars else '_' for char in title)
    return re.sub('_+', '_', clean_title).strip('_')

def get_video_title(youtube_url):
    try:
        yt = YouTube(youtube_url)
        return yt.title
    except Exception as e:
        print(f"Error: {e}")
        return None

def start_recording(link, title):
    today = datetime.datetime.now()
    date_now = today.strftime("%d_%b_%Y_%H_%M_%S")

    if title:
        file_name = get_valid_filename(title)
    else:
        file_name = f"recording_{time.time()}"

    command = ["streamlink", link, "best", "-o", f"./recorded/{file_name}_{date_now}.ts"]
    subprocess.run(command)

def process_link(link):
    if is_link_available(link):
        video_title = get_video_title(link)
        print(f"Link {link} is available.")
        if video_title:
            print(f"Video title: {video_title}")
        else:
            print("Could not fetch video title.")

        print("Starting recording...")
        start_recording(link, video_title)
    else:
        print(f"Link {link} is not available. Skipping.")

def main():
    filename = 'wish.txt'
    previous_links = set()

    while True:
        with open(filename, 'r') as file:
            current_links = set(file.read().splitlines())

        new_links = current_links - previous_links
        if new_links:
            with ThreadPoolExecutor() as executor:
                executor.map(process_link, new_links)
            previous_links = current_links

        time.sleep(60)  

if __name__ == "__main__":
    main()
