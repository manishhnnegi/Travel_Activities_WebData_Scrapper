# creating excel file
from modularproject.creatFilPath import *
import time
from openpyxl import Workbook

def creatExcel(zpped_lists, folder_nm, keyword):
    try:
        wb = Workbook()
        sh1 = wb.active

        for x in list(zpped_lists):
            try:
                sh1.append(x)
            except Exception as e:
                print(e)
        time.sleep(15)
        t = autofile_path(keyword, folder_nm)
        wb.save(t)
    except:
        print("excel not created")
    print("data collected successfully")
