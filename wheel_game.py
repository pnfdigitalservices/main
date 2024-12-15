import tkinter as tk
import random
import math

# Create the main application window
app = tk.Tk()
app.title("Spinning Game")
app.geometry("400x500")

# Canvas to draw the spinning wheel
canvas = tk.Canvas(app, width=300, height=300, bg="white")
canvas.pack(pady=20)

# Draw the wheel (circle)
center_x, center_y, radius = 150, 150, 120
wheel = canvas.create_oval(center_x - radius, center_y - radius, 
                           center_x + radius, center_y + radius, fill="lightblue")

"""
Wheel = canvas.create_line(150, 80, 170, 70, 210, 70, 180, 110,
                          190, 150, 150, 130, 110, 150, 120, 110, 
                          90, 70, 130, 70, fill="gold", width=2)
"""
# Draw sectors and labels
sectors = [1, 2, 3, 4, 5, 6, 7, 8, 9]
num_sectors = len(sectors)

# Draw sectors with labels
for i, sector in enumerate(sectors):
    angle = (360 / num_sectors) * i
    x = center_x + radius * 0.7 * math.cos(math.radians(angle))
    y = center_y + radius * 0.7 * math.sin(math.radians(angle))
    canvas.create_text(x, y, text=str(sector), font=("Arial", 12, "bold"))


def spin_wheel():
    # Set up the number of spins
    spins = random.randint(1, 10) * 360  # Random number of full spins (between 1 and 10 full spins)
    target_angle = random.randint(0, 360)  # Random final target position
    total_angle = spins + target_angle  # Total rotation angle

# Arrow indicating the current selection
#canvas.create_polygon(150, 10, 140, 30, 160, 30, fill="red", outline="black")
# Set the duration of the spin (in seconds) and calculate the total number of frames
    spin_duration = random.uniform(1, 3)  # Random time between 2 to 3 seconds
    total_frames = int(spin_duration * 100)  # Number of frames (100 frames per second)

    # Frame delay between each step (in milliseconds)
    frame_delay = int(spin_duration * 1000 / total_frames)

    # Animation: rotate the wheel step-by-step
    for frame in range(total_frames):
        angle = (frame / total_frames) * total_angle
        app.update()
        canvas.delete("highlight")
        # Rotate the wheel by applying a "rotate" transformation
        canvas.coords(wheel, center_x - radius, center_y - radius, 
                      center_x + radius, center_y + radius)
        highlight_angle = (angle % 360) / (360 / num_sectors)
        highlight_sector = int(highlight_angle) % num_sectors
        x = center_x + radius * 0.7 * math.cos(math.radians((360 / num_sectors) * highlight_sector))
        y = center_y + radius * 0.7 * math.sin(math.radians((360 / num_sectors) * highlight_sector))
        canvas.create_text(x, y, text=str(sectors[highlight_sector]), font=("Arial", 12, "bold"), tags="highlight", fill="orange")
        app.after(frame_delay)

    # After the animation ends, display the result (final sector)
    result = sectors[int(target_angle / (360 / num_sectors)) % num_sectors]
    result_label.config(text=f"Result: {result}")
    #result_label2.config(text=f"Spinning to: {total_angle} degrees")s")


# Add spin button
spin_button = tk.Button(app, text="Spin the Wheel", command=spin_wheel)
spin_button.pack(pady=10)
result_label = tk.Label(app, text="Spin result will appear here", font=("Arial", 12))
result_label.pack(pady=10)

# Label to display the result
result_label = tk.Label(app, text="Result: ", font=("Arial", 12, "bold"))
result_label.pack(pady=10)

# Start the Tkinter event loop
app.mainloop()
