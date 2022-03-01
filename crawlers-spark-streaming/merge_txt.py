import os


path = "car_url/"  # 文件夹目录
files = os.listdir(path)
url_list = list()
for i in files:
    with open('{directory}{file}'.format(directory=path, file=i)) as f:
        lines = f.readline()
        url_list += lines.split('-')