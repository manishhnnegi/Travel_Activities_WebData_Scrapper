import os

def autofolder_creation(folder_nm):
    try:
        if not os.path.exists(folder_nm):
            x = os.getcwd()
            parent = x
            child = folder_nm
            path = os.path.join(parent, child)
            os.mkdir(path)
            print(path)
            print("foldercreated succesfully")
        else:
            print("foldder already exist")
    except Exception as e:
        print("error due to ___",e)

