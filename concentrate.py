#!/usr/bin/env python3

import tkinter as tk
from tkinter import messagebox
import os
import subprocess  # To run the Telegram kill command

# Predefined list of websites to block/unblock
websites = [
    "facebook.com",
    "www.facebook.com",
    "linkedin.com",
    "www.linkedin.com",
    "9gag.com",
    "www.9gag.com",
    "netflix.com",
    "www.netflix.com",
    "instagram.com",
    "www.instagram.com",
    "youtube.com",
    "www.youtube.com", 
    "www.online-go.com", 
    "online-go.com",
    "gomagic.org", 
    "www.gomagic.org"
]

hosts_file = "/etc/hosts"
is_blocked = False  # Track the state of websites being blocked or unblocked

# Function to kill Telegram
def kill_telegram():
    try:
        subprocess.run(
            "kill -9 $(ps aux | grep '/Applications/Telegram.app/Contents/MacOS/Telegram' | grep -v grep | awk '{print $2}')",
            shell=True,
            check=True
        )
        messagebox.showinfo("Success", "Telegram process terminated!")
    except subprocess.CalledProcessError:
        messagebox.showerror("Error", "Failed to terminate Telegram. It might not be running.")

# Function to block websites
def block_websites():
    global is_blocked
    success = False

    if os.name == 'posix':
        try:
            if not is_blocked:
                # Append websites to the /etc/hosts file
                with open(hosts_file, 'a') as file:
                    for website in websites:
                        file.write(f"127.0.0.1 {website}\n")
                        file.write(f"127.0.0.1 www.{website}\n")
                # Kill Telegram
                kill_telegram()
                success = True
                button.config(text="Unblock Websites")
                is_blocked = True
            else:
                # Unblock websites by removing them from /etc/hosts
                with open(hosts_file, 'r') as file:
                    lines = file.readlines()
                with open(hosts_file, 'w') as file:
                    for line in lines:
                        if not any(website in line for website in websites):
                            file.write(line)
                success = True
                button.config(text="Block Websites")
                is_blocked = False
        except PermissionError:
            messagebox.showerror("Error", "Permission denied. Try running as sudo.")
    else:
        messagebox.showerror("Error", "Unsupported OS. This script is for macOS/Linux.")

    if success:
        if is_blocked:
            messagebox.showinfo("Success", "Websites blocked successfully!")
        else:
            messagebox.showinfo("Success", "Websites unblocked successfully!")

# Create the Tkinter UI
root = tk.Tk()
root.title("Website Blocker/Unblocker")

# Informative label
label = tk.Label(root, text="Manage access to distracting websites.")
label.pack(pady=10)

# Block/Unblock button
button = tk.Button(root, text="Block Websites", command=block_websites)
button.pack(pady=20)

# Run the Tkinter loop
root.mainloop()
