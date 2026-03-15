# Event Management GUI

A Python-based desktop application for managing events, registrations, and participant data — built with a clean graphical interface using Tkinter.

---

## Features

- **User authentication** — Login and registration system backed by Excel storage
- **Event registration** — Register participants and manage event data
- **PDF reports** — Generate printable registration summaries
- **Audio feedback** — Plays a sound on successful login
- **Data persistence** — All records stored in structured CSV/Excel files

---

## Tech Stack

| Library | Purpose |
|---|---|
| `tkinter` | GUI framework (built-in) |
| `Pillow` | Image handling |
| `fpdf` | PDF generation |
| `pygame` | Audio playback |
| `pandas` | Data management (Excel/CSV) |

---

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/vedantsharma2586/IP-Project.git
cd IP-Project
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the application

```bash
python event_gui.py
```

---

## Usage

1. **Login** using credentials stored in `users.xlsx`, or register a new account.
2. **Browse and register** for available events.
3. **Manage records** — view and update participant data.
4. **Generate a PDF report** for any registration.

---

## Project Structure

```
IP-Project/
├── event_gui.py          # Main application entry point
├── events.xlsx           # Event details
├── registrations.xlsx    # Registration records
├── users.xlsx            # User login credentials
├── logo.png              # Application logo
├── login.mp3             # Login audio feedback
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

---

## Requirements

- Python 3.x
- All dependencies listed in `requirements.txt`

Install everything at once:

```bash
pip install -r requirements.txt
```

> `tkinter` comes bundled with standard Python installations and does not need to be installed separately.

---

## License

This project was developed for educational purposes as part of an IP subject.  
Feel free to use and modify it freely.

---

## Author

**Vedant Sharma**  
📧 arushi.verma10101@gmail.com
