import tkinter as tk
from tkinter import messagebox
import pandas as pd

# Update the path to the new CSV file
dataset_path = "c:\\Users\\LEGION\\PycharmProjects\\projectcuoiky\\students.csv"

class QuanLy:
    def __init__(self, root):
        self.root = root
        self.root.title("Hệ thống quản lý sinh viên")
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

        tk.Label(self.header_frame, text="Quản lý sinh viên", font=("Segoe UI", 18, "bold"), bg="white", fg="#6200EE").pack(padx=20, pady=10, anchor="w")

        self.main_container = tk.Frame(self.root, bg="#f5f5f5")
        self.main_container.pack(fill=tk.BOTH, expand=True)

        self.menu_frame = tk.Frame(self.main_container, bg="white", width=120, relief="raised", bd=1)
        self.menu_frame.pack(side=tk.LEFT, fill=tk.Y)
        self.menu_frame.pack_propagate(False)

        self.content_frame = tk.Frame(self.main_container, bg="#f5f5f5")
        self.content_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

    def create_menu(self):
        menu_items = [
            ("Đọc", self.show_read_students),
            ("Quản lý sinh viên", self.show_manage_student),
            ("Quay lại", self.back_to_main)  # Ensure this calls back_to_main
        ]

        for idx, (text, command) in enumerate(menu_items):
            btn = tk.Button(
                self.menu_frame, text=text, font=("Segoe UI", 10), bg="white", fg="#333333", bd=0,
                activebackground="#E0E0E0", activeforeground="#6200EE",
                command=command, padx=10, pady=10
            )
            btn.pack(fill=tk.X, pady=(10 if idx == 0 else 5, 0), padx=5)
            self.add_hover_effect(btn)

    def back_to_main(self):
        self.root.destroy()  # Close the current window
        from interfaces.trang_chu import TrangChu  # Import TrangChu class
        root = tk.Tk()
        app = TrangChu(root)  # Launch TrangChu
        root.mainloop()

    def create_dashboard(self):
        self.clear_content()
        tk.Label(self.content_frame, text="Chào mừng đến với Hệ thống Quản lý Sinh viên!",
                 font=("Segoe UI", 20, "bold"), bg="#f5f5f5", fg="#333333").pack(pady=50)

    def add_hover_effect(self, widget):
        widget.bind("<Enter>", lambda e: widget.config(bg="#E0E0E0"))
        widget.bind("<Leave>", lambda e: widget.config(bg="white"))

    def clear_content(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()

    def show_manage_student(self):
        self.clear_content()
        tk.Label(self.content_frame, text="Quản lý sinh viên", font=("Segoe UI", 18, "bold"), bg="#f5f5f5", fg="#333333").pack(pady=20)
    
        # Create a frame for the form
        form_frame = tk.Frame(self.content_frame, bg="#f5f5f5")
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
            tk.Label(form_frame, text=field, font=("Segoe UI", 12), bg="#f5f5f5", fg="#333333").grid(row=idx, column=0, padx=10, pady=5, sticky="e")
            entry = tk.Entry(form_frame, font=("Segoe UI", 12), width=30)
            entry.grid(row=idx, column=1, padx=10, pady=5)
            entry.insert(0, last_student[field])  # Insert last student's data
            self.entries[field] = entry
    
        # Second row of fields
        for idx, field in enumerate(fields[half:]):
            tk.Label(form_frame, text=field, font=("Segoe UI", 12), bg="#f5f5f5", fg="#333333").grid(row=idx, column=2, padx=10, pady=5, sticky="e")
            entry = tk.Entry(form_frame, font=("Segoe UI", 12), width=30)
            entry.grid(row=idx, column=3, padx=10, pady=5)
            entry.insert(0, last_student[field])  # Insert last student's data
            self.entries[field] = entry
    
        # Create a frame for buttons at the bottom
        button_frame = tk.Frame(self.content_frame, bg="#f5f5f5")
        button_frame.pack(pady=20)
    
        # Add buttons in a horizontal row with equal sizes
        buttons = [
            ("Thêm", self.add_student),
            ("Sửa", self.edit_student),
            ("Xóa", self.delete_student),
            ("Làm sạch", self.clear_form),
            ("Tìm kiếm", self.search_student)  # Update to call search_student method
        ]
    
        for idx, (text, command) in enumerate(buttons):
            btn = tk.Button(button_frame, text=text, font=("Segoe UI", 12), bg="white", fg="#333333", bd=0,
                            activebackground="#E0E0E0", activeforeground="#6200EE",
                            command=command, width=15, height=2)
            btn.grid(row=0, column=idx, padx=5, pady=5)
            self.add_hover_effect(btn)

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

        canvas = tk.Canvas(self.content_frame, bg="#f5f5f5")
        scrollbar = tk.Scrollbar(self.content_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg="#f5f5f5")

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="top", fill="both", expand=True)
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
