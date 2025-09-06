import tkinter as tk
from tkinter import messagebox

def schedule_notification():
    try:
        hrs = int(hour_entry.get())
        mins = int(min_entry.get())
        msg = msg_entry.get()

        total_ms = (hrs * 3600 + mins * 60) * 1000  # convert to milliseconds

        if total_ms <= 0:
            messagebox.showerror("Error", "Please enter a valid time!")
            return

        root.after(total_ms, lambda: messagebox.showinfo("Reminder", msg))
        messagebox.showinfo("Scheduled", f"✅ Reminder set for {hrs} hrs {mins} mins from now")

    except ValueError:
        messagebox.showerror("Error", "Please enter numbers for time!")

root = tk.Tk()
root.title("Personalized Notification System")
root.geometry("400x250")

# Labels
tk.Label(root, text="Enter Reminder Message:", font=("Arial", 12)).pack(pady=5)
msg_entry = tk.Entry(root, width=40)
msg_entry.pack(pady=5)

tk.Label(root, text="Set Time (hours & minutes):", font=("Arial", 12)).pack(pady=5)

# Hour and Minute Input
frame = tk.Frame(root)
frame.pack(pady=5)

hour_entry = tk.Entry(frame, width=5)
hour_entry.insert(0, "0")
hour_entry.pack(side="left", padx=5)

tk.Label(frame, text="hrs").pack(side="left")

min_entry = tk.Entry(frame, width=5)
min_entry.insert(0, "1")
min_entry.pack(side="left", padx=5)

tk.Label(frame, text="mins").pack(side="left")

# Button
btn = tk.Button(root, text="Set Reminder", command=schedule_notification, bg="lightblue")
btn.pack(pady=20)

root.mainloop()
