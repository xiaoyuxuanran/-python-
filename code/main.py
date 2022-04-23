import musicplayer as mp
import ui_1 as ui
import tkinter as tk
import time
import threading
def music():
    mp.run()
def my_ui():
    ui.run()
a1=threading.Thread(target=music)
a2=threading.Thread(target=my_ui)
if __name__ == '__main__':
        a1.start()
        a2.start()
