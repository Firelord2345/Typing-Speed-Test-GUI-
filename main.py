import tkinter as tk
import time

# Initialize global variables
target_text = "The quick brown fox jumps over the lazy dog"
start_time = None
timer_started = False
typed_text = ""

# Create the main window
root = tk.Tk()
root.title("Typing Speed Test")
root.geometry("600x400")

# Display the target text
target_label = tk.Label(root, text=target_text, font=("Arial", 14))
target_label.pack(pady=10)

# Entry field for typing
user_input = tk.Entry(root, font=("Arial", 14), width=40)
user_input.pack(pady=10)

# Label to show typing progress and accuracy
typed_label = tk.Label(root, text="", font=("Arial", 14))
typed_label.pack(pady=10)

# Label to show WPM and accuracy results
result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack(pady=10)

# Label to show remaining text
remaining_label = tk.Label(root, text="", font=("Arial", 14))
remaining_label.pack(pady=10)

# Add keyboard display label
keyboard_label = tk.Label(root, text="", font=("Arial", 14))
keyboard_label.pack(pady=10)

# Function to start the timer when the user starts typing
def start_timer(event):
    global start_time, timer_started
    if not timer_started:
        start_time = time.time()
        timer_started = True

# Function to calculate WPM
def calculate_wpm(typed_text, elapsed_time):
    words = len(typed_text.split())
    wpm = words / (elapsed_time / 60)
    return wpm

# Function to calculate accuracy
def calculate_accuracy(typed_text):
    correct = sum(1 for a, b in zip(typed_text, target_text) if a == b)
    accuracy = (correct / len(target_text)) * 100
    return accuracy

# Function to update the display with correct characters (no red for errors)
def update_display(typed_text):
    typed_label.config(text=f"Typed: {typed_text}", font=("Arial", 14))

    # Handle the remaining text
    if len(typed_text) < len(target_text):
        remaining_text = target_text[len(typed_text):]
        remaining_label.config(text=f"Remaining: {remaining_text}")
    else:
        remaining_label.config(text="")

# Function to check the typing
def check_typing(event):
    global typed_text
    typed_text = user_input.get()

    # Start timer when user begins typing
    start_timer(event)

    # Update the display with the typed text
    update_display(typed_text)

    # If the user has typed the entire target text
    if typed_text == target_text or len(typed_text) >= len(target_text):
        end_time = time.time() - start_time
        accuracy = calculate_accuracy(typed_text)
        wpm = calculate_wpm(typed_text, end_time)
        result_label.config(text=f"Finished! WPM: {wpm:.2f} | Accuracy: {accuracy:.2f}%")
        user_input.config(state="disabled")  # Disable further typing after completion

# Function to update the keyboard display
def update_keyboard():
    # Display the next expected character on the virtual keyboard (for example)
    if len(typed_text) < len(target_text):
        next_char = target_text[len(typed_text)]
        keyboard_label.config(text=f"Next Character: {next_char}")
    else:
        keyboard_label.config(text="")

# Bind the KeyRelease event to check typing on each key release
user_input.bind("<KeyRelease>", lambda event: [check_typing(event), update_keyboard()])

# Start the GUI event loop
root.mainloop()
