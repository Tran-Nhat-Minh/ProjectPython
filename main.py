from interfaces.dang_nhap import DangNhap
import tkinter as tk

def main():
    root = tk.Tk()
    app = DangNhap(root)
    root.mainloop()

if __name__ == "__main__":
    main()