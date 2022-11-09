import pygame
from tkinter  import *
from tkinter.filedialog import askdirectory
from PIL import ImageTk, Image
import os
from tkinter import filedialog


root = Tk()
root.title("Emotional Music Player")
root.geometry("500x300")

pygame.mixer.init()


# Add Song Funtion
def add_song():
    song= filedialog.askopenfilename(initialdir= 'audio/songs/Angry', title="Choose A Song", filetypes=(("mp3 files", "*.mp3"), ))
    song = song.replace("/Users/kenny/Desktop/MyProjects/DL_projects/Face_emotion_recognition/Music_Player/audio/songs/Angry/", '')
    
    song_box.insert(END,song)

# Play selected song
def play():
    song = song_box.get(ACTIVE)
    song = f'/Users/kenny/Desktop/MyProjects/DL_projects/Face_emotion_recognition/Music_Player/audio/songs/Angry/{song}'

    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

# Stop playing song
def stop():
    pygame.mixer.music.stop()
    song_box.selection_clear(ACTIVE)

# Pause Song
def pause():
    pass

# Back to previous song
def previous():
    pass

# Next Song
def next():
    pass


song_box = Listbox(root, bg="black", fg="green", width=60)
song_box.pack(pady=20)

# Resizing Images
back_img = Image.open('Face_emotion_recognition/Music_Player/Images/Previous.png')
frwd_img = Image.open('Face_emotion_recognition/Music_Player/Images/Next.png')
play_img = Image.open('Face_emotion_recognition/Music_Player/Images/Play.png')
pause_img = Image.open('Face_emotion_recognition/Music_Player/Images/Pause.png')
stop_img = Image.open('Face_emotion_recognition/Music_Player/Images/Stop.png')

resized_back= back_img.resize((50,50), Image.ANTIALIAS)
resized_frwd= frwd_img.resize((50,50), Image.ANTIALIAS)
resized_play= play_img.resize((50,50), Image.ANTIALIAS)
resized_pause= pause_img.resize((50,50), Image.ANTIALIAS)
resized_stop= stop_img.resize((50,50), Image.ANTIALIAS)

new_back = ImageTk.PhotoImage(resized_back)
new_frwd = ImageTk.PhotoImage(resized_frwd)
new_play = ImageTk.PhotoImage(resized_play)
new_pause = ImageTk.PhotoImage(resized_pause)
new_stop = ImageTk.PhotoImage(resized_stop)

# Initialise Buttons

back_btn_img = new_back
forward_btn_img = new_frwd
play_btn_img = new_play
pause_btn_img = new_pause
stop_btn_img = new_stop

control_frame = Frame(root)
control_frame.pack()

# Create Buttons

back_btn = Button(control_frame, image= back_btn_img, borderwidth=0, command= previous)
forward_btn = Button(control_frame, image= forward_btn_img, borderwidth=0, command = next)
play_btn = Button(control_frame, image= play_btn_img, borderwidth=0, command = play)
pause_btn = Button(control_frame, image= pause_btn_img, borderwidth=0, command = pause)
stop_btn = Button(control_frame, image= stop_btn_img, borderwidth=0, command = stop)

back_btn.grid(row=0, column =0, padx=10)
forward_btn.grid(row=0, column = 1,padx=10)
play_btn.grid(row=0, column = 2,padx=10)
pause_btn.grid(row=0, column = 3,padx=10)
stop_btn.grid(row=0, column = 4,padx=10)

# Create Menu
my_menu = Menu(root)
root.config(menu=my_menu)

# Add Song Menu
add_song_menu = Menu(my_menu)
my_menu.add_cascade(label="Add Songs", menu = add_song_menu)
add_song_menu.add_command(label="Add one Song to Playlist", command= add_song)

root.mainloop()


# music_player = tkr.Tk()
# music_player.title("Emotional Music Player")
# music_player.geometry("500x300")

# directory= askdirectory()
# os.chdir(directory)
# song_list= os.listdir()

# playlist= tkr.listbox(music_player, font = "Verdana 12 bold",fg = "navy", bg = "gold", selectmode = tke.SINGLE)

# x=0
# for i in song_list:
#     playlist.insert(x, i)
#     x+=1

# pygame.init()
# pygame.mixer.init()

# def play():
#     pygame.mixer.music.load(playlist.get(tke.ACTIVE))
#     var.set(playlist.get(tke.ACTIVE))
#     pygame.mixer.music.play()

# def stop():
#     pygame.mixer.music.stop()

# def pause():
#     pygame.mixer.music.pause()

# Button1 = tkr.Button(music_player, width = 5, height = 3, font = "Verdana 12 bold", text = "Play", command = play, bg= "navy", fg = "gold")

# Button2 = tkr.Button(music_player, width = 5, height = 3, font = "Verdana 12 bold", text = "Stop", command = stop, bg= "navy", fg = "gold")

# Button3 = tkr.Button(music_player, width = 5, height = 3, font = "Verdana 12 bold", text = "Pause", command = pause, bg= "navy", fg = "gold")

# var = tkr.StringVar()
# song_title = tkr.Label(music_player, font = "Verdana 12 bold", textvariable= var)

# song_title.pack()
# Button1.pack(fill = "x")
# Button2.pack(fill = "x")
# Button3.pack(fill = "x")
# playlist.pack(fill= "both", expand = "yes")

# music_player.mainloop()
