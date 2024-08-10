import os
# # a= {1: '项目1', 2: '项目2', 3: '项目3'}
basepath=os.path.dirname(os.path.abspath(__file__))
dir=os.listdir(basepath)
print(dir[3])
filepath=os.path.join(basepath,dir[3])
print(filepath)
print(
filepath.split(".")[0]+'.lnk'

)


inner_dir = os.path.join(basepath, '查看类别','仅内部文件')
outer_dir = os.path.join(basepath, '查看类别','非内部文件')
if not os.path.exists(inner_dir):
    os.makedirs(inner_dir)
if not os.path.exists(outer_dir):
    os.makedirs(outer_dir)






#
# list1=['1','2','3']
# #
# # chr =['1','2']
# #
# # print(not set(chr)<set(['1','2','3']))
#
# classifications={
#     '1':'项目类别',
#     '2':'查看类别(仅内部，非内部)',
#     '3':'标准/临时类别'
# }
#
# print(list(classifications.keys()))

# chr = input()

# if len(chr) == 1:
#     print(1)
# else:print('not 1')
# permission={
#     '1':'仅内部文件',
#     '2':'非内部文件'
# }
# print(permission)
#
# while True:
#     chr = input('输入序号:\n')
#     if set(chr) <= set(list(permission.keys())):
#         permit = permission[chr]
#         break
#     else:
#         print('输入错误！')
#
# print(permit)

# if not set(chr_list) <= set(list(classifications.keys()))