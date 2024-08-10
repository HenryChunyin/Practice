import shutil,os
def move_files(base_path,file,new_path):
    src = os.path.join(base_path, file)
    dst = os.path.join(new_path, file)
    shutil.move(src, dst)
