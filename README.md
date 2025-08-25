# Custom Timer

A Python countdown timer with:

- Overtime tracking (numbers go negative)
- Auto reset on Start button
- Red color display when overtime
- Input in minutes only
- Copyright © 2025 Dirga Rahman

## Usage

1. Run `timer.py` with Python 3.13+
2. Enter the number of minutes
3. Click **Start** to begin countdown
4. Click **Stop** to pause

## Convert to .exe (Windows)

To make a standalone executable:

1. Make sure Python and pip are installed.
2. Install PyInstaller:
   ```bash
   pip install pyinstaller
   ```
3. Open a terminal (PowerShell or CMD) in the project folder.
4. Run PyInstaller:
   ```bash
   python -m pyinstaller --onefile --noconsole timer.py
   ```
   - `--onefile` → creates a single executable file  
   - `--noconsole` → hides the terminal window  

5. After completion, check the `dist` folder.  
6. Your executable is `dist/timer.exe`, ready to run on any Windows machine.

## Notes

- Each time you click Start, the timer automatically stops, resets, and starts from the new input.  
- Overtime numbers appear in **red**.  
- Input in **minutes only**. You can enter values greater than 60; it will automatically convert to hours and minutes in the display.
