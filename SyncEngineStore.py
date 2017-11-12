import Connection as connect
import CRUD_bank
import CRUD_connector
import CRUD_store
import datetime

# connection
commit_conductor = connect.db_konduktor.commit()
commit_bank = connect.db_bank.commit()

# preparation
curr_connector = connect.db_konduktor.cursor()
curr_store = connect.db_store.cursor()

# INSERT PREPERATION

curr_connector.execute("SELECT MAX(tanggal_transaksi) FROM `tb_transaksi` ORDER BY `tanggal_transaksi` DESC")
curr_store.execute("SELECT MAX(tanggal_transaksi) FROM `tb_transaksi` ORDER BY `tanggal_transaksi` DESC")

f = '%Y-%m-%d %H:%M:%S'

row_connector = curr_connector.fetchall()
commit_conductor

row_bank = curr_store.fetchall()
commit_bank

# UPDATE PREPREATION
curr_connector.execute("SELECT `kode_transaksi`,STATUS FROM `tb_transaksi` ORDER BY `tanggal_transaksi` DESC")
curr_store.execute("SELECT `kode_transaksi`,STATUS FROM `tb_transaksi` ORDER BY `tanggal_transaksi` DESC")

status_connector = curr_connector.fetchall()
status_store = curr_store.fetchall()

# BEGIN ENGINE

#GET MAX DATE IN DB_BANK_TOKO AS MAX DATE IN CONNECTOR
for connector in row_connector:
    # fetch data di db_bank_toko
    con_max_date = connector

# GET MAX DATE IN DB_STORE AS A DATABASE OBJECT
for store in row_bank:
    store_max_date = store
    # bigining insert

    # commit connection for a while
    commit_bank
    commit_conductor

print(con_max_date)
print(store_max_date)
print("BEGIN SYNCRONIZATION")
#INSERT SYSNCRONIZED LOGIC ENGINE
if (store_max_date >con_max_date ):
    print("True")
    date = con_max_date[0]

    sql = "SELECT * FROM `tb_transaksi`  WHERE `tanggal_transaksi` > '%s' " % (date)
    print(sql)
    try:
        curr_store.execute(sql)
        if(curr_store.execute(sql)):
            print("True in sql")
            xxx = curr_store.execute(sql)
            for connector in curr_store.fetchall():
                no_rekening = connector[2]
                kode_transaksi = connector[6]
                total = connector[6]
                status = connector[4]
                tangal_transaksi = connector[3]

                CRUD_connector.insert_transaksi(no_rekening, kode_transaksi, total, tangal_transaksi)

                print("SUCCESSFULY ADD DATA FROM KODE TRANSAKSI",kode_transaksi," TO CONECTOR")
                print(connector)

        else:
            print("False in sql")

    except Exception as e:
        print(e)
elif(con_max_date==store_max_date):
    # GET ID AND STATUS FROM DB_BANK_TOKO AS OBJECT FROM CONNECTOR
    for con_row in status_connector:
        con_kode_transaksi, con_status = con_row

        # GET ID AND STATUS FROM DB_BUKU_TOKO AS OBJECT
        for store_row in status_store:
            store_kode_transaksi, store_status = store_row

            try:
                # UPDATE SYNCRONIZED ENGINE
                if (con_kode_transaksi == store_kode_transaksi):
                    if (con_status != store_status):
                        CRUD_store.update_status(con_kode_transaksi, con_status)
                        print("UPDATE SYSNCRONIZATION COMPLETE")
            except Exception as e:
                print(e)

else:
    print("False")

print("SYNCRONIZATION COMPLETE")
