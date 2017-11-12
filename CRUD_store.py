import Connection as connect
import MySQLdb

#Prepration
curr_store = connect.db_store.cursor()

#BANK

#INSERT
def insert_transasi(NO_REKENING,ID_USER,KODE_TRANSAKSI,TOTAL,KETERANGAN):
    try:
        script = " INSERT INTO `tb_transaksi` (`id_user`, `no_rekening`, `tanggal_transaksi`, `status`, `total`, `kode_transaksi`,`detail_transaksi`) " \
                 "VALUES ('%s', '%s', NOW(), '0', '%s', '%s','%s'); "%(ID_USER,NO_REKENING,TOTAL,KODE_TRANSAKSI,KETERANGAN)
        curr_store.execute(script)
        connect.db_store.commit()
    except MySQLdb.Error as e:
        print("INSERT ERROR ",e)


def update_status(KODE_TRANSAKSI,STATUS):
    try:
        script = "UPDATE `tb_transaksi` SET `status` = '%s' WHERE `kode_transaksi` = '%s'; "%(STATUS,KODE_TRANSAKSI)
        curr_store.execute(script)
        connect.db_store.commit()
    except MySQLdb.Error as e:
        print("UPDATE ERROR ",e)
