import PlayAudio
from Kana import Kana
from config import *
import random
import time


def showFlashCard(kana, mode=None):
    modes = ['HIRA', 'KATA', 'ROMA']
    if mode is None:
        mode = random.choice(modes)

    print("==========")

    if mode == 'HIRA':
        ans = [kana.getKata(), kana.getRoma()]
        print("平假名：%s" % kana.getHira())
        input_ans = [input("片假名：").strip(), input("罗马字：").strip().upper()]

    elif mode == 'KATA':
        ans = [kana.getHira(), kana.getRoma()]
        print("片假名：%s" % kana.getKata())
        input_ans = [input("平假名：").strip(), input("罗马字：").strip().upper()]
    else:
        ans = [kana.getHira(), kana.getKata()]
        print("罗马字：%s" % kana.getRoma())
        input_ans = [input("平假名：").strip(), input("片假名：").strip().upper()]

    if input_ans == ans:
        print("正确！")
    else:
        print("错误！应为：")
        print(kana.getInfo())

    print("==========")


def playSound(kana):
    roma = kana.getRoma().lower()
    audio_path = AUDIO_PATH
    file = audio_path + roma + '.wav'

    PlayAudio.AudioPlayer().play_audio(file)


if __name__ == '__main__':
    kana_A = Kana('a', 'あ', 'ア')
    playSound(kana_A)


