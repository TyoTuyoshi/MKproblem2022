from pydub import AudioSegment
from pydub.playback import play
import random
import numpy as np
import glob
import PySimpleGUI as sg

#音源取得
files = glob.glob("C:/Users/atala/OneDrive/デスクトップ/JKspeech/*")
pos = []
sourceAudio = []
i = 0
#画面作成
#最大値と最小値は値要変更
sg.theme('Tan')
layout = [[sg.Text("言語選択",text_color = 'black'),sg.Combo(('日本語','英語'),text_color = 'black',default_value="日本語",size = (10,5),key = 'lang')],
          [sg.Text("ファイルNo",text_color = 'black'),sg.InputText('',text_color = 'black',key = 'num')],
          [sg.Text("開始時間    ",text_color = 'black'),sg.Slider(range=(1,3000),default_value =1,resolution=10,orientation='h',size=(35, 15),enable_events=True,text_color = 'black',key = 's')],
          [sg.Text("終了時間    ",text_color = 'black'),sg.Slider(range=(5000,8000),default_value =5000,resolution=10,orientation='h',size=(35, 15),enable_events=True,text_color = 'black',key = 'e')],
          [sg.Text("ずれ　　    ",text_color = 'black'),sg.Slider(range=(1,2000),default_value =1,resolution=10,orientation='h',size=(35, 15),enable_events=True,text_color = 'black',key = 'pos')],
          [sg.Text("ずれ　　    ",text_color = 'black'),sg.Slider(range=(1,2000),default_value =1,resolution=10,orientation='h',size=(35, 15),enable_events=True,text_color = 'black',key = 'pos')],
          [sg.Button(("登録"),key = 'rgs')],
          [sg.Text("最大値",text_color = 'black'),sg.Slider(range=(1,2000),default_value =1,resolution=10,orientation='h',size=(35, 15),enable_events=True,text_color = 'black',key = 'max')],
          [sg.Text("最小値",text_color = 'black'),sg.Slider(range=(1,2000),default_value =1,resolution=10,orientation='h',size=(35, 15),enable_events=True,text_color = 'black',key = 'min')],
          [sg.Button(("実行"),key = 'go')]]
window = sg.Window('ツール',layout)
while True:
    event,values = window.read()
    if event == sg.WIN_CLOSED:
        move = 0
        break
    if event == 'rgs':
        move = 1
        num = int(values['num'])
        if values['lang'] == '日本語':
            num = num + 44
        
        sourceAudio.append(AudioSegment.from_file(files[num]))
        start = int(values['s'])
        end = int(values['e'])
        pos.append(int(values['pos']))
        sourceAudio[i] = sourceAudio[i][start:end]
        i += 1
        window['num'].update("")
        window['s'].update("")
        window['e'].update("")
        window['pos'].update("")
    if event == 'go':
        break
window.close()

#問題の作成
if move != 0:
    for i in range(1,int(num)):
        exAudio = sourceAudio[0]*sourceAudio[i][start:end]
    play(exAudio)
    exAudio1 = exAudio

    #ファイル出力
    #ExportFname = input("出力ファイル名を入力＞＞　")
    exAudio1.export("problem.wav",format='wav')