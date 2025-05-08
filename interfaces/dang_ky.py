import tkinter as tk
from tkinter import messagebox

class DangKy:
    def __init__(self, root):
        self.root = root
        self.root.title("Đăng Ký")
        self.root.geometry("1000x600")
        self.root.configure(bg="#f5f5f5")
        self.fade_in()

        self.create_layout()

    def fade_in(self):
        self.root.attributes('-alpha', 0.0)
        alpha = 0.0
        while alpha < 1.0:
            alpha += 0.05
            self.root.attributes('-alpha', alpha)
            self.root.update()
            self.root.after(20)

    def create_layout(self):
        self.header_frame = tk.Frame(self.root, bg="white", height=60, relief="raised", bd=1)
        self.header_frame.pack(fill=tk.X)

        tk.Label(self.header_frame, text="Đăng Ký Tài Khoản", font=("Segoe UI", 18, "bold"), bg="white", fg="#6200EE").pack(padx=20, pady=10, anchor="w")

        self.main_container = tk.Frame(self.root, bg="#f5f5f5")
        self.main_container.pack(fill=tk.BOTH, expand=True)

        self.form_frame = tk.Frame(self.main_container, bg="white", width=400, relief="raised", bd=2)
        self.form_frame.pack(side=tk.LEFT, fill=tk.Y, padx=20, pady=20)

        self.create_register_form()

    def create_register_form(self):
        # Username field
        tk.Label(self.form_frame, text="Tên đăng nhập", font=("Segoe UI", 12), bg="white", fg="#333333").pack(pady=(10, 5))
        self.username_entry = tk.Entry(self.form_frame, font=("Segoe UI", 12), bg="#f5f5f5", fg="#333333", bd=0)
        self.username_entry.pack(pady=(0, 10), padx=20, fill=tk.X)
        tk.Frame(self.form_frame, bg="#6200EE", height=2).pack(padx=20, fill=tk.X)

        # Password field
        tk.Label(self.form_frame, text="Mật khẩu", font=("Segoe UI", 12), bg="white", fg="#333333").pack(pady=(10, 5))
        self.password_entry = tk.Entry(self.form_frame, font=("Segoe UI", 12), bg="#f5f5f5", fg="#333333", bd=0, show="•")
        self.password_entry.pack(pady=(0, 10), padx=20, fill=tk.X)
        tk.Frame(self.form_frame, bg="#6200EE", height=2).pack(padx=20, fill=tk.X)

        # Confirm Password field
        tk.Label(self.form_frame, text="Xác nhận mật khẩu", font=("Segoe UI", 12), bg="white", fg="#333333").pack(pady=(10, 5))
        self.confirm_password_entry = tk.Entry(self.form_frame, font=("Segoe UI", 12), bg="#f5f5f5", fg="#333333", bd=0, show="•")
        self.confirm_password_entry.pack(pady=(0, 20), padx=20, fill=tk.X)
        tk.Frame(self.form_frame, bg="#6200EE", height=2).pack(padx=20, fill=tk.X)

        # Register button
        self.register_button = tk.Button(self.form_frame, text="Đăng ký", font=("Segoe UI", 14, "bold"),
                                        bg="#6200EE", fg="white", bd=0, command=self.register)
        self.register_button.pack(pady=(20, 10), padx=20, fill=tk.X)
        self.add_hover_effect(self.register_button)

        # Login prompt
        tk.Label(self.form_frame, text="Đã có tài khoản?", font=("Segoe UI", 10), bg="white", fg="#333333").pack(pady=5)
        login_link = tk.Label(self.form_frame, text="Đăng nhập", font=("Segoe UI", 10, "underline"), bg="white", fg="#6200EE", cursor="hand2")
        login_link.pack(pady=(0, 20))
        login_link.bind("<Button-1>", self.go_to_login)

    def add_hover_effect(self, widget):
        widget.bind("<Enter>", lambda e: widget.config(bg="#3700B3"))
        widget.bind("<Leave>", lambda e: widget.config(bg="#6200EE"))

    def register(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        confirm_password = self.confirm_password_entry.get()

        # Check if all fields are filled
        if not username or not password or not confirm_password:
            messagebox.showwarning("Cảnh báo", "Vui lòng điền đầy đủ thông tin!")
            return

        # Check if passwords match
        if password != confirm_password:
            messagebox.showerror("Lỗi", "Mật khẩu và xác nhận mật khẩu không khớp!")
            return

        # Save credentials to a file
        with open(".\\credentials.txt", "a") as file:
            file.write(f"{username},{password}\n")

        # Register logic (giả sử đăng ký thành công)
        messagebox.showinfo("Thành công", "Đăng ký thành công!")
        self.root.destroy()
        self.open_login_page()

    def go_to_login(self, event):
        self.root.destroy()
        root = tk.Tk()
        from interfaces.dang_nhap import DangNhap  # Update the import path
        app = DangNhap(root)
        root.mainloop()

    def open_login_page(self):
        # Remove the check for window existence
        root = tk.Tk()
        from interfaces.dang_nhap import DangNhap  # Update the import path
        app = DangNhap(root)
        root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = DangKy(root)
    root.mainloop()
