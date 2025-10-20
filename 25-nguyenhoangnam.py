# 25_NguyenHoangNam.py

student_list = []

def add_student(name, year_of_birth, address):
    """
    YÊU CẦU 1: Thêm sinh viên vào danh sách
    """
    student = {
        "name": name,
        "year_of_birth": year_of_birth,
        "address": address
    }
    student_list.append(student)
    print(f"Da them sinh vien {name} thanh cong.")

def print_student_list():
    """
    YÊU CẦU 2: In danh sách sinh viên
    """
    print("--- DANH SACH SINH VIEN ---")
    if not student_list:
        print("Danh sach trong.")
        return
    for s in student_list:
        print(f" - Ten: {s['name']}, Nam sinh: {s['year_of_birth']}, Dia chi: {s['address']}")

def search_student(search_name):
    """
    YÊU CẦU 3: Tìm kiếm sinh viên theo tên (không phân biệt hoa/thường)
    """
    print("--- KET QUA TIM KIEM ---")
    results = []
    for s in student_list:
        if search_name.lower() in s["name"].lower():
            results.append(s)
    if not results:
        print("Khong tim thay sinh vien nao.")
    else:
        for s in results:
            print(f" - Ten: {s['name']}, Nam sinh: {s['year_of_birth']}, Dia chi: {s['address']}")

# --- Phần kiểm tra ---
if __name__ == "__main__":
    print("--- CHUONG TRINH QUAN LY SINH VIEN ---")
    print("\n1. Them sinh vien:")
    add_student("Nguyen Van An", 2003, "Da Nang")
    add_student("Tran Thi Binh", 2002, "Quang Nam")
    add_student("Le Van Hung", 2003, "Hue")

    print("\n2. In danh sach sinh vien:")
    print_student_list()

    print("\n3. Tim kiem sinh vien theo ten 'an':")
    search_student("an")
    
    print("\nTim kiem sinh vien theo ten 'Dung':")
    search_student("Dung")

