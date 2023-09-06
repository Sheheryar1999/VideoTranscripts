import os
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

def store_text(result):
    ch = input("Make a new file or update an old one?\n Answer: ")
    path = input("Enter File Name: ")
    if ch == "old":
        if os.path.exists(path):
            try:
                # Open the file in write mode ('w')
                with open(path, "w", encoding="utf-8") as file:
                    # You can now write data to the file
                    file.write(result)

                # The file is automatically closed when the "with" block exits
                print(f"File '{path}' was opened and written successfully.")
            except Exception as e:
                # Handle any exceptions that may occur during file operations
                print(f"An error occurred: {e}")
        else:
            print("'{path}' does not exist. It cannot be opened.")

    else:
        path = path + ".txt"
        with open(path, "w", encoding= "utf-8") as file:
            file.write(result)
    print(f"Text stored in {path}")


def main():

    link = input("Enter Video Link: ")
    id = extract_video_id(link)
    # print(id)
    result = yt.get_transcript(id, languages= ['en'])
    formatter = TextFormatter()
    result = formatter.format_transcript(result)

    store_text(result)

if __name__ == "__main__":
    main()
