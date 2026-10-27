import tkinter as tk
from tkinter import messagebox
import pandas as pd


# -----------------------------
# Calculate Productivity
# -----------------------------
def calculate_productivity():
    try:
        subject = subject_entry.get().strip()
        duration = float(duration_entry.get())
        focus = float(focus_entry.get())
        energy = float(energy_entry.get())
        distraction = float(distraction_entry.get())

        if not subject:
            messagebox.showerror("Error", "Please enter a subject.")
            return

        if duration <= 0:
            messagebox.showerror("Error", "Duration must be greater than 0.")
            return

        if not (1 <= focus <= 10):
            messagebox.showerror("Error", "Focus must be between 1 and 10.")
            return

        if not (1 <= energy <= 10):
            messagebox.showerror("Error", "Energy must be between 1 and 10.")
            return

        if not (1 <= distraction <= 10):
            messagebox.showerror(
                "Error",
                "Distraction must be between 1 and 10."
            )
            return

        score = (
            focus * 0.5
            + energy * 0.3
            + (10 - distraction) * 0.2
        )

        score = round(score * 10, 2)

        if score >= 80:
            level = "Excellent 🔥"
        elif score >= 60:
            level = "Good 👍"
        elif score >= 40:
            level = "Average 🙂"
        else:
            level = "Low ⚠️"

        result_label.config(
            text=f"Productivity Score: {score}/100\nLevel: {level}"
        )

    except ValueError:
        messagebox.showerror(
            "Error",
            "Please enter valid numbers."
        )


# -----------------------------
# Save Study Session
# -----------------------------
def save_session():
    try:
        subject = subject_entry.get().strip()
        duration = float(duration_entry.get())
        focus = float(focus_entry.get())
        energy = float(energy_entry.get())
        distraction = float(distraction_entry.get())

        if not subject:
            messagebox.showerror("Error", "Please enter a subject.")
            return

        if duration <= 0:
            messagebox.showerror("Error", "Duration must be greater than 0.")
            return

        if not (1 <= focus <= 10):
            messagebox.showerror("Error", "Focus must be between 1 and 10.")
            return

        if not (1 <= energy <= 10):
            messagebox.showerror("Error", "Energy must be between 1 and 10.")
            return

        if not (1 <= distraction <= 10):
            messagebox.showerror(
                "Error",
                "Distraction must be between 1 and 10."
            )
            return

        score = (
            focus * 0.5
            + energy * 0.3
            + (10 - distraction) * 0.2
        )

        score = round(score * 10, 2)

        if score >= 80:
            level = "Excellent"
        elif score >= 60:
            level = "Good"
        elif score >= 40:
            level = "Average"
        else:
            level = "Low"

        new_session = pd.DataFrame([{
            "Subject": subject,
            "Duration": duration,
            "Focus": focus,
            "Energy": energy,
            "Distraction": distraction,
            "Productivity": score,
            "Level": level
        }])

        try:
            old_data = pd.read_csv("data.csv")
            data = pd.concat(
                [old_data, new_session],
                ignore_index=True
            )
        except FileNotFoundError:
            data = new_session

        data.to_csv("data.csv", index=False)

        messagebox.showinfo(
            "Success",
            "Study session saved successfully!"
        )

        # Clear input fields
        subject_entry.delete(0, tk.END)
        duration_entry.delete(0, tk.END)
        focus_entry.delete(0, tk.END)
        energy_entry.delete(0, tk.END)
        distraction_entry.delete(0, tk.END)

        result_label.config(
            text="Session saved! Enter another session."
        )

    except ValueError:
        messagebox.showerror(
            "Error",
            "Please enter valid numbers."
        )


# -----------------------------
# Main Window
# -----------------------------
root = tk.Tk()

root.title("StudyPulse - Smart Study Analyzer")
root.geometry("600x650")
root.resizable(False, False)


# Title
tk.Label(
    root,
    text="📚 StudyPulse",
    font=("Arial", 24, "bold")
).pack(pady=15)

tk.Label(
    root,
    text="Smart Study Session Analyzer",
    font=("Arial", 12)
).pack()


# -----------------------------
# Input Form
# -----------------------------
form = tk.Frame(root)
form.pack(pady=25)

fields = [
    ("Subject:", "subject"),
    ("Duration (minutes):", "duration"),
    ("Focus (1-10):", "focus"),
    ("Energy (1-10):", "energy"),
    ("Distraction (1-10):", "distraction")
]

entries = {}

for row, (label_text, name) in enumerate(fields):

    tk.Label(
        form,
        text=label_text,
        font=("Arial", 11)
    ).grid(
        row=row,
        column=0,
        padx=10,
        pady=10,
        sticky="w"
    )

    entry = tk.Entry(
        form,
        width=30
    )

    entry.grid(
        row=row,
        column=1,
        padx=10,
        pady=10
    )

    entries[name] = entry


subject_entry = entries["subject"]
duration_entry = entries["duration"]
focus_entry = entries["focus"]
energy_entry = entries["energy"]
distraction_entry = entries["distraction"]


# -----------------------------
# Buttons
# -----------------------------
tk.Button(
    root,
    text="Calculate Productivity",
    font=("Arial", 12, "bold"),
    command=calculate_productivity,
    padx=15,
    pady=8
).pack(pady=8)


tk.Button(
    root,
    text="Save Session",
    font=("Arial", 12, "bold"),
    command=save_session,
    padx=25,
    pady=8
).pack(pady=5)


# -----------------------------
# Result
# -----------------------------
result_label = tk.Label(
    root,
    text="Enter your study session",
    font=("Arial", 14, "bold")
)

result_label.pack(pady=25)


# Start application
root.mainloop()