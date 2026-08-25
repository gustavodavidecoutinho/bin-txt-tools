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

def main():
    username = first_run_setup()
    print(f"Hello, {username}! Welcome to bin-txt-tools.")
    print("Your CLI tool is running successfully.")

if __name__ == "__main__":
    main()