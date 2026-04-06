
# bài 1
a = float(input("Nhập a: "))
b = float(input("Nhập b: "))

print(f"Tổng: {a + b}")
print(f"Hiệu: {a - b}")
print(f"Tích: {a * b}")
print(f"Thương: {a / b if b != 0 else 'Không thể chia cho 0'}")
#
Nhập a: 10
Nhập b: 5
Tổng: 15.0
Hiệu: 5.0
Tích: 50.0
Thương: 2.0

#bai 2
s = "Hello World"
print(s[2:5])
#KQ
llo

#bai 3
s = "  Hello World  "

s_trimmed = s.strip()
print(f"Xóa khoảng trắng: '{s_trimmed}'")

print(f"Dạng hoa: {s_trimmed.upper()}")
print(f"Dạng thường: {s_trimmed.lower()}")

s_replaced = s_trimmed.replace("H", "J")
print(f"Thay H thành J: {s_replaced}")

#KQ
Xóa khoảng trắng: 'Hello World'
Dạng hoa: HELLO WORLD
Dạng thường: hello world
Thay H thành J: Jello World


#bai 4 den bai 8

a = float(input("Nhập a: "))
b = float(input("Nhập b: "))

if a > b: print("Hello World!")
print("Yes") if a == b else print("No")

if a == b:
    print(1)
elif a > b:
    print(2)
else:
    print(3)

c = float(input("Nhập c: "))
d = float(input("Nhập d: "))
if a == b and b == d: print("Hello World!")
if a == b or c == d: print("Hello World!")

#Nhập a: 5
Nhập b: 5
Yes
1
Nhập c: 3
Nhập d: 3
Hello World!

#bai9
print('Yes') if a > b else print('No')

#bai 10
a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
print("A") if a > b else print("=") if a == b else print("B")

#bai 11
n = int(input("Nhập số phần tử n: "))
a = [int(input(f"Nhập phần tử {i+1}: ")) for i in range(n)]

b = [x for x in a if x % 2 == 0]
print(f"Mảng b (các số chẵn): {b}")

#KQ
Nhập số phần tử n: 2
Nhập phần tử 1: 1
Nhập phần tử 2: 2
Mảng b (các số chẵn): [2]

#bai 12
tong = sum(x for x in range(1000) if x % 3 == 0 or x % 5 == 0)
print(f"Tổng là: {tong}")

#KQ
Tổng là: 233168

#bai13
def tron_mang(a, b):
    res = []

    min_len = min(len(a), len(b))

    for i in range(min_len):
        res.append(a[i] + b[i])


    if len(a) > len(b):
        res.extend(a[min_len:])
    else:
        res.extend(b[min_len:])

    return res


mang_a = [3, 9, 1, 4]
mang_b = [2, 7, 4, 3, 2, 8]
print(f"Kết quả trộn: {tron_mang(mang_a, mang_b)}")
#bai14
Kết quả trộn: [5, 16, 5, 7, 2, 8]

#bai 14

# bai 14


# a
def tao_mang(m, n):
    return [[random.randint(1, 100) for _ in range(n)] for _ in range(m)]

# b
def xuat_dong_k(a, k):
    if 0 <= k < len(a):
        print(f"Dòng {k}: {a[k]}")

# c
def xuat_cot_k(a, k):
    cot = [dong[k] for dong in a]
    print(f"Cột {k}: {cot}")

# d
def dong_tong_max(a):
    tong_cac_dong = [sum(dong) for dong in a]
    max_val = max(tong_cac_dong)
    print(f"Dòng có tổng lớn nhất ({max_val}) là dòng số: {tong_cac_dong.index(max_val)}")

# e
def cot_tich_min(a):
    m, n = len(a), len(a[0])
    tich_min = float('inf')
    index_min = 0
    for j in range(n):
        tich_cot = 1
        for i in range(m):
            tich_cot *= a[i][j]
        if tich_cot < tich_min:
            tich_min = tich_cot
            index_min = j
    print(f"Cột có tích nhỏ nhất là cột {index_min} với tích = {tich_min}")

# f
def xuat_dong_chan_cot_le(a):
    res = []
    for i in range(0, len(a), 2):
        for j in range(1, len(a[0]), 2):
            res.append(a[i][j])
    print("Các phần tử dòng chẵn, cột lẻ:", res)

# g
def tbc_chan_dong_le(a):
    list_so = []
    for i in range(1, len(a), 2):
        for x in a[i]:
            if x % 2 == 0: list_so.append(x)
    return sum(list_so) / len(list_so) if list_so else 0

# h & i.
def tinh_bien(a, loai="bien"):
    m, n = len(a), len(a[0])
    bien = []
    khong_bien = []
    for i in range(m):
        for j in range(n):
            if i == 0 or i == m-1 or j == 0 or j == n-1:
                bien.append(a[i][j])
            else:
                khong_bien.append(a[i][j])

    if loai == "bien":
        return sum(bien) / len(bien) if bien else 0
    else:
        import math
        return math.prod(khong_bien)**(1/len(khong_bien)) if khong_bien else 0
