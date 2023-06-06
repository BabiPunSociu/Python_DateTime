import datetime

# 1, Thời gian hiện tại:
obj_time_now = datetime.datetime.now()
print(obj_time_now)
print('====================================')

# 2, Tạo đối tượng datetime (năm, tháng, ngày, giờ, phút, giây):
date_obj = datetime.datetime(2002, 10, 28, 7, 30, 20)
print(date_obj)
print('====================================')

# 3, So sánh 2 ngày khác nhau:(>,>=,=,<,<=)

from datetime import datetime as dt
hientai = dt.now()
# sáng 8h-12h
# Chiều 13h30-17h30
if dt(hientai.year, hientai.month, hientai.day, 8) <= hientai <= dt(hientai.year, hientai.month, hientai.day, 12):
    print('Đang trong giờ làm việc buổi sáng')
elif dt(hientai.year, hientai.month, hientai.day, 13, 30) <= hientai <= dt(hientai.year, hientai.month, hientai.day, 17, 30):
    print('Đang trong giờ làm việc buổi chiều')
else: print("Ngoài giờ hành chính rồi, chơi đêiiiii")
print('====================================')
