import tkinter as tk  # Import the tkinter module for GUI creation
from tkinter import messagebox  # Import messagebox from tkinter for displaying messages


def gcd(a, b):
    # Function to compute the Greatest Common Divisor (GCD) using the Euclidean algorithm
    while b != 0:
        c = b
        b = a % b
        a = c
    return a


def calculate():
    # Function to retrieve input values, calculate GCD and LCM, and display the results
    try:
        # Retrieve and convert the input values to integers
        num1 = int(entry_num1.get())
        num2 = int(entry_num2.get())

        # Calculate the GCD
        result = gcd(num1, num2)

        # Calculate the LCM using the formula: LCM = (num1 * num2) // GCD
        lcm = (num1 * num2) // result

        # Display the GCD and LCM in a message box
        messagebox.showinfo("Result",
                            f"The GCD of {num1} and {num2} is {result}\nThe LCM of {num1} and {num2} is {lcm}")
    except ValueError:
        # Handle invalid input (non-integer values)
        messagebox.showerror("Error", "Please enter valid integers for both numbers.")


# Create the main tkinter window
root = tk.Tk()
root.title("GCD and LCM Calculator")  # Set the title of the window

# Set the font for the title label
bold_font = ("Kristen ITC", 20, "bold")

# Create and pack the title label with specified background and foreground colors and font
title_label = tk.Label(root, text="GCD and LCM Calculator", bg="PaleTurquoise", fg="DodgerBlue", font=bold_font)
title_label.pack()

# Create and pack the label for the first number with specified foreground color
label_num1 = tk.Label(root, text="Enter first number:", fg="MidnightBlue")
label_num1.pack(padx=5, pady=5)

# Create and pack the entry field for the first number
entry_num1 = tk.Entry(root)
entry_num1.pack(padx=5, pady=5)

# Create and pack the label for the second number with specified foreground color
label_num2 = tk.Label(root, text="Enter second number:", fg="MidnightBlue")
label_num2.pack(padx=5, pady=5)

# Create and pack the entry field for the second number
entry_num2 = tk.Entry(root)
entry_num2.pack(padx=5, pady=5)

# Create and pack the button to trigger the calculation with specified background color and font
calculate_button = tk.Button(root, text="Calculate GCD And LCM", command=calculate, bg="Lavender",
                             font=("Comic Sans MS", 10))
calculate_button.pack(padx=5, pady=5)

# Run the main tkinter event loop
root.mainloop()
