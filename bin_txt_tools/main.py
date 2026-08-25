import os
import sys

def decode_text():
    print("\n=== BINARY DECODER ===")
    filepath = input("Enter the path to the text file containing binary data (e.g., bin.txt): \n> ").strip()
    
    if os.path.exists(filepath):
        with open(filepath, "r", encoding="utf-8") as f:
            bin_input = f.read()
    else:
        bin_input = filepath
        
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
    print("-" * 60)

def decode_image():
    print("\n=== IMAGE / PIXEL ART DECODER ===")
    
    try:
        width = int(input("What is the width (number of pixels per row, e.g., 23)? \n> "))
    except ValueError:
        print("Invalid width. It has to be a whole number.")
        return
        
    filepath = input("Enter the path to the text file with the binary matrix (e.g., arecibo.txt): \n> ").strip()
    
    if not os.path.exists(filepath):
        print(f"Error: File '{filepath}' not found.")
        print("Tip: Create a file named 'arecibo.txt' on your Desktop, paste your binary block there, and point to it.")
        return
        
    with open(filepath, "r", encoding="utf-8") as f:
        bin_input = f.read()
        
    clean_bin = "".join(bin_input.split())
    
    print(f"\nTotal bits processed: {len(clean_bin)}")
    print(f"[Graphic Result for Width {width}]:\n")
    
    for i in range(0, len(clean_bin), width):
        row = clean_bin[i:i+width]
        visual_row = row.replace('1', '█').replace('0', ' ')
        print(visual_row)
    print("-" * 60)

def encode_file_to_binary():
    print("\n=== FILE TO BINARY ENCODER ===")
    filepath = input("Enter the path to the text or ASCII file you want to encode (e.g., text.txt): \n> ").strip()
    
    if not os.path.exists(filepath):
        print(f"Error: File '{filepath}' not found.")
        print("Tip: Create a text file on your Desktop, put your text or ASCII art inside, and point to it.")
        return
        
    with open(filepath, "r", encoding="utf-8") as f:
        file_content = f.read()
        
    if not file_content:
        print("The file is empty.")
        return
        
    # Converte cada caractere do ficheiro (incluindo quebras de linha e espaços) para binário de 8 bits
    binary_result = ' '.join(format(ord(char), '08b') for char in file_content)
    
    print(f"\nTotal characters encoded: {len(file_content)}")
    print("\n[Binary Result]:")
    print(binary_result)
    print("-" * 60)

def main():
    while True:
        print("\n=== MULTIFUNCTION DECODER & ENCODER TOOL ===")
        print("1. Decode Binary to Text")
        print("2. Decode Binary to Image / Pixel Matrix")
        print("3. Encode Text/ASCII File to Binary")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): \n> ").strip()
        
        if choice == '1':
            decode_text()
        elif choice == '2':
            decode_image()
        elif choice == '3':
            encode_file_to_binary()
        elif choice == '4':
            print(f"Exiting... Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()