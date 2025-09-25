#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Enhanced System Management Tool
A comprehensive Ubuntu/Debian system management utility
with intuitive arrow-key navigation and color-coded interface.

Features:
- System updates and upgrades
- Package management and cleanup
- Security updates
- System information display
- Disk usage analysis
- Package cache management

Created by: zarga
Date: 2025-09-25
Version: 2.0
"""

import subprocess
import sys

# Windows compatibility for keyboard input
try:
    import msvcrt
    WINDOWS = True
except ImportError:
    import termios
    import tty
    WINDOWS = False

def get_key():
    """Get a single key press from user"""
    if WINDOWS:
        # Windows implementation
        key = msvcrt.getch()
        if key == b'\xe0':  # Arrow key prefix on Windows
            key = msvcrt.getch()
            if key == b'H':  # Up arrow
                return 'up'
            elif key == b'P':  # Down arrow
                return 'down'
        elif key == b'\r':  # Enter key
            return 'enter'
        elif key == b'\x1b':  # Escape key
            return 'escape'
    else:
        # Unix/Linux implementation
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            key = sys.stdin.read(1)
            if key == '\x1b':  # Escape sequence
                key += sys.stdin.read(2)
                if key == '\x1b[A':
                    return 'up'
                elif key == '\x1b[B':
                    return 'down'
            elif key == '\r' or key == '\n':
                return 'enter'
            elif key == '\x1b':
                return 'escape'
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return None

def display_menu(options, selected):
    """Display enhanced menu with arrow and improved formatting"""
    print("\033[1;36m" + "System Management Tool" + "\033[0m")  # Cyan title
    print("=" * 60)
    
    for i, (title, command) in enumerate(options):
        if i == selected:
            print(f"\033[1;32m► {i+1:2d}. {title}\033[0m")  # Green arrow and title with command
        else:
            # Extract just the action name from the title (before the bracket)
            action_name = title.split(' [')[0] if ' [' in title else title
            print(f"  {i+1:2d}. {action_name}")
    
    print("\n" + "=" * 60)
    print("\033[1;34mUse ↑↓ arrows to navigate\033[0m")
    print("\033[1;34mPress Enter to execute, Escape to exit\033[0m")

def main():
    """Enhanced menu for comprehensive system management"""
    
    options = [
        ("Update & Upgrade System [sudo apt-get update && sudo apt-get upgrade -y]", "sudo apt-get update && sudo apt-get upgrade -y"),
        ("Distribution Upgrade [sudo apt dist-upgrade -y]", "sudo apt dist-upgrade -y"),
        ("Full System Upgrade [sudo apt full-upgrade -y]", "sudo apt full-upgrade -y"),
        ("Complete System Cleanup [sudo apt autoclean && sudo apt autoremove --purge -y && sudo apt clean]", "sudo apt autoclean && sudo apt autoremove --purge -y && sudo apt clean"),
        ("Fix Broken Packages [sudo apt --fix-broken install -y && sudo dpkg --configure -a]", "sudo apt --fix-broken install -y && sudo dpkg --configure -a"),
        ("Check Available Updates [apt list --upgradable]", "apt list --upgradable"),
        ("Show System Information [neofetch || screenfetch || uname -a]", "neofetch || screenfetch || uname -a"),
        ("Security Updates Only [sudo apt-get update && sudo apt-get upgrade -y --only-upgrade]", "sudo apt-get update && sudo apt-get upgrade -y --only-upgrade $(apt list --upgradable 2>/dev/null | grep -i security | cut -d'/' -f1)"),
        ("Package Cache Info [sudo du -sh /var/cache/apt/archives && apt-cache stats]", "sudo du -sh /var/cache/apt/archives && apt-cache stats"),
        ("Disk Usage Analysis [df -h && sudo du -sh /*]", "df -h && echo '\n--- Large directories ---' && sudo du -sh /* 2>/dev/null | sort -hr | head -10")
    ]
    
    selected = 0
    
    while True:
        # Clear screen and display menu
        print("\033[2J\033[H", end="")  # Clear screen, move cursor to top
        display_menu(options, selected)
        
        # Get user input with timeout to make navigation smoother
        key = get_key()
        
        if key == 'up':
            selected = (selected - 1) % len(options)
        elif key == 'down':
            selected = (selected + 1) % len(options)
        elif key == 'enter':
            command = options[selected][1]
            title = options[selected][0]
            print(f"\n\033[1;35mExecuting: {title}\033[0m")  # Magenta
            print(f"\033[0;33mCommand: {command}\033[0m")    # Yellow
            print("-" * 60)
            
            try:
                # Enhanced command execution with better error handling
                if '&&' in command or '||' in command:
                    result = subprocess.run(command, shell=True, capture_output=False, text=True)
                else:
                    result = subprocess.run(command.split(), capture_output=False, text=True)
                
                print("-" * 60)
                if result.returncode == 0:
                    print(f"\033[1;32m✓ {title} completed successfully\033[0m")  # Green checkmark
                else:
                    print(f"\033[1;31m✗ {title} failed with exit code {result.returncode}\033[0m")  # Red X
                    
            except FileNotFoundError:
                print(f"\033[1;31mError: Command not found. This tool is designed for Ubuntu/Debian systems.\033[0m")
            except KeyboardInterrupt:
                print(f"\n\033[1;33mOperation cancelled by user\033[0m")
            except Exception as e:
                print(f"\033[1;31mError executing command: {e}\033[0m")
            
            print(f"\n\033[1;36mPress Enter to continue...\033[0m")
            input()
            break

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\033[1;36mExiting System Management Tool...\033[0m")
        print("\033[0;32mThank you for using the tool!\033[0m")
        sys.exit(0)