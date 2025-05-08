import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

class ThongKe:
    def __init__(self, root):
        self.root = root
        self.root.title("Thống kê dữ liệu")
        self.root.geometry("1000x600")
        self.root.configure(bg="#f5f5f5")
        self.fade_in()
        
        # Load data
        self.data_path = ".\\students.csv"
        try:
            self.df = pd.read_csv(self.data_path)
        except FileNotFoundError:
            messagebox.showerror("Lỗi", "Không tìm thấy file dữ liệu students.csv")
            self.root.destroy()
            return
            
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

        tk.Label(self.header_frame, text="Thống kê dữ liệu", font=("Segoe UI", 18, "bold"), bg="white", fg="#6200EE").pack(padx=20, pady=10, anchor="w")

        self.main_container = tk.Frame(self.root, bg="#f5f5f5")
        self.main_container.pack(fill=tk.BOTH, expand=True)

        self.menu_frame = tk.Frame(self.main_container, bg="white", width=200, relief="raised", bd=1)
        self.menu_frame.pack(side=tk.LEFT, fill=tk.Y)
        self.menu_frame.pack_propagate(False)

        self.content_frame = tk.Frame(self.main_container, bg="#f5f5f5")
        self.content_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        
    def create_menu(self):
        menu_items = [
            ("Biểu đồ cột số lượng sinh viên theo khoa", self.show_department_student_count),
            ("Biểu đồ đường GPA trung bình qua các năm", self.show_line_chart_gpa_by_year),
            ("Biểu đồ tán xạ Tuổi vs GPA", self.show_scatter_age_vs_gpa),
            ("Biểu đồ Boxplot GPA theo khoa", self.show_boxplot),
            ("Biểu đồ tròn tỷ lệ sinh viên theo khoa", self.show_pie_chart),
            ("Biểu đồ cột GPA theo khoa và năm", self.show_grouped_bar),
            ("Quay lại", self.back_to_main)
        ]

        for idx, (text, command) in enumerate(menu_items):
            btn = tk.Button(
                self.menu_frame, text=text, font=("Segoe UI", 10), bg="white", fg="#333333", bd=0,
                activebackground="#E0E0E0", activeforeground="#6200EE",
                command=command, padx=10, pady=10, wraplength=180, justify="left"
            )
            btn.pack(fill=tk.X, pady=(10 if idx == 0 else 5, 0), padx=5)
            self.add_hover_effect(btn)
            
        # Add exit button at the bottom
        exit_btn = tk.Button(
            self.menu_frame, text="Thoát", font=("Segoe UI", 10), bg="white", fg="#333333", bd=0,
            activebackground="#E0E0E0", activeforeground="#6200EE",
            command=self.exit_app, padx=10, pady=10
        )
        exit_btn.pack(fill=tk.X, pady=5, padx=5, side=tk.BOTTOM)
        self.add_hover_effect(exit_btn)

    def add_hover_effect(self, widget):
        widget.bind("<Enter>", lambda e: widget.config(bg="#E0E0E0"))
        widget.bind("<Leave>", lambda e: widget.config(bg="white"))
        
    def create_dashboard(self):
        self.clear_content()
        tk.Label(self.content_frame, text="Chọn loại biểu đồ từ menu bên trái",
                 font=("Segoe UI", 20, "bold"), bg="#f5f5f5", fg="#333333").pack(pady=50)
        
    def clear_content(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()

    def show_department_student_count(self):
        self.clear_content()
    
        # Create figure
        fig, ax = plt.subplots(figsize=(10, 6))
    
        # Count students by department
        dept_counts = self.df['Department'].value_counts()
    
        # Create bar chart
        bars = ax.bar(dept_counts.index, dept_counts.values, color='#80b1d3', alpha=0.8)
    
        # Add data labels on top of each bar
        for bar in bars:
            height = bar.get_height()
            ax.annotate(f'{int(height)}',
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 5),  # Offset label upward
                    textcoords="offset points",
                    ha='center', va='bottom', fontsize=9, fontweight='bold')
    
        # Set labels and title
        ax.set_title('Số lượng sinh viên theo từng khoa', fontsize=14, fontweight='bold')
        ax.set_xlabel('Khoa', fontsize=12)
        ax.set_ylabel('Số lượng sinh viên', fontsize=12)
        ax.set_xticklabels(dept_counts.index, rotation=45, ha='right')
        ax.grid(True, linestyle='--', alpha=0.3, axis='y')
    
        # Create canvas
        canvas = FigureCanvasTkAgg(fig, master=self.content_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

    def show_line_chart_gpa_by_year(self):
        self.clear_content()
    
        # Create figure
        fig, ax = plt.subplots(figsize=(10, 6))
    
        # Group by GraduationYear, calculate mean GPA
        gpa_by_year = self.df.groupby('GraduationYear')['GPA'].mean().sort_index()
    
        # Plot line chart
        ax.plot(gpa_by_year.index, gpa_by_year.values, marker='o', linestyle='-', color='#fb8072', linewidth=2)
    
        # Add data labels
        for x, y in zip(gpa_by_year.index, gpa_by_year.values):
            ax.text(x, y + 0.02, f'{y:.2f}', ha='center', va='bottom', fontsize=9, fontweight='bold')
    
        # Set labels and title
        ax.set_title('Xu hướng GPA trung bình theo năm tốt nghiệp', fontsize=14, fontweight='bold')
        ax.set_xlabel('Năm tốt nghiệp', fontsize=12)
        ax.set_ylabel('GPA trung bình', fontsize=12)
        ax.grid(True, linestyle='--', alpha=0.5)
    
        # Create canvas
        canvas = FigureCanvasTkAgg(fig, master=self.content_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

    def show_scatter_age_vs_gpa(self):
        self.clear_content()
    
        # Create figure
        fig, ax = plt.subplots(figsize=(10, 6))
    
        # Plot scatter
        ax.scatter(self.df['Age'], self.df['GPA'], color='#80b1d3', alpha=0.7, edgecolors='w', s=70)
    
        # Set labels and title
        ax.set_title('Mối quan hệ giữa Tuổi và GPA', fontsize=14, fontweight='bold')
        ax.set_xlabel('Tuổi', fontsize=12)
        ax.set_ylabel('GPA', fontsize=12)
        ax.grid(True, linestyle='--', alpha=0.5)
    
        # Create canvas
        canvas = FigureCanvasTkAgg(fig, master=self.content_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True, padx=20, pady=20)


    def show_boxplot(self):
        self.clear_content()
        
        # Create figure
        fig, ax = plt.subplots(figsize=(10, 6))
        
        # Create boxplot
        departments = self.df['Department'].unique()
        data = [self.df[self.df['Department'] == dept]['GPA'] for dept in departments]
        
        box = ax.boxplot(data, patch_artist=True, labels=departments)
        
        # Customize boxplot colors
        colors = ['#8dd3c7', '#ffffb3', '#bebada', '#fb8072', '#80b1d3', '#fdb462']
        for patch, color in zip(box['boxes'], colors[:len(departments)]):
            patch.set_facecolor(color)
            
        # Set labels and title
        ax.set_title('Phân bố GPA theo từng khoa', fontsize=14, fontweight='bold')
        ax.set_xlabel('Khoa', fontsize=12)
        ax.set_ylabel('GPA', fontsize=12)
        ax.grid(True, linestyle='--', alpha=0.7)
        
        # Create canvas
        canvas = FigureCanvasTkAgg(fig, master=self.content_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
    def show_pie_chart(self):
        self.clear_content()
        
        # Create figure
        fig, ax = plt.subplots(figsize=(10, 6))
        
        # Count students by department
        dept_counts = self.df['Department'].value_counts()
        
        # Create pie chart
        colors = ['#8dd3c7', '#ffffb3', '#bebada', '#fb8072', '#80b1d3', '#fdb462']
        explode = [0.05] * len(dept_counts)  # Explode all slices slightly
        
        wedges, texts, autotexts = ax.pie(
            dept_counts, 
            labels=dept_counts.index,
            autopct='%1.1f%%',
            startangle=90,
            explode=explode,
            colors=colors[:len(dept_counts)],
            shadow=True
        )
        
        # Customize text
        for text in texts:
            text.set_fontsize(10)
        for autotext in autotexts:
            autotext.set_fontsize(9)
            autotext.set_fontweight('bold')
            
        ax.set_title('Tỷ lệ sinh viên theo khoa', fontsize=14, fontweight='bold')
        ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
        
        # Create canvas
        canvas = FigureCanvasTkAgg(fig, master=self.content_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
    def show_grouped_bar(self):
        self.clear_content()
        
        # Create figure
        fig, ax = plt.subplots(figsize=(12, 6))
        
        # Group by Department and GraduationYear, calculate mean GPA
        grouped_data = self.df.groupby(['GraduationYear', 'Department'])['GPA'].mean().reset_index()
        
        # Get unique departments and years
        departments = self.df['Department'].unique()
        years = sorted(self.df['GraduationYear'].unique())
        
        # Set width of bars
        bar_width = 0.15
        
        # Set positions of bars on X-axis
        positions = np.arange(len(years))
        
        # Create bars for each department
        for i, dept in enumerate(departments):
            dept_data = grouped_data[grouped_data['Department'] == dept]
            
            # Create a dictionary to map years to GPA values
            year_to_gpa = dict(zip(dept_data['GraduationYear'], dept_data['GPA']))
            
            # Get GPA values for each year, using 0 if no data
            gpa_values = [year_to_gpa.get(year, 0) for year in years]
            
            # Plot bars
            ax.bar(
                positions + i * bar_width - (len(departments) - 1) * bar_width / 2, 
                gpa_values, 
                bar_width, 
                label=dept,
                alpha=0.8
            )
        
        # Set labels and title
        ax.set_title('GPA trung bình theo khoa và năm tốt nghiệp', fontsize=14, fontweight='bold')
        ax.set_xlabel('Năm tốt nghiệp', fontsize=12)
        ax.set_ylabel('GPA trung bình', fontsize=12)
        ax.set_xticks(positions)
        ax.set_xticklabels(years)
        ax.legend(title='Khoa')
        ax.grid(True, linestyle='--', alpha=0.3, axis='y')
        
        # Create canvas
        canvas = FigureCanvasTkAgg(fig, master=self.content_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
    def back_to_main(self):
        self.root.destroy()
        from interfaces.trang_chu import TrangChu
        root = tk.Tk()
        app = TrangChu(root)
        root.mainloop()
        
    def exit_app(self):
        if messagebox.askyesno("Xác nhận", "Bạn có muốn thoát ứng dụng?"):
            self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = ThongKe(root)
    root.mainloop()
