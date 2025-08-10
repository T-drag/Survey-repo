# Survey-repo
# Acoustic Sculpture Survey

A simple desktop app for collecting visitor feedback on an **acoustic sculpture** installation. Built with **Python + Tkinter**, it records responses (name, age, demographics, and 1–5 ratings) and includes an **Admin Panel** that displays responses plus basic stats (average age, standard deviation, and a count of women who liked the sculpture).

---

## What this app does 
- Friendly form for name, age, and a few multiple‑choice questions
- 1–5 ratings for enjoyment, curiosity, and interest in science
- **Admin Panel** with a table of responses and basic statistics
- Clean, lightweight UI (no extra installs beyond Python)

---

## How to run it
Choose one of the two options below.

### Option A — Easiest (Download as a ZIP)
1. On the GitHub page, click **Code ▸ Download ZIP**.
2. Unzip the file somewhere on your computer.
3. Open the folder in your file explorer.
4. Double‑click the folder address bar and type `cmd` (Windows) or open **Terminal** (macOS/Linux).
5. Run:
   ```bash
   python survey.py
   ```
   The app window should pop open.

### Option B — For Git users
```bash
git clone https://github.com/<your-username>/acoustic-sculpture-survey.git
cd acoustic-sculpture-survey
python survey.py
```

> If you have multiple versions of Python, try `python3 survey.py` instead.

---

## Requirements
- **Python 3.9+** (Tkinter is included with most standard Python installs)
- Works on Windows, macOS, and Linux

---

## Using the app
1. Launch the app:
   ```bash
   python survey.py
   ```
2. Fill in the form (name required, age must be a whole number).
3. Click **Submit** to record a response.
4. To view responses and stats, click **Admin Panel** and log in with:
   - **Username:** `admin`
   - **Password:** `password`

> Data is stored in memory for the current session only (it resets when you close the app).

---

## Screenshots (add yours)
Place images in `docs/images/` and reference them here:

```
/docs/images/form.png
/docs/images/admin-panel.png
```

---

## Project structure
```
.
├─ survey.py        # Tkinter app: form, admin login, stats
├─ README.md
└─ docs/images/     # (add your screenshots/GIFs)
```

---

## Roadmap
- Save responses to CSV/SQLite
- Replace numeric fields with dropdowns/sliders
- Export stats and responses
- Package app for Windows/macOS (no Python needed to run)

---

## License
MIT

