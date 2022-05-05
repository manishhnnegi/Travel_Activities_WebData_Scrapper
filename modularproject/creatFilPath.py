import os
import random
def autofile_path(keyword, folder_nm):
    try:
        no = random.random()
        xno = round(no, 2)
        rno = str(xno)
        x = os.getcwd()
        parent = os.path.join(x, folder_nm)
        child = keyword + "data" + rno + ".xlsx"
        file_path = os.path.join(parent, child)
        return file_path
        print("filecreated succesfully")
    except Exception as e:
        print("error due to ___",e)