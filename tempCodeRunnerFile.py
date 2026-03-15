import tkinter as tk
from tkinter import messagebox, simpledialog
from PIL import Image, ImageTk
import csv, os, datetime
from fpdf import FPDF
import pygame
import json

# Constants
EVENTS_FILE = "events.csv"
REGISTRATIONS_FILE = "registrations.csv"
USERS_FILE = "users.csv"
LOGIN_SOUND = "login.mp3"
LOGO_FILE = "logo.png"

# Initialize CSV files if not present
def initialize_files():
    if not os.path.exists(EVENTS_FILE):
        with open(EVENTS_FILE, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Event ID", "Event Name", "Date", "Venue", "Max Participants", "Teacher In-Charge"])
    if not os.path.exists(REGISTRATIONS_FILE):
        with open(REGISTRATIONS_FILE, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Registration ID", "Student Name", "Class", "Event ID", "student_house_name","student_phone_no", "Registration Date"])
    if not os.path.exists(USERS_FILE):
        with open(USERS_FILE, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Username", "Password", "Role"])
            writer.writerow(["admin", "pass2008", "Authority"])
            writer.writerow(["user", "pass123", "User"])

def generate_registration_id():
    with open(REGISTRATIONS_FILE, "r") as f:
        reader = csv.reader(f)
        next(reader)
        count = sum(1 for _ in reader)
    return f"REG{count + 1:04}"

def validate_login(username, password):
    with open(USERS_FILE, "r") as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            if row[0] == username and row[1] == password:
                return row[2]
    return None

class EventApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Event Management System")
        self.root.configure(bg="#222222")
        self.username = ""
        self.role = ""
        self.logo = None

        try:
            image = Image.open(LOGO_FILE)
            image = image.resize((100, 100))
            self.logo = ImageTk.PhotoImage(image)
        except Exception as e:
            print("Logo not found or invalid.")

        pygame.mixer.init()
        self.login_screen()

    def play_login_sound(self):
        if os.path.exists(LOGIN_SOUND):
            pygame.mixer.music.load(LOGIN_SOUND)
            pygame.mixer.music.play()

    def login_screen(self):
        self.clear_screen()
        if self.logo:
            tk.Label(self.root, image=self.logo, bg="#222222").pack(pady=10)

        tk.Label(self.root, text="Login", font=("Arial", 18, "bold"), bg="#222222", fg="white").pack(pady=10)
        tk.Label(self.root, text="Username:", bg="#222222", fg="white").pack()
        self.username_entry = tk.Entry(self.root, bg="#444", fg="white")
        self.username_entry.pack()

        tk.Label(self.root, text="Password:", bg="#222222", fg="white").pack()
        self.password_entry = tk.Entry(self.root, show="*", bg="#444", fg="white")
        self.password_entry.pack()

        tk.Button(self.root, text="Login", command=self.login, bg="#00b894", fg="white").pack(pady=10)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        role = validate_login(username, password)

        if role:
            self.username = username
            self.role = role
            self.play_login_sound()
            self.main_menu()
        else:
            messagebox.showerror("Login Failed", "Invalid credentials!")

    def main_menu(self):
        self.clear_screen()

        if self.logo:
            tk.Label(self.root, image=self.logo, bg="#222222").pack(pady=10)

        tk.Label(self.root, text=f"Welcome {self.username} ({self.role})", font=("Arial", 14), bg="#222222", fg="white").pack(pady=10)
        tk.Button(self.root, text="View Events", command=self.view_events, bg="#0984e3", fg="white").pack(pady=5)
        tk.Button(self.root, text="Register for Event", command=self.register_event, bg="#00cec9", fg="white").pack(pady=5)
        tk.Button(self.root, text="Delete Registration", command=self.delete_registration, bg="#fab1a0", fg="black").pack(pady=5)
        tk.Button(self.root, text="View Registrations", command=self.view_registrations, bg="#81ecec", fg="black").pack(pady=5)
        


        if self.role == "Authority":
            tk.Button(self.root, text="Add Event", command=self.add_event, bg="#6c5ce7", fg="white").pack(pady=5)
            tk.Button(self.root, text="Edit Event", command=self.edit_event, bg="#fd79a8", fg="white").pack(pady=5)
            tk.Button(self.root, text="Delete Event", command=self.delete_event, bg="#d63031", fg="white").pack(pady=5)
            tk.Button(self.root, text="Generate Certificate", command=self.generate_certificate, bg="#e17055", fg="white").pack(pady=5)
            


        tk.Button(self.root, text="Logout", command=self.login_screen, bg="#636e72", fg="white").pack(pady=20)

    def view_events(self):
        self.clear_screen()
        if self.logo:
            tk.Label(self.root, image=self.logo, bg="#222222").pack(pady=10)
        with open(EVENTS_FILE, "r") as f:
            reader = csv.reader(f)
            for row in reader:
                tk.Label(self.root, text=" | ".join(row), bg="#222222", fg="white").pack()
        tk.Button(self.root, text="Back", command=self.main_menu, bg="#636e72", fg="white").pack(pady=10)

    def register_event(self):
        event_id = simpledialog.askstring("Register", "Enter Event ID to register for:")
        student_class = simpledialog.askstring("Register", "Enter Your Class:")
        student_name = simpledialog.askstring("Register", "Enter Your Name:")
        student_house_name= simpledialog.askstring("Register","Enter Your House Name:")
        student_phone_no= simpledialog.askstring("Register","Enter Your Phone No.:")

        if not event_id or not student_class or not student_name or not student_house_name or not student_phone_no:
            messagebox.showwarning("Error", "Missing information")
            return

        event_exists, max_participants, current_reg = False, 0, 0
        with open(EVENTS_FILE, "r") as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                if row[0] == event_id:
                    event_exists = True
                    max_participants = int(row[4])
                    break

        if not event_exists:
            messagebox.showerror("Error", "Event ID not found!")
            return

        with open(REGISTRATIONS_FILE, "r") as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                if row[3] == event_id:
                    current_reg += 1

        if current_reg >= max_participants:
            messagebox.showinfo("Full", "Event registration is full.")
            return

        reg_id = generate_registration_id()
        reg_date = datetime.datetime.now().strftime("%d-%m-%Y")

        with open(REGISTRATIONS_FILE, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([reg_id, student_name, student_class, event_id, student_house_name, student_phone_no, reg_date])
        messagebox.showinfo("Registered", f"Registration successful! ID: {reg_id}")

    def delete_registration(self):
        reg_id = simpledialog.askstring("Delete Registration", "Enter Registration ID to delete:")
        if not reg_id:
            return

        updated_rows = []
        deleted = False

        with open(REGISTRATIONS_FILE, "r") as f:
            reader = csv.reader(f)
            headers = next(reader)
            updated_rows.append(headers)
            for row in reader:
                if row[0] != reg_id:
                    updated_rows.append(row)
                else:
                    deleted = True

        if deleted:
            with open(REGISTRATIONS_FILE, "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerows(updated_rows)
            messagebox.showinfo("Deleted", f"Registration ID {reg_id} has been deleted.")
        else:
            messagebox.showerror("Error", f"No registration found with ID {reg_id}.")

    def view_registrations(self):
        self.clear_screen()
        if self.logo:
            tk.Label(self.root, image=self.logo, bg="#222222").pack(pady=10)

        tk.Label(self.root, text="Registrations", font=("Arial", 14, "bold"), bg="#222222", fg="white").pack(pady=10)

        frame = tk.Frame(self.root, bg="#222222")
        frame.pack(expand=True, fill="both", padx=10)

        canvas = tk.Canvas(frame, bg="#222222", highlightthickness=0)
        scrollbar = tk.Scrollbar(frame, orient="vertical", command=canvas.yview)
        scroll_frame = tk.Frame(canvas, bg="#222222")

        scroll_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=scroll_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        try:
            with open(REGISTRATIONS_FILE, "r") as f:
                reader = csv.reader(f)
                for i, row in enumerate(reader):
                    bg_color = "#2d3436" if i % 2 == 0 else "#353b48"
                    tk.Label(scroll_frame, text=" | ".join(row), bg=bg_color, fg="white", anchor="w").pack(fill="x", pady=1)
        except Exception as e:
            messagebox.showerror("Error", f"Could not read registrations: {e}")

        tk.Button(self.root, text="Back", command=self.main_menu, bg="#636e72", fg="white").pack(pady=10)

    def add_event(self):
        eid = simpledialog.askstring("Event", "Enter Event ID:")
        name = simpledialog.askstring("Event", "Event Name:")
        date = simpledialog.askstring("Event", "Date (DD-MM-YYYY):")
        venue = simpledialog.askstring("Event", "Venue:")
        maxp = simpledialog.askstring("Event", "Max Participants:")
        teacher= simpledialog.askstring("Event","Teacher In-Charge")

        if not all([eid, name, date, venue, maxp, teacher]):
            messagebox.showwarning("Missing", "All fields are required.")
            return

        with open(EVENTS_FILE, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([eid, name, date, venue, maxp, teacher])
        messagebox.showinfo("Success", "Event added!")

    def edit_event(self):
        eid = simpledialog.askstring("Edit", "Enter Event ID to edit:")
        updated_rows, found = [], False
        with open(EVENTS_FILE, "r") as f:
            reader = csv.reader(f)
            headers = next(reader)
            updated_rows.append(headers)
            for row in reader:
                if row[0] == eid:
                    name = simpledialog.askstring("Edit", "New Name:")
                    date = simpledialog.askstring("Edit", "New Date:")
                    venue = simpledialog.askstring("Edit", "New Venue:")
                    maxp = simpledialog.askstring("Edit", "New Max Participants:")
                    teacher= simpledialog.askstring("Event","Teacher In-Charge")
                    updated_rows.append([eid, name, date, venue, maxp, teacher])
                    found = True
                else:
                    updated_rows.append(row)

        if found:
            with open(EVENTS_FILE, "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerows(updated_rows)
            messagebox.showinfo("Updated", "Event updated!")
        else:
            messagebox.showerror("Error", "Event not found!")

    def delete_event(self):
        eid = simpledialog.askstring("Delete", "Enter Event ID to delete:")
        updated, deleted = [], False
        with open(EVENTS_FILE, "r") as f:
            reader = csv.reader(f)
            for row in reader:
                if row[0] != eid:
                    updated.append(row)
                else:
                    deleted = True

        if deleted:
            with open(EVENTS_FILE, "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerows(updated)
            messagebox.showinfo("Deleted", "Event deleted.")
        else:
            messagebox.showerror("Error", "Event not found!")

    



    def generate_certificate(self):
        reg_id = simpledialog.askstring("Certificate", "Enter Registration ID:")
        student_info, event_info = None, None

        with open(REGISTRATIONS_FILE, "r") as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                if row[0] == reg_id:
                    student_info = row
                    break

        if not student_info:
            messagebox.showerror("Error", "Registration ID not found.")
            return

        with open(EVENTS_FILE, "r") as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                if row[0] == student_info[3]:
                    event_info = row
                    break

        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", "B", 16)
        pdf.cell(200, 10, txt="Certificate of Participation", ln=True, align="C")
        pdf.set_font("Arial", "", 12)
        pdf.ln(20)
        pdf.cell(200, 10, txt=f"This is to certify that {student_info[1]}", ln=True, align="C")
        pdf.cell(200, 10, txt=f"of Class {student_info[2]} participated in", ln=True, align="C")
        pdf.cell(200, 10, txt=f"'{event_info[1]}' held on {event_info[2]} at {event_info[3]}.", ln=True, align="C")
        pdf.cell(200, 10, txt=f"Teacher In-Charge: {event_info[5]}", ln=True, align="C")
        pdf.ln(30)
        pdf.cell(200, 10, txt="School Event Committee", ln=True, align="C")

        filename = f"certificate_{reg_id}.pdf"
        pdf.output(filename)
        messagebox.showinfo("Generated", f"Certificate saved as {filename}")

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

# Start App
initialize_files()
root = tk.Tk()
root.geometry("400x550")
app = EventApp(root)
root.mainloop()