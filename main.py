import win32gui, win32con, win32api
import pyautogui
import pyperclip
import keyboard
from time import sleep

class Client:
    def __init__(self, hWnd, size):
        self.hWnd = hWnd;
        self.size = {
            "left" : size[0],
            "top" : size[1],
            "right" : size[2],
            "bottom" : size[3],
        };
        
    def getPosition(self, positionTag="left"):
        try:
            return self.size[positionTag]
        except KeyError:
            return -1

    def getClientSize(self):
        return self.size

    def getClientHandle(self):
        return self.hWnd

# class Spammer(Client):
#     def __init__(self):
#         self.msg = ""
#         self.isActivate = False

#     def setSpamMessage(self, msg):
#         self.msg = msg


if __name__ == "__main__":

    spamMessage = f'ㅁㄷㅁㄷㅁㄷ'
    
    try:
        hWnd = win32gui.FindWindow(None, "League of Legends");
    except:
        print("게임을 찾을 수 없음")
    

    size = win32gui.GetWindowRect(hWnd);
    
    LoL = Client(hWnd, size);
    
    win32gui.ShowWindow(hWnd,5) #5 = SW_SHOW
    win32gui.SetForegroundWindow(hWnd)

    while True:
        x_pos = LoL.getPosition(positionTag="left") + 45
        y_pos = LoL.getPosition(positionTag="bottom") - 40
        
        pyautogui.click(x=x_pos, y=y_pos)

        keyboard.wait('esc')        
        
        pyperclip.copy(spamMessage)
        pyautogui.hotkey("ctrl", "v")
        pyautogui.press("enter")


"""
vscode에서 파이썬 import 인식불가 해결방법
https://moonfac.tistory.com/69

[vscode] vscode의 import 에러 해결
https://velog.io/@coding_egg/vscode-vscode%EC%9D%98-import-%EC%97%90%EB%9F%AC-%ED%95%B4%EA%B2%B0
"""