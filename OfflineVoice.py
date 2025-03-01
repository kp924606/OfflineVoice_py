#The following code is based on the "AI Application Development Course" and has been partially modified after further personal research.

#1.please install pkg as below command:
#pip install pyttsx3
import pyttsx3
engine = pyttsx3.init()
engine.setProperty('rate', 100) #語速 50~500, 越大講話速度越快
engine.setProperty('volume', 1) #聲音大小 0~1, 越大講話越大聲
voices = engine.getProperty('voices')

from datetime import datetime
# 獲取當前時間, 要組成語音內容用的(我想讓牠抓取今天日期時間)
now = datetime.now().strftime("%Y年%m月%d日%H時%M分%S秒")
#設定語音內容
textVoice = f"歡迎光臨,今天日期為{now},天氣晴,請享受美好時光"
engine.say(textVoice)
engine.runAndWait()

print("播放完成")