def main():
    
    
    m = int(input("Nhập số dòng m: "))
    n = int(input("Nhập số cột n: "))
    
    
    a = tao_mang(m, n)
    
    
    print("\n--- Ma trận vừa tạo ---")
    for i in range(m):
        print(f"Dòng {i}: {a[i]}")
        
    
    k_dong = int(input(f"\nNhập dòng k muốn xuất (từ 0 đến {m-1}): "))
    xuat_dong_k(a, k_dong)
    
    
    k_cot = int(input(f"Nhập cột k muốn xuất (từ 0 đến {n-1}): "))
    xuat_cot_k(a, k_cot)
    
    print("\n--- Phân tích tổng / tích ---")
    dong_tong_max(a)
    
    
    cot_tich_min(a)
    
    
    print("\n--- Lọc phần tử theo vị trí ---")
    xuat_dong_chan_cot_le(a)
    
    
    ket_qua_g = tbc_chan_dong_le(a)
    print(f"TBC các phần tử chẵn trên dòng lẻ: {ket_qua_g}")
    
    # h & i. Tính phần tử biên và không biên
    print("\n--- Tính biên và không biên ---")
    ket_qua_h = tinh_bien(a, "bien")
    print(f"TBC các phần tử nằm trên biên: {ket_qua_h}")
    
    ket_qua_i = tinh_bien(a, "khong_bien")
    print(f"Trung bình nhân các phần tử không nằm trên biên: {ket_qua_i}")


if __name__ == "__main__":
    main()
#KQ
Nhập số dòng m: 2
Nhập số cột n: 2

--- Ma trận vừa tạo ---
Dòng 0: [2, 76]
Dòng 1: [73, 27]

Nhập dòng k muốn xuất (từ 0 đến 1): 0
Dòng 0: [2, 76]
Nhập cột k muốn xuất (từ 0 đến 1): 1
Cột 1: [76, 27]

--- Phân tích tổng / tích ---
Dòng có tổng lớn nhất (100) là dòng số: 1
Cột có tích nhỏ nhất là cột 0 với tích = 146

--- Lọc phần tử theo vị trí ---
Các phần tử dòng chẵn, cột lẻ: [76]
TBC các phần tử chẵn trên dòng lẻ: 0

--- Tính biên và không biên ---
TBC các phần tử nằm trên biên: 44.5
Trung bình nhân các phần tử không nằm trên biên: 0

from datetime import datetime


# bai 15
# a.
class SinhVien:
    def __init__(self, mssv, ten, nam_sinh, diem_tb):
        self.mssv = mssv[:10]
        self.ten = ten[:20]
        self.nam_sinh = int(nam_sinh)
        self.diem_tb = float(diem_tb)
# b.
ds_sinh_vien = [
    SinhVien("01DH0001", "Phan Anh Lan", 2004, 7.5),
    SinhVien("02DH0002", "Nguyen Van B", 2006, 4.5),
    SinhVien("03CD0003", "Tran Lan", 2003, 8.0),
    SinhVien("04DH0004", "Phan Thanh C", 2004, 6.0)
]



# c.
def sv_len_lop(ds):
    count = sum(1 for sv in ds if sv.diem_tb >= 5)
    print(f"Số sinh viên đủ điều kiện lên lớp: {count}")

# d. 
def sv_20_tuoi(ds):
    nam_hien_tai = datetime.now().year
    print("\nDanh sách sinh viên đủ 20 tuổi trở lên:")
    for sv in ds:
        if nam_hien_tai - sv.nam_sinh >= 20:
            print(f"  - {sv.ten} (Sinh năm: {sv.nam_sinh})")

# e. 
def dem_he_dh(ds):
    count = sum(1 for sv in ds if sv.mssv[2:4] == "DH")
    print(f"\nSố sinh viên hệ Đại học: {count}")

# f.
def dem_ten_lan(ds):
    count = sum(1 for sv in ds if sv.ten.split()[-1].lower() == "lan")
    print(f"Số sinh viên tên Lan: {count}")

# g. 
def dem_ho_phan(ds):
    count = sum(1 for sv in ds if sv.ten.split()[0].lower() == "phan")
    print(f"Số sinh viên họ Phan: {count}")

def main():
    
  
    print("[Danh sách sinh viên hiện tại]")
    for sv in ds_sinh_vien:
        print(f"MSSV: {sv.mssv:<10} | Tên: {sv.ten:<20} | Năm sinh: {sv.nam_sinh} | ĐTB: {sv.diem_tb}")
    
    print("\n" + "-"*45)
    
    
    sv_len_lop(ds_sinh_vien)
    sv_20_tuoi(ds_sinh_vien)
    dem_he_dh(ds_sinh_vien)
    dem_ten_lan(ds_sinh_vien)
    dem_ho_phan(ds_sinh_vien)
    
    print("-" * 45)

if __name__ == "__main__":
    main()
[Danh sách sinh viên hiện tại]
MSSV: 01DH0001   | Tên: Phan Anh Lan         | Năm sinh: 2004 | ĐTB: 7.5
MSSV: 02DH0002   | Tên: Nguyen Van B         | Năm sinh: 2006 | ĐTB: 4.5
MSSV: 03CD0003   | Tên: Tran Lan             | Năm sinh: 2003 | ĐTB: 8.0
MSSV: 04DH0004   | Tên: Phan Thanh C         | Năm sinh: 2004 | ĐTB: 6.0

---------------------------------------------
Số sinh viên đủ điều kiện lên lớp: 3

Danh sách sinh viên đủ 20 tuổi trở lên:
  - Phan Anh Lan (Sinh năm: 2004)
  - Nguyen Van B (Sinh năm: 2006)
  - Tran Lan (Sinh năm: 2003)
  - Phan Thanh C (Sinh năm: 2004)

Số sinh viên hệ Đại học: 3
Số sinh viên tên Lan: 2
Số sinh viên họ Phan: 2
---------------------------------------------
