
import math
import string
def nhapmang1():
    a = []
    n = int(input("Nhap so luong mang muon khoi tao:"))
    for i in  range(n):
        giatri = float(input(f"Nhap gia tri thu {i} la:"))
        a.append(giatri)
    return a

def nhapmang2():
    b = []
    m = int(input("Nhap so luong mang muon khoi tao:"))
    for j in range(m):
        giatri = float(input(f"Nhap gia tri thu {j} la:"))
        b.append(giatri)
    return b
def tronmang(a, b):
    mang_ket_qua = []
    min_len = min(len(a), len(b))
    for i in range(min_len):
        gia_tri_min = min(a[i], b[i])
        mang_ket_qua.append(gia_tri_min)
    if len(a) > len(b):
        mang_ket_qua.extend(a[min_len:])
    else:
        mang_ket_qua.extend(b[min_len:])
    return mang_ket_qua

    return mang_ket_qua
def main():
    mang_a = nhapmang1()
    mang_b = nhapmang2()
    ketqua = tronmang(mang_a, mang_b)
    print(f"Cac phan tu co trong mang la: {ketqua}")

if __name__ == "__main__":
    main()

ket qua

Nhap so luong mang muon khoi tao:3
Nhap gia tri thu 0 la:1
Nhap gia tri thu 1 la:3
Nhap gia tri thu 2 la:5
Nhap so luong mang muon khoi tao:5
Nhap gia tri thu 0 la:2
Nhap gia tri thu 1 la:4
Nhap gia tri thu 2 la:6
Nhap gia tri thu 3 la:7
Nhap gia tri thu 4 la:8
Cac phan tu co trong mang la: [1.0, 3.0, 5.0, 7.0, 8.0]


import math
import numpy
def Tao_Mang():
    a = []
    rows = int(input("Nhap so luong hang muon tao:"))
    colums = int(input("Nhap so luong cot muon khoi tao:"))
    for i in range(rows):
        row = []
        for j in range(colums):
            value = int(input(f"Nhap gia tri thu {i}{j} la: "))
            row.append(value)
        a.append(row)
    return a

# a.
def tong_tam_giac_tren_duong_cheo_phu(a):
    n = len(a) 
    tong = 0
    
   
    for i in range(n):
      
        for j in range(n):
            if i + j <= n - 1:
                tong += a[i][j]
                
    return tong

# b. 
def tri_tuyet_doi_ma_tran(a):
    m, n = len(a), len(a[0])
    for i in range(m):
        for j in range(n):
            if a[i][j] < 0:
                a[i][j] = abs(a[i][j])
    return a

# c. 
def thay_chan_bang_x(a, x):
    for i in range(len(a)):
        for j in range(len(a[0])):
            if a[i][j] % 2 == 0:
                a[i][j] = x
    return a

# d. 
def kiem_tra_toan_chan(a):
    for row in a:
        for item in row:
            if item % 2 != 0:
                return False 
    return True

def kiem_tra_doi_xung(a):
    n = len(a)
    for i in range(n):
        for j in range(i + 1, n): # Chỉ cần kiểm tra 1 nửa tam giác
            if a[i][j] != a[j][i]:
                return False
    return True

# f. Kiểm tra đường chéo chính có tăng dần không?
def duong_cheo_chinh_tang_dan(a):
    n = len(a)
    for i in range(n - 1):
        if a[i][i] >= a[i+1][i+1]:
            return False
    return True

# g. Xuất tam giác dưới đường chéo phụ (kể cả đường chéo phụ)
def xuat_tam_giac_duoi_phu(a):
    n = len(a)
    for i in range(n):
        for j in range(n):
            if i + j >= n - 1:
                print(a[i][j], end=" ")
        print()

# h. Kiểm tra đường chéo phụ có giảm dần không?
def duong_cheo_phu_giam_dan(a):
    n = len(a)
    for i in range(n - 1):
        if a[i][n - 1 - i] <= a[i+1][n - 1 - (i+1)]:
            return False
    return True

def main():
    mang2chieu = Tao_Mang()
    tongtamgiac = tong_tam_giac_tren_duong_cheo_phu(mang2chieu)
    print(f"Tong cac phan tu thuoc duong cheo tren: {tongtamgiac}")
    chuyendoi = tri_tuyet_doi_ma_tran(mang2chieu)
    print(f"Chuyen doi cac gia tri am trong mang thanh gia tri tuyet doi: {chuyendoi}")
    x = float(input("Nhap gia tri x muon thay the:"))
    thayx = thay_chan_bang_x(mang2chieu, x)
    print(f"Thay phan tu chan trong mang thanh x: {thayx}")
    kiemtrachan = kiem_tra_toan_chan(mang2chieu)
    print(f"Kiem tra so co toan chan: {kiemtrachan}")
    kiemtradoixung = kiem_tra_doi_xung(mang2chieu)
    print(f"Kiem tra a co doi xung: {kiemtradoixung}")
    duongcheotangdan = duong_cheo_chinh_tang_dan(mang2chieu)
    print(f"Kiem tra duong cheo chinh co tang dan hay khong: {duongcheotangdan}")
    xuattamgiac = xuat_tam_giac_duoi_phu(mang2chieu)
    kiemtraduongcheo = duong_cheo_phu_giam_dan(mang2chieu)
    print(f"Kiem tra duong cheo phu co giam dan hay khong: {kiemtraduongcheo}")

if __name__ == "__main__":
    main()


#ketqua

Nhap so luong hang muon tao:2
Nhap so luong cot muon khoi tao:2
Nhap gia tri thu 00 la: 1
Nhap gia tri thu 01 la: 2
Nhap gia tri thu 10 la: 3
Nhap gia tri thu 11 la: 4
Tong cac phan tu thuoc duong cheo tren: 6
Chuyen doi cac gia tri am trong mang thanh gia tri tuyet doi: [[1, 2], [3, 4]]
Nhap gia tri x muon thay the:4
Thay phan tu chan trong mang thanh x: [[1, 4.0], [3, 4.0]]
Kiem tra so co toan chan: False
Kiem tra a co doi xung: False
Kiem tra duong cheo chinh co tang dan hay khong: True
4.0
3 4.0
Kiem tra duong cheo phu co giam dan hay khong: True
Press any key to continue . . .



#bai 2



