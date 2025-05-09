import pandas as pd
import os

# Đường dẫn mặc định đến file CSV
DEFAULT_DATA_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
DEFAULT_DATA_FILE = os.path.join(DEFAULT_DATA_DIR, 'students.csv')

def create_student(student_data, file_path=None):
    if file_path is None:
        file_path = DEFAULT_DATA_FILE
    try:
        if not os.path.exists(file_path):
            df = pd.DataFrame([student_data])
        else:
            df = pd.read_csv(file_path)

            df["StudentID"] = df["StudentID"].astype(str)
            student_id = str(student_data["StudentID"])

            if student_id in df["StudentID"].values:
                return False
            df = pd.concat([df, pd.DataFrame([student_data])], ignore_index=True)
        df.to_csv(file_path, index=False)
        return True
    except Exception as e:
        print(f"Lỗi khi thêm sinh viên: {e}")
        return False

def read_students(file_path=None):
    if file_path is None:
        file_path = DEFAULT_DATA_FILE
        print(file_path)
    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        print("Không tìm thấy dữ liệu sinh viên!")
        return pd.DataFrame()  # Trả về dataframe rỗng

def update_student(student_id, updated_data, file_path=None):
    if file_path is None:
        file_path = DEFAULT_DATA_FILE
    try:
        # Đọc dữ liệu từ file CSV
        df = pd.read_csv(file_path)

        # Kiểm tra nếu student_id có trong danh sách sinh viên
        df['StudentID'] = df['StudentID'].astype(str)
        if student_id in df['StudentID'].values:
            # Cập nhật từng thông tin trong updated_data
            for key, value in updated_data.items():
                df.loc[df['StudentID'] == student_id, key] = value
            # Lưu lại dữ liệu vào file
            df.to_csv(file_path, index=False)
            return True
        else:
            return False
    except Exception as e:
        print(f"Lỗi khi sửa sinh viên: {e}")
        return False

def delete_student(student_id, file_path=None):
    if file_path is None:
        file_path = DEFAULT_DATA_FILE
    try:
        df = pd.read_csv(file_path)
        df['StudentID'] = df['StudentID'].astype(str)
        if student_id in df['StudentID'].values:
            df = df[df['StudentID'] != student_id]
            df.to_csv(file_path, index=False)
            return True
        else:
            return False
    except Exception as e:
        print(f"Lỗi khi xóa sinh viên: {e}")
        return False
