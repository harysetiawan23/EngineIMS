import Connection as connect
import MySQLdb

#Prepration
curr_bank = connect.db_bank.cursor()

#BANK

#INSERT
def insert_transasi(NO_REKENING,KODE_TRANSAKSI,TOTAL,TANGGAL_TRANSAKSI):
    try:
        script = "INSERT INTO `tb_transaksi` (`no_rekening`, `kode_transaksi`, `total`, `status`, `tanggal_transaksi`) " \
                 "VALUES ('%s','%s','%s','0','%s')"%(NO_REKENING,KODE_TRANSAKSI,TOTAL,TANGGAL_TRANSAKSI)
        curr_bank.execute(script)
        connect.db_bank.commit()
    except MySQLdb.Error as e:
        print("INSERT ERROR ",e)




