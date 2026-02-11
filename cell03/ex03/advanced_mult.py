#!/usr/bin/python3
import sys

temp = ""
row = 0
mult_num =0

if type(sys.argv[1]) == str:
    print("none")
    sys.exit()

#ลูปบรรทัด
while row < 11:
    #ลูปตัวเลช
    while mult_num < 11:
        temp += str(mult_num*row)+" "
        mult_num += 1
    #แสดงผลข้อความทีสร้างสำหรับบรรทัดนั้นๆ
    print(f"Table de {row}: {temp}")
    #Reset ค่าก่อนเริ่มแถวถัดไป
    temp = ""
    mult_num = 0
    row += 1
        