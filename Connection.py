import MySQLdb

# koneksi ke db penghubung database bank dengan database toko
db_konduktor = MySQLdb.connect(host="localhost",
                               user="root",
                               password="",
                               db="db_bank_toko")

# koneksi ke db penghubung database
db_bank = MySQLdb.connect(host="localhost",
                          user="root",
                          password="",
                          db="db_bank")

#koneksi ke db store
db_store = MySQLdb.connect(host="localhost",
                          user="root",
                          password="",
                          db="db_cloud_store")