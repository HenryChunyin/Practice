import os, ProjectChoose, move_files,read_permision

#归档路径指定
print('请指定一个\033[1;32m归档文件夹\033[0m，文件整理后，所有文件将存储在该文件夹中。\n\033[1;31m注意：文件的分类是通过快捷方式实现\033[0m。\n')
arch_path=input('请输入归档文件夹的\033[4m绝对路径\033[0m：\n')

#主分类
classifications={
    '1':'项目类别',
    '2':'查看类别(仅内部，非内部)',
    '3':'标准/临时类别'
}

#当前目录
base_path = os.path.dirname(os.path.abspath(__file__))
cwd=os.getcwd()
#分类
for name in os.listdir():
    print(
        '\n当前文件夹整理中……\n',
        f"将文件\033[1;34m{name}\033[0m按照下列哪种（几种）类别归类？\n",
        " ".join([f"{k}.{v}\n" for k, v in classifications.items()])
    )
    chr = input('输入序号，逗号隔开，回车跳过:\n')  #str

    chr_list = chr.split(",")
    if not set(chr_list) <= set(list(classifications.keys())):  #跳过当前文件
        continue
    else:
        move_files.move_files(cwd,name,arch_path) #先归档，再生成分类快捷方式
        for item in chr_list:
            if int(item) == 1:
                ProjectChoose.project(name,cwd,arch_path)
            elif int(item) == 2:
                read_permision.read_permision(name,cwd,arch_path)
            else:
                read_permision.std_tmp(name,cwd,arch_path)

