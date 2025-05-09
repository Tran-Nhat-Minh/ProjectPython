import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os

class DangNhap:
    def __init__(self, root):
        self.root = root
        self.root.title("Đăng Nhập")
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

        tk.Label(self.header_frame, text="Đăng Nhập Hệ Thống", font=("Segoe UI", 18, "bold"), bg="white", fg="#6200EE").pack(side=tk.LEFT, padx=10, pady=10)

        self.main_container = tk.Frame(self.root, bg="#f5f5f5")
        self.main_container.pack(fill=tk.BOTH, expand=True)

        # Form đăng nhập bên trái
        self.form_frame = tk.Frame(self.main_container, bg="white", width=400, relief="raised", bd=2)
        self.form_frame.pack(side=tk.LEFT, fill=tk.Y, padx=20, pady=20)

        # Khung chứa ảnh bên phải
        self.image_frame = tk.Frame(self.main_container, bg="#f5f5f5")
        self.image_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Thêm ảnh vào phần body
        try:
            img_path = os.path.join(os.path.dirname(__file__), "..", "img2.png")
            if os.path.exists(img_path):
                # Sử dụng PIL để xử lý ảnh
                img = Image.open(img_path)
                img = img.resize((800, 600), Image.LANCZOS)  # Điều chỉnh kích thước ảnh
                self.body_img = ImageTk.PhotoImage(img)
                
                # Tạo label để hiển thị ảnh
                img_label = tk.Label(self.image_frame, image=self.body_img, bg="#f5f5f5")
                img_label.pack(expand=True)

            else:
                print(f"Không tìm thấy ảnh tại đường dẫn: {img_path}")
        except Exception as e:
            print(f"Lỗi khi tải ảnh: {e}")

        self.create_login_form()

    def create_login_form(self):
        # Username field
        tk.Label(self.form_frame, text="Tên đăng nhập", font=("Segoe UI", 12), bg="white", fg="#333333").pack(pady=(20, 5))
        self.username_entry = tk.Entry(self.form_frame, font=("Segoe UI", 12), bg="#f5f5f5", fg="#333333", bd=0)
        self.username_entry.pack(pady=(0, 10), padx=20, fill=tk.X)
        tk.Frame(self.form_frame, bg="#6200EE", height=2).pack(padx=20, fill=tk.X)

        # Password field
        tk.Label(self.form_frame, text="Mật khẩu", font=("Segoe UI", 12), bg="white", fg="#333333").pack(pady=(10, 5))
        self.password_entry = tk.Entry(self.form_frame, font=("Segoe UI", 12), bg="#f5f5f5", fg="#333333", bd=0, show="•")
        self.password_entry.pack(pady=(0, 20), padx=20, fill=tk.X)
        tk.Frame(self.form_frame, bg="#6200EE", height=2).pack(padx=20, fill=tk.X)

        # Login button
        self.login_button = tk.Button(self.form_frame, text="Đăng nhập", font=("Segoe UI", 14, "bold"),
                                      bg="#6200EE", fg="white", bd=0, command=self.login)
        self.login_button.pack(pady=(20, 10), padx=20, fill=tk.X)
        self.add_hover_effect(self.login_button)

        # Register prompt
        tk.Label(self.form_frame, text="Chưa có tài khoản?", font=("Segoe UI", 10), bg="white", fg="#333333").pack(pady=5)
        register_link = tk.Label(self.form_frame, text="Đăng ký", font=("Segoe UI", 10, "underline"), bg="white", fg="#6200EE", cursor="hand2")
        register_link.pack(pady=(0, 20))
        register_link.bind("<Button-1>", self.go_to_register)

    def add_hover_effect(self, widget):
        widget.bind("<Enter>", lambda e: widget.config(bg="#3700B3"))
        widget.bind("<Leave>", lambda e: widget.config(bg="#6200EE"))

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
    
        # Read credentials from the file
        try:
            credentials_path = os.path.join(os.path.dirname(__file__), "..", "credentials.txt")
            with open(credentials_path, "r") as file:
                credentials = file.readlines()
        except FileNotFoundError:
            messagebox.showerror("Lỗi", "Không tìm thấy tệp thông tin đăng nhập!")
            return
    
        # Check if the entered credentials match any stored credentials
        for line in credentials:
            stored_username, stored_password = line.strip().split(',')
            if username == stored_username and password == stored_password:
                messagebox.showinfo("Thành công", "Đăng nhập thành công!")
                self.root.destroy()
                self.open_main_page()
                return
    
        messagebox.showerror("Lỗi", "Tên đăng nhập hoặc mật khẩu không đúng!")

    def go_to_register(self, event):
        self.root.destroy()
        root = tk.Tk()
        from interfaces.dang_ky import DangKy  # Update the import path
        app = DangKy(root)
        root.mainloop()

    def open_main_page(self):
        root = tk.Tk()
        from interfaces.trang_chu import TrangChu  # Update the import path
        app = TrangChu(root)
        root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = DangNhap(root)
    root.mainloop()
