import time

# 1, Mốc thời gian nhỏ nhất:
# - Giống như hầu hết các ngôn ngữ lập trình, python lấy ngày
#     01/01/1970 00:00:00 UTC làm mốc nhỏ nhất
# - Hàm time() sẽ trả về tổng số giây đã trôi qua tính 
#     từ ngày 01/01/1970

sum_time_second = time.time()
print("Tổng thời gian (giây) từ 1/1/1970 là:"+str(sum_time_second) )
print('====================================')

# 2, Lấy thời gian hiện tại - localtime():

# - Time tuple là bộ các đơn vị thời gian, gồm 9 thông số:
#     year: 4 số nguyên
#     month: 1->12
#     day: 1->31
#     hour: 0->23
#     minute: 0->59
#     second: 0->60
#     day of week: 0->6
#     day of year: 1->366
#     daylight savings time: -1, 0, 1

# - Lấy thời gian hiện tại trên hệ thống bằng
#    localtime(tổng thời gian theo giây), return 1 time tuple


now = time.localtime(sum_time_second)
print(now)
print()
print(f'Hiện tại {now[3]}:{now[4]}:{now[5]} {now[2]}/{now[1]}/{now[0]}')
print(f'Ngày trong tuần: {now[6]+1}')
print(f'Ngày trong năm: {now[7]}')
print('====================================')

# 3, Hàm asctime() thay đổi format time:
asc_time = time.asctime(now)
print(asc_time)
print('====================================')

# 4, Hàm sleep(n): để dừng chương trình trong n giây
for i in range(10):
    print(i)
    time.sleep(3)
