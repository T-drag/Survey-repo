import tkinter as tk
from tkinter import messagebox, ttk
import statistics

# Global list to store survey data
survey_data = []

# Admin credentials
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "password"

# Function to validate and submit form
def submit_form():
    name = name_entry.get()
    try:
        age = int(age_entry.get())
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a valid numerical age.")
        return

    sex = sex_var.get()
    ethnicity = ethnicity_var.get()
    disabled = disabled_var.get()
    enjoyment = enjoyment_var.get()
    curiosity = curiosity_var.get()
    science_interest = science_interest_var.get()

    if not name:
        messagebox.showerror("Missing information", "Please enter your name.")
        return

    entry = {
        "name": name,
        "age": age,
        "sex": sex,
        "ethnicity": ethnicity,
        "disabled": disabled,
        "enjoyment": enjoyment,
        "curiosity": curiosity,
        "science_interest": science_interest
    }

    survey_data.append(entry)
    messagebox.showinfo("Thank you", "Your response has been recorded.")
    clear_form()

# Function to clear form fields
def clear_form():
    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    sex_var.set(0)
    ethnicity_var.set(0)
    disabled_var.set(0)
    enjoyment_var.set(0)
    curiosity_var.set(0)
    science_interest_var.set(0)

# Admin login window
def open_admin_panel():
    def authenticate():
        if username_entry.get() == ADMIN_USERNAME and password_entry.get() == ADMIN_PASSWORD:
            admin_window.destroy()
            show_admin_panel()
        else:
            messagebox.showerror("Login failed", "Invalid credentials.")

    admin_window = tk.Toplevel(root)
    admin_window.title("Admin Login")
    admin_window.configure(bg="#ffeeee")
    tk.Label(admin_window, text="Username", bg="#ffeeee").pack()
    username_entry = tk.Entry(admin_window)
    username_entry.pack()
    tk.Label(admin_window, text="Password", bg="#ffeeee").pack()
    password_entry = tk.Entry(admin_window, show="*")
    password_entry.pack()
    tk.Button(admin_window, text="Login", command=authenticate, bg="#ffcccc").pack(pady=5)

# Display admin statistics and responses
def show_admin_panel():
    panel = tk.Toplevel(root)
    panel.title("Admin Panel")
    panel.configure(bg="#e6f2ff")

    tk.Label(panel, text="Survey Responses:", font=("Arial", 12, "bold"), bg="#e6f2ff").pack()
    text = tk.Text(panel, height=15, width=100, bg="#f0f8ff")
    text.pack()

    for entry in survey_data:
        text.insert(tk.END, f"{entry['name']} | Age: {entry['age']} | Sex: {entry['sex']} | Ethnicity: {entry['ethnicity']} | Disabled: {entry['disabled']} | Enjoyment: {entry['enjoyment']} | Curiosity: {entry['curiosity']} | Science Interest: {entry['science_interest']}\n")

    if survey_data:
        ages = [entry['age'] for entry in survey_data]
        avg_age = statistics.mean(ages)
        std_dev = statistics.stdev(ages) if len(ages) > 1 else 0
        women_liked = sum(1 for entry in survey_data if entry['sex'] == 2 and entry['enjoyment'] in [1, 2])

        stats = f"\nAverage Age: {avg_age:.2f}\nStandard Deviation: {std_dev:.2f}\nNumber of women who liked the sculpture: {women_liked}"
        text.insert(tk.END, stats)
    else:
        text.insert(tk.END, "No data available.")

# Main application window
root = tk.Tk()
root.title("Acoustic Sculpture Survey")
root.configure(bg="#f0f0ff")

header = tk.Label(root, text="Welcome to the Acoustic Sculpture Survey!", font=("Helvetica", 16, "bold"), bg="#f0f0ff", fg="#3333cc")
header.grid(row=0, column=0, columnspan=2, pady=10)

# Form UI
fields = [
    ("Name:", "name_entry"),
    ("Age:", "age_entry"),
    ("Sex (1=Male, 2=Female, 3=Other):", "sex_var"),
    ("Ethnicity (1=White, 2=Black, 3=Chinese, 4=Asian, 5=Other):", "ethnicity_var"),
    ("Disabled (1=Yes, 2=No):", "disabled_var"),
    ("Enjoyed sculpture (1-5):", "enjoyment_var"),
    ("Curious how it worked (1-5):", "curiosity_var"),
    ("Want to know more about science (1-5):", "science_interest_var")
]

entries = {}
row = 1
for label_text, var_name in fields:
    tk.Label(root, text=label_text, bg="#f0f0ff").grid(row=row, column=0, sticky="w", padx=10, pady=5)
    if "entry" in var_name:
        entries[var_name] = tk.Entry(root)
        entries[var_name].grid(row=row, column=1, padx=10, pady=5)
    else:
        entries[var_name] = tk.IntVar()
        tk.Entry(root, textvariable=entries[var_name]).grid(row=row, column=1, padx=10, pady=5)
    row += 1

name_entry = entries["name_entry"]
age_entry = entries["age_entry"]
sex_var = entries["sex_var"]
ethnicity_var = entries["ethnicity_var"]
disabled_var = entries["disabled_var"]
enjoyment_var = entries["enjoyment_var"]
curiosity_var = entries["curiosity_var"]
science_interest_var = entries["science_interest_var"]

# Submit and Admin buttons
tk.Button(root, text="Submit", command=submit_form, bg="#ccffcc").grid(row=row, column=0, pady=15)
tk.Button(root, text="Admin Panel", command=open_admin_panel, bg="#ffcccc").grid(row=row, column=1, pady=15)

# Run the application
root.mainloop()