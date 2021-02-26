import PlayAudio
from Kana import Kana
import time

if __name__ == '__main__':
    Kana_A = Kana('A', 'あ', 'ア')
    print(Kana_A.getHira(), Kana_A.getKata(), Kana_A.getRoma())
