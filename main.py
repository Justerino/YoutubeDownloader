import customtkinter as ctk
import pytube.exceptions
from pytube import YouTube

# initialize global settings
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("green")

# set title and size of window
app = ctk.CTk()
app.title("YouTube Downloader")
app.geometry("600x240")

# create frame for label and search bar
# create label and search bar
title = ctk.CTkLabel(app, text="Enter URL to YouTube video")
title.pack(padx=10, pady=10)

url = ctk.StringVar()
link = ctk.CTkEntry(app, height=25, width=400, textvariable=url)
link.pack(padx=10, pady=10)

# Downloading label
finishLabel = ctk.CTkLabel(app, text="")
finishLabel.pack()


def downloadVideo():
    try:
        ytLink = url.get()
        ytObject = YouTube(ytLink,
                           use_oauth=True,
                           allow_oauth_cache=True)
        video = ytObject.streams.get_highest_resolution()
        video.download(output_path='Downloads/Video')
        finishLabel.configure(text="Video downloaded successfully")
    except pytube.exceptions.AgeRestrictedError:
        print("Video is age restricted, please enable Youtube on TV and provide the device ID of this application.")
    except:
        print("Invalid URL")


def downloadAudio():
    try:
        ytLink = url.get()
        ytObject = YouTube(ytLink,
                           use_oauth=True,
                           allow_oauth_cache=True)
        audio = ytObject.streams.filter(only_audio=True).first()
        audio.download(output_path='Downloads/Audio',
                       filename_prefix="Audio_")
        finishLabel.configure(text="Audio downloaded successfully")
    except pytube.exceptions.AgeRestrictedError:
        print("Video is age restricted, please enable Youtube on TV and provide the device ID of this application.")
    except:
        print("Invalid URL")


# main function
def main():

    # create download video button, pass url and finish label as argument to allow functions to modify
    videoButton = ctk.CTkButton(app, text="Download Video", command=downloadVideo)
    videoButton.pack(padx=10, pady=10)

    # create download audio button, pass url and finish label as argument to allow functions to modify
    audioButton = ctk.CTkButton(app, text="Download Audio", command=downloadAudio)
    audioButton.pack(padx=10, pady=10)

    # enter the main loop until program is closed
    app.mainloop()


# run the main function only if this module is executed as the main script
if __name__ == "__main__":
    # call the main function
    main()
