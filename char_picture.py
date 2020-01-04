#从PIL库导入Image模块
from PIL import Image

#导入os库
import os

#定义字符列表
ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")

#计算每一个字符的区间
unit = 256 / len(ascii_char)

#定义图片文件路径
path = r'C:\Users\MyPC\Desktop'

#定义图片文件名
file = 'huaji.jfif'

#定义图片精细程度，数字越大，图片越精细
parameter = 100

#根据灰度值大小取出区间内对应的字符
def get_char(gray):
    return ascii_char[int(gray/unit)]

if __name__ == '__main__':
    #打开图片文件并赋值给img
    img = Image.open(os.path.join(path, file))
    
    #调整文件的尺寸，元组第一个元素为新图片的宽，第二个元素为新图片的高
    img = img.resize((int(img.width / img.height * parameter * 1.8) , parameter))
    
    #把图片转换为灰度值图片
    img = img.convert('L')

    #定义要输出的字符串
    txt = ""

    #遍历图片的每一个像素
    for height in range(img.height):
        for width in range(img.width):
            txt += get_char(img.getpixel((width, height)))
        txt += '\n'
        
    #保存为文件
    with open(os.path.join(path, file.split('.')[0] + '.txt'),'w') as f:
        f.write(txt)

    print('文件已保存')
