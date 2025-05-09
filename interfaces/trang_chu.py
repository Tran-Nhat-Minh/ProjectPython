import tkinter as tk
from tkinter import ttk, PhotoImage
import os
from PIL import Image, ImageTk

class TrangChu:
    def __init__(self, root):
        self.root = root
        self.root.title("Quản lý sinh viên")
        self.root.geometry("1000x600")
        self.root.configure(bg="#f5f5f5")
        
        # Material Design Colors
        self.primary_color = "#6200EE"
        self.primary_dark = "#3700B3"
        self.secondary_color = "#03DAC6"
        self.background_color = "#f5f5f5"
        self.card_color = "#ffffff"
        self.text_primary = "#333333"
        self.text_secondary = "#757575"
        
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
        # Header với shadow effect
        self.header_frame = tk.Frame(self.root, bg=self.card_color, height=60)
        self.header_frame.pack(fill=tk.X)
        
        # Tạo shadow effect cho header
        self.header_shadow = tk.Frame(self.root, bg="#E0E0E0", height=2)
        self.header_shadow.pack(fill=tk.X)

        # Tiêu đề với font Material Design
        title_label = tk.Label(
            self.header_frame, 
            text="Hệ thống Quản lý Sinh viên", 
            font=("Segoe UI", 18, "bold"), 
            bg=self.card_color, 
            fg=self.primary_color
        )
        title_label.pack(padx=20, pady=10, anchor="w")

        # Container chính
        self.main_container = tk.Frame(self.root, bg=self.background_color)
        self.main_container.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Khung chứa ảnh và nội dung
        self.content_frame = tk.Frame(self.main_container, bg=self.card_color)
        self.content_frame.pack(fill=tk.BOTH, expand=True)
        
        # Thêm ảnh banner
        try:
            # Đường dẫn đến ảnh banner
            banner_path = os.path.join("c:\\Users\\LEGION\\PycharmProjects\\projectcuoiky\\images", "banner.png")
            
            # Kiểm tra xem file có tồn tại không
            if os.path.exists(banner_path):
                # Sử dụng PIL để xử lý ảnh
                banner_img = Image.open(banner_path)
                banner_img = banner_img.resize((960, 200), Image.LANCZOS)  # Điều chỉnh kích thước ảnh
                
                # Chuyển đổi sang định dạng PhotoImage của Tkinter
                self.banner_photo = ImageTk.PhotoImage(banner_img)

        except Exception as e:
            print(f"Lỗi khi tải ảnh: {e}")
        
        # Tiêu đề chào mừng
        welcome_label = tk.Label(
            self.content_frame, 
            text="Chào mừng đến với Hệ thống Quản lý Sinh viên", 
            font=("Segoe UI", 20, "bold"), 
            bg=self.card_color, 
            fg=self.primary_color
        )
        welcome_label.pack(pady=20)
        
        # Mô tả ngắn
        description_label = tk.Label(
            self.content_frame, 
            text="Hệ thống quản lý thông tin sinh viên hiện đại, dễ sử dụng và hiệu quả", 
            font=("Segoe UI", 12), 
            bg=self.card_color, 
            fg=self.text_secondary,
            wraplength=800
        )
        description_label.pack(pady=10)
        
        # Khung chứa các nút chức năng
        button_frame = tk.Frame(self.content_frame, bg=self.card_color)
        button_frame.pack(pady=30)
        
        # Tạo các nút chức năng với hình ảnh
        self.create_feature_button(button_frame, "Quản lý sinh viên", "student_icon.png", self.open_student_management)
        self.create_feature_button(button_frame, "Thống kê dữ liệu", "stats_icon.png", self.open_statistics)
        self.create_feature_button(button_frame, "Thoát", "exit_icon.png", self.exit_app)
        
    def create_feature_button(self, parent, text, icon_name, command):
        # Tạo frame cho mỗi nút
        btn_frame = tk.Frame(parent, bg=self.card_color, padx=15, pady=15)
        btn_frame.pack(side=tk.LEFT, padx=10)
        
        # Thử tải ảnh icon
        try:
            icon_path = os.path.join("c:\\Users\\LEGION\\PycharmProjects\\projectcuoiky\\images", icon_name)
            if os.path.exists(icon_path):
                icon_img = Image.open(icon_path)
                icon_img = icon_img.resize((48, 48), Image.LANCZOS)
                icon_photo = ImageTk.PhotoImage(icon_img)
                
                # Lưu tham chiếu để tránh bị thu hồi bởi garbage collector
                setattr(self, f"{text}_icon", icon_photo)
                
                # Tạo label hiển thị icon
                icon_label = tk.Label(btn_frame, image=icon_photo, bg=self.card_color)
                icon_label.pack(pady=(0, 10))
            else:
                # Nếu không có icon, hiển thị emoji thay thế
                emoji_map = {
                    "Quản lý sinh viên": "👨‍🎓",
                    "Thống kê dữ liệu": "📊",
                    "Thoát": "🚪"
                }
                emoji = emoji_map.get(text, "📋")
                
                emoji_label = tk.Label(btn_frame, text=emoji, font=("Segoe UI", 24), bg=self.card_color)
                emoji_label.pack(pady=(0, 10))
        except Exception as e:
            print(f"Lỗi khi tải icon {icon_name}: {e}")
            # Hiển thị emoji thay thế
            emoji_map = {
                "Quản lý sinh viên": "👨‍🎓",
                "Thống kê dữ liệu": "📊",
                "Thoát": "🚪"
            }
            emoji = emoji_map.get(text, "📋")
            
            emoji_label = tk.Label(btn_frame, text=emoji, font=("Segoe UI", 24), bg=self.card_color)
            emoji_label.pack(pady=(0, 10))
        
        # Tạo nút với Material Design
        button = tk.Button(
            btn_frame,
            text=text,
            font=("Segoe UI", 12, "bold"),
            bg=self.primary_color,
            fg="white",
            padx=15,
            pady=8,
            bd=0,
            relief="flat",
            command=command
        )
        button.pack(fill=tk.X)
        
        # Thêm hiệu ứng hover
        button.bind("<Enter>", lambda e: button.config(bg=self.primary_dark))
        button.bind("<Leave>", lambda e: button.config(bg=self.primary_color))
        
    def open_student_management(self):
        self.root.destroy()
        from interfaces.quan_ly import QuanLy
        root = tk.Tk()
        app = QuanLy(root)
        root.mainloop()
        
    def open_statistics(self):
        self.root.destroy()
        from interfaces.thong_ke import ThongKe
        root = tk.Tk()
        app = ThongKe(root)
        root.mainloop()

        
    def exit_app(self):
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = TrangChu(root)
    root.mainloop()