# -*- coding: utf-8 -*-

import MySQLdb

if __name__ == "__main__":

    connector = MySQLdb.connect(host="http://shower.human.waseda.ac.jp/~sugaya/Tpis_System", db="personal_data", user="sugaya", passwd="5296", charset="utf8")
    cursor = connector.cursor()

    sql = u"insert into test_table values('1','python')"
    cursor.execute(sql)
    sql = u"insert into test_table values('2','パイソン')"
    cursor.execute(sql)
    sql = u"insert into test_table values('3','ぱいそん')"
    cursor.execute(sql)

    connector.commit()

    cursor.close()
    connector.close()
