/*
SQLyog Ultimate v11.11 (64 bit)
MySQL - 5.5.5-10.1.19-MariaDB : Database - db_bank_toko
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`db_bank_toko` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `db_bank_toko`;

/*Table structure for table `tb_transaksi` */

DROP TABLE IF EXISTS `tb_transaksi`;

CREATE TABLE `tb_transaksi` (
  `id_transaksi` int(11) NOT NULL AUTO_INCREMENT,
  `no_rekening` bigint(20) DEFAULT NULL,
  `kode_transaksi` int(11) DEFAULT NULL,
  `tanggal_transaksi` datetime DEFAULT NULL,
  `keterangan` text,
  `total` float DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  PRIMARY KEY (`id_transaksi`)
) ENGINE=InnoDB AUTO_INCREMENT=41 DEFAULT CHARSET=latin1;

/*Data for the table `tb_transaksi` */

LOCK TABLES `tb_transaksi` WRITE;

insert  into `tb_transaksi`(`id_transaksi`,`no_rekening`,`kode_transaksi`,`tanggal_transaksi`,`keterangan`,`total`,`status`) values (1,1121,1001,'2017-11-12 21:17:33','Pembelian Sabun Mandi',23000,1),(2,1122,2001,'2017-11-12 21:26:52','Pembayaran Item A',45000,0),(5,1121,2002,'2017-11-13 01:09:07','Pembayaran Ena Ena',120000,0),(6,1122,2003,'2017-11-13 01:59:56','Pembayaran habis sisa jatah semalam',22000,1),(7,1122,9999,'2017-11-13 02:21:38','Pembayaran CouchDB',9999,1),(30,1121,22121,'2017-11-13 02:23:20',NULL,22121,0),(31,1121,22123,'2017-11-13 02:23:26',NULL,22123,1),(32,1121,22123,'2017-11-13 02:23:55',NULL,22123,1),(33,1121,22121,'2017-11-13 02:24:44',NULL,22121,0),(34,1121,22121,'2017-11-13 02:25:52',NULL,22121,0),(35,1121,22121,'2017-11-13 02:26:45',NULL,22121,0),(36,1121,22121,'2017-11-13 02:27:30',NULL,22121,0),(37,1121,22121,'2017-11-13 02:27:43',NULL,22121,0),(38,1121,22121,'2017-11-13 02:28:05',NULL,22121,0),(39,1121,22121,'2017-11-13 02:28:28',NULL,22121,0),(40,1121,22121,'2017-11-13 02:28:57',NULL,22121,0);

UNLOCK TABLES;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
