import os
from PIL import Image

def decode_text():
    print("\n--- BINARY DECODER BY Gustavo ---")
    bin_input = input("Paste the whole binary string: \n> ")
    
    # Clean spaces and line breaks
    clean_bin = "".join(bin_input.split())
    
    # Validate if length is a multiple of 8
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
        
    bin_input = input("Paste your binary string (zeros and ones): \n> ")
    clean_bin = "".join(bin_input.split())
    
    print(f"\nTotal bits: {len(clean_bin)}")
    print("[Graphic Result]:\n")
    
    # Draw row by row replacing 1 with a full block and 0 with a space
    for i in range(0, len(clean_bin), width):
        row = clean_bin[i:i+width]
        visual_row = row.replace('1', '█').replace('0', ' ')
        print(visual_row)
    print("-" * 40)

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
            print("Exiting... Goodbye, Gustavo!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()