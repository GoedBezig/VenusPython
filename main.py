import tkinter as tk
from mqttConnect import *


class CoordinateSystem(tk.Canvas):
    def __init__(self, master=None, width=600, height=600, **kwargs):
        super().__init__(master, width=width, height=height, **kwargs)
        self.width = width
        self.height = height
        self.create_line(0, height/2, width, height/2, fill="black")  # X-axis
        self.create_line(width/2, 0, width/2, height, fill="black")  # Y-axis
        self.origin = (width/2, height/2)  # Coordinate system origin
        self.legend_items = [
            ("Cliff", "black", "circle"),
            ("Hill", "blue", "hexagon"),
            ("Small Rock", "red", "square", 10),
            ("Big Rock", "green", "square", 30)
        ]

    def plot_point(self, x, y, color="red", shape="oval", size=2):
        scaled_x = self.origin[0] + x * self.x_scale
        scaled_y = self.origin[1] - y * self.y_scale
        if shape == "oval":
            self.create_oval(scaled_x - size, scaled_y - size, scaled_x + size, scaled_y + size, fill=color)
        elif shape == "rectangle":
            self.create_rectangle(scaled_x - size, scaled_y - size, scaled_x + size, scaled_y + size, fill=color)

    def draw_axis_labels(self):
        # Calculate the range of values displayed on the axis
        x_min = -self.origin[0] / self.x_scale
        x_max = (self.width - self.origin[0]) / self.x_scale
        y_min = (self.height - self.origin[1]) / self.y_scale
        y_max = -self.origin[1] / self.y_scale

        # Calculate the scaling factors based on the range of values
        x_spacing = self.width / (x_max - x_min)
        y_spacing = self.height / (y_max - y_min)

        # Draw x-axis labels
        for i in range(int(x_min), int(x_max) + 1):
            x = self.origin[0] + i * self.x_scale
            self.create_text(x, self.origin[1] + 10, text=str(i*5), anchor=tk.N)

        # Draw y-axis labels
        for i in range(int(y_min), int(y_max) + 1):
            y = self.origin[1] - i * self.y_scale
            self.create_text(self.origin[0] - 10, y, text=str(i*5), anchor=tk.E)

    # Other methods remain unchanged...

    def __init__(self, master=None, width=600, height=600, **kwargs):
        super().__init__(master, width=width, height=height, **kwargs)
        self.width = width
        self.height = height
        self.create_line(0, height/2, width, height/2, fill="black")  # X-axis
        self.create_line(width/2, 0, width/2, height, fill="black")  # Y-axis
        self.origin = (width/2, height/2)  # Coordinate system origin
        self.legend_items = [
            ("Cliff", "black", "circle"),
            ("Hill", "blue", "hexagon"),
            ("Small Rock", "red", "square", 10),
            ("Big Rock", "green", "square", 30)
        ]

    def plot_point(self, x, y, color="red", shape="oval", size=2):
        # Calculate the scaling factors based on the axis label spacing
        x_spacing = self.width / (len(range(-self.width // 2, self.width // 2, 5)) - 1)
        y_spacing = self.height / (len(range(-self.height // 2, self.height // 2, 5)) - 1)
        x_scale = x_spacing / 5
        y_scale = y_spacing / 5

        # Calculate the scaled coordinates
        scaled_x = self.origin[0] + x * x_scale
        scaled_y = self.origin[1] - y * y_scale

        # Plot the point
        if shape == "oval":
            self.create_oval(scaled_x - size, scaled_y - size, scaled_x + size, scaled_y + size, fill=color)
        elif shape == "rectangle":
            self.create_rectangle(scaled_x - size, scaled_y - size, scaled_x + size, scaled_y + size, fill=color)

    def __init__(self, master=None, width=600, height=600, **kwargs):
        super().__init__(master, width=width, height=height, **kwargs)
        self.width = width
        self.height = height
        self.create_line(0, height/2, width, height/2, fill="black")  # X-axis
        self.create_line(width/2, 0, width/2, height, fill="black")  # Y-axis
        self.origin = (width/2, height/2)  # Coordinate system origin
        self.x_scale = 4
        self.y_scale = 4
        self.legend_items = [
            ("Cliff", "black", "circle"),
            ("Hill", "blue", "hexagon"),
            ("Small Rock", "red", "square", 10),
            ("Big Rock", "green", "square", 30)
        ]

    def plot_point(self, x, y, color="red", shape="oval", size=2):
        scaled_x = self.origin[0] + x * self.x_scale
        scaled_y = self.origin[1] - y * self.y_scale
        if shape == "oval":
            self.create_oval(scaled_x - size, scaled_y - size, scaled_x + size, scaled_y + size, fill=color)
        elif shape == "rectangle":
            self.create_rectangle(scaled_x - size, scaled_y - size, scaled_x + size, scaled_y + size, fill=color)

    def draw_axis_labels(self):
        # Draw x-axis labels
        for i in range(-self.width // (2 * self.x_scale), self.width // (2 * self.x_scale) + 1, 5):
            if i % 15 == 0:  # Only draw labels when the number is a multiple of 5
                x = self.origin[0] + i * self.x_scale
                self.create_text(x, self.origin[1] + 10, text=str(i), anchor=tk.N)
        # Draw y-axis labels
        for i in range(-self.height // (2 * self.y_scale), self.height // (2 * self.y_scale) + 1, 5):
            if i % 15 == 0:  # Only draw labels when the number is a multiple of 5
                y = self.origin[1] - i * self.y_scale
                self.create_text(self.origin[0] - 10, y, text=str(i), anchor=tk.E)


    def draw_legend(self):
        self.create_text(self.width - 50, 50, text="Legend:", anchor=tk.N)
        y_offset = 70
        for item in self.legend_items:
            label, color, shape, size = item[:4] if len(item) > 3 else (item[0], item[1], item[2], 5)
            legend_text = f"{label}: {shape.capitalize()}"
            self.create_text(self.width - 50, y_offset, text=legend_text, fill=color, anchor=tk.N)
            y_offset += 20

class CoordinateSystemApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Coordinate System")

        self.coordinate_system = CoordinateSystem(master, width=600, height=600)
        self.coordinate_system.pack()

        # Plot predefined coordinates
        self.plot_predefined_points()

        # Draw axis labels
        self.coordinate_system.draw_axis_labels()

        # Draw legend
        self.coordinate_system.draw_legend()

    def plot_predefined_points(self):
        # Use the imported predefined_points from coordinates.py
        for x, y, color, shape, size in predefined_points:
            self.coordinate_system.plot_point(x, y, color=color, shape=shape, size=size)

if __name__ == "__main__":
    root = tk.Tk()
    app = CoordinateSystemApp(root)
    root.mainloop()
