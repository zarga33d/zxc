# System Management Tool

Enhanced System Management Tool - A comprehensive Ubuntu/Debian system management utility with intuitive arrow-key navigation and color-coded interface.

## 🌟 Features

- **System updates and upgrades** - Complete system updates and upgrades
- **Package management and cleanup** - Clean and remove unused packages
- **Security updates** - Security-only updates for better protection
- **System information display** - Detailed system information
- **Disk usage analysis** - Check space and large files
- **Package cache management** - Clean and manage apt cache

## 🎨 User Interface

- **Arrow key navigation** - Use ↑↓ arrow keys to navigate
- **Color-coded interface** - ANSI colors for visual clarity
- **Direct execution** - Press Enter to execute selected command
- **Command display** - Shows actual command next to each option

## 🚀 How to Use

### Quick Start

```bash
# Make sure Python 3 is installed
python3 --version

# Run the tool
python3 zxc.py

# Or using
./zxc.py

# Or if you set up an alias (see installation section):
zxc
```

### Interface Controls

- **Arrow keys (↑↓)**: Navigate between options
- **Enter**: Execute selected command
- **Escape or Ctrl+C**: Exit the program

## 📋 Available Options

### 1. Update & Upgrade System
```bash
sudo apt-get update && sudo apt-get upgrade -y
```
Update package lists and upgrade all installed packages

### 2. Distribution Upgrade
```bash
sudo apt dist-upgrade -y
```
Smart system upgrade with dependency handling

### 3. Full System Upgrade
```bash
sudo apt full-upgrade -y
```
Complete system upgrade with removal of unnecessary packages

### 4. Complete System Cleanup
```bash
sudo apt autoclean && sudo apt autoremove --purge -y && sudo apt clean
```
Comprehensive system cleanup and removal of unused packages

### 5. Fix Broken Packages
```bash
sudo apt --fix-broken install -y && sudo dpkg --configure -a
```
Fix broken packages and installation issues

### 6. Check Available Updates
```bash
apt list --upgradable
```
Display list of packages available for update

### 7. Show System Information
```bash
neofetch || screenfetch || uname -a
```
Display detailed system information

### 8. Security Updates Only
```bash
sudo apt-get update && sudo apt-get upgrade -y --only-upgrade
```
Install security updates only

### 9. Package Cache Info
```bash
sudo du -sh /var/cache/apt/archives && apt-cache stats
```
Package cache storage information

### 10. Disk Usage Analysis
```bash
df -h && sudo du -sh /*
```
Disk usage analysis and large directories

## 🔧 Requirements

### Supported Systems
- **Ubuntu** (all versions)
- **Debian** (all versions)
- **Linux Mint**
- **Any system supporting apt package manager**

### Software Requirements
- **Python 3.6+**
- **sudo privileges** (for administrative commands)

### Compatibility Check
```bash
# Check Python
python3 --version

# Check apt
which apt

# Check sudo
sudo -V
```

## ⚙️ Installation

### 1. Download the file
```bash
# Copy file to project directory
wget https://example.com/zxc.py
# or
curl -O https://example.com/zxc.py
```

### 2. Make executable
```bash
chmod +x zxc.py
```

### 3. Run the tool
```bash
./zxc.py
```

### 4. Optional: Create an alias for easy access
```bash
# Add alias to your shell configuration
nano ~/.zshrc

# Add this line (replace 'path-to' with actual path):
alias zxc='python3 /path-to/zxc.py'

# Reload configuration
source ~/.zshrc

# Now you can run the tool from anywhere with:
zxc
```

**Note**: For bash users, use `~/.bashrc` instead of `~/.zshrc`

## 🛡️ Security

- **Using sudo**: All administrative commands use sudo for protection
- **Error handling**: Comprehensive exception and error handling
- **Permission checking**: Requests sudo password when needed
- **No password storage**: No sensitive data is stored

## 🔍 Troubleshooting

### Common Issues and Solutions

**1. "Command not found" error**
```bash
# Make sure system supports apt
sudo apt --version
```

**2. Permission issues**
```bash
# Check sudo privileges
sudo -l
```

**3. Python issues**
```bash
# Check Python version
python3 --version

# Install Python if not present
sudo apt update && sudo apt install python3
```

## 📝 Important Notes

- **Requires internet connection** for package updates
- **May take time** depending on internet speed and update size
- **Use carefully** with administrative commands
- **Make backups** before major updates

## 🤝 Contributing

We welcome contributions! You can:
- **Report bugs**
- **Suggest new features**
- **Improve code**
- **Update documentation**

## 📄 License

This project is open source and available for free use.

## 👨‍💻 Developer Information

- **Developer**: zarga
- **Creation Date**: 2025-09-25
- **Version**: 2.0

---

**Warning**: Use this tool carefully. Make sure you understand what the commands do before executing them, especially on production systems.
