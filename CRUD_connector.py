import Connection as connect
import MySQLdb

#Prepration
curr_connector = connect.db_konduktor.cursor()


def update_status(KODE_TRANSAKSI,STATUS):
    try:
        script = "UPDATE `tb_transaksi` SET `status` = '%s' WHERE `kode_transaksi` = '%s'; "%(STATUS,KODE_TRANSAKSI)
        curr_connector.execute(script)
        connect.db_konduktor.commit()
    except MySQLdb.Error as e:
        print("UPDATE ERROR ",e)



def insert_transaksi(NO_REKENING,KODE_TRANSAKSI,TOTAL,TANGGAL_TRANSAKSI):
    try:
        script = "INSERT INTO `tb_transaksi` (`no_rekening`, `kode_transaksi`, `total`, `status`, `tanggal_transaksi`) " \
                 "VALUES ('%s','%s','%s','0','%s')" % (NO_REKENING, KODE_TRANSAKSI, TOTAL, TANGGAL_TRANSAKSI)
        curr_connector.execute(script)
        connect.db_konduktor.commit()
        print(script)
    except MySQLdb.Error as e:
        print("INSERT ERROR ",e)
