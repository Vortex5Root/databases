import sqlite3

import os
from os      import walk
from pathlib import Path

from Libs.v_logger import logg

class database():
    def __init__(self,name):
        self.scripy = []

        self.db_name = name

        self.tb_name = ''

        self.c = ''

        self.logg = logg('database')

        self.path = Path('./database/')
        if not self.path.exists():
            self.path.mkdir()

        #print(not self.if_db_exists())
        if not self.if_db_exists():
            self.conn = sqlite3.connect('./database/'+str(self.db_name).lower()+'.db')
            self.conn.commit()
        else:
            self.conn = sqlite3.connect('./database/'+str(self.db_name).lower()+'.db')


    def create_table(self,variables):
        for to_fix in range(2):
            #print()
            if self.if_db_exists():
                #print('create open')
                if self.tb_name == '':
                    self.logg.logg = 'error'
                    self.logg.lprint(' Table not defined')
                else:
                    c = self.conn.cursor()
                    sqlcomd = "CREATE TABLE IF NOT EXISTS " + str(self.tb_name)+"( ell text,"+variables+")"
                    #print(sqlcomd)
                    c.execute(sqlcomd)
                    self.conn.commit()
                    #self.logg.logg = 'success'
                    #self.logg.lprint(f'{self.tb_name} Table added successfaly')
                #break
            else:
                self.load_or_gen()

    def add_info(self,infos,query=False):
        rows = self.get_rows()
        #print(Rows)
        c = self.conn.cursor()
        sqlcmd = "INSERT INTO "+self.tb_name+"("
        conta = 0
        for row in rows:
            if conta == len(rows)-1:
                sqlcmd = sqlcmd + str(row)
            else:
                sqlcmd = sqlcmd + str(row) + ","
            conta +=1
        data = ''
        for info in str(infos).split(','):
            if str(infos).split(',').index(info) == len(str(infos).split(','))-1:
                data += f"'{info}'"
            else:
                data += f"'{info}',"
        sqlcmd = sqlcmd + ") VALUES ('All'," +data+");"
        #print(sqlcmd)
        if query == True:
            self.scripy.append(sqlcmd)
            print(f"{len(self.scripy)}{' '*10}",end='\r')
            if len(self.scripy) >= 5000:#106872
                c.execute('BEGIN TRANSACTION')
                for query in self.scripy:
                    c.execute(query)
                c.execute('COMMIT')
                self.scripy = []
            return None
        c.execute(str(sqlcmd))
        self.conn.commit()

    def commint_script(self):
        c = self.conn.cursor()
        c.execute('BEGIN TRANSACTION')
        for query in self.scripy:
            c.execute(query)
        c.execute('COMMIT')

    # Functions of api

    def if_db_exists(self):
        for (dirpath, dirnames, filenames) in walk('./database'):
            #print(filenames)
            #print(self.db_name)
            #print(filenames)
            if f"{self.db_name}.db" in filenames:
                return True
            else:
                return False

    def load_or_gen(self):
        if not self.if_db_exists():
            self.conn = sqlite3.connect('./database/'+str(self.db_name).lower()+'.db')
            self.conn.commit()
            self.logg.logg = 'success'
            self.logg.lprint(f' {self.db_name} add successfaly')
        else:
            self.conn = sqlite3.connect('./database/'+str(self.db_name).lower()+'.db')
            self.logg.logg = 'success'
            self.logg.lprint(f' {self.db_name} loaded successfaly')

    def rename_db(self,db_name):
        os.rename(r'./DataBase/'+self.db_name+'.db',r'./DataBase/'+db_name+'.db')
        self.db_name = db_name
        self.load_or_gen()
        return True


    #    Gets

    def get_rows(self):
        #test = self.load_or_gen()
        c = self.conn.cursor()
        sqlcomd = "SELECT * FROM "+str(self.tb_name)
        try:
            Rows = c.execute(sqlcomd)
            names = list(map(lambda x: x[0], c.description))
            self.conn.commit()
            return names
        except:
            self.logg.logg = 'error'
            self.logg.lprint(f' {self.tb_name} not found plz add the table to get rows')

    def get_info(self,code = '',value = '',Expecial=''):
        #self.load_or_gen()
        info = ''
        c = self.conn.cursor()
        if Expecial != '':
            sqlcomd = "SELECT * FROM "+str(self.tb_name) + " " + str(Expecial)
            info = c.execute(sqlcomd)
        elif value == '':
            sqlcomd = "SELECT * FROM "+str(self.tb_name)+" WHERE ell = 'All'"
            info = c.execute(sqlcomd)
        elif code != '' and value == '':
            sqlcomd = "SELECT * FROM " + str(self.tb_name) + " WHERE " + str(code)
            info = c.execute(sqlcomd)
        else:
            sqlcomd = "SELECT * FROM "+str(self.tb_name)+" WHERE "+str(code)+" = '"+str(value)+"'"
            info = c.execute(sqlcomd)
        info = info.fetchall()
        self.conn.commit()
        return info

    def update_info(self,target,set):
        c = self.conn.cursor()
        sqlcmd = f"UPDATE {self.tb_name} SET {set[0]} = '{set[1]}' WHERE {target[0]} = '{target[1]}'" # set = "column = value"
        info = c.execute(sqlcmd)
        self.conn.commit()
        return True


    def get_tables(self,NameOfdb):
        try:
            cursor = self.con.cursor()
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
            tabelas = cursor.fetchall()
            self.con.close()
            return tabelas
        except:
            return False

    def rename_tabel(self,tabel_name):
        try:
            sql = "RENAME TABLE " + str(self.tb_name) +' TO '+ str(tabel_name)+";"
            cursor = self.con.cursor()
            cursor.execute(sql)
            self.con.commit()
            self.load_or_gen()
            self.tb_name = tabel_name
            return True
        except:
            return False
    #Alet Var Type
    def change_type(self,column,new_type):
        try:
            sql = "ALTER TABLE "+str(self.tb_name)+" ALTER COLUMN " + str(column) +" "+str(new_type)+ ";"
            cursor = self.con.cursor()
            cursor.execute(sql)
            self.con.commit()
            return True
        except:
            return False
    #drop tabel
    def del_tabel(self):
        try:
            sql = "DROP TABLE "+str(self.tb_name)+";"
            cursor = self.con.cursor()
            cursor.execute(sql)
            self.con.commit()
            return True
        except:
            return False
            
    #Del DB
    def delete_db(self):
        if self.if_db_exists(self.db_name):
            os.remove(r".\API\DBS"+r'\ '.replace(' ','')+str(self.db_name)+'.db')
            return True
        return False

    #Remove
    def remove_info(self,code = '',value = '',sp=''):
        c = self.conn.cursor()
        if value == '':
            sqlcmd = "DELETE from "+str(self.tb_name)+" where * = *;"
            c.execute(sqlcmd)
        elif code != '' and value == '':
            sqlcmd = "DELETE from " + str(self.tb_name) + " where " + str(code) + "';"
            c.execute(sqlcmd)
        elif code == '' and value == '' and sp != '':
            sqlcmd = "DELETE from " + str(self.tb_name) + " where " + str(sp) + "';"
            c.execute(sqlcmd)
        else:
            sqlcmd = "DELETE from " + str(self.tb_name) + " where "+str(code)+" = '"+str(value)+"';"
            #print(sqlcmd)
            c.execute(sqlcmd)
        self.conn.commit()
        return True
