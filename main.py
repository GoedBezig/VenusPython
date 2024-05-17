import tkinter as tk

class CoordinateSystem(tk.Canvas):
    def __init__(self, master=None, width=600, height=600, **kwargs):
        super().__init__(master, width=width, height=height, **kwargs)
        self.width = width
        self.height = height
        self.create_line(0, height/2, width, height/2, fill="black")  # X-axis
        self.create_line(width/2, 0, width/2, height, fill="black")  # Y-axis
        self.origin = (width/2, height/2)  # Coordinate system origin
        self.x_scale = 10
        self.y_scale = 10


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
            x = self.origin[0] + i * self.x_scale
            self.create_text(x, self.origin[1] + 10, text=str(i * 5), anchor=tk.N)
        # Draw y-axis labels
        for i in range(-self.height // (2 * self.y_scale), self.height // (2 * self.y_scale) + 1, 5):
            y = self.origin[1] - i * self.y_scale
            self.create_text(self.origin[0] - 10, y, text=str(i * 5), anchor=tk.E)


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

    def plot_predefined_points(self):
        # Define your predefined points here with custom x and y values
        predefined_points = [
            (10, 20, "blue", "oval", 5),
            (-5, 10, "green", "rectangle", 3),
            (20, -15, "red", "oval", 4),
            (-15, -5, "purple", "rectangle", 6)
        ]
        for x, y, color, shape, size in predefined_points:
            self.coordinate_system.plot_point(x, y, color=color, shape=shape, size=size)

if __name__ == "__main__":
    root = tk.Tk()
    app = CoordinateSystemApp(root)
    root.mainloop()
