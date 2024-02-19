import tkinter as tk
from tkinter import messagebox, simpledialog
import random

class ElevatorSimulator:
    def __init__(self):
        # Initialize current floor
        self.current_floor = "A"

        # Create the main Tkinter window
        self.root = tk.Tk()
        self.root.title("Elevator Simulator")

        # Label to display current floor
        self.floor_label = tk.Label(self.root, text="Elevator is now at Floor " + self.current_floor)
        self.floor_label.pack(pady=20)

        # Frame to hold buttons
        button_box = tk.Frame(self.root)
        button_box.pack()

        floors = ["A", "B", "C"]

        # Create buttons for each floor
        for floor in floors:
            floor_button = tk.Button(button_box, text="Floor " + floor, command=lambda f=floor: self.move_elevator(f))
            floor_button.pack(side=tk.LEFT, padx=10)

        # Create button for requesting a specific floor
        request_button = tk.Button(button_box, text="Request Floor", command=self.request_floor_dialog)
        request_button.pack(side=tk.LEFT, padx=10)

    def move_elevator(self, target_floor):
        # Simulate elevator movement
        if not self.is_elevator_busy():
            self.current_floor = target_floor
            self.show_info_dialog("Arrived at Floor " + self.current_floor, 40)
            self.update_ui()
        else:
            self.show_info_dialog("Elevator is busy. Please wait.", 40)

    def update_ui(self):
        self.floor_label.config(text="Elevator is now at Floor " + self.current_floor)

    def is_elevator_busy(self):
        # Simulate randomness for elevator being busy
        return random.random() < 0.3  # Adjust the probability as needed (now set to 30%)

    def request_floor_dialog(self):
        selected_floor = self.show_input_dialog("Enter the floor you wish to go to:", self.current_floor)
        if self.is_valid_floor(selected_floor):
            self.move_elevator(selected_floor)
        else:
            self.show_info_dialog("Invalid floor. Please enter A, B, or C.", 40)

    def is_valid_floor(self, floor):
        return floor and floor.upper() in {"A", "B", "C"}

    def show_input_dialog(self, prompt, default_text):
        # Show a simple input dialog
        return simpledialog.askstring("Input Dialog", prompt, initialvalue=default_text)

    def show_info_dialog(self, message, y_offset):
        # Show a simple information dialog
        messagebox.showinfo("Information", message)

    def run(self):
        # Set the window size and start the Tkinter event loop
        self.root.geometry("300x150")
        self.root.mainloop()

if __name__ == "__main__":
    # Create an instance of the ElevatorSimulator class and run the application
    elevator_simulator = ElevatorSimulator()
    elevator_simulator.run()
