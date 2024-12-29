from PIL import Image

# 读取img文件
img_file = 'C:\\Users\\wind\\Desktop\\1\\1.png'
im = Image.open(img_file)

# quality 是设置压缩比
im.save('C:\\Users\\wind\\Desktop\\1\\2.png', quality=10)