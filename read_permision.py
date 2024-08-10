
import os,shortcut

permission={
    '1':'仅内部文件',
    '2':'非内部文件'
}

std_tmp_dic={
    '1':'标准材料',
    '2':'临时材料'
}
def read_permision(name,base_path,arch_path):
    print(
        "按照查看类别归类中……\n",
        f"将文件\033[1;34m{name}\033[0m归为哪个类别？\n",
        " ".join([f"{k}.{v}\n" for k, v in permission.items()])
    )
    while True:
        chr = input('输入序号:\n')
        if set(chr) <= set(list(permission.keys())):
            permit = permission[chr]
            break
        else:
            print('输入错误！')
    # 查看类别
    inner_dir = os.path.join(base_path, '查看类别','仅内部文件')
    outer_dir = os.path.join(base_path, '查看类别','非内部文件')
    if not os.path.exists(inner_dir):
        os.makedirs(inner_dir)
    if not os.path.exists(outer_dir):
        os.makedirs(outer_dir)



    shortcut_path = os.path.join(base_path, '查看类别', permit, name)
    dest_path = os.path.join(arch_path,name)
    shortcut.createshortcut(shortcut_path, dest_path)


def std_tmp(name,base_path,arch_path):
    print(
        "按照标准/临时材料归类中……\n",
        f"将文件\033[1;34m{name}\033[0m归为哪个类别？\n",
        " ".join([f"{k}.{v}\n" for k, v in std_tmp_dic.items()])
    )
    while True:
        chr = input('输入序号:\n')
        if set(chr) <= set(list(std_tmp_dic.keys())):
            permit = std_tmp_dic[chr]
            break
        else:
            print('输入错误！')
    # 查看类别
    std_dir = os.path.join(base_path, '材料类别','标准材料')
    tmp_dir = os.path.join(base_path, '材料类别','临时材料')
    if not os.path.exists(std_dir):
        os.makedirs(std_dir)
    if not os.path.exists(tmp_dir):
        os.makedirs(tmp_dir)



    shortcut_path = os.path.join(base_path, '材料类别', permit, name)
    dest_path = os.path.join(arch_path,name)
    shortcut.createshortcut(shortcut_path, dest_path)