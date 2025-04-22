import pandas as pd

def read_students(file_path="c:\\Users\\LEGION\\PycharmProjects\\tuan10\\Churn_Modelling.csv"):  # Default to Churn_Modelling.csv
    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        print("Không tìm thấy dữ liệu sinh viên!")
        return None

def add_student(student_data, file_path="c:\\Users\\LEGION\\PycharmProjects\\tuan10\\Churn_Modelling.csv"):
    try:
        df = pd.read_csv(file_path)
        df = df.append(student_data, ignore_index=True)
        df.to_csv(file_path, index=False)
        print("Thêm sinh viên thành công!")
    except Exception as e:
        print(f"Lỗi khi thêm sinh viên: {e}")

def edit_student(student_id, updated_data, file_path="c:\\Users\\LEGION\\PycharmProjects\\tuan10\\Churn_Modelling.csv"):
    try:
        df = pd.read_csv(file_path)
        if student_id in df['CustomerId'].values:
            df.loc[df['CustomerId'] == student_id, updated_data.keys()] = updated_data.values()
            df.to_csv(file_path, index=False)
            print("Sửa sinh viên thành công!")
        else:
            print("Không tìm thấy sinh viên!")
    except Exception as e:
        print(f"Lỗi khi sửa sinh viên: {e}")

def delete_student(student_id, file_path="c:\\Users\\LEGION\\PycharmProjects\\tuan10\\Churn_Modelling.csv"):
    try:
        df = pd.read_csv(file_path)
        if student_id in df['CustomerId'].values:
            df = df[df['CustomerId'] != student_id]
            df.to_csv(file_path, index=False)
            print("Xóa sinh viên thành công!")
        else:
            print("Không tìm thấy sinh viên!")
    except Exception as e:
        print(f"Lỗi khi xóa sinh viên: {e}")