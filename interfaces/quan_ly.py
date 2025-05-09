import tkinter as tk
from tkinter import messagebox
import pandas as pd
import os
from PIL import Image, ImageTk

# Update the path to the new CSV file
dataset_path = ".\\students.csv"

class QuanLy:
    def __init__(self, root):
        self.root = root
        self.root.title("Hệ thống quản lý sinh viên")
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
        
        # Khung chứa nội dung
        self.content_frame = tk.Frame(self.main_container, bg=self.card_color)
        self.content_frame.pack(fill=tk.BOTH, expand=True)

    def create_menu(self):
        # Khung chứa các nút chức năng
        button_frame = tk.Frame(self.content_frame, bg=self.card_color)
        button_frame.pack(pady=30)
        
        # Tạo các nút chức năng với hình ảnh
        self.create_feature_button(button_frame, "Xem danh sách", "read_icon.png", self.show_read_students)
        self.create_feature_button(button_frame, "Quản lý sinh viên", "manage_icon.png", self.show_manage_student)
        self.create_feature_button(button_frame, "Quay lại", "back_icon.png", self.back_to_main)
        
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
                    "Xem danh sách": "📖",
                    "Quản lý sinh viên": "👨‍🎓",
                    "Quay lại": "🔙"
                }
                emoji = emoji_map.get(text, "📋")
                
                emoji_label = tk.Label(btn_frame, text=emoji, font=("Segoe UI", 24), bg=self.card_color)
                emoji_label.pack(pady=(0, 10))
        except Exception as e:
            print(f"Lỗi khi tải icon {icon_name}: {e}")
            # Hiển thị emoji thay thế
            emoji_map = {
                "Xem danh sách": "📖",
                "Quản lý sinh viên": "👨‍🎓",
                "Quay lại": "🔙"
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

    def back_to_main(self):
        self.root.destroy()  # Close the current window
        from interfaces.trang_chu import TrangChu  # Import TrangChu class
        root = tk.Tk()
        app = TrangChu(root)  # Launch TrangChu
        root.mainloop()

    def create_dashboard(self):
        self.clear_content()
        
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
        self.create_feature_button(button_frame, "Xem danh sách", "read_icon.png", self.show_read_students)
        self.create_feature_button(button_frame, "Quản lý sinh viên", "manage_icon.png", self.show_manage_student)
        self.create_feature_button(button_frame, "Quay lại", "back_icon.png", self.back_to_main)

    def add_hover_effect(self, widget):
        widget.bind("<Enter>", lambda e: widget.config(bg="#E0E0E0"))
        widget.bind("<Leave>", lambda e: widget.config(bg=self.card_color))

    def clear_content(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()

    def show_manage_student(self):
        self.clear_content()
        tk.Label(self.content_frame, text="Quản lý sinh viên", font=("Segoe UI", 18, "bold"), bg=self.background_color, fg=self.text_primary).pack(pady=20)
    
        # Create a frame for the form
        form_frame = tk.Frame(self.content_frame, bg=self.background_color)
        form_frame.pack(pady=10)
    
        # Define fields based on the new dataset columns
        fields = ["StudentID", "Name", "Age", "Email", "Department", "GPA", "GraduationYear"]
    
        # Read the dataset and get the last student's data
        df = pd.read_csv(dataset_path)
        last_student = df.iloc[-1]
    
        # Split fields into two rows
        half = len(fields) // 2
        self.entries = {}
    
        # First row of fields
        for idx, field in enumerate(fields[:half]):
            tk.Label(form_frame, text=field, font=("Segoe UI", 12), bg=self.background_color, fg=self.text_primary).grid(row=idx, column=0, padx=10, pady=5, sticky="e")
            entry = tk.Entry(form_frame, font=("Segoe UI", 12), width=30)
            entry.grid(row=idx, column=1, padx=10, pady=5)
            entry.insert(0, last_student[field])  # Insert last student's data
            self.entries[field] = entry
    
        # Second row of fields
        for idx, field in enumerate(fields[half:]):
            tk.Label(form_frame, text=field, font=("Segoe UI", 12), bg=self.background_color, fg=self.text_primary).grid(row=idx, column=2, padx=10, pady=5, sticky="e")
            entry = tk.Entry(form_frame, font=("Segoe UI", 12), width=30)
            entry.grid(row=idx, column=3, padx=10, pady=5)
            entry.insert(0, last_student[field])  # Insert last student's data
            self.entries[field] = entry
    
        # Create a frame for buttons at the bottom
        button_frame = tk.Frame(self.content_frame, bg=self.background_color)
        button_frame.pack(pady=20)
    
        # Add buttons in a horizontal row with equal sizes and icons
        buttons = [
            ("Thêm", self.add_student, "add_icon.png", "➕"),
            ("Sửa", self.edit_student, "edit_icon.png", "✏️"),
            ("Xóa", self.delete_student, "delete_icon.png", "🗑️"),
            ("Làm sạch", self.clear_form, "clear_icon.png", "🧹"),
            ("Tìm kiếm", self.search_student, "search_icon.png", "🔍")
        ]
    
        for idx, (text, command, icon_name, emoji) in enumerate(buttons):
            # Tạo frame cho mỗi nút
            btn_frame = tk.Frame(button_frame, bg=self.card_color, padx=10, pady=10)
            btn_frame.grid(row=0, column=idx, padx=5, pady=5)
            
            # Thử tải ảnh icon
            try:
                icon_path = os.path.join("c:\\Users\\LEGION\\PycharmProjects\\projectcuoiky\\images", icon_name)
                if os.path.exists(icon_path):
                    icon_img = Image.open(icon_path)
                    icon_img = icon_img.resize((32, 32), Image.LANCZOS)
                    icon_photo = ImageTk.PhotoImage(icon_img)
                    
                    # Lưu tham chiếu để tránh bị thu hồi bởi garbage collector
                    setattr(self, f"{text}_icon", icon_photo)
                    
                    # Tạo label hiển thị icon
                    icon_label = tk.Label(btn_frame, image=icon_photo, bg=self.card_color)
                    icon_label.pack(pady=(0, 5))
                else:
                    # Nếu không có icon, hiển thị emoji thay thế
                    emoji_label = tk.Label(btn_frame, text=emoji, font=("Segoe UI", 18), bg=self.card_color)
                    emoji_label.pack(pady=(0, 5))
            except Exception as e:
                print(f"Lỗi khi tải icon {icon_name}: {e}")
                # Hiển thị emoji thay thế
                emoji_label = tk.Label(btn_frame, text=emoji, font=("Segoe UI", 18), bg=self.card_color)
                emoji_label.pack(pady=(0, 5))
            
            # Tạo nút với Material Design
            btn = tk.Button(
                btn_frame,
                text=text,
                font=("Segoe UI", 12, "bold"),
                bg=self.primary_color,
                fg="white",
                padx=10,
                pady=5,
                bd=0,
                relief="flat",
                command=command,
                width=10
            )
            btn.pack(fill=tk.X)
            
            # Thêm hiệu ứng hover
            btn.bind("<Enter>", lambda e, b=btn: b.config(bg=self.primary_dark))
            btn.bind("<Leave>", lambda e, b=btn: b.config(bg=self.primary_color))
            
            # Thêm hiệu ứng hover cho frame
            self.add_hover_effect(btn_frame)
            
        # Thêm nút quay lại ở dưới cùng
        back_frame = tk.Frame(self.content_frame, bg=self.background_color)
        back_frame.pack(pady=20)
        
        # Thử tải ảnh icon cho nút quay lại
        try:
            icon_path = os.path.join("c:\\Users\\LEGION\\PycharmProjects\\projectcuoiky\\images", "back_icon.png")
            if os.path.exists(icon_path):
                icon_img = Image.open(icon_path)
                icon_img = icon_img.resize((24, 24), Image.LANCZOS)
                self.back_icon = ImageTk.PhotoImage(icon_img)
                
                back_btn = tk.Button(
                    back_frame,
                    text="Quay lại",
                    font=("Segoe UI", 12, "bold"),
                    bg=self.primary_color,
                    fg="white",
                    padx=15,
                    pady=8,
                    bd=0,
                    relief="flat",
                    command=self.create_dashboard,
                    image=self.back_icon,
                    compound=tk.LEFT
                )
            else:
                back_btn = tk.Button(
                    back_frame,
                    text="🔙 Quay lại",
                    font=("Segoe UI", 12, "bold"),
                    bg=self.primary_color,
                    fg="white",
                    padx=15,
                    pady=8,
                    bd=0,
                    relief="flat",
                    command=self.create_dashboard
                )
        except Exception as e:
            print(f"Lỗi khi tải icon back_icon.png: {e}")
            back_btn = tk.Button(
                back_frame,
                text="🔙 Quay lại",
                font=("Segoe UI", 12, "bold"),
                bg=self.primary_color,
                fg="white",
                padx=15,
                pady=8,
                bd=0,
                relief="flat",
                command=self.create_dashboard
            )
            
        back_btn.pack()
        
        # Thêm hiệu ứng hover
        back_btn.bind("<Enter>", lambda e: back_btn.config(bg=self.primary_dark))
        back_btn.bind("<Leave>", lambda e: back_btn.config(bg=self.primary_color))

    def search_student(self):
        student_id = self.entries["StudentID"].get()
        df = pd.read_csv(dataset_path)
        student = df[df['StudentID'] == int(student_id)]
    
        if student.empty:
            messagebox.showinfo("Thông báo", "Không tìm thấy sinh viên!")
            return
    
        student_data = student.iloc[0]
        for field in self.entries:
            self.entries[field].delete(0, tk.END)
            self.entries[field].insert(0, student_data[field])

    def show_read_students(self):
        self.clear_content()
        # Read the new dataset
        df = pd.read_csv(dataset_path)
        if df.empty:
            messagebox.showinfo("Thông báo", "Không có dữ liệu sinh viên!")
            return

        tk.Label(self.content_frame, text="Danh sách sinh viên", font=("Segoe UI", 18, "bold"), bg="#f5f5f5", fg="#333333").pack(pady=20)

        scroll_frame = tk.Frame(self.content_frame, bg="#f5f5f5")
        scroll_frame.pack(fill="both", expand=True)

        canvas = tk.Canvas(scroll_frame, bg="#f5f5f5")
        scrollbar = tk.Scrollbar(scroll_frame, orient="vertical", command=canvas.yview)

        scrollable_frame = tk.Frame(canvas, bg="#f5f5f5")

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        columns = df.columns.tolist()
        self.current_page = 0
        self.rows_per_page = 20

        def display_page(page):
            for widget in scrollable_frame.winfo_children():
                widget.destroy()

            for col in columns:
                tk.Label(scrollable_frame, text=col, font=("Segoe UI", 12, "bold"), bg="#f5f5f5", fg="#333333").grid(row=0, column=columns.index(col), padx=10, pady=5)

            start_row = page * self.rows_per_page
            end_row = start_row + self.rows_per_page
            for i, row in df.iloc[start_row:end_row].iterrows():
                for j, col in enumerate(columns):
                    tk.Label(scrollable_frame, text=row[col], font=("Segoe UI", 12), bg="#f5f5f5", fg="#333333").grid(row=i-start_row+1, column=j, padx=10, pady=5)

        def next_page():
            if (self.current_page + 1) * self.rows_per_page < len(df):
                self.current_page += 1
                display_page(self.current_page)

        def prev_page():
            if self.current_page > 0:
                self.current_page -= 1
                display_page(self.current_page)

        display_page(self.current_page)

        nav_frame = tk.Frame(self.content_frame, bg="#f5f5f5")
        nav_frame.pack(side="bottom", pady=10, fill="x")
        tk.Button(nav_frame, text="Previous", command=prev_page).pack(side="left", padx=5)
        tk.Button(nav_frame, text="Next", command=next_page).pack(side="right", padx=5)
        
        # Thêm nút quay lại
        back_btn = tk.Button(
            nav_frame,
            text="Quay lại",
            font=("Segoe UI", 12, "bold"),
            bg=self.primary_color,
            fg="white",
            padx=10,
            pady=5,
            bd=0,
            relief="flat",
            command=self.create_dashboard
        )
        back_btn.pack(side="bottom", pady=10)
        
        # Thêm hiệu ứng hover
        back_btn.bind("<Enter>", lambda e: back_btn.config(bg=self.primary_dark))
        back_btn.bind("<Leave>", lambda e: back_btn.config(bg=self.primary_color))

    def clear_form(self):
        # Clear all textboxes
        for field in self.entries:
            self.entries[field].delete(0, tk.END)
        messagebox.showinfo("Thông báo", "Đã làm sạch form!")
    
    def add_student(self):
        # Logic to add a student
        student_data = {field: self.entries[field].get() for field in self.entries}
        df = pd.read_csv(dataset_path)
        
        # Convert student_data to a DataFrame
        new_student_df = pd.DataFrame([student_data])
        
        # Concatenate the new student DataFrame with the existing DataFrame
        df = pd.concat([df, new_student_df], ignore_index=True)
        
        df.to_csv(dataset_path, index=False)
        messagebox.showinfo("Thông báo", "Thêm sinh viên thành công!")
    
    def edit_student(self):
        # Logic to edit a student
        student_id = self.entries["StudentID"].get()
        df = pd.read_csv(dataset_path)
        student_index = df[df['StudentID'] == int(student_id)].index
    
        if student_index.empty:
            messagebox.showinfo("Thông báo", "Không tìm thấy sinh viên!")
            return
    
        # Cast values to appropriate types
        df.at[student_index[0], "StudentID"] = int(self.entries["StudentID"].get())
        df.at[student_index[0], "Name"] = self.entries["Name"].get()
        df.at[student_index[0], "Age"] = int(self.entries["Age"].get())
        df.at[student_index[0], "Email"] = self.entries["Email"].get()
        df.at[student_index[0], "Department"] = self.entries["Department"].get()
        df.at[student_index[0], "GPA"] = float(self.entries["GPA"].get())
        df.at[student_index[0], "GraduationYear"] = int(self.entries["GraduationYear"].get())
    
        df.to_csv(dataset_path, index=False)
        messagebox.showinfo("Thông báo", "Sửa sinh viên thành công!")
    
    def delete_student(self):
        # Logic to delete a student
        student_id = self.entries["StudentID"].get()
        df = pd.read_csv(dataset_path)
        df = df[df['StudentID'] != int(student_id)]
        df.to_csv(dataset_path, index=False)
        messagebox.showinfo("Thông báo", "Xóa sinh viên thành công!")



if __name__ == "__main__":
    root = tk.Tk()
    app = QuanLy(root)
    root.mainloop()
