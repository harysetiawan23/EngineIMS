import Connection as connect
import CRUD_bank
import CRUD_connector
import datetime

# connection
commit_conductor = connect.db_konduktor.commit()
commit_bank = connect.db_bank.commit()

# preparation
curr_connector = connect.db_konduktor.cursor()
curr_bank = connect.db_bank.cursor()

# INSERT PREPERATION

curr_connector.execute("SELECT MAX(tanggal_transaksi) FROM `tb_transaksi` ORDER BY `tanggal_transaksi` DESC")
curr_bank.execute("SELECT MAX(tanggal_transaksi) FROM `tb_transaksi` ORDER BY `tanggal_transaksi` DESC")

f = '%Y-%m-%d %H:%M:%S'

row_connector = curr_connector.fetchall()
commit_conductor

row_bank = curr_bank.fetchall()
commit_bank

# UPDATE PREPREATION
curr_connector.execute("SELECT `kode_transaksi`,STATUS FROM `tb_transaksi` ORDER BY `tanggal_transaksi` DESC")
curr_bank.execute("SELECT `kode_transaksi`,STATUS FROM `tb_transaksi` ORDER BY `tanggal_transaksi` DESC")

status_connector = curr_connector.fetchall()
status_bank = curr_bank.fetchall()

# BEGIN ENGINE

#GET MAX DATE IN DB_BANK_TOKO AS MAX DATE IN CONNECTOR
for connector in row_connector:
    # fetch data di db_bank_toko
    con_max_date = connector

# GET MAX DATE IN DB_BANK AS A DATABASE OBJECT
for bank in row_bank:
    bank_max_date = bank
    # bigining insert

    # commit connection for a while
    commit_bank
    commit_conductor


print("BEGIN SYNCRONIZATION")
#INSERT SYSNCRONIZED LOGIC ENGINE
if (con_max_date > bank_max_date):

    date = bank_max_date[0]

    sql = "SELECT * FROM `tb_transaksi`  WHERE `tanggal_transaksi` > '%s' " % (date)

    try:
        curr_connector.execute(sql)

        for connector in curr_connector.fetchall():
            no_rekening = connector[1]
            kode_transaksi = connector[2]
            total = connector[5]
            status = connector[6]
            tangal_transaksi = connector[3]

            CRUD_bank.insert_transasi(no_rekening, kode_transaksi, total, tangal_transaksi)

            print("SUCCESSFULY ADD DATA FROM KODE TRANSAKSI",kode_transaksi," TO BANK DATABASE")

    except Exception as e:
        print(e)
elif(con_max_date==bank_max_date):
    # GET ID AND STATUS FROM DB_BANK_TOKO AS OBJECT FROM CONNECTOR
    for con_row in status_connector:
        con_kode_transaksi, con_status = con_row

        # GET ID AND STATUS FROM DB_TOKO AS OBJECT
        for bank_row in status_bank:
            bank_kode_transaksi, bank_status = bank_row

            try:
                # UPDATE SYNCRONIZED ENGINE
                if (con_kode_transaksi == bank_kode_transaksi):
                    if (con_status != bank_status):
                        CRUD_connector.update_status(bank_kode_transaksi, bank_status)
                        print("UPDATE SYSNCRONIZATION COMPLETE")
            except Exception as e:
                print(e)

print("SYNCRONIZATION COMPLETE")
