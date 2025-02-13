import tkinter as tk
from PIL import Image, ImageTk
import random

# Set up the main window
root = tk.Tk()
root.title("Birthday Card")
root.geometry("500x400")

# Create a canvas to display the birthday card elements
canvas = tk.Canvas(root, width=500, height=400, bg="black")
canvas.pack()

# Function to create hearts
def create_heart():
    hearts = []
    for i in range(16):  # Create 10 hearts
        x = random.randint(50, 450)
        y = random.randint(50, 350)
        size = random.randint(20, 40)
        color = random.choice(["#D1004D", "pink", "#C8A2C8", "brown"])
        heart = canvas.create_oval(x - size, y - size, x + size, y + size, fill=color, outline="black")
        hearts.append((heart, x, y, size, color))  # Save the heart object with its properties
    return hearts

# Function to float hearts upwards
def float_heart(hearts):
    for heart, x, y, size, color in hearts:
        canvas.move(heart, 0, -2)  # Move the heart upwards
    root.after(40, float_heart, hearts)  # Continue moving the hearts every 20 ms

# Create hearts and start the animation
hearts = create_heart()  # Create hearts on the canvas
float_heart(hearts)  # Start the floating animation

# Add background gradient effect
def create_gradient(canvas, red,magenta):
    for i in range(500):
        canvas.create_line(i, 0, i, 400, fill=blend_colors(red, magenta, i / 500), width=1)

def blend_colors(red, magenta, weight):
    return "#%02x%02x%02x" % (
        int(red[1:3], 16) * (1 - weight) + int(magenta[1:3], 16) * weight,
        int(red[3:5], 16) * (1 - weight) + int(magenta[3:5], 16) * weight,
        int(red[5:7], 16) * (1 - weight) + int(magenta[5:7], 16) * weight
    )

# Function to simulate burning party popper animation
def pop_party_popper(event=None):
    # Clear the canvas and start the animation
    canvas.delete("all")

    # Display crackers that burn (changing images)
    def show_burn_animation(i=0):
        if i < len(party_popper_images):
            img = party_popper_images[i]
            canvas.create_image(250, 150, image=img)
            canvas.update()  # Update canvas to show changes
            root.after(500, show_burn_animation, i + 1)  # Schedule next image

    # Start the animation by calling the first frame
    show_burn_animation()

    # After animation, show heart and birthday wish
    root.after(500 * len(party_popper_images), show_heart_and_wish)

    # After heart and wish, start floating balloons animation
    root.after(500 * len(party_popper_images) + 1000, create_balloons)

def show_heart_and_wish():
    # Clear the canvas
    canvas.delete("all")
    
    # Display the heart emoji and birthday message
    heart = "❤️"
    canvas.create_text(300, 100, text=heart, font=("Dancing Script", 50, "bold"), fill="maroon")

    # Correcting the multi-line text with proper formatting
    birthday_message = (
        "🎂 Happy Birthday, Akkiiiii! 🎂\n"
        "Thank you for always being there for me,\n"
        "especially when I needed you the most!\n"
        "I seriously found a gem whom I never want to lose.\n"
        "May God bless you with all the happiness, love,\n"
        "and laughter that you deserve."
    )
    canvas.create_text(250, 250, text=birthday_message, font=("Dancing Script", 14),fill='white')

# Load your friend's photo and resize it
friend_photo = Image.open(r"C:\Users\Sneha Agrawal\Desktop\file-handling\sneha file\ak.pic.png")  # Use raw string to avoid escape issues
friend_photo = friend_photo.resize((150, 150))  # Resize to fit the canvas
friend_photo_tk = ImageTk.PhotoImage(friend_photo)

# Add the friend's photo to the card
canvas.create_image(250, 100, image=friend_photo_tk)

# Add initial text on the card with emojis
canvas.create_text(250, 280, text="🎉 Click to open your birthday card🎉", font=("Lobster", 20), fill='#F7E1C3')

# Load party popper images (simulating burning crackers)
party_popper_images = []
for i in range(1, 6):
    # Use f-string to correctly format the file path for each cracker image
    img_path = fr"C:/Users/Sneha Agrawal/Desktop/file-handling/sneha file/party.pop.{i}.jpg"
    print("Loading image:", img_path)  # Debugging line to print the image path
    try:
        img = Image.open(img_path)
        img = img.resize((100, 100))  # Resize the image if needed
        party_popper_images.append(ImageTk.PhotoImage(img))
    except FileNotFoundError:
        print(f"Error: {img_path} not found!")  # If file is not found, print an error message

# Check if we loaded any images, if not, show a warning
if not party_popper_images:
    print("Warning: No party popper images were loaded.")

# Function to create and animate balloons
canvas.bind("<Button-1>", pop_party_popper)

# Start the GUI loop
root.mainloop()
