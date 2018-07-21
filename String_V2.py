strA = "Khoanacaddsbfbfbfbfbfb"
print(strA[0])
strB = "hello"
strC = strA +" " +  strB
print(strC)
#kiểm tra tồn tại
strD = "h"
strcF = strD in strA
strcG = strA[-1] # ngược lấy kí tự a
strH = strA[len(strA)-1] # lây ra kí tự cuối cùng của chuỗi
strE = strA[1:3] # cắt chuôi
strM = strA[-1:None:4] # cắt chuổi theo bước nhảy
print(strM)