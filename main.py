from script.linenoti_script import noti_pipeline
import pandas as pd
import time
from datetime import datetime


# ให้ datetime จับว่าเป็นวันอะไร 0= วันจันทร์
today = datetime.today().weekday()

# เป็วันไหนก็โหลดตารางเรียนวันนั้น วันศุกร์ผมใส่else เลย เพราะยังไงวันอื่นก็ไม่มีเรียนแล้วครับ ขี้เกียจทำครบ 7 วัน
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
    while True:
        now = datetime.now().strftime("%H:%M")
        if now in str(df['time']):
            row = df.loc[df['time'] == now]
            mood = str(row.iloc[0, 3]).lower()
            subject = str(row.iloc[0, 1])
            link = str(row.iloc[0, 2])
            if mood == 'happy':
                msg = f"Fuiyoh! Finally a fun class: {subject}. Here's your zoom link: {link}"
            else:
                msg = f"Haiyaa You got a sad class of subject {subject}. Hia your zoom link {link}"
            noti_pipeline(msg, mood)
            time.sleep(60)

if __name__ == '__main__':
    main()
