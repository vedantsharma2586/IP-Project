#  Event Management GUI

##  Overview
This project is a Python-based Event Management application with a graphical user interface (GUI).  
It allows users to register for events, manage participant data, generate PDF reports, and play audio feedback.  
Designed as part of an **IP subject project**, it demonstrates integration of multiple Python libraries for real-world functionality.

---

##  Features
-  User-friendly GUI built with **Tkinter**
-  Image handling with **PIL (Pillow)**
-  Event data stored and managed in **CSV/Excel files**
-  PDF generation using **FPDF**
-  Audio playback with **Pygame**
-  Simple login and registration system

---

##  Installation

1. **Clone the repository**
   git clone https://github.com/vedantsharma2586/IP-Project.git
   cd IP-Project

2. **Install dependencies**
   pip install -r requirements.txt

---

##  Usage

Run the main application:
   python event_gui.py

- Login with your credentials (stored in `users.xlsx`).
- Register for events and manage participant data.
- Generate PDF reports for registrations.
- Enjoy audio feedback on login.

---

##  Requirements

The project depends on:
- tkinter (built-in with Python)
- pillow
- fpdf
- pygame
- pandas

Install them all at once:
   pip install -r requirements.txt

---

##  Project Structure

IP-Project/
│
├── event_gui.py          # Main GUI application
├── events.xlsx           # Event details
├── registrations.xlsx    # Registration records
├── users.xlsx            # User login data
├── logo.png              # Application logo
├── login.mp3             # Audio feedback
├── requirements.txt      # Dependencies
└── README.md             # Project documentation

---

##  License
This project is for **educational purposes** (IP subject).  
You may use and modify it freely.

---

##  Credits
Developed by **Vedant Sharma**  
Email: arushi.verma10101@gmail.com
