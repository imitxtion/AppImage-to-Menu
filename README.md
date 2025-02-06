# Add AppImage to Menu

A simple Python script to easily add `.AppImage` files to your application launcher menu.

This script creates a `.desktop` file in `~/.local/share/applications` for your `.AppImage` application, allowing you to launch them from your desktop environment's application menu. It supports custom names and custom icons.

Works seamlessly with most Linux desktop environments.

## Installation
### Step 1: Clone the Repository
Clone this repository to your local machine:
```
git clone https://github.com/imitxtion/AppImage-to-Menu.git && cd AppImage-to-Menu
```
### Step 2: Make the Script Executable 
Ensure the Python script is executable by running: 
```
chmod +x add_img.py
```
### (Optional) Step 3: Move the Script to a Directory in Your PATH 
To make the script globally accessible and more convenient to use, move it to a directory that is part of your system's PATH. Follow the instructions below based on your shell.<br/>

Move the script to `~/.local/bin` (create the directory if it doesn't exist):
```
mkdir -p ~/.local/bin
```
```
mv add_img.py ~/.local/bin/add_img
```
**For `Bash` and `Zsh` Users:**<br/>
1. Ensure `~/.local/bin` is in your PATH:<br/>
Add the following line to your shell configuration file (`~/.bashrc` for Bash or `~/.zshrc` for Zsh):
```
export PATH="$HOME/.local/bin:$PATH"
```
2. Reload your shell configuration:
```
source ~/.bashrc
```
(or `source ~/.zshrc` if you're using **Zsh**).

**For `Fish` Shell Users:**
1. Ensure `~/.local/bin` is in your PATH:<br/>
Add the following line to your Fish configuration file (`~/.config/fish/config.fish`):
```
set -gx PATH $HOME/.local/bin $PATH
```
2. Reload your Fish configuration:
```
source ~/.config/fish/config.fish
```
## Usage
To display the help message and available options:<br/>
`add_img -h`
### Basic usage (Default name and icon):
`add_img app.AppImage`
### Custom Name and/or Icon:
`add_img app.AppImage -n MyApp -i /path/to/icon.png`
