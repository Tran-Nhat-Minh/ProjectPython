import tkinter as tk
from tkinter import ttk,messagebox
from interfaces.trang_chu import TrangChu
from controller import quanlysinhvien_controller as qlsv

class QuanLySinhVien:
    def __init__(self, root):
        self.root = root
        self.root.title("Hệ thống quản lý sinh viên")
        self.root.geometry("1300x700")
        self.setup_theme()
        self.create_layout()
        self.load_students_to_treeview()

    def setup_theme(self):
        # Màu sắc
        self.bg_color = "#f5f5f5"
        self.primary_color = "#6200EE"
        self.primary_dark = "#3700B3"
        self.secondary_color = "#03DAC6"
        self.background_color = "#f5f5f5"
        self.card_color = "#ffffff"
        self.text_primary = "#333333"
        self.text_secondary = "#757575"

        self.root.configure(bg=self.bg_color)

        self.root.attributes('-alpha', 0.0)
        alpha = 0.0
        while alpha < 1.0:
            alpha += 0.05
            self.root.attributes('-alpha', alpha)
            self.root.update()
            self.root.after(20)

    def create_layout(self):
        self.create_header()
        self.create_main_content()

    def create_header(self):
        # Header
        self.header_frame = tk.Frame(self.root, bg=self.card_color, height=60)
        self.header_frame.pack(fill=tk.X)
        # Tạo shadow effect cho header
        self.header_shadow = tk.Frame(self.root, bg="#E0E0E0", height=2)
        self.header_shadow.pack(fill=tk.X)

        # Nút Back (Quay lại)
        btn_back = tk.Button(
            self.header_frame,
            text="🔙",
            font=("Segoe UI", 16, "bold"),
            bg=self.card_color,
            fg=self.primary_color,
            bd=0,
            relief="flat",
            command=self.back_to_main
        )
        btn_back.bind("<Enter>", lambda e: btn_back.config(
            fg=self.primary_dark,
            bg="#f0f0f0"  # Màu nền khi hover
        ))
        btn_back.bind("<Leave>", lambda e: btn_back.config(
            fg=self.primary_color,
            bg=self.card_color
        ))
        btn_back.pack(side=tk.LEFT, padx=20, pady=10)

        # Tiêu đề với font Material Design
        title_label = tk.Label(
            self.header_frame,
            text="Quản lý sinh viên",
            font=("Segoe UI", 18, "bold"),
            bg=self.card_color,
            fg=self.primary_color
        )
        title_label.pack(padx=20, pady=10, anchor="w")

    def back_to_main(self):
        self.root.destroy()
        root = tk.Tk()
        app = TrangChu(root)
        root.mainloop()

    def create_main_content(self):
        main_container = tk.Frame(self.root, bg=self.background_color)
        main_container.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        self.create_list_frame(main_container)  #Danh sách sinh viên
        self.create_form_frame(main_container) #Chức năng thêm xoá sửa

    def create_list_frame(self, parent):
        list_frame = tk.Frame(parent, bg=self.card_color, bd=2, relief=tk.GROOVE)
        list_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))

        tk.Label(
            list_frame,
            text="DANH SÁCH SINH VIÊN",
            font=("Segoe UI", 14, "bold"),
            bg=self.card_color,
            fg=self.primary_color
        ).pack(pady=10)

        # Frame chứa tiêu đề và thanh tìm kiếm
        header_frame = tk.Frame(list_frame, bg=self.card_color)
        header_frame.pack(fill=tk.X, padx=10, pady=5)
        # Thanh tìm kiếm
        search_frame = tk.Frame(header_frame, bg=self.card_color)
        search_frame.pack(side=tk.LEFT)
        tk.Label(
            search_frame,
            text="Tìm kiếm:",
            font=("Segoe UI", 9),
            bg=self.card_color
        ).pack(side=tk.LEFT)

        self.search_var = tk.StringVar()
        search_entry = tk.Entry(
            search_frame,
            textvariable=self.search_var,
            font=("Segoe UI", 9),
            width=80,
            relief=tk.GROOVE,
            bd=1
        )
        search_entry.pack(side=tk.LEFT, padx=5)
        search_entry.bind("<KeyRelease>", self.filter_students)

        # Treeview
        self.tree = ttk.Treeview(
            list_frame,
            columns=("StudentID", "Name", "Age", "Email", "Department", "GPA", "GraduationYear"),
            show="headings",
            height=20,
            selectmode="browse"
        )

        # Cấu hình từng cột
        columns_config = [
            ("StudentID", "StudentID", 50),
            ("Name", "Name", 150),
            ("Age", "Age", 30),
            ("Email", "Email", 150),
            ("Department", "Department", 150),
            ("GPA", "GPA", 30),
            ("GraduationYear", "GraduationYear", 70)
        ]

        for col, text, width in columns_config:
            self.tree.heading(col, text=text)
            self.tree.column(col, width=width, anchor="center")

        # Thanh cuộn ngang và dọc
        scroll_y = ttk.Scrollbar(list_frame, orient="vertical", command=self.tree.yview)
        scroll_y.pack(side=tk.RIGHT, fill=tk.Y)

        scroll_x = ttk.Scrollbar(list_frame, orient="horizontal", command=self.tree.xview)
        scroll_x.pack(side=tk.BOTTOM, fill=tk.X)

        self.tree.configure(yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
        self.tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        self.tree.bind("<<TreeviewSelect>>", self.on_student_select)

    def create_form_frame(self, parent):
        """Tạo khung form nhập liệu với các trường mới"""
        form_frame = tk.Frame(parent, bg=self.card_color, bd=2, relief=tk.GROOVE, width=400)
        form_frame.pack(side=tk.RIGHT, fill=tk.Y, padx=(10, 0))

        tk.Label(
            form_frame,
            text="THÔNG TIN SINH VIÊN",
            font=("Segoe UI", 14, "bold"),
            bg=self.card_color,
            fg=self.primary_color
        ).pack(pady=10)

        self.create_form_fields(form_frame)
        self.create_action_buttons(form_frame)

    def create_form_fields(self, parent):
        """Tạo các trường nhập liệu theo yêu cầu"""
        fields = [
            ("StudentID", "StudentID"),
            ("Name", "Name"),
            ("Age", "Age"),
            ("Email", "Email"),
            ("Department", "Department"),
            ("GPA", "GPA"),
            ("GraduationYear", "GraduationYear")
        ]

        self.entries = {}

        for field, label in fields:
            frame = tk.Frame(parent, bg=self.card_color)
            frame.pack(fill=tk.X, padx=15, pady=5)

            tk.Label(
                frame,
                text=f"{label}:",
                font=("Segoe UI", 11),
                bg=self.card_color,
                width=15,
                anchor="w"
            ).pack(side=tk.LEFT)

            # Xử lý đặc biệt cho trường Age (chỉ nhập số)
            if field == "Age":
                entry = tk.Spinbox(frame, from_=16, to=30, font=("Segoe UI", 11))
            else:
                entry = tk.Entry(frame, font=("Segoe UI", 11))

            entry.pack(fill=tk.X, padx=5)
            self.entries[field] = entry

    def create_action_buttons(self, parent):
        """Tạo các nút chức năng nhỏ gọn"""
        btn_frame = tk.Frame(parent, bg=self.card_color)
        btn_frame.pack(fill=tk.X, pady=10, padx=10)

        # Danh sách các nút với màu sắc
        buttons = [
            ("➕ Thêm", self.primary_color, self.add_student),
            ("✏️ Sửa", "#FFA000", self.edit_student),
            ("🗑️ Xóa", "#D32F2F", self.delete_student),
            ("🔄 Làm mới", "#757575", self.clear_form)
        ]

        for text, color, command in buttons:
            btn = tk.Button(
                btn_frame,
                text=text,
                font=("Segoe UI", 9, "bold"),
                bg=color,
                fg="white",
                padx=8,
                pady=4,
                bd=0,
                relief="flat",
                width=8,
                command=command
            )
            btn.pack(side=tk.LEFT, expand=True, padx=3)

            # Hiệu ứng hover đơn giản
            btn.bind("<Enter>", lambda e, b=btn: b.config(relief="groove"))
            btn.bind("<Leave>", lambda e, b=btn: b.config(relief="flat"))

    def load_students_to_treeview(self):
        df = qlsv.read_students()
        if df is not None:
            # Xóa dữ liệu cũ trong treeview
            for item in self.tree.get_children():
                self.tree.delete(item)

            # Thêm dữ liệu mới từ dataframe
            for _, row in df.iterrows():
                self.tree.insert("", tk.END, values=(
                    row["StudentID"],
                    row["Name"],
                    row["Age"],
                    row["Email"],
                    row["Department"],
                    row["GPA"],
                    row["GraduationYear"]
                ))

    def filter_students(self, event=None):
        keyword = self.search_var.get().lower()
        df = qlsv.read_students()
        if df is None:
            return

        filtered_df = df[df.apply(lambda row: keyword in str(row.values).lower(), axis=1)]

        # Xóa dữ liệu cũ trong treeview
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Hiển thị kết quả tìm kiếm
        for _, row in filtered_df.iterrows():
            self.tree.insert("", tk.END, values=(
                row["StudentID"],
                row["Name"],
                row["Age"],
                row["Email"],
                row["Department"],
                row["GPA"],
                row["GraduationYear"]
            ))

    def on_student_select(self, event):
        selected_item = self.tree.focus()
        if not selected_item:
            return

        values = self.tree.item(selected_item)["values"]
        if not values:
            return

        field_keys = ["StudentID", "Name", "Age", "Email", "Department", "GPA", "GraduationYear"]
        for i, key in enumerate(field_keys):
            entry = self.entries[key]
            entry.delete(0, tk.END)
            entry.insert(0, values[i])

    def add_student(self):
        student_data = {k: self.entries[k].get().strip() for k in self.entries}

        if "" in student_data.values():
            tk.messagebox.showwarning("Thiếu thông tin", "Vui lòng nhập đầy đủ thông tin.")
            return

        try:
            student_data["Age"] = int(student_data["Age"])
            student_data["GPA"] = float(student_data["GPA"])
            student_data["GraduationYear"] = int(student_data["GraduationYear"])
        except ValueError:
            tk.messagebox.showerror("Lỗi dữ liệu", "Tuổi, GPA và năm tốt nghiệp phải là số.")
            return

        if qlsv.create_student(student_data):
            self.load_students_to_treeview()
            self.clear_form()
            tk.messagebox.showinfo("Thành công", "Đã thêm sinh viên.")
        else:
            tk.messagebox.showerror("Thất bại", "Mã sinh viên đã tồn tại.")

    def edit_student(self):
        selected_item = self.tree.focus()
        if not selected_item:
            tk.messagebox.showwarning("Chưa chọn", "Hãy chọn sinh viên để sửa.")
            return

        student_data = {k: self.entries[k].get().strip() for k in self.entries}

        try:
            student_data["Age"] = int(student_data["Age"])
            student_data["GPA"] = float(student_data["GPA"])
            student_data["GraduationYear"] = int(student_data["GraduationYear"])
        except ValueError:
            tk.messagebox.showerror("Lỗi dữ liệu", "Tuổi, GPA và năm tốt nghiệp phải là số.")
            return

        # Bạn cần truyền vào tham số updated_data, chẳng hạn như là student_data
        if qlsv.update_student(student_data["StudentID"], student_data):
            self.load_students_to_treeview()
            self.clear_form()
            tk.messagebox.showinfo("Thành công", "Đã cập nhật thông tin.")
        else:
            tk.messagebox.showerror("Thất bại", "Không tìm thấy sinh viên để cập nhật.")

    def delete_student(self):
        selected_item = self.tree.focus()
        if not selected_item:
            tk.messagebox.showwarning("Chưa chọn", "Hãy chọn sinh viên để xoá.")
            return

        student_id = self.entries["StudentID"].get().strip()
        if not student_id:
            tk.messagebox.showwarning("Lỗi", "Không có mã sinh viên để xoá.")
            return

        if tk.messagebox.askyesno("Xác nhận", f"Bạn có chắc muốn xoá sinh viên {student_id}?"):
            if qlsv.delete_student(student_id):
                self.load_students_to_treeview()
                self.clear_form()
                tk.messagebox.showinfo("Thành công", "Đã xoá sinh viên.")
            else:
                tk.messagebox.showerror("Thất bại", "Không tìm thấy sinh viên.")

    def clear_form(self):
        for entry in self.entries.values():
            entry.delete(0, tk.END)
        self.tree.selection_remove(self.tree.selection())

if __name__ == "__main__":
    root = tk.Tk()
    app = QuanLySinhVien(root)
    root.mainloop()