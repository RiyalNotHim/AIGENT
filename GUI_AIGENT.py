import tkinter as tk
from PIL import Image, ImageTk
from datetime import datetime
import pygame
from tkinter.scrolledtext import ScrolledText
from main_aigent import *

class AnimatedGIF(tk.Label):
    def __init__(self, master, paths, audio_path=None):
        self.master = master
        self.sequences = []
        self.delay = 100
        self.transition_frames = 10
        self.transition_time = 1000

        for path in paths:
            self.load_frames(path)

        self.idx = 0
        self.current_frame = self.sequences[0][0]

        super().__init__(master, image=self.current_frame)

        # Load audio if provided
        self.audio_path = audio_path
        if self.audio_path:
            pygame.mixer.init()
            pygame.mixer.music.load(self.audio_path)
            pygame.mixer.music.play()

    def load_frames(self, path):
        gif = Image.open(path)
        sequence = []
        try:
            while True:
                gif.seek(len(sequence))
                sequence.append(ImageTk.PhotoImage(gif.copy()))
        except EOFError:
            pass
        self.sequences.append(sequence)

    def show_next_frame(self):
        if self.idx >= len(self.sequences[self.play_count]) - 1:
            self.idx = 0
            self.play_count += 1
            if self.play_count >= len(self.sequences):
                self.after(5000, self.open_new_window)
                return
        self.current_frame = self.sequences[self.play_count][self.idx]
        self.configure(image=self.current_frame)
        self.idx += 1
        self.after(self.delay, self.show_next_frame)

    def transition_to_next_image(self):
        current_sequence = self.sequences[-1]
        next_sequence = self.sequences[-2]

        transition_sequence = []

        for i in range(self.transition_frames + 1):
            alpha = i / self.transition_frames
            blended_frame = Image.blend(current_sequence[-1], next_sequence[0], alpha)
            transition_sequence.append(ImageTk.PhotoImage(blended_frame))

        self.show_transition_frames(transition_sequence, 0)

    def show_transition_frames(self, transition_sequence, idx):
        if idx < len(transition_sequence):
            self.configure(image=transition_sequence[idx])
            self.after(self.transition_time // self.transition_frames,
                       lambda: self.show_transition_frames(transition_sequence, idx + 1))
        else:
            self.sequences.pop(-1)
            self.show_next_frame()

    def open_new_window(self):
        new_window = tk.Toplevel(self.master)
        new_window.title("Login")
        new_window.attributes('-fullscreen', True)

        def exit_fullscreen(event):
            new_window.attributes('-fullscreen', False)

        def minimize_window(event):
            new_window.iconify()

        def maximize_window(event):
            new_window.attributes('-fullscreen', True)

        new_window.bind("<Escape>", exit_fullscreen)
        new_window.bind("<F11>", exit_fullscreen)
        new_window.bind("<F10>", minimize_window)
        new_window.bind("<F9>", maximize_window)

        # Display the background image
        gif_path = "D:/PROGRAMMING/PYTHON/AIGENT/bckground.gif"
        gif_image = Image.open(gif_path)
        gif_photo = ImageTk.PhotoImage(gif_image)
        gif_label = tk.Label(new_window, image=gif_photo)
        gif_label.image = gif_photo
        gif_label.pack()

        # Load and play the audio
        login_audio_path = "D:/PROGRAMMING/PYTHON/AIGENT/loginaudio.mp3"
        pygame.mixer.init()
        pygame.mixer.music.load(login_audio_path)
        pygame.mixer.music.play()

        # Display the login form
        login_frame = tk.Frame(new_window, bg="#0047ab", bd=100)
        login_frame.place(relx=0.5, rely=0.5, anchor="center")

        # Fixed username and password
        fixed_username = "user"
        fixed_password = "password"

        label_username = tk.Label(login_frame, text="Username:", bg="#4682B4", font=("Tekton Pro", 14))
        label_username.grid(row=0, column=0, padx=10, pady=5, sticky="e")
        entry_username = tk.Entry(login_frame, font=("Tekton Pro", 14))
        entry_username.grid(row=0, column=1, padx=10, pady=5)

        label_password = tk.Label(login_frame, text="Password:", bg="#4682B4", font=("Tekton Pro", 14))
        label_password.grid(row=1, column=0, padx=10, pady=5, sticky="e")
        entry_password = tk.Entry(login_frame, font=("Tekton Pro", 14), show="*")
        entry_password.grid(row=1, column=1, padx=10, pady=5)

        def login():
            username = entry_username.get()
            password = entry_password.get()

            if username == fixed_username and password == fixed_password:
                new_window.destroy()
                root.destroy()
                aigent_ex()
                 # Close login window if login successful # Open third screen after successful login
            else:
                lbl_error.config(text="Invalid username or password")

        btn_login = tk.Button(login_frame, text="Login", font=("Tekton Pro", 14), bg="#87CEEB", fg="white", command=login)
        btn_login.grid(row=2, columnspan=2, padx=10, pady=10)

        lbl_error = tk.Label(login_frame, text="", bg="#0047ab", fg="red")
        lbl_error.grid(row=3, columnspan=2, padx=10, pady=5)



root = tk.Tk()
root.title("Animated GIF")
root.attributes('-fullscreen', True)

# Pass the path to the audio file as an argument
gif_label = AnimatedGIF(root, ["D:/PROGRAMMING/PYTHON/AIGENT/initgif.gif", "D:/PROGRAMMING/PYTHON/AIGENT/a.gif"], "D:/PROGRAMMING/PYTHON/AIGENT/why1.mp3")
gif_label.pack(fill=tk.BOTH, expand=True)

gif_label.play_count = 0
gif_label.show_next_frame()

root.mainloop()

