#!/usr/bin/env python3
import os
import sys
from yt_dlp import YoutubeDL

# Create DOWNLOADS folder
DOWNLOAD_DIR = os.path.join(os.getcwd(), "DOWNLOADS")
if not os.path.exists(DOWNLOAD_DIR):
    os.makedirs(DOWNLOAD_DIR)

# Strong single color
C = "\033[38;5;46m"   # strong green
R = "\033[0m"

def clear():
    os.system("clear" if os.name != "nt" else "cls")

def get_video_info(url):
    try:
        ydl_opts = {"quiet": True, "skip_download": True}
        with YoutubeDL(ydl_opts) as ydl:
            return ydl.extract_info(url, download=False)
    except Exception as e:
        print(f"{C}Error fetching video info: {e}{R}")
        return None

def download_video(url, quality):
    print(f"\n{C}[+] Downloading video in {quality}p...\n{R}")
    ydl_opts = {
        "outtmpl": f"{DOWNLOAD_DIR}/%(title)s.%(ext)s",
        "format": f"bestvideo[height<={quality}]+bestaudio/best",
        "merge_output_format": "mp4"
    }
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def download_audio(url):
    print(f"\n{C}[+] Downloading audio (MP3)...\n{R}")
    ydl_opts = {
        "outtmpl": f"{DOWNLOAD_DIR}/%(title)s.%(ext)s",
        "format": "bestaudio/best",
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }
        ],
    }
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def banner():
    print(f"{C} /$$$$$$$$       /$$             /$$   /$$       /$$   /$$       /$$$$$$$        /$$            {R}")
    print(f"{C}| $$_____/      | $$            | $$  | $$      | $$  / $$      | $$__  $$      | $$            {R}")
    print(f"{C}| $$            | $$            | $$  | $$      |  $$/ $$/      | $$  \\ $$      | $$            {R}")
    print(f"{C}| $$$$$         | $$            | $$  | $$       \\  $$$$/       | $$  | $$      | $$            {R}")
    print(f"{C}| $$__/         | $$            | $$  | $$        >$$  $$       | $$  | $$      | $$            {R}")
    print(f"{C}| $$            | $$            | $$  | $$       /$$/\\  $$      | $$  | $$      | $$            {R}")
    print(f"{C}| $$            | $$$$$$$$      |  $$$$$$/      | $$  \\ $$      | $$$$$$$/      | $$$$$$$$      {R}")
    print(f"{C}|__/            |________/       \\______/       |__/  |__/      |_______/       |________/      {R}")
    print("")
    print(f"{C}                             ⚡ F L U X D L ⚡{R}")
    print("")
    print(f"{C}                      powered by HUN73R N37W0RK{R}")
    print("")
    print(f"{C}                 Support to  all YTDL Suported websites{R}")
    print("")

def main():
    while True:
        try:
            clear()
            banner()

            print(f"{C}Enter Video URL (or type 'exit' or press ' ctrl + c ' to exit ):{R}")
            url = input("> ").strip()

            if url.lower() == "exit":
                print(f"{C}Goodbye!{R}")
                sys.exit(0)

            if not url:
                print(f"{C}URL cannot be empty!{R}")
                continue

            info = get_video_info(url)
            if info is None:
                print(f"{C}Failed to load video. Try again.{R}")
                continue

            title = info.get("title", "Unknown")
            print(f"\n{C}Title:{R} {title}\n")

            print(f"{C}Choose Format:{R}")
            print(f"{C}1.{R} MP4 (Video)")
            print(f"{C}2.{R} MP3 (Audio Only)")
            choice = input("> ").strip()

            if choice == "1":
                print(f"\n{C}Available Qualities:{R}")
                print(f"{C}360, 480, 720, 1080, 1440, 2160{R}")
                quality = input(f"\n{C}Enter resolution (e.g. 720):{R} ").strip()

                if not quality.isdigit():
                    print(f"{C}Invalid resolution!{R}")
                    continue

                download_video(url, quality)

            elif choice == "2":
                download_audio(url)

            else:
                print(f"{C}Invalid choice!{R}")
                continue

            print(f"\n{C}Download complete! ✔{R}")
            print(f"{C}Saved to:{R} {DOWNLOAD_DIR}\n")

            input(f"{C}Press ENTER to return to menu...{R}")

        except KeyboardInterrupt:
            print(f"\n{C}Exiting...{R}")
            sys.exit(0)

if __name__ == "__main__":
    main()
