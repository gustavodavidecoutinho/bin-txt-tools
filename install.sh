#!/bin/bash

PACKAGE_NAME="bin-txt-tools"
REPO_URL="https://github.com/gustavodavidecoutinho/bin-txt-tools.git"

echo "=== Installing $PACKAGE_NAME Package Suite ==="

if ! command -v pip3 &> /dev/null; then
    echo "Error: pip3 is required to install this package."
    exit 1
fi

echo "Installing package locally from repository..."
pip3 install --user git+$REPO_URL

echo -e "\nDONE! Now try running '$PACKAGE_NAME' to see if it works."
echo "If your shell says 'command not found', make sure your Python user 
bin directory is in your PATH."
echo "You can add it permanently using:"
echo 'echo '\''export PATH="$PATH:$HOME/Library/Python/$(python3 -c 
"import sys; 
print(f\"{sys.version_info.major}.{sys.version_info.minor}\")")/bin"'\'' 
>> ~/.zshrc && source ~/.zshrc'
