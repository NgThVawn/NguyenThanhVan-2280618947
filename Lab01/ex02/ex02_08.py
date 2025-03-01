def chiaHetCho5(soNhiPhan):
    soThapPhan = int(soNhiPhan, 2)
    if soThapPhan % 5 == 0:
        return True
    else:
        return False
chuoiSoNhiPhan = input("Nhập chuỗi số nhị phân (Phân cách nhau bằng dấu phẩy): ")
soNhiPhanList = chuoiSoNhiPhan.split(",")
soChiaHetCho5 = [so for so in soNhiPhanList if chiaHetCho5(so)]
if len(soChiaHetCho5) > 0:
    ketQua = ", ".join(soChiaHetCho5)
    print(f"Các số nhị phân sau chia hết cho 5: {ketQua}")
else:
    print("Không có số nhị phân nào chia hết cho 5 trong chuỗi đã nhập.")