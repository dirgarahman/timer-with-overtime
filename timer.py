import tkinter as tk
from tkinter import messagebox

class CountdownApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Timer Aja 2.0")

        self.running = False
        self.seconds = 0
        self.timer_id = None  # simpan id after untuk cancel jika perlu

        # Input waktu (menit saja)
        tk.Label(root, text="Set Timer (menit):").pack(pady=5)
        self.entry_minutes = tk.Entry(root, justify="center")
        self.entry_minutes.pack(pady=5)
        self.entry_minutes.insert(0, "1")  # default 1 menit

        # Label Timer
        self.label = tk.Label(root, text="00:00:00", font=("Helvetica", 60), fg="black")
        self.label.pack(pady=30)

        # Tombol kontrol
        frame = tk.Frame(root)
        frame.pack(pady=10)

        self.start_btn = tk.Button(frame, text="Start", width=12, command=self.start_timer)
        self.start_btn.grid(row=0, column=0, padx=5)

        self.stop_btn = tk.Button(frame, text="Stop", width=12, command=self.stop_timer)
        self.stop_btn.grid(row=0, column=1, padx=5)

        # Garis horizontal (separator)
        self.separator = tk.Frame(root, height=1, bd=1, relief="sunken", bg="gray")
        self.separator.pack(fill="x", padx=5, pady=5)

        # Copyright
        self.footer = tk.Label(
            root,
            text="©2025 D-Project",
            font=("Arial", 7),
            fg="gray"
        )
        self.footer.pack(side="bottom", pady=5)

    def update_timer(self):
        if self.running:
            # Tentukan tanda & warna
            color = "red" if self.seconds < 0 else "black"
            sign = "-" if self.seconds < 0 else ""

            abs_seconds = abs(self.seconds)
            hours, remainder = divmod(abs_seconds, 3600)
            mins, secs = divmod(remainder, 60)

            # Update teks + warna
            self.label.config(text=f"{sign}{hours:02}:{mins:02}:{secs:02}", fg=color)

            self.seconds -= 1
            # Simpan id after agar bisa cancel
            self.timer_id = self.root.after(1000, self.update_timer)

    def start_timer(self):
        try:
            # --- Auto stop dulu ---
            if self.timer_id:
                self.root.after_cancel(self.timer_id)  # cancel timer lama
            self.running = False

            # Reset ke waktu baru
            menit = int(self.entry_minutes.get())
            self.seconds = menit * 60

            # Update tampilan awal
            hours, remainder = divmod(self.seconds, 3600)
            mins, secs = divmod(remainder, 60)
            self.label.config(text=f"{hours:02}:{mins:02}:{secs:02}", fg="black")

            # Start baru
            self.running = True
            self.update_timer()

        except ValueError:
            messagebox.showerror("Error", "Masukkan angka menit yang valid!")

    def stop_timer(self):
        if self.timer_id:
            self.root.after_cancel(self.timer_id)
        self.running = False

if __name__ == "__main__":
    root = tk.Tk()
    app = CountdownApp(root)
    root.mainloop()
