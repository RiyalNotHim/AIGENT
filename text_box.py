import tkinter as tk
from tkinter.scrolledtext import ScrolledText

def main():
    # Create the main window
    root = tk.Tk()
    root.title("Text Browser Example")
    
    custom_font = ("Times New Roman", 12)
    # Create a text browser widget
    text_browser = ScrolledText(root, width=30, height=1,font=custom_font)
    text_browser.pack(padx=10, pady=2)
    
    # Add some text to the text browser
    text_browser.insert(tk.END, "This is a text browser widget.")
    
    # Start the Tkinter event loop
    root.mainloop()

if __name__ == "__main__":
    main()
