import tkinter as t
from tkinter import messagebox
from PIL import Image, ImageTk
import pygame

# Initialize pygame mixer for audio playback
pygame.mixer.init()

# Function to handle artist selection
def on_artist_click(artist_name):
    global current_frame
    
    if artist_name == "Selena Gomez":
        songs = [
            ("Same Old Love", r"C:\Users\ADMIN\Downloads\Selena Gomez - Same Old Love (Lyrics).mp3"),
            ("Come And Get It", r"C:\Users\ADMIN\Downloads\Selena Gomez - Come And Get It (lyrics).mp3"),
            ("Wolves", r"C:\Users\ADMIN\Downloads\Selena Gomez, Marshmello - Wolves (Lyrics).mp3"),
            ("People You Know", r"C:\Users\ADMIN\Downloads\Selena Gomez - People You Know (Lyrics).mp3"),
            ("Who Says", r"C:\Users\ADMIN\Downloads\Selena Gomez - Who says.mp3")
        ]
    elif artist_name == "Justin Bieber":
        songs = [
            ("Peaches", r"C:\Users\ADMIN\Downloads\Justin Bieber - Peaches ft. Daniel Caesar, Giveon.mp3"),
            ("Baby", r"C:\Users\ADMIN\Downloads\Justin Bieber - Baby (Lyrics) ft. Ludacris.mp3"),
            ("Let Me Love You", r"C:\Users\ADMIN\Downloads\DJ Snake ft. Justin Bieber - Let Me Love You [Lyric Video].mp3"),
            ("Never Say Never", r"C:\Users\ADMIN\Downloads\Justin Bieber - Never Say Never (Lyrics) ft. Jaden Smith.mp3"),
            ("Sorry", r"C:\Users\ADMIN\Downloads\Justin Bieber - Sorry (Lyric Video).mp3")
        ]
    elif artist_name == "The Weeknd":
        songs = [
            ("Popular", r"C:\Users\ADMIN\Downloads\The Weeknd, Playboi Carti & Madonna - Popular (Lyrics).mp3"),
            ("House Of Balloons", r"C:\Users\ADMIN\Downloads\The Weeknd - House Of Balloons  Glass Table Girls.mp3"),
            ("I Was Never There", r"C:\Users\ADMIN\Downloads\The Weeknd - I Was Never There (Lyrics).mp3"),
            ("Call Out My Name", r"C:\Users\ADMIN\Downloads\The Weeknd - Call Out My Name (Official Audio).mp3"),
            ("Starboy", r"C:\Users\ADMIN\Downloads\The Weeknd - Starboy (Audio) ft. Daft Punk.mp3")
        ]
    elif artist_name == "Eminem":
        songs = [
            ("Without Me", r"C:\Users\ADMIN\Downloads\Eminem - Without Me (Lyrics).mp3"),
            ("Superman", r"C:\Users\ADMIN\Downloads\Eminem - Superman.mp3"),
            ("Venom", r"C:\Users\ADMIN\Downloads\Eminem - Venom(Official Audio).mp3"),
            ("Mockingbird", r"C:\Users\ADMIN\Downloads\Eminem - Mockingbird [Official Music Video].mp3"),
            ("Rap God", r"C:\Users\ADMIN\Downloads\Eminem - Rap God (Lyrics).mp3")
        ]

    elif artist_name == "Imagine Dragons":
        songs = [
        ("Believer", r"C:\Users\ADMIN\Downloads\Imagine Dragons - Believer (Official Music Video).mp3"),
        ("Bones", r"C:\Users\ADMIN\Downloads\Imagine Dragons - Bones (Official Music Video).mp3"),
        ("Enemy", r"C:\Users\ADMIN\Downloads\Imagine Dragons x J.I.D - Enemy (from the series Arcane League of Legends).mp3"),
        ("Thunder", r"C:\Users\ADMIN\Downloads\Imagine Dragons - Thunder.mp3")
    ]

    else:
        return
    
    # Hide previous elements
    title_label.pack_forget()
    artist_frame.pack_forget()
    
    # Create a new frame for displaying songs
    current_frame = t.Frame(r, bg="black")
    current_frame.pack(pady=40)
    
    # Label for the song list
    song_label = t.Label(current_frame, text=f"🎵 Songs by {artist_name} 🎵", font=("Arial", 20, "bold"), fg="white", bg="black")
    song_label.pack(pady=20)
    
    # Display song titles
    song_frame = t.Frame(current_frame, bg="black")
    song_frame.pack(pady=20)
    
    for song_title, song_path in songs:
        song_button = t.Button(
            song_frame, text=song_title, font=("Arial", 12, "bold"), fg="black", bg="lightblue", 
            activebackground="deepskyblue", relief="raised", width=40, height=2, bd=4,
            command=lambda path=song_path: play_song(path)
        )
        song_button.pack(pady=5)
    
    # Stop song button
    stop_button = t.Button(
        current_frame, text="Stop Song", font=("Arial", 14, "bold"), fg="white", bg="darkred", 
        activebackground="darkorange", relief="raised", command=stop_song
    )
    stop_button.pack(pady=10)
    
    # Go back button
    go_back_button = t.Button(
        current_frame, text="Go Back to Artist List", font=("Arial", 14, "bold"), fg="white", bg="darkgreen", 
        activebackground="limegreen", relief="raised", command=go_back
    )
    go_back_button.pack(pady=20)

