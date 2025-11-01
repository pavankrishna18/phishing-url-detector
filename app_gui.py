import ttkbootstrap as tb
from ttkbootstrap.constants import *
from tkinter import messagebox
from predict_url import predict_url


class URLCheckerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🔒 Phishing URL Detector")
        self.root.geometry("600x350")

        # Use a modern dark theme (you can try "flatly", "minty", etc.)
        style = tb.Style("cyborg")

        frame = tb.Frame(root, padding=20)
        frame.pack(fill=BOTH, expand=True)

        tb.Label(frame, text="Enter a URL to check:", font=("Arial", 16, "bold")).pack(pady=10)
        self.entry = tb.Entry(frame, font=("Arial", 14), width=50)
        self.entry.pack(pady=5)

        self.button = tb.Button(
            frame, text="Check URL", bootstyle=SUCCESS, width=20, command=self.check_url
        )
        self.button.pack(pady=15)

        # Result label
        self.result_label = tb.Label(frame, text="", font=("Arial", 16, "bold"))
        self.result_label.pack(pady=20)

        # History box
        self.history_box = tb.ScrolledText(frame, height=5, width=60, wrap="word", font=("Arial", 12))
        self.history_box.pack(pady=10)
        self.history_box.insert("end", "History:\n")
        self.history_box.config(state="disabled")

    def check_url(self):
        url = self.entry.get().strip()
        if not url:
            messagebox.showwarning("Input Error", "Please enter a URL")
            return
        result = predict_url(url)

        # Set color
        color = "danger" if result == "Phishing" else "success"
        self.result_label.config(
            text=f"Result: {result}",
            foreground=tb.Style().colors.get(color),
        )

        # Update history
        self.history_box.config(state="normal")
        self.history_box.insert("end", f"{url} → {result}\n")
        self.history_box.config(state="disabled")


if __name__ == '__main__':
    root = tb.Window(themename="cyborg")
    app = URLCheckerApp(root)
    root.mainloop()
