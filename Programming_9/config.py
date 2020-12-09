import pymysql

DB_URI = "mysql+pymysql://{user}:{password}@{host}:{port}/{db}".format(user='root', password='12345678', host="127.0.0.1",
                                                                       port="3306", db="departments")
