import tkinter as tk
import time

# Function to start the timer when the user starts typing
def start_timer(event):
    global timer_started  # Declare as global
    if not timer_started:
        global start_time
        start_time = time.time()
        timer_started = True
        update_timer()

# Function to update the timer every 100 ms
def update_timer():
    if timer_started:
        elapsed_time = time.time() - start_time
        minutes = int(elapsed_time // 60)
        seconds = int(elapsed_time % 60)
        timer_label.config(text=f"Time: {minutes:02d}:{seconds:02d}")
        root.after(100, update_timer)  # Continue updating the timer

# Function to check the typing speed and accuracy
def check_typing(event):
    typed_text = user_input.get()
    if len(typed_text) == len(target_text):  # Stop when the length matches
        end_time = time.time() - start_time
        accuracy = calculate_accuracy(typed_text)  # Calculate accuracy
        wpm = calculate_wpm(typed_text, end_time)  # Calculate WPM
        result_label.config(text=f"Finished! WPM: {wpm:.2f} | Accuracy: {accuracy:.2f}%")
        stop_timer()  # Stop the timer when done

    # Highlight mistakes in red and update the display
    update_display(typed_text)

# Function to update the display with correct/incorrect typed portion
def update_display(typed_text):
    correct_part = ""
    incorrect_part = ""
    typed_display = ""
    
    # Compare typed text with target text character by character
    for i in range(len(typed_text)):
        if typed_text[i] == target_text[i]:
            correct_part += typed_text[i]
            typed_display += typed_text[i]
        else:
            incorrect_part += typed_text[i]
            typed_display += typed_text[i]

    # Highlight mistakes in red and correct part in black
    typed_area.delete(1.0, tk.END)  # Clear the previous text
    typed_area.insert(tk.END, typed_display)  # Insert typed text

    # Apply color styling to correct and incorrect parts
    typed_area.tag_add("correct", "1.0", f"1.{len(correct_part)}")
    typed_area.tag_add("incorrect", f"1.{len(correct_part)}", f"1.{len(typed_text)}")

    # Apply red color for incorrect text
    typed_area.tag_config("incorrect", foreground="red")
    typed_area.tag_config("correct", foreground="black")

    remaining_text = target_text[len(typed_text):]
    remaining_label.config(text=f"Remaining: {remaining_text}")

# Function to stop the timer
def stop_timer():
    global timer_started
    timer_started = False

# Function to update the keyboard display
def update_keyboard():
    typed_text = user_input.get()
    next_char = target_text[len(typed_text)] if len(typed_text) < len(target_text) else ""
    keyboard_label.config(text=f"Next letter: {next_char}")

# Function to calculate typing accuracy
def calculate_accuracy(typed_text):
    correct_chars = 0
    for i in range(min(len(typed_text), len(target_text))):
        if typed_text[i] == target_text[i]:
            correct_chars += 1
    accuracy = (correct_chars / len(target_text)) * 100
    return accuracy

# Function to calculate WPM
def calculate_wpm(typed_text, time_taken):
    wpm = (len(typed_text.split()) / (time_taken / 60))
    return wpm

# Setting up the main window
root = tk.Tk()
root.title("Speed Typing Test")

# Target text to type
target_text = "The quick brown fox jumps over the lazy dog."

# Label to show the target text
target_label = tk.Label(root, text=target_text, font=("Arial", 16), wraplength=400)
target_label.pack(pady=10)

# User input field for typing
user_input = tk.Entry(root, font=("Arial", 16), width=40)
user_input.pack(pady=10)
user_input.bind("<KeyPress>", start_timer)  # Start the timer on key press
user_input.bind("<KeyRelease>", lambda event: [check_typing(event), update_keyboard()])  # Check typing on key release

# Timer label
timer_label = tk.Label(root, text="Time: 00:00", font=("Arial", 14))
timer_label.pack(pady=10)

# Result label to display WPM and accuracy
result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack(pady=10)

# Label to show the next letter in the keyboard
keyboard_label = tk.Label(root, text="Next letter: ", font=("Arial", 14))
keyboard_label.pack(pady=10)

# Display for typed text and remaining text
typed_area = tk.Text(root, height=2, width=40, font=("Arial", 14))
typed_area.pack(pady=5)

remaining_label = tk.Label(root, text="Remaining: ", font=("Arial", 14))
remaining_label.pack(pady=5)

# Initialize timer status
timer_started = False

# Run the Tkinter main loop
root.mainloop()
