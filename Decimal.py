a= 1
b= 1.6
print(a)
print(b)
print(type(a))
print(type(b))
#decimal
from decimal import* #lấy toàn bộ nội dung thư viện decimal
getcontext().prec = 30 #ham để lấy lớn ra hoặc nhỏ lại
print(10/3)