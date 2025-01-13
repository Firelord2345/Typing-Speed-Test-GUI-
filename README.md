

# Typing Speed Test

This is a Typing Speed Test application built using Python and the Tkinter library. The goal of this app is to help users measure their typing speed (Words Per Minute - WPM) and accuracy while typing a given sentence.

## Features

- **Real-Time Typing Test**: As you type, the app tracks your input and compares it with the target sentence.
- **Words Per Minute (WPM)**: The app calculates your typing speed in terms of words per minute.
- **Accuracy**: It calculates the accuracy of your typing by comparing your input to the target text.
- **Remaining Text Display**: It shows the remaining characters of the target text as you type.
- **Virtual Keyboard Display**: Shows the next expected character to guide your typing.

## Requirements

To run this application, you will need:
- Python 3.x
- Tkinter (usually comes pre-installed with Python)

## Installation

1. Clone or download this repository to your local machine.

   ```bash
   git clone https://github.com/your-username/typing-speed-test.git
   ```

2. Navigate to the project folder.

   ```bash
   cd typing-speed-test
   ```

3. If Tkinter is not installed on your machine, you can install it using the following command (for most systems, Tkinter should already be installed with Python):

   ```bash
   pip install tk
   ```

4. Run the application:

   ```bash
   python main.py
   ```

## How to Use

1. The target text will be displayed at the top of the window.
2. Start typing in the text entry box below the target text.
3. As you type, the application will display:
   - **Your typed text**
   - **Remaining text** to complete the target sentence
   - **Next expected character** on the virtual keyboard display
4. The timer starts as soon as you type the first character.
5. Once you complete typing the target sentence, the application will:
   - Display your **WPM** (Words Per Minute)
   - Show your **accuracy** as a percentage
   - Disable the input field to prevent further typing

## Results

After completing the sentence, the results are displayed as:
- **WPM**: Words per minute based on your typing speed.
- **Accuracy**: The percentage of correctly typed characters compared to the target text.

![Screenshot 2025-01-13 205038](https://github.com/user-attachments/assets/08d50a11-f55c-4b9c-8ac5-070365923f66)


## Example

```plaintext
The quick brown fox jumps over the lazy dog
```

When you start typing, the app tracks your input and gives you real-time feedback. Once you finish typing the entire sentence, the app will display your WPM and accuracy.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- The app is built using the **Tkinter** library in Python for the graphical user interface.
- The target sentence used in the app is a famous pangram that contains every letter of the English alphabet: **"The quick brown fox jumps over the lazy dog."**

---

