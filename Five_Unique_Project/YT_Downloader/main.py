



# Importing the necessary libraries
from pytube import YouTube
from tqdm import tqdm

# Asking the user for the URL of the YouTube video
url = input("Enter the YouTube video URL: ")

try:
    # Creating a YouTube object using the URL
    yt = YouTube(url)

    # Printing the video title as confirmation
    print(f"Video Title: {yt.title}")

    # Getting the highest quality video stream
    video_stream = yt.streams.get_highest_resolution()
    print(f"Video Resolution: {video_stream.resolution}")

    # Asking the user for the folder to save the video
    output_folder = input("Enter the folder to save the video (leave blank for current directory): ")
    if output_folder == "":
        output_folder = "."

    # Initialize the progress bar
    progress_bar = tqdm(total=video_stream.filesize, unit='B', unit_scale=True, desc="Downloading Video")

    # Function to update the progress bar
    def progress_function(stream, chunk, bytes_remaining):
        bytes_downloaded = stream.filesize - bytes_remaining
        progress_bar.update(len(chunk))  # Update progress bar with each chunk downloaded

    # Link the progress function to the stream
    video_stream.on_progress = progress_function

    # Download the video
    print("Downloading...")
    video_stream.download(output_folder)

    # Close the progress bar after the download is complete
    progress_bar.close()

    print(f"Download complete! Video saved to: {output_folder}")

except Exception as e:
    print(f"Error: {e}. Please check the URL and try again.")
