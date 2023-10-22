import sys
import os
import shutil
import random

# Function to get the file path from command-line arguments or use a default
def get_file_path():
    if len(sys.argv) == 2:
        user_input = sys.argv[1]
    else:
        user_input = ""
    return user_input

# Function to validate the user input file path
def valid_path(file_path):
    validity = True
    comment = ""
    if not os.path.exists(file_path):
        comment = "File does not exist"
        validity = False
    return comment, validity

# Function to open and read the content of a text file
def open_and_read_file(file_path, validity, comment):
    if validity:
        try:
            with open(file_path, "r") as file_data:
                return file_data.read()
        except Exception as e:
            return f"Error opening or reading the file: {comment}"
    else:
        return f"Error: {comment}"

# Function to create a design element (line of underscores) based on terminal width
def line(char):
    try:
        width, column = shutil.get_terminal_size(fallback=(80, 24))
        print(char * width)
    except:
        pass

# Applies color to text
def apply_color(clr, message):
    color_list = ['GREEN', 'YELLOW', 'CYAN', 'MAGENTA']
    index = random.randint(0, len(color_list) - 1)
    if clr == "random" and index is not None:
        color = color_list[index]
    else:
        color = clr.upper()
    try:
        from colorama import Fore, Style
        return f"{getattr(Fore, color)}{message}{Style.RESET_ALL}"
    except:
        return message

# Main function to execute the program
def main():
    user_input = get_file_path()
    comment, validity = valid_path(user_input)
    file_content = open_and_read_file(user_input, validity, comment)
    if user_input.lower() != "" and validity:
        print(apply_color("random", f"{user_input}"))
        line("_")
        print(apply_color("white", file_content))
        line("‾")
    elif user_input == "" and not validity:
        print(apply_color("random", "reedr v1.0"))
        print("Usage: python3 readit.py [file path]")
    else:
        print(apply_color("random", "reedr v1.0"))
        print(f"Error: {comment}")
        print("Usage: python3 readit.py [file path]")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
    except Exception as e:
        print(str(e))
        sys.exit()