# Minami -「 Amewomatsu、」
# vid = 'https://www.youtube.com/watch?v=766qmHTc2ro'

import re
from youtube_transcript_api import YouTubeTranscriptApi as yt
from youtube_transcript_api.formatters import TextFormatter

def extract_video_id(youtube_link):
    match = re.search(r'v=([a-zA-Z0-9_-]+)', youtube_link)
    if match:
        video_id = match.group(1)
        return video_id
    else:
        return None


def main():
    try:
        link = input("Enter Video Link: ")
        id = extract_video_id(link)
    except Exception as e:
        print(f"Invalid Input {e}")

    else:
        # print(id)
        result = yt.get_transcript(id, languages= ['en'])
        formatter = TextFormatter()
        result = formatter.format_transcript(result)
        with open("storage.txt", "w", encoding= "utf-8") as file:
            file.write(result)
        print("Text stored in storage.txt")


if __name__ == "__main__":
    main()