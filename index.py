
import pyautogui
import random
import time


# 随机数
def rand_num(x, y):
    return round(random.uniform(x, y),3);

# 判断是否为数字
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
 
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
 
    return False

# 位置，偏移量，点击次数，时间间隔，鼠标移动持续时间，按键
def mouse_click(img, offset, click_number, interval, duration, keydown, des, n = False):
    loc = pyautogui.locateCenterOnScreen(img)
    if des:
        print(des + str(loc))
    if loc is not None:
        loc2 = [int(loc.x) + rand_num(offset[0], offset[1]), int(loc.y) + rand_num(offset[2], offset[3])]
        # 模拟鼠标点击事件
        pyautogui.click(loc2[0], loc2[1], clicks = click_number, interval = interval, duration = duration, button = keydown)
        if n :
            print('成功执行{}次'.format(n))
            return n + 1
    return n
    

def game_start(num):
    num = int(num)
    all_num = 0
    n = 1
    while int(n) < num:
        # mouse_click方法可以根据自己要求进行更改
        mouse_click('D:/yysImages/tiaozhan.PNG',[-50, 50, -10, 10], 1, rand_num(0,1), 0.2, 'left', '不间断获取挑战坐标：')
            
        mouse_click('D:/yysImages/shengli.PNG',[-200, 200, -20, 20], 3, rand_num(0,0.5), 0.1, 'left', '不间断获取胜利坐标：')

        n = mouse_click('D:/yysImages/jiesu.PNG',[-250, 250, -100, 100], 1, rand_num(0,1), 0.2, 'left', '不间断获取结束坐标：', n)
        
        all_num += 1

        if(all_num > 100):
            
            print('一直未找到坐标，程序将取消执行!')

            break

        time.sleep(rand_num(3,5))

if __name__ == "__main__":
    print('仅供学习参考，不允许用于任何商业用途。')
    game_number= input('请输入御魂执行次数：\n')
    
    if is_number(game_number):
        
        num = game_number

    else:
        num = 999999999

    # print('程序开始执行！！！！')
    # num = 10000000000
    
    game_start(num)
   
