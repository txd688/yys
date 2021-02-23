# 1.0 版本 适用于房主

import pyautogui
import random
import time

# 这是作为房主有个'挑战'按钮事件

# 产生随机数
def randNum(x, y):
    return round(random.uniform(x, y),3);

n = 0;

while True:
    # 点击挑战按钮,有两个坐标分别为x(randNum(1320,1377))和y(randNum(1320,1377))，可以自由设置。
    pyautogui.click(x=randNum(1320,1377), y=randNum(720,778), clicks=1, interval=randNum(1,4), button='left', duration=randNum(1,3), tween=pyautogui.linear);
    # 随机游戏时间，我的设置在15s-28s之间。可以自由设置
    time.sleep(randNum(15,28));
    # 这是游戏结束后的动画，连点3下(如果不需要可以去掉)
    pyautogui.click(x=randNum(100,1377), y=randNum(80,300), clicks=3, interval=randNum(1,3), button='left', duration=randNum(1,3), tween=pyautogui.linear);
    # 这是点击屏幕继续的页面，返回到主页
    pyautogui.click(x=randNum(100,1377), y=randNum(80,600), clicks=1, interval=randNum(1,3), button='left', duration=randNum(1,3), tween=pyautogui.linear);
    n += 1;
    print(n);
    time.sleep(randNum(1,3));
   
