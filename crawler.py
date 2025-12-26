import pyautogui
import time

screenwidth, screenhight = pyautogui.size()
folderPath = 'D:\\VSCodeProjects\\Python\\OCTA2024\\picts\\'


def Location(png, confidence=0.8):
    try:
        icon = pyautogui.locateOnScreen(png, confidence=confidence)
    except pyautogui.ImageNotFoundException:
        return None
    except Exception:
        return None
    if icon is not None:
        return pyautogui.center(icon)
    return None

time.sleep(1)

while True:
    # 先找到上一个对勾
    previousCheckMarkLocation = Location(f'{folderPath}previousCheckMark.png')
    if previousCheckMarkLocation is not None:
        pyautogui.moveTo(previousCheckMarkLocation[0], previousCheckMarkLocation[1], duration=0.5)
        # 取消勾选，保证只有一个对勾
        pyautogui.click()
        pyautogui.scroll(-59)
        time.sleep(0.5)
        pyautogui.click()
    # 勾选后点击下载按钮
    downloadButtonLocation = Location(f'{folderPath}downloadButton.png')
    if downloadButtonLocation is not None:
        pyautogui.moveTo(downloadButtonLocation[0], downloadButtonLocation[1], duration=0.5)
        pyautogui.click()
    # 等待下载开始，下载图标由完成转为正在下载
    time.sleep(10)
    # 下载期间，检测下载图标为非完成状态，此时等待下载完成
    while True:
        downloadDoneLocation = Location(f'{folderPath}downloadDone.png')
        if downloadDoneLocation is None:
            time.sleep(1)
        else:
            break
