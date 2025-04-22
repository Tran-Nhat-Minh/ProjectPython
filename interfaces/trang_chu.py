import tkinter as tk
from tkinter import messagebox

class TrangChu:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Manager")
        self.root.geometry("1000x600")
        self.root.configure(bg="#f5f5f5")
        self.fade_in()

        self.create_layout()
        self.create_menu()
        self.create_dashboard()

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

        tk.Label(self.header_frame, text="Student Manager", font=("Segoe UI", 18, "bold"), bg="white", fg="#6200EE").pack(padx=20, pady=10, anchor="w")

        self.main_container = tk.Frame(self.root, bg="#f5f5f5")
        self.main_container.pack(fill=tk.BOTH, expand=True)

        self.menu_frame = tk.Frame(self.main_container, bg="white", width=120, relief="raised", bd=1)
        self.menu_frame.pack(side=tk.LEFT, fill=tk.Y)
        self.menu_frame.pack_propagate(False)

        self.content_frame = tk.Frame(self.main_container, bg="#f5f5f5")
        self.content_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

    def create_menu(self):
        menu_items = [
            ("Quản lý", self.show_management),
            # ("Trực quan", self.show_visualization),
            ("Thống kê", self.show_statistics),
            ("Đăng xuất", self.logout),
            ("Thoát", self.exit_app)
        ]

        for idx, (text, command) in enumerate(menu_items):
            btn = tk.Button(self.menu_frame, text=text, font=("Segoe UI", 10), bg="white", fg="#333333", bd=0,
                            activebackground="#E0E0E0", activeforeground="#6200EE",
                            command=command, padx=10, pady=10)
            btn.pack(fill=tk.X, pady=(10 if idx == 0 else 5, 0), padx=5)
            self.add_hover_effect(btn)

    def add_hover_effect(self, widget):
        widget.bind("<Enter>", lambda e: widget.config(bg="#E0E0E0"))
        widget.bind("<Leave>", lambda e: widget.config(bg="white"))

    def create_dashboard(self):
        self.clear_content()
        tk.Label(self.content_frame, text="Chào mừng đến với Hệ thống Quản lý Sinh viên!",
                 font=("Segoe UI", 20, "bold"), bg="#f5f5f5", fg="#333333").pack(pady=50)

    def clear_content(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()

    def show_management(self):
        if messagebox.askyesno("Xác nhận", "Chuyển đến trang quản lý sinh viên?"):
            self.root.destroy()
            from interfaces.quan_ly import QuanLy  # Update the import path
            root = tk.Tk()
            app = QuanLy(root)
            root.mainloop()

    # def show_visualization(self):
    #     if messagebox.askyesno("Xác nhận", "Chuyển đến trang trực quan hóa dữ liệu?"):
    #         self.root.destroy()
    #         from truc_quan import TrucQuan
    #         root = tk.Tk()
    #         app = TrucQuan(root)
    #         root.mainloop()

    def show_statistics(self):
        if messagebox.askyesno("Xác nhận", "Chuyển đến trang thống kê dữ liệu?"):
            self.root.destroy()
            from thong_ke import ThongKe  # Import from the correct location
            root = tk.Tk()
            app = ThongKe(root)
            root.mainloop()

    def logout(self):
        if messagebox.askyesno("Xác nhận", "Bạn có muốn đăng xuất?"):
            self.root.destroy()
            from dang_nhap import DangNhap
            root = tk.Tk()
            app = DangNhap(root)
            root.mainloop()

    def exit_app(self):
        if messagebox.askyesno("Xác nhận", "Bạn có muốn thoát ứng dụng?"):
            self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = TrangChu(root)
    root.mainloop()