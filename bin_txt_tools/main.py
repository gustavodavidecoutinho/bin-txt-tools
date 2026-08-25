import os
import sys

def decode_text():
    print("\n=== BINARY DECODER ===")
    print("Instructions: Paste your binary text below.")
    print("When finished, press Enter on a new line and type 'END' (or press Ctrl+D):")
    print("-" * 60)
    
    lines = []
    while True:
        try:
            line = input()
            if line.strip() == "END":
                break
            lines.append(line)
        except EOFError:
            break
            
    bin_input = "".join(lines)
    clean_bin = "".join(bin_input.split())
    
    if len(clean_bin) % 8 != 0:
        print(f"\nWarning: The total number of bits ({len(clean_bin)}) is not a multiple of 8. The message might get cut off.")
        
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
    print("-" * 60)

def decode_image():
    print("\n=== IMAGE / PIXEL ART DECODER ===")
    print("Instructions:")
    print("1. Enter the width of the grid (e.g., 23 for Arecibo).")
    print("2. Paste your binary block (zeros and ones).")
    print("3. Press Enter, type 'END' on a new line, and press Enter again to generate.")
    print("-" * 60)
    
    try:
        width = int(input("What is the width (number of pixels per row)? \n> "))
    except ValueError:
        print("Invalid width. It has to be a whole number.")
        return
        
    print("\nPaste your binary string now (type 'END' on a new line when done):")
    lines = []
    while True:
        try:
            line = input()
            if line.strip() == "END":
                break
            lines.append(line)
        except EOFError:
            break
            
    bin_input = "".join(lines)
    clean_bin = "".join(bin_input.split())
    
    print(f"\nTotal bits processed: {len(clean_bin)}")
    print(f"[Graphic Result for Width {width}]:\n")
    
    for i in range(0, len(clean_bin), width):
        row = clean_bin[i:i+width]
        visual_row = row.replace('1', '█').replace('0', ' ')
        print(visual_row)
    print("-" * 60)

def main():
    while True:
        print("\n=== MULTIFUNCTION DECODER TOOL ===")
        print("1. Decode Binary to Text")
        print("2. Decode Binary to Image / Pixel Matrix")
        print("3. Exit")
        
        choice = input("Choose an option (1, 2, or 3): \n> ").strip()
        
        if choice == '1':
            decode_text()
        elif choice == '2':
            decode_image()
        elif choice == '3':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()