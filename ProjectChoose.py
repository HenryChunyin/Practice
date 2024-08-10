import NewProjects, os, shortcut

def project(name,base_path,arch_path):
    print("按照项目归类中……\n")
    projects = []
    # "项目"总目录
    proj_dir = os.path.join(base_path, '项目')
    if not os.path.exists(proj_dir):
        os.mkdir(proj_dir)
    # 获取项目列表
    if os.listdir(proj_dir) == []:
        print('当前尚无项目，请先添加项目')
        projects = NewProjects.NewProjects()
        for item in projects:
            os.mkdir(os.path.join(proj_dir, item))  # 一个项目一个子目录
    else:
        for item in os.listdir(proj_dir):
            if os.path.isdir(os.path.join(proj_dir,item)):
              projects.append(item)


    def chooseProject():
        while True:
            proj_dic = dict(zip(range(1, len(projects) + 1), projects))
            print('请输入文件归入的项目编号：', proj_dic, "\n新增项目请按N")
            proj_num = input()
            if not proj_num == 'N':
                return proj_dic[int(proj_num)]
            new_add_projects=NewProjects.NewProjects()
            for item in new_add_projects:
                os.mkdir(os.path.join(proj_dir, item))
                projects.append(item)


    project_name = chooseProject()
    shortcut_path=os.path.join(proj_dir, project_name,name)
    dest_path=os.path.join(arch_path,name)
    shortcut.createshortcut(shortcut_path,dest_path)





