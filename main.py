import tkinter as tk
from PIL import Image, ImageTk

class SlideshowApp:
    def __init__(self, root, image_paths):
        self.root = root
        self.image_paths = image_paths
        self.current_image_index = 0

        # Configure window to be full screen
        self.root.attributes('-fullscreen', True)

        self.image_label = tk.Label(root)
        self.image_label.pack(expand=True, fill=tk.BOTH)

        self.show_image()

        # Bind left and right arrow key events
        self.root.bind('<Left>', self.prev_image_key_pressed)
        self.root.bind('<Right>', self.next_image_key_pressed)

        # Bind arrow key releases to stop slideshow movement
        self.root.bind('<KeyRelease-Left>', self.stop_slide_movement)
        self.root.bind('<KeyRelease-Right>', self.stop_slide_movement)

        # Bind Ctrl + C to exit the program
        self.root.bind('<Control-c>', lambda event: self.root.destroy())

        # Variable to track arrow key presses
        self.arrow_key_pressed = False

    def show_image(self):
        image_path = self.image_paths[self.current_image_index]
        image = Image.open(image_path)
        photo = ImageTk.PhotoImage(image)

        self.image_label.config(image=photo)
        self.image_label.image = photo

    def next_image(self):
        if self.arrow_key_pressed:
            self.current_image_index = (self.current_image_index + 1) % len(self.image_paths)
            self.show_image()

    def prev_image(self):
        if self.arrow_key_pressed:
            self.current_image_index = (self.current_image_index - 1) % len(self.image_paths)
            self.show_image()

    def prev_image_key_pressed(self, event):
        self.arrow_key_pressed = True
        self.prev_image()

    def next_image_key_pressed(self, event):
        self.arrow_key_pressed = True
        self.next_image()

    def stop_slide_movement(self, event):
        self.arrow_key_pressed = False

if __name__ == "__main__":
    # Replace these paths with the paths of your own images
    image_paths = [
        r"C:\Users\sarau\Mockup\mockup1.png",
        r"C:\Users\sarau\Mockup\mockup2.png",
        r"C:\Users\sarau\Mockup\mockup3.png",
    ]

    root = tk.Tk()
    root.title("Slideshow App")

    app = SlideshowApp(root, image_paths)

    root.mainloop()
