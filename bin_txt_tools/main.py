#!/usr/bin/env python3
import os
import json

CONFIG_DIR = os.path.expanduser("~/.config/bin-txt-tools")
CONFIG_FILE = os.path.join(CONFIG_DIR, "config.json")

def load_config():
    if not os.path.exists(CONFIG_FILE):
        return {}
    try:
        with open(CONFIG_FILE, "r") as f:
            return json.load(f)
    except:
        return {}

def save_config(config):
    if not os.path.exists(CONFIG_DIR):
        os.makedirs(CONFIG_DIR)
    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f)

def first_run_setup():
    config = load_config()
    if "username" not in config:
        print("\n=== WELCOME TO BIN-TXT-TOOLS ===")
        print("The ultimate open-source binary & text CLI suite.")
        name = input("Enter your name for display purposes only (or just 
press Enter to skip): \n> ").strip()
        config["username"] = name if name else "Traveler"
        save_config(config)
        print(f"Setup complete! Welcome, {config['username']}.\n")
    return config["username"]

# --- DECODERS ---
def decode_text():
    print("\n--- DECODE BINARY TO TEXT ---")
    bin_input = input("Paste the binary string: \n> ")
    clean_bin = "".join(bin_input.split())
    
    if len(clean_bin) % 8 != 0:
        print(f"Warning: Total bits ({len(clean_bin)}) is not a multiple 
of 8. Might be cut off.")
        
    final_text = ""
    for i in range(0, len(clean_bin) - 7, 8):
        byte = clean_bin[i:i+8]
        try:
            final_text += chr(int(byte, 2))
        except ValueError:
            final_text += "?"
    print(f"\n[Result]:\n{final_text}\n" + "-" * 40)

def decode_image():
    print("\n--- DECODE BINARY TO PIXEL MATRIX ---")
    try:
        width = int(input("Width of the grid (number of pixels per row): 
\n> "))
    except ValueError:
        print("Invalid width.")
        return
    bin_input = input("Paste the binary string: \n> ")
    clean_bin = "".join(bin_input.split())
    
    print(f"\n[Graphic Result]:\n")
    for i in range(0, len(clean_bin), width):
        row = clean_bin[i:i+width]
        print(row.replace('1', '█').replace('0', ' '))
    print("-" * 40)

# --- ENCODERS ---
def encode_text():
    print("\n--- ENCODE TEXT TO BINARY ---")
    text = input("Type the text you want to encode: \n> ")
    binary_result = " ".join(format(ord(char), '08b') for char in text)
    print(f"\n[Binary Result]:\n{binary_result}\n" + "-" * 40)

def encode_image():
    print("\n--- ENCODE PIXEL ART TO BINARY ---")
    print("Type your pixel art row by row. Use '1' for filled, '0' for 
empty.")
    print("Type 'done' when you finish the grid.\n")
    
    rows = []
    while True:
        row = input("Row > ").strip()
        if row.lower() == 'done':
            break
        filtered_row = "".join([c for c in row if c in '01'])
        if filtered_row:
            rows.append(filtered_row)
            
    binary_result = "".join(rows)
    print(f"\n[Binary String Result]:\n{binary_result}")
    print(f"Total bits: {len(binary_result)}\n" + "-" * 40)

# --- UTILITIES ---
def number_base_converter():
    print("\n--- NUMBER BASE CONVERTER ---")
    print("1. Decimal to Binary & Hex")
    print("2. Hexadecimal to Decimal & Binary")
    sub_choice = input("Choose an option (1-2): \n> ").strip()
    
    if sub_choice == '1':
        try:
            dec_val = int(input("Enter decimal number: \n> "))
            print(f"Binary: {bin(dec_val)[2:]}")
            print(f"Hexadecimal: {hex(dec_val)[2:].upper()}")
        except ValueError:
            print("Invalid decimal number.")
    elif sub_choice == '2':
        hex_val = input("Enter hex number (e.g. 4F): \n> ").strip()
        try:
            dec_val = int(hex_val, 16)
            print(f"Decimal: {dec_val}")
            print(f"Binary: {bin(dec_val)[2:]}")
        except ValueError:
            print("Invalid hexadecimal number.")
    print("-" * 40)

def analyze_bits():
    print("\n--- BIT STATS & ANALYSIS ---")
    bin_input = input("Paste the binary string to analyze: \n> ")
    clean_bin = "".join(bin_input.split())
    
    total_bits = len(clean_bin)
    if total_bits == 0:
        print("Empty string provided.")
        return
        
    zeros = clean_bin.count('0')
    ones = clean_bin.count('1')
    others = total_bits - (zeros + ones)
    
    print(f"\n[Analysis Results]:")
    print(f"- Total Bits: {total_bits}")
    print(f"- Zeros ('0'): {zeros} ({(zeros/total_bits)*100:.2f}%)")
    print(f"- Ones ('1'):  {ones} ({(ones/total_bits)*100:.2f}%)")
    if others > 0:
        print(f"- Invalid characters: {others}")
    print("-" * 40)

def main():
    username = first_run_setup()
    
    while True:
        print(f"\n=== BIN-TXT-TOOLS CLI (User: {username}) ===")
        print("1. Decode Binary to Text")
        print("2. Decode Binary to Pixel Matrix")
        print("3. Encode Text to Binary")
        print("4. Encode Pixel Art to Binary")
        print("5. Number Base Converter (Dec/Hex/Bin)")
        print("6. Bit Stats & Analysis")
        print("7. Exit")
        
        choice = input("Choose an option (1-7): \n> ").strip()
        
        if choice == '1':
            decode_text()
        elif choice == '2':
            decode_image()
        elif choice == '3':
            encode_text()
        elif choice == '4':
            encode_image()
        elif choice == '5':
            number_base_converter()
        elif choice == '6':
            analyze_bits()
        elif choice == '7':
            print(f"Goodbye, {username}!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
