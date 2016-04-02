# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 21:40:49 2016

@author: liwj0
update:syb at Apr 2
"""

import pymysql
import sys

script, file_path = sys.argv

conn = pymysql.connect(host="127.0.0.1", port=3306, user="root",
        passwd="shi520shi", db="recsys16", charset="UTF8")
cur=conn.cursor()
cur.execute("SELECT user_id FROM tar_usr")
targets = cur.fetchall()

print(1)
cur.execute("SELECT	item_id,	SUM(1) FROM	join_uia WHERE	i_active_during_test = 1 AND interaction_type IN (1, 2, 3) GROUP BY	item_id ORDER BY	2 DESC LIMIT 30;")
populor_items = cur.fetchall()

import csv
print(2)
with open(file_path + '/merge_p.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter='\t', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(['user_id','recommended_items'])

    for r in targets:
        u_id=r[0]
        cur.execute("SELECT item_id, SUM(1) FROM join_uia WHERE  user_id=%d AND i_active_during_test=1 AND interaction_type in (1,2,3) GROUP BY item_id ORDER BY 2 DESC LIMIT 30" % (u_id))
        items = cur.fetchall()
        
        lst= [i[0] for i in items]
        
        num=0
        while len(lst)<30:
            if populor_items[num][0] not in lst:
                lst.append(populor_items[num][0])
            num+=1
            
        d=[str(i) for i in lst]

        
        spamwriter.writerow([u_id,','.join(d)])
cur.close()
conn.close()
