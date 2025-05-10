import pandas as pd
import os

def clean_student_data(input_file: str, output_file: str) -> None:
    """
    Hàm đọc dữ liệu sinh viên từ file CSV, làm sạch và chuẩn hoá dữ liệu,
    sau đó ghi lại vào file mới.

    Parameters:
        input_file (str): Đường dẫn tới file CSV đầu vào.
        output_file (str): Đường dẫn tới file CSV đầu ra sau khi làm sạch.
    """

    # Đọc dữ liệu từ file CSV
    df = pd.read_csv(input_file)

    print(df.dtypes)

    print(df.shape)

    # Làm sạch tên cột (xóa khoảng trắng thừa)
    df.columns = df.columns.str.strip()

    # Xoá các dòng có giá trị bị thiếu
    df.dropna(inplace=True)

    # Ép kiểu dữ liệu
    df['StudentID'] = df['StudentID'].astype(str)
    df['Age'] = df['Age'].astype(int)
    df['GPA'] = df['GPA'].astype(float)
    df['GraduationYear'] = df['GraduationYear'].astype(int)

    # Chuẩn hoá dữ liệu:
    df['Name'] = df['Name'].str.title()           # Viết hoa tên
    df['Email'] = df['Email'].str.lower()         # Email viết thường
    df['Department'] = df['Department'].str.title()  # Tên khoa viết hoa đầu

    # Kiểm tra và tạo file output nếu chưa tồn tại
    if not os.path.exists(output_file):
        df.to_csv(output_file, index=False)
        print(f"File {output_file} đã được tạo thành công.")
    else:
        print(f"File {output_file} đã tồn tại.")
    print(df.shape)
clean_student_data("students.csv", "students_cleaned.csv")