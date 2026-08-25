import os
import json

CONFIG_FILE = os.path.expanduser("~/.bin_txt_tools_config.json")

def load_config():
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return {}
    return {}

def save_config(config):
    try:
        with open(CONFIG_FILE, "w", encoding="utf-8") as f:
            json.dump(config, f, indent=4)
    except Exception as e:
        print(f"Error saving config: {e}")

def first_run_setup():
    config = load_config()
    if "username" not in config:
        print("\n=== WELCOME TO BIN-TXT-TOOLS ===")
        print("The ultimate open-source binary & text CLI suite.")
        name = input("Enter your name for display purposes only (or just press Enter to skip):\n> ").strip()
        config["username"] = name if name else "Traveler"
        save_config(config)
        print(f"Setup complete! Welcome, {config['username']}.\n")
    return config["username"]

def decode_text():
    print("\n--- BINARY DECODER ---")
    bin_input = input("Paste the whole binary string: \n> ")
    
    clean_bin = "".join(bin_input.split())
    
    if len(clean_bin) % 8 != 0:
        print(f"Warning: The total number of bits ({len(clean_bin)}) is not a multiple of 8. The message might get cut off.")
        
    final_text = ""
    for i in range(0, len(clean_bin) - 7, 8):
        byte = clean_bin[i:i+8]
        try:
            char = chr(int(byte, 2))
            final_text += char
        except ValueError:
            final_text += "?"
            
    print("\n[Text Result]:")
    print(final_text)
    print("-" * 40)

def decode_image():
    print("\n--- IMAGE / PIXEL ART DECODER ---")
    print("You need to specify the width of the grid (e.g., 23 for Arecibo).")
    
    try:
        width = int(input("What is the width (number of pixels per row)? \n> "))
    except ValueError:
        print("Invalid width. It has to be a whole number.")
        return
        
    print("Paste your binary string (zeros and ones). Press Enter twice when finished:")
    lines = []
    while True:
        try:
            line = input()
            if not line.strip():
                break
            lines.append(line.strip())
        except EOFError:
            break
            
    bin_input = "".join(lines)
    clean_bin = "".join(bin_input.split())
    
    print(f"\nTotal bits: {len(clean_bin)}")
    print("[Graphic Result]:\n")
    
    for i in range(0, len(clean_bin), width):
        row = clean_bin[i:i+width]
        visual_row = row.replace('1', '█').replace('0', ' ')
        print(visual_row)
    print("-" * 40)

def text_to_binary():
    print("\n--- TEXT TO BINARY ENCODER ---")
    text = input("Enter text to encode: \n> ")
    binary = ' '.join(format(ord(char), '08b') for char in text)
    print(f"\n[Binary Result]:\n{binary}")
    print("-" * 40)

def main():
    username = first_run_setup()
    
    while True:
        print(f"\n=== MULTIFUNCTION DECODER TOOL (User: {username}) ===")
        print("1. Decode Binary to Text")
        print("2. Decode Binary to Image / Pixel Matrix")
        print("3. Encode Text to Binary")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): \n> ").strip()
        
        if choice == '1':
            decode_text()
        elif choice == '2':
            decode_image()
        elif choice == '3':
            text_to_binary()
        elif choice == '4':
            print(f"Exiting... Goodbye, {username}!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()