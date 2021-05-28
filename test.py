import pyautogui
import cv2

print('启动成功')

# 作为房主

# 查找挑战按钮

# 游戏结束后，点击三次跳过动画

# 结束点击

# 普通识图
def searchButton(img):
  return pyautogui.locateOnScreen(img,confidence=0.9)

# 识图率优化
def searchButton2(img):
  print('启用优化识图')
  # 读取屏幕，并保存到本地
  pyautogui.screenshot('bg.png')
  # 读入背景图片
  gray = cv2.imread("bg.png",0)
   # 读入需要查找的图片
  img_template = cv2.imread(img,0)
  # 得到图片的高和宽
  w, h = img_template.shape[::-1]

  # 模板匹配操作
  res = cv2.matchTemplate(gray,img_template,cv2.TM_SQDIFF)

  # 得到最大和最小值得位置
  min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

  top = min_loc[0]
  left = min_loc[1]
  x = [top, left, w, h]

  return [top,left]
a = searchButton2('./images/1.png')
pyautogui.moveTo(a[0], a[1])
print(searchButton('./images/1.png'));
