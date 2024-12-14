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
sectors = [1, 2, 3, 4, 5, 6, 7, 8]
num_sectors = len(sectors)

# Draw sectors with labels
for i, sector in enumerate(sectors):
    angle = (360 / num_sectors) * i
    x = center_x + radius * 0.7 * math.cos(math.radians(angle))
    y = center_y + radius * 0.7 * math.sin(math.radians(angle))
    canvas.create_text(x, y, text=str(sector), font=("Arial", 12, "bold"))

# Arrow indicating the current selection
#canvas.create_polygon(150, 10, 140, 30, 160, 30, fill="red", outline="black")
# Spin function
def spin_wheel():
    spins = random.randint(1, 10) * 360  # Number of full spins
    target_angle = random.randint(0, 360)  # Final position
    total_angle = spins  + target_angle
    
    for angle in range(0, total_angle, 10):  # Animate the spinning
        app.update()
        canvas.delete("highlight")
        highlight_angle = (angle % 360) / (360 / num_sectors)
        highlight_sector = int(highlight_angle) % num_sectors
        x = center_x + radius * 0.7 * math.cos(math.radians((360 / num_sectors) * highlight_sector))
        y = center_y + radius * 0.7 * math.sin(math.radians((360 / num_sectors) * highlight_sector))
        canvas.create_text(x, y, text=str(sectors[highlight_sector]), font=("Arial", 12, "bold"), tags="highlight", fill="orange")
        app.after(50)
    
    result = sectors[int(target_angle / (360 / num_sectors)) % num_sectors]
    result_label.config(text=f"Result: {result}")
    #result_label.config(text=f"Spinning to: {spins / 360} degrees")


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
