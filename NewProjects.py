def NewProjects():
    n = 1
    projects = []
    while True:
        print(f'请输入第{n}个项目名称(退出请输入大写N):')
        prj = input()
        if prj != 'N':
            projects.append(prj)
            n += 1
        elif prj == None:
            print('请输入有效名称！')
        else:
            break
    print('录入完毕！')
    return projects



