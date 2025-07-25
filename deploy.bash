#!/bin/bash

find_venv() {
    local dir="$PWD"
    while [ "$dir" != "/" ]; do
        if [ -d "$dir/venv" ]; then
            echo "$dir/venv"
            return 0
        fi
        dir=$(dirname "$dir")
    done
    return 1
}

venv_folder=$(find_venv)
if [ -z "$venv_folder" ]; then
    echo "no venv found."
    exit 1
fi

echo "venv found at at: $venv_folder"

source "$venv_folder/Scripts/activate"

echo "Activated venv."

echo "Building app..."
pyinstaller --onefile --add-data "Tesseract-OCR:Tesseract-OCR" main.py

echo "Build complete."