# Function to play a song
def play_song(song_path):
    pygame.mixer.music.load(song_path)
    pygame.mixer.music.play()

# Function to stop the current song
def stop_song():
    pygame.mixer.music.stop()

# Go Back function to restore the artist list
def go_back():
    global current_frame
    if current_frame:
        current_frame.destroy()
    title_label.pack(pady=30, anchor="center")
    artist_frame.pack(pady=40)

# Set up the main tkinter window
r = t.Tk()
r.title("🎶 Choose Your Favorite Artist/Singer 🎤")
r.geometry("1000x800")
r.configure(bg="black")

# Title Label
title_label = t.Label(r, text="🎶 Click on your favorite artist's name below! 🎤", font=("Comic Sans MS", 30, "italic"), fg="blue", bg="black")
title_label.pack(pady=30, anchor="center")

# Frame to hold clickable artist names and images
artist_frame = t.Frame(r, bg="black")
artist_frame.pack(pady=40)

# List of artists with their images
artists = [
    ("Selena Gomez", r"C:\Users\ADMIN\Pictures\selena.png"),
    ("Justin Bieber", r"C:\Users\ADMIN\Pictures\justin.png"),
    ("The Weeknd", r"C:\Users\ADMIN\Pictures\weekend.png"),
    ("Eminem", r"C:\Users\ADMIN\Pictures\emenem.png"),
    ("Imagine Dragons", r"C:\Users\ADMIN\Pictures\img dragons.png")
]

# Create artist buttons
for artist_name, image_path in artists:
    artist_row = t.Frame(artist_frame, bg="black")
    artist_row.pack(pady=10)
    
    img = Image.open(image_path)
    img = img.resize((80, 80))
    photo = ImageTk.PhotoImage(img)
    
    image_label = t.Label(artist_row, image=photo, bg="black")
    image_label.image = photo
    image_label.pack(side="left", padx=10)
    
    artist_button = t.Button(
        artist_row, text=artist_name, font=("Helvetica", 22, "bold"), fg="white", bg="gray", 
        activebackground="darkgray", activeforeground="black", width=30, relief="solid", bd=2,
        command=lambda artist_name=artist_name: on_artist_click(artist_name)
    )
    artist_button.pack(side="left")

# Initialize current frame
current_frame = None

# Run the Tkinter event loop
r.mainloop()
