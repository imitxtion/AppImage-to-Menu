#!/usr/bin/env python3

import os
import sys
import argparse
from pathlib import Path

# Default icon path (relative to the script's location)
DEFAULT_ICON = Path(__file__).parent / "default-icon.png"

def main():
    # Parse arguments
    parser = argparse.ArgumentParser(description="Add .AppImage files to the application launcher menu.")
    parser.add_argument("app_image", help="Path to the .AppImage file")
    parser.add_argument("-n", "--name", help="setup a custom name for the application")
    parser.add_argument("-i", "--icon", help="setup a custom icon path")
    args = parser.parse_args()

    # Validate the AppImage file
    appimage_path = Path(args.app_image)
    if not appimage_path.is_file():
        print(f"Error: File '{args.app_image}' does not exist or is not a valid file.")
        sys.exit(1)

    # Extract the base name of the AppImage file
    app_name = args.name or appimage_path.stem

    # Determine the icon path
    if args.icon:
        icon_path = Path(args.icon)
        if not icon_path.is_file():
            print(f"Error: Icon file '{args.icon}' does not exist.")
            sys.exit(1)
    else: 
        icon_path = "application-x-executable"

    # Define paths for the .desktop file
    desktop_dir = Path.home() / ".local/share/applications"
    desktop_file = desktop_dir / f"{app_name}.desktop"

    # Ensure the directory exists
    desktop_dir.mkdir(parents=True, exist_ok=True)

    # Write the .desktop file
    with open(desktop_file, "w") as f:
        f.write(f"""[Desktop Entry]
Type=Application
Name={app_name}
Icon={icon_path}
Exec={appimage_path}
Categories=Utility;
""")

    # Make the .desktop file executable
    os.chmod(desktop_file, 0o755)

    print(f"Successfully created desktop entry for '{app_name}' at '{desktop_file}'.")

if __name__ == "__main__":
    main()