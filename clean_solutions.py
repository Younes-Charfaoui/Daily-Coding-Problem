import os 

def get_files(skip=True):
    files = os.listdir()
    needed_folders = []
    for file in files:
        if skip:
            if '.' in file or '0' in file or "LICENSE" == file or "data_structure" == file:
                continue
        needed_folders.append(file)
    return needed_folders

def clean_content(files):
    for file in files:
        if '.py' in file:
            file_obj = open(file, 'r')
            content = file_obj.readlines()
            content = ''.join(content[:])
            task = content.split('"""')[1]
            file_obj = open(file, 'w')
            file_obj.truncate()
            task = '"""' + task + '"""'
            file_obj.write(task)

def remove_solutions():
    needed_folders = get_files()
    for folder in needed_folders:
        os.chdir(folder)
        files = get_files(skip=False)
        clean_content(files)
        os.chdir("..")

if __name__ == '__main__':
    remove_solutions()
    