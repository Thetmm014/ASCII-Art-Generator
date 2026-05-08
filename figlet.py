"""
ASCII Art Generator - CLI Tool
================================
A command-line tool that converts text into stylized ASCII art
using 571+ font styles powered by the pyfiglet library.
 
Usage:
    python figlet.py                        # Interactive mode
    python figlet.py -f <font_name>         # Specific font directly
    python figlet.py --font <font_name>     # Specific font (full flag)
 
Examples:
    python figlet.py
    python figlet.py -f slant
    python figlet.py --font banner
 
See fonts.txt in this repo for all 571 available fonts.
 
Author: Lovish Grover
Version: 2.0.0
"""
 
import sys
import random
from pyfiglet import Figlet
 
 
# A curated list of popular fonts shown to user on launch
SAMPLE_FONTS = [
    "slant", "banner", "block", "bubble", "digital",
    "italic", "mirror", "script", "shadow", "speed",
    "starwars", "bell", "cyber", "doom", "graffiti"
]
 
 
def get_available_fonts(figlet: Figlet) -> list:
    """
    Retrieve all available fonts from pyfiglet.
 
    Args:
        figlet (Figlet): An instance of the Figlet class.
 
    Returns:
        list: A sorted list of all available font names.
    """
    return sorted(figlet.getFonts())
 
 
def set_font(figlet: Figlet, font_name: str) -> bool:
    """
    Set a specific font for the Figlet instance.
 
    Args:
        figlet (Figlet): An instance of the Figlet class.
        font_name (str): The name of the font to set.
 
    Returns:
        bool: True if font was set successfully, False otherwise.
    """
    try:
        figlet.setFont(font=font_name)
        return True
    except Exception:
        return False
 
 
def render_text(figlet: Figlet, text: str) -> str:
    """
    Render the given text as ASCII art.
 
    Args:
        figlet (Figlet): A configured Figlet instance.
        text (str): The input text to convert.
 
    Returns:
        str: The rendered ASCII art string.
    """
    return figlet.renderText(text)
 
 
def parse_arguments(args: list) -> tuple:
    """
    Parse and validate command-line arguments.
 
    Args:
        args (list): List of command-line arguments (excluding script name).
 
    Returns:
        tuple: (font_name or None, error_message or None)
    """
    if len(args) == 0:
        return None, None
 
    if len(args) == 2 and args[0] in ("-f", "--font"):
        return args[1], None
 
    return None, "Invalid Usage.\nTry: python figlet.py -f <font_name>\nOr just run: python figlet.py"
 
 
def show_banner():
    """Display the welcome banner and sample fonts on launch."""
    print("=" * 50)
    print("        ASCII Art Generator v2.0")
    print("=" * 50)
    print(f"\nSample fonts: {', '.join(SAMPLE_FONTS)}")
    print("See fonts.txt in this repo for all 571 fonts")
    print("pyfiglet fonts: https://github.com/pwaller/pyfiglet/tree/main/pyfiglet/fonts")
    print("\n" + "-" * 50)
 
 
def choose_font_interactive(figlet: Figlet) -> str:
    """
    Interactively prompt the user to choose a font.
 
    Args:
        figlet (Figlet): An instance of the Figlet class.
 
    Returns:
        str: The selected font name.
    """
    print("\nOptions:")
    print("  [1] Enter a font name")
    print("  [2] Use a random font")
    print("  [3] Exit")
    print()
 
    while True:
        choice = input("Your choice (1/2/3): ").strip()
 
        if choice == "3":
            print("Goodbye!")
            sys.exit(0)
 
        elif choice == "2":
            random_font = random.choice(get_available_fonts(figlet))
            print(f"\nRandom font selected: {random_font}\n")
            return random_font
 
        elif choice == "1":
            font_name = input("Enter font name: ").strip()
            if not font_name:
                print("No font entered. Try again.\n")
                continue
            success = set_font(figlet, font_name)
            if not success:
                print(f"Font '{font_name}' not found. Check fonts.txt for valid names.\n")
                continue
            print(f"\nFont set: {font_name}\n")
            return font_name
 
        else:
            print("Invalid choice. Enter 1, 2, or 3.\n")
 
 
def main():
    """
    Main entry point for the ASCII Art Generator CLI tool.
 
    Supports both CLI flag mode and interactive mode.
    """
    figlet = Figlet()
 
    # Show welcome banner
    show_banner()
 
    # Parse command-line arguments
    font_name, error = parse_arguments(sys.argv[1:])
 
    if error:
        sys.exit(error)
 
    # Determine font — CLI flag takes priority, else interactive
    if font_name:
        success = set_font(figlet, font_name)
        if not success:
            sys.exit(f"Invalid font: '{font_name}'.\nCheck fonts.txt for valid font names.")
        print(f"\nUsing font: {font_name}\n")
    else:
        selected_font = choose_font_interactive(figlet)
        set_font(figlet, selected_font)
 
    # Get user input
    user_input = input("Input: ").strip()
 
    if not user_input:
        sys.exit("Error: Please enter some text to convert.")
 
    # Render and display ASCII art
    print("\n" + "=" * 50)
    print(render_text(figlet, user_input))
    print("=" * 50)
 
 
if __name__ == "__main__":
    main()