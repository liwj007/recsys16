
"""Save data to table `small_sample`(MyISAM) or `small_sample_2`(InnoDB)

data means csv file
"""

import sys
import csv
import pymysql
from collections import namedtuple

script, csv_file_path = sys.argv

with open(csv_file_path + "/small_sample.csv","r") as f:
    spamreader = csv.reader(f,delimiter='\t')
    headers = next(spamreader)
    Row = namedtuple('Row',headers)

    # establish connection
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root',
            passwd='shi520shi', db='recsys16', charset='UTF8')
    cur=conn.cursor()

    n = 0
    for r in spamreader:
        row = Row(*r)

        id = int(row.id)
        usr_id = int(row.user_id)
        itm_id = int(row.item_id)
        ser = int(row.serial)
        lab = int(row.label)

        #flag = True

        sj_t_11n = int(row.sj_title_1_1_n)
        sj_t_11p = int(row.sj_title_1_1_p)
        sj_t_21n = int(row.sj_title_2_1_n)
        sj_t_21p = int(row.sj_title_2_1_p)
        sj_t_22n = int(row.sj_title_2_2_n)
        sj_t_22p = int(row.sj_title_2_2_p)

        sj_tag_11n = int(row.sj_tags_1_1_n)
        sj_tag_11p = int(row.sj_tags_1_1_p)
        sj_tag_21n = int(row.sj_tags_2_1_n)
        sj_tag_21p = int(row.sj_tags_2_1_p)
        sj_tag_22n = int(row.sj_tags_2_2_n)
        sj_tag_22p = int(row.sj_tags_2_2_p)

        sj_g_11n = int(row.sj_geo_1_1_n)
        sj_g_11p = int(row.sj_geo_1_1_p)
        sj_g_21n = int(row.sj_geo_2_1_n)
        sj_g_21p = int(row.sj_geo_2_1_p)
        sj_g_22n = int(row.sj_geo_2_2_n)
        sj_g_22p = int(row.sj_geo_2_2_p)

        sj_di_11n = int(row.sj_dis_1_1_n)
        sj_di_11p = int(row.sj_dis_1_1_p)
        sj_di_21n = int(row.sj_dis_2_1_n)
        sj_di_21p = int(row.sj_dis_2_1_p)
        sj_di_22n = int(row.sj_dis_2_2_n)
        sj_di_22p = int(row.sj_dis_2_2_p)

        sj_cl_11n = int(row.sj_cl_1_1_n)
        sj_cl_11p = int(row.sj_cl_1_1_p)
        sj_cl_21n = int(row.sj_cl_2_1_n)
        sj_cl_21p = int(row.sj_cl_2_1_p)
        sj_cl_22n = int(row.sj_cl_2_2_n)
        sj_cl_22p = int(row.sj_cl_2_2_p)

        sj_emp_11n = int(row.sj_emp_1_1_n)
        sj_emp_11p = int(row.sj_emp_1_1_p)
        sj_emp_21n = int(row.sj_emp_2_1_n)
        sj_emp_21p = int(row.sj_emp_2_1_p)
        sj_emp_22n = int(row.sj_emp_2_2_n)
        sj_emp_22p = int(row.sj_emp_2_2_p)

        usj_t_1n = int(row.usj_title_1_n)
        usj_t_1p = int(row.usj_title_1_p)
        usj_t_2n = int(row.usj_title_2_n)
        usj_t_2p = int(row.usj_title_2_p)
        usj_t_3n = int(row.usj_title_3_n)
        usj_t_3p = int(row.usj_title_3_p)

        usj_tag_1n = int(row.usj_tags_1_n)
        usj_tag_1p = int(row.usj_tags_1_p)
        usj_tag_2n = int(row.usj_tags_2_n)
        usj_tag_2p = int(row.usj_tags_2_p)
        usj_tag_3n = int(row.usj_tags_3_n)
        usj_tag_3p = int(row.usj_tags_3_p)

        usj_g_1n = int(row.usj_geo_1_n)
        usj_g_1p = int(row.usj_geo_1_p)
        usj_g_2n = int(row.usj_geo_2_n)
        usj_g_2p = int(row.usj_geo_2_p)
        usj_g_3n = int(row.usj_geo_3_n)
        usj_g_3p = int(row.usj_geo_3_p)

        usj_di_1n = int(row.usj_dis_1_n)
        usj_di_1p = int(row.usj_dis_1_p)
        usj_di_2n = int(row.usj_dis_2_n)
        usj_di_2p = int(row.usj_dis_2_p)
        usj_di_3n = int(row.usj_dis_3_n)
        usj_di_3p = int(row.usj_dis_3_p)

        usj_cl_1n = int(row.usj_cl_1_n)
        usj_cl_1p = int(row.usj_cl_1_p)
        usj_cl_2n = int(row.usj_cl_2_n)
        usj_cl_2p = int(row.usj_cl_2_p)
        usj_cl_3n = int(row.usj_cl_3_n)
        usj_cl_3p = int(row.usj_cl_3_p)

        usj_emp_1n = int(row.usj_emp_1_n)
        usj_emp_1p = int(row.usj_emp_1_p)
        usj_emp_2n = int(row.usj_emp_2_n)
        usj_emp_2p = int(row.usj_emp_2_p)
        usj_emp_3n = int(row.usj_emp_3_n)
        usj_emp_3p = int(row.usj_emp_3_p)

        jsu_j_1n = int(row.jsu_jr_1_n)
        jsu_j_1p = int(row.jsu_jr_1_p)
        jsu_j_2n = int(row.jsu_jr_2_n)
        jsu_j_2p = int(row.jsu_jr_2_p)
        jsu_j_3n = int(row.jsu_jr_3_n)
        jsu_j_3p = int(row.jsu_jr_3_p)

        jsu_f_1n = int(row.jsu_f_1_n)
        jsu_f_1p = int(row.jsu_f_1_p)
        jsu_f_2n = int(row.jsu_f_2_n)
        jsu_f_2p = int(row.jsu_f_2_p)
        jsu_f_3n = int(row.jsu_f_3_n)
        jsu_f_3p = int(row.jsu_f_3_p)

        jsu_d_1n = int(row.jsu_d_1_n)
        jsu_d_1p = int(row.jsu_d_1_p)
        jsu_d_2n = int(row.jsu_d_2_n)
        jsu_d_2p = int(row.jsu_d_2_p)
        jsu_d_3n = int(row.jsu_d_3_n)
        jsu_d_3p = int(row.jsu_d_3_p)

        jsu_cl_1n = int(row.jsu_cl_1_n)
        jsu_cl_1p = int(row.jsu_cl_1_p)
        jsu_cl_2n = int(row.jsu_cl_2_n)
        jsu_cl_2p = int(row.jsu_cl_2_p)
        jsu_cl_3n = int(row.jsu_cl_3_n)
        jsu_cl_3p = int(row.jsu_cl_3_p)

        jsu_dis_1n = int(row.jsu_dis_1_n)
        jsu_dis_1p = int(row.jsu_dis_1_p)
        jsu_dis_2n = int(row.jsu_dis_2_n)
        jsu_dis_2p = int(row.jsu_dis_2_p)
        jsu_dis_3n = int(row.jsu_dis_3_n)
        jsu_dis_3p = int(row.jsu_dis_3_p)

        jsu_y_1n = int(row.jsu_y_1_n)
        jsu_y_1p = int(row.jsu_y_1_p)
        jsu_y_2n = int(row.jsu_y_2_n)
        jsu_y_2p = int(row.jsu_y_2_p)
        jsu_y_3n = int(row.jsu_y_3_n)
        jsu_y_3p = int(row.jsu_y_3_p)

        u_jr = str(row.u_jobroles)
        u_cl = int(row.u_career_level)
        u_dis = int(row.u_discipline_id)
        u_idy = int(row.u_industry_id)
        u_co = str(row.u_country)
        u_r = int(row.u_region)
        u_ex_n = int(row.u_experience_n_entries_class)
        u_ex_y_p = int(row.u_experience_years_experience)
        u_ex_y_c = int(row.u_experience_years_in_current)
        u_d = int(row.u_edu_degree)
        u_fi = str(row.u_edu_fieldofstudies)

        i_t = str(row.i_title)
        i_cl = int(row.i_career_level)
        i_dis = int(row.i_discipline_id)
        i_idy = int(row.i_industry_id)
        i_co = str(row.i_country)
        i_r = int(row.i_region)
        i_lat = float(row.i_latitude)
        i_log = float(row.i_longitude)
        i_emp = int(row.i_employment)
        i_tag = str(row.i_tags)

        sql = "INSERT IGNORE INTO `small_sample` (id,user_id,item_id,serial,label,sj_title_1_1_n,sj_title_1_1_p,sj_title_2_1_n,sj_title_2_1_p,sj_title_2_2_n,sj_title_2_2_p,sj_tags_1_1_n,sj_tags_1_1_p,sj_tags_2_1_n,sj_tags_2_1_p,sj_tags_2_2_n,sj_tags_2_2_p,sj_geo_1_1_n,sj_geo_1_1_p,sj_geo_2_1_n,sj_geo_2_1_p,sj_geo_2_2_n,sj_geo_2_2_p,sj_dis_1_1_n,sj_dis_1_1_p,sj_dis_2_1_n,sj_dis_2_1_p,sj_dis_2_2_n,sj_dis_2_2_p,sj_cl_1_1_n,sj_cl_1_1_p,sj_cl_2_1_n,sj_cl_2_1_p,sj_cl_2_2_n,sj_cl_2_2_p,sj_emp_1_1_n,sj_emp_1_1_p,sj_emp_2_1_n,sj_emp_2_1_p,sj_emp_2_2_n,sj_Emp_2_2_p,usj_title_1_n,usj_title_1_p,usj_title_2_n,usj_title_2_p,usj_title_3_n,usj_title_3_p,usj_tags_1_n,usj_tags_1_p,usj_tags_2_n,usj_tags_2_p,usj_tags_3_n,usj_tags_3_p,usj_geo_1_n,usj_geo_1_p,usj_geo_2_n,usj_geo_2_p,usj_geo_3_n,usj_geo_3_p,usj_dis_1_n,usj_dis_1_p,usj_dis_2_n,usj_dis_2_p,usj_dis_3_n,usj_dis_3_p,usj_cl_1_n,usj_cl_1_p,usj_cl_2_n,usj_cl_2_p,usj_cl_3_n,usj_cl_3_p,usj_emp_1_n,usj_emp_1_p,usj_emp_2_n,usj_emp_2_p,usj_emp_3_n,usj_emp_3_p,jsu_jr_1_n,jsu_jr_1_p,jsu_jr_2_n,jsu_jr_2_p,jsu_jr_3_n,jsu_jr_3_p,jsu_f_1_n,jsu_f_1_p,jsu_f_2_n,jsu_f_2_p,jsu_f_3_n,jsu_f_3_p,jsu_d_1_n,jsu_d_1_p,jsu_d_2_n,jsu_d_2_p,jsu_d_3_n,jsu_d_3_p,jsu_cl_1_n,jsu_cl_1_p,jsu_cl_2_n,jsu_cl_2_p,jsu_cl_3_n,jsu_cl_3_p,jsu_dis_1_n,jsu_dis_1_p,jsu_dis_2_n,jsu_dis_2_p,jsu_dis_3_n,jsu_dis_3_p,jsu_y_1_n,jsu_y_1_p,jsu_y_2_n,jsu_y_2_p,jsu_y_3_n,jsu_y_3_p,u_jobroles,u_career_level,u_discipline_id,u_industry_id,u_country,u_region,u_experience_n_entries_class,u_experience_years_experience,u_experience_years_in_current,u_edu_degree,u_edu_fieldofstudies,i_title,i_career_level,i_discipline_id,i_industry_id,i_country,i_region,i_latitude,i_longitude,i_employment,i_tags) VALUES ('%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%d','%s','%d','%d','%d','%s','%d','%d','%d','%d','%d','%s','%s','%d','%d','%d','%s','%d','%f','%f','%d','%s')"

        cur.execute(sql % (id,usr_id,itm_id,ser,lab,sj_t_11n,sj_t_11p,sj_t_21n,sj_t_21p,sj_t_22n,sj_t_22p,sj_tag_11n,sj_tag_11p,sj_tag_21n,sj_tag_21p,sj_tag_22n,sj_tag_22p,sj_g_11n,sj_g_11p,sj_g_21n,sj_g_21p,sj_g_22n,sj_g_22p,sj_di_11n,sj_di_11p,sj_di_21n,sj_di_21p,sj_di_22n,sj_di_22p,sj_cl_11n,sj_cl_11p,sj_cl_21n,sj_cl_21p,sj_cl_22n,sj_cl_22p,sj_emp_11n,sj_emp_11p,sj_emp_21n,sj_emp_21p,sj_emp_22n,sj_emp_22p,usj_t_1n,usj_t_1p,usj_t_2n,usj_t_2p,usj_t_3n,usj_t_3p,usj_tag_1n,usj_tag_1p,usj_tag_2n,usj_tag_2p,usj_tag_3n,usj_tag_3p,usj_g_1n,usj_g_1p,usj_g_2n,usj_g_2p,usj_g_3n,usj_g_3p,usj_di_1n,usj_di_1p,usj_di_2n,usj_di_2p,usj_di_3n,usj_di_3p,usj_cl_1n,usj_cl_1p,usj_cl_2n,usj_cl_2p,usj_cl_3n,usj_cl_3p,usj_emp_1n,usj_emp_1p,usj_emp_2n,usj_emp_2p,usj_emp_3n,usj_emp_3p,jsu_j_1n,jsu_j_1p,jsu_j_2n,jsu_j_2p,jsu_j_3n,jsu_j_3p,jsu_f_1n,jsu_f_1p,jsu_f_2n,jsu_f_2p,jsu_f_3n,jsu_f_3p,jsu_d_1n,jsu_d_1p,jsu_d_2n,jsu_d_2p,jsu_d_3n,jsu_d_3p,jsu_cl_1n,jsu_cl_1p,jsu_cl_2n,jsu_cl_2p,jsu_cl_3n,jsu_cl_3p,jsu_dis_1n,jsu_dis_1p,jsu_dis_2n,jsu_dis_2p,jsu_dis_3n,jsu_dis_3p,jsu_y_1n,jsu_y_1p,jsu_y_2n,jsu_y_2p,jsu_y_3n,jsu_y_3p,u_jr,u_cl,u_dis,u_idy,u_co,u_r,u_ex_n,u_ex_y_p,u_ex_y_c,u_d,u_fi,i_t,i_cl,i_dis,i_idy,i_co,i_r,i_lat,i_log,i_emp,i_tag))

        n += 1

        if n % 1000 == 0:
            conn.commit()
            print("line:", n)
        else:
            pass

conn.commit()
      
cur.close()
conn.close()    

print("ok")
