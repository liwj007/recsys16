# -*- coding: utf-8 -*-

"""制作新的推荐列表，为15万的目标用户

使用俊神的merge_p.csv，和丽姐的lys_rlt_sec.csv
"""

import csv
import pymysql
import sys

script, file_path = sys.argv

conn = pymysql.connect(host="127.0.0.1", port=3306, user="root",
        passwd="shi520shi", db="recsys16", charset="UTF8")
cur=conn.cursor()

# 过滤丽姐的推荐列表，只保留目标用户子集的，同时替换第一个“，”为tab

cur.execute("SELECT user_id FROM tar_usr")
targets = cur.fetchall()
conn.commit()

cur.close()
conn.close()

st = set()
for t in targets:
    st.add(t[0])

lst_fir = sorted(st)

# 第一遍过滤

#with open(file_path + "/lyl_rlt_fir.csv", "w", newline="") as csv_file:
#    spamwriter = csv.writer(csv_file, delimiter='\t', quotechar='|', quoting=csv.QUOTE_MINIMAL)
#    spamwriter.writerow(['user_id','recommended_items'])
#
#    with open(file_path + "/impressionorderresult.csv", "r") as f_2:
#
#        line = 0
#        for r in f_2.readlines():
#
#            if line != 0:
#                r_new = r.replace(",", "\t", 1)
#                lst = r_new.strip().split("\t")
#
#                if lst[0] == "":
#                    pass
#                elif int(lst[0]) in st:
#
#                    if len(lst) == 2:
#                        spamwriter.writerow([lst[0], lst[1]])
#                    else:
#                        print("str split error")
#
#                else:
#                    line += 1
#                    continue
#
#                #if int(lst[0]) in st:
#                #    if len(lst) == 1:
#                #        spawriter.writerow(lst[0], "")
#                #    elif lst[1] == "":
#                #        spawriter.writerow(lst[0], "")
#                #    elif len(lst) == 2:
#                #        spamwriter.writerow([lst[0], lst[1]])
#                #    else:
#                #        print("str filter error")
#                #else:
#                #    print("else")
#                #    line += 1
#                #    continue
#
#            else:
#                pass
#
#            line += 1

# 第二遍过滤，填充成15万行的
dit_fir = {}
with open(file_path + "/lyl_rlt_fir.csv", "r") as f_fir:

    line = 0
    for r in f_fir.readlines(): 
        ui = r.strip().split("\t")

        #if ui[0] not in dit_fir:
        #    dit_fir.update({int(ui[0]): ui[1]})
        #else:
        #    pass

        if line  == 0:
            pass
        elif ui[0] == "":
            pass
        else:
           dit_fir.update({int(ui[0]): ui[1]})

        line += 1


print("length of the dit is", len(dit_fir))

with open(file_path + "lys_rlt_sec.csv", "w", newline="") as f_sec:
    spamwriter = csv.writer(f_sec, delimiter="\t", quotechar="|", 
            quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(['user_id','recommended_items'])

    for u in lst_fir:

        if u in dit_fir:
            spamwriter.writerow([u, dit_fir[u]])
        else:
            spamwriter.writerow([u, ""])

print("save file ok")

# 保存俊神的推荐列表

# 考虑融合
