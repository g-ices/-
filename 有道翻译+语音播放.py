# 首先安装这三个模块
# pip install requests
# pip install pyttsx3
# pip install pywin32

import requests
import pyttsx3

def main():
    word = input('请输入翻译的内容：')
    url = 'http://fanyi.youdao.com/translate'
    data = {'i': word,
             'doctype':'json'}
    header = {'User-Agent': 'Mozilla/5.0'}
    response = requests.post(url, data=data, headers = header)
    voice = response.json()['translateResult'][0][0]['tgt']
    print(voice)
    engine(voice)

# 语音播报
def engine(voice):
    engine = pyttsx3.init()
    engine.say(voice)
    engine.runAndWait()

if __name__ == "__main__":
    main()
