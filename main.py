
# อันนี้ทำการ import library ต่างๆ รวมถึงฟังก์ชั่นที่เราเขียนจาก folder script
# ใครจะดู script ที่ต่อกับ API ไปดูในนั้นนะครับ
from script.linenoti_script import noti_pipeline
import pandas as pd
import time
from datetime import datetime


# ให้ datetime จับว่าเป็นวันอะไร 0= วันจันทร์
today = datetime.today().weekday()

# เป็นวันไหนก็โหลดตารางเรียนวันนั้น วันศุกร์ผมใส่else เลย เพราะยังไงวันอื่นก็ไม่มีเรียนแล้วครับ ขี้เกียจทำครบ 7 วัน
# ใครอยากดู format ไปดูได้ตามไฟล์ใน git ตามชื่อไฟล์เลยนะครับ
if today == 0:
    df = pd.read_csv('time_table_mon.csv')
elif today == 1:
    df = pd.read_csv('time_table_tue.csv')
elif today == 2:
    df = pd.read_csv('time_table_wed.csv')
elif today == 3:
    df = pd.read_csv('time_table_thu.csv')
else:
    df = pd.read_csv('time_table_fri.csv')


def main():
    # loop หลักคอยเช็คเวลากับในตารางครับ
    while True:
        now = datetime.now().strftime("%H:%M")
        if now in str(df['time']):
            row = df.loc[df['time'] == now]
            # ดึงข้อมูลออกมา เพื่อเขียนข้อความและเอาไปเข้าสคริปที่ใช้ส่งไปใน line api ครับ
            mood = str(row.iloc[0, 3]).lower()
            subject = str(row.iloc[0, 1])
            link = str(row.iloc[0, 2])
            if mood == 'happy':
                msg = f"Fuiyoh! Finally a fun class: {subject}. Here's your zoom link: {link}"
            else:
                msg = f"Haiyaa You got a sad class of subject {subject}. Hia your zoom link {link}"
            noti_pipeline(msg, mood)
            # ให้โปรแกรมหยุดไป 1 นาทีก่อน loop อีกครั้ง ไม่งั้นมันจะส่ง noti รัวๆ
            time.sleep(60)

if __name__ == '__main__':
    main()
