from pydub import AudioSegment
from pydub.playback import play
import pydub
import random
import numpy as np
import PySimpleGUI as sg
import matplotlib.pyplot as plt
import sys,glob,pathlib,os,time,wave,soundfile

a = 0
b = 1
#音声編集のクラス
#SHIFT_WAVFILEメソッド
#引数(AudioSegment wav,int millsecond)
#シフトしたAudioSegment型を返します。
def SHIFT_WAVFILE(wav,st,en):
        begin = st
        end = en
        print(begin)
        print(end)
        begin_data = wav[begin:]
        #end_data = AudioSegment.empty()[end]
        #debug loop
        end_data = wav[:begin]
        wav_data = begin_data + end_data
        return wav_data
#音源取得
files = glob.glob("C:/Users/atala/OneDrive/デスクトップ/JKspeech/*")
pos = []
sourceAudio = []
pops = []
i = 0
#画面作成
#最大値と最小値は値要変更
sg.theme('Tan')
layout = [[sg.Text("言語選択",text_color = 'black'),sg.Combo(('日本語','英語'),text_color = 'black',default_value="日本語",size = (10,5),key = 'lang')],
          [sg.Text("ファイルNo",text_color = 'black'),sg.InputText('',text_color = 'black',key = 'num')],
          [sg.Text("開始時間    ",text_color = 'black'),sg.Slider(range=(1,3000),default_value =1,resolution=10,orientation='h',size=(35, 15),enable_events=True,text_color = 'black',key = 's')],
          [sg.Text("終了時間    ",text_color = 'black'),sg.Slider(range=(5000,8000),default_value =5000,resolution=10,orientation='h',size=(35, 15),enable_events=True,text_color = 'black',key = 'e')],
          [sg.Button(("音声ファイルの長さを見る"), key = 'long'),sg.Text('',text_color = 'black',key = 'time')],
          #[sg.Text("音声の長さ",text_color = 'black'),sg.Text(int(e) - int(s))],
          [sg.Button(("登録"),key = 'rgs'),sg.Button(("一部再生"), key = 'play')],
          [sg.Combo(values = [''],text_color = 'black',size = (30,5),key = 'pop'),sg.Button(("削除"), key = 'del')],
          #[sg.Text("最大値",text_color = 'black'),sg.Slider(range=(1,2000),default_value =1,resolution=10,orientation='h',size=(35, 15),enable_events=True,text_color = 'black',key = 'max')],
          #[sg.Text("最小値",text_color = 'black'),sg.Slider(range=(1,2000),default_value =1,resolution=10,orientation='h',size=(35, 15),enable_events=True,text_color = 'black',key = 'min')],
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
        pops.append(num)
        
        if values['lang'] == '日本語':
            num = num + 44
        
        sourceAudio.append(AudioSegment.from_file(files[num]))
        print(pops)
        start = int(values['s'])
        end = int(values['e'])
        sourceAudio[i] = SHIFT_WAVFILE(sourceAudio[i],start,end)
        i += 1
        window['num'].update("")
        window.FindElement('pop').update(values = pops)
    if event == 'long':
        window['time'].update(f'{}'.format(e-s))
    if event == 'play':
        play(sourceAudio[i-1])
    if event == 'del':
        j = 0
        print(pops[j])
        while pops[j] != int(values['pop']):
            print("1\n")
            j += 1
        sourceAudio.pop(j)
    if event == 'go':
        break
window.close()

#問題の作成
if move != 0:
    exAudio = sourceAudio[0]
    j = 0
    for i in sourceAudio:
        #use_f = i
        #use_f = SHIFT_WAVFILE(use_f,pos[j])
        exAudio *= sourceAudio[j]
        j += 1
    play(exAudio)

    #ファイル出力
    #ExportFname = input("出力ファイル名を入力＞＞　")
    exAudio.export("problem.wav",format='wav')