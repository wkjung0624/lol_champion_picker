import win32gui, win32con, win32api
import pyautogui
import pyperclip
import keyboard
import asyncio

import tkinter as tk
from time import sleep

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        
        self.master = master

        try:
            self.hWnd = win32gui.FindWindow(None, "League of Legends");
            self.client_left, self.client_top, self.client_right, self.client_bottom = win32gui.GetWindowRect(self.hWnd);
            
        except Exception as e:
            print("게임을 찾을 수 없음")
            print(e,"dsa")

        self.create_widgets()
        self.pack()

        self.quit = tk.Button(self, text="QUIT", fg="red", command=self.new)
        self.quit.grid(column=0, row=6, sticky=tk.N+tk.S+tk.W+tk.E)
    def new(self):
        try:
            self.hWnd = win32gui.FindWindow(None, "League of Legends");
            self.client_left, self.client_top, self.client_right, self.client_bottom = win32gui.GetWindowRect(hWnd);
            
        except:
            print("게임을 찾을 수 없음")

    def create_widgets(self):
        
        self.elements = []
        
        for lineIndex in range(3):
            line = {}
            hotKeys = []

            self.label = tk.Label(self)
            self.label["text"] = f'Message {lineIndex}'
            self.label.grid(column=0, row=lineIndex, sticky=tk.N+tk.S+tk.W+tk.E)

            self.textbox=tk.Text(self, width=30, height=0)
            self.textbox.grid(column=1, row=lineIndex, sticky=tk.N+tk.S+tk.W+tk.E)

            for hotKeyIndex in range(3):
                self.hotkey=tk.Text(self, width=5, height=0)
                self.hotkey.grid(column=2+hotKeyIndex, row=lineIndex, sticky=tk.N+tk.S+tk.W+tk.E)
                
                hotKeys.append(self.hotkey)
            
            line["label"] = self.label
            line["textbox"] = self.textbox
            line["hotkeys"] = hotKeys
            
            self.elements.append(line)

            # self.setBtn = tk.Button(self)
            # self.setBtn["text"] = "SET Message"
            # self.setBtn["command"] = self.say_hi
            # self.setBtn.grid(column=5, row=lineIndex, sticky=tk.N+tk.S+tk.W+tk.E)
        
        self.setBtn = tk.Button(self)
        self.setBtn["text"] = "refresh"
        self.setBtn["command"] = self.new
        self.setBtn.grid(column=0, row=lineIndex+1, sticky=tk.N+tk.S+tk.W+tk.E)
        
        self.quit = tk.Button(self, text="QUIT", fg="red", command=self.master.destroy)
        self.quit.grid(column=1, row=lineIndex+1, sticky=tk.N+tk.S+tk.W+tk.E)

        self.quit = tk.Button(self, text="do", command=self.doSpamming)
        self.quit.grid(column=2, row=lineIndex+1, sticky=tk.N+tk.S+tk.W+tk.E)

    async def doSpamming(self):
        win32gui.ShowWindow(self.hWnd,5) #5 = SW_SHOW
        win32gui.SetForegroundWindow(self.hWnd)

        x_pos = self.client_left + 45
        y_pos = self.client_bottom - 40
        
        pyautogui.click(x=x_pos, y=y_pos)

        await keyboard.wait('esc')        
            
        pyperclip.copy(self.elements[0]["textbox"].get("1.0", "end"))

        pyautogui.hotkey("ctrl", "v")
        #pyautogui.press("enter")


if __name__ == "__main__":
    
    window = tk.Tk()
    window.title("LOL Spammer v0.01")
    window.geometry("480x320+100+100")
    #window.resizable(False, False)

    app = Application(master=window)
    app.mainloop()

    spamMessage = f'ㅁㄷㅁㄷㅁㄷ'
    exit()

    
"""
vscode에서 파이썬 import 인식불가 해결방법
https://moonfac.tistory.com/69

[vscode] vscode의 import 에러 해결
https://velog.io/@coding_egg/vscode-vscode%EC%9D%98-import-%EC%97%90%EB%9F%AC-%ED%95%B4%EA%B2%B0
"""