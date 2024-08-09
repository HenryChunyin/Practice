import NewProjects, os

projects = []
# 当前目录与"项目"目录
base_path = os.path.dirname(os.path.abspath(__file__))
proj_dir = os.path.join(base_path, '项目')

# 获取项目列表
if os.listdir(proj_dir) == []:
    print('当前尚无项目，请先添加项目')
    projects = NewProjects.NewProjects()
    for item in projects:
        os.mkdir(os.path.join(proj_dir, item))  # 一个项目一个目录
else:
    for item in os.listdir(proj_dir):
        if os.path.isdir(item):
            projects.append(item)


def chooseProject():
    proj_dic = dict(zip(range(1, len(projects) + 1), projects))
    print('请输入项目编号：', proj_dic)
    proj_num = input()
    return proj_dic[proj_num]


os.path.join(proj_dir, chooseProject())
