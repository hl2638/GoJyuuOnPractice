from tkinter import *
import tkinter.font as font
from BackendDriver import BackendDriver
from MainGUIUtil import *
from config import *
from Kana import Kana

"""
This is the client/front-end/main program.
Anything that is "back-end" is within self.driver.
"""


# noinspection PyAttributeOutsideInit
class MainGUI(Tk):

    def __init__(self):
        super().__init__()
        self.initLayout()
        self.backend = BackendDriver()

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self.frm_content is not None:
            self.frm_content.destroy()
        self.frm_content = new_frame
        self.frm_content.pack()

    def initLayout(self):
        self.title("五十音图for小猫咪")
        self.window_width = 500
        self.window_height = 400
        self.minsize(self.window_width, self.window_height)
        self.geometry("%sx%s" % (self.window_width, self.window_height))
        self.configure(bg='#33BAFF', padx=50, pady=50)
        """
        Main Layout: background frame and main frame container. 
        Everything meaningful happens in the container.
        """
        Grid.rowconfigure(self, 0, weight=1)
        Grid.columnconfigure(self, 0, weight=1)

        """
        Content Frame: initially at the welcome page
        """
        self.frm_content = None
        self.switch_frame(WelcomePage)


class ContentFrame(Frame):
    def __init__(self, master):
        super().__init__(master, padx=10, pady=10, bg="#D1EEFC")


class WelcomePage(ContentFrame):
    def __init__(self, master):
        super().__init__(master)
        lbl_welcome = Label(self, text=welcomeText, bg='#F6FCFF').grid(row=0, column=0, padx=10, pady=10, sticky='nesw')
        btn_start = Button(self, text="开始学习吧", bg='#F6FCFF', command=lambda: master.switch_frame(MainPage)).grid(row=1, column=0, padx=10, pady=10, sticky='nesw')


class MainPage(ContentFrame):
    def __init__(self, master):
        super().__init__(master)
        btn_table = Button(self, text="五十音图", bg='#F6FCFF', command=lambda: master.switch_frame(TablePage)).grid(row=0, column=0, padx=10, pady=10, sticky='nesw')


class TablePage(ContentFrame):
    def __init__(self, master):
        super().__init__(master)
        """
        Mode: Hira/Kata
        """
        # TODO: Mode: Single/Combined
        # TODO: add a button to switch kana mode.
        # TODO: add a back button.
        # TODO: add descriptive text (click to view kana detail)
        # TODO: add click to play sound/click to view detail switch
        kanaTable = []
        for row in kanaTableMap:
            new_row = [None if kana is None else master.backend.romaTable[kana] for kana in row]
            # print(new_row)
            # for kana in row:
            #     if kana is None:
            #         new_row.append(None)
            #     else:
            #         new_row.append(master.backend.romaTable[kana])
            kanaTable.append(new_row)

        mode = SHOW_HIRA
        if mode == SHOW_HIRA:
            for i in range(len(kanaTable)):
                row = kanaTable[i]
                for j in range(len(row)):
                    # Grid.rowconfigure(self, 0, weight=1)
                    # Grid.columnconfigure(self, 0, weight=1)
                    kana = row[j]
                    if kana is not None:
                        btn = Button(self, text=kana.getHira(), bg='#EAF5FB', width=6, height=2)
                        btn['font'] = font.Font(size=18)
                    else:
                        btn = Button(self, bg='#FFFFFF')
                        btn['state'] = DISABLED
                        # btn = Label(self)
                    btn.grid(row=i, column=j, sticky='nsew')

        else:
            pass


if __name__ == '__main__':
    main = MainGUI()
    main.mainloop()