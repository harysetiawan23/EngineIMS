/*
SQLyog Ultimate v11.11 (64 bit)
MySQL - 5.5.5-10.1.19-MariaDB : Database - db_bank
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`db_bank` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `db_bank`;

/*Table structure for table `tb_nasabah` */

DROP TABLE IF EXISTS `tb_nasabah`;

CREATE TABLE `tb_nasabah` (
  `id_nasabah` int(11) NOT NULL AUTO_INCREMENT,
  `nama` text,
  `alamat` text,
  `tempat_lahir` text,
  `tanggal_lahir` date DEFAULT NULL,
  PRIMARY KEY (`id_nasabah`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `tb_nasabah` */

LOCK TABLES `tb_nasabah` WRITE;

insert  into `tb_nasabah`(`id_nasabah`,`nama`,`alamat`,`tempat_lahir`,`tanggal_lahir`) values (1,'I Putu Gede','Br Dinas Kuwum Ancak, Kuwum, Marga, Tabanan','Denpasar','1974-11-12');

UNLOCK TABLES;

/*Table structure for table `tb_rekening` */

DROP TABLE IF EXISTS `tb_rekening`;

CREATE TABLE `tb_rekening` (
  `no_rekening` bigint(20) NOT NULL AUTO_INCREMENT,
  `id_nasabah` int(11) DEFAULT NULL,
  `tanggal_buka` datetime DEFAULT NULL,
  PRIMARY KEY (`no_rekening`),
  KEY `id_nasabah` (`id_nasabah`),
  CONSTRAINT `tb_rekening_ibfk_1` FOREIGN KEY (`id_nasabah`) REFERENCES `tb_nasabah` (`id_nasabah`)
) ENGINE=InnoDB AUTO_INCREMENT=1123 DEFAULT CHARSET=latin1;

/*Data for the table `tb_rekening` */

LOCK TABLES `tb_rekening` WRITE;

insert  into `tb_rekening`(`no_rekening`,`id_nasabah`,`tanggal_buka`) values (1121,1,'2017-11-01 21:43:22'),(1122,1,'2017-11-16 22:31:22');

UNLOCK TABLES;

/*Table structure for table `tb_transaksi` */

DROP TABLE IF EXISTS `tb_transaksi`;

CREATE TABLE `tb_transaksi` (
  `id_transaksi` int(11) NOT NULL AUTO_INCREMENT,
  `no_rekening` bigint(11) DEFAULT NULL,
  `kode_transaksi` int(11) NOT NULL,
  `total` float NOT NULL,
  `status` int(11) NOT NULL,
  `tanggal_transaksi` datetime NOT NULL,
  PRIMARY KEY (`id_transaksi`),
  KEY `no_rekening` (`no_rekening`),
  CONSTRAINT `tb_transaksi_ibfk_1` FOREIGN KEY (`no_rekening`) REFERENCES `tb_rekening` (`no_rekening`)
) ENGINE=InnoDB AUTO_INCREMENT=77 DEFAULT CHARSET=latin1;

/*Data for the table `tb_transaksi` */

LOCK TABLES `tb_transaksi` WRITE;

insert  into `tb_transaksi`(`id_transaksi`,`no_rekening`,`kode_transaksi`,`total`,`status`,`tanggal_transaksi`) values (15,1121,121,11,1,'2017-11-10 00:00:00'),(61,1121,1001,23000,1,'2017-11-12 21:17:33'),(62,1122,2001,45000,0,'2017-11-12 21:26:52'),(63,1121,2002,120000,0,'2017-11-13 01:09:07'),(64,1122,2003,22000,1,'2017-11-13 01:59:56'),(65,1122,9999,9999,1,'2017-11-13 02:21:38'),(66,1121,22121,22121,0,'2017-11-13 02:23:20'),(67,1121,22123,22123,1,'2017-11-13 02:23:26'),(68,1121,22123,22123,0,'2017-11-13 02:23:55'),(69,1121,22121,22121,0,'2017-11-13 02:24:44'),(70,1121,22121,22121,1,'2017-11-13 02:25:52'),(71,1121,22121,22121,0,'2017-11-13 02:26:45'),(72,1121,22121,22121,0,'2017-11-13 02:27:30'),(73,1121,22121,22121,0,'2017-11-13 02:27:43'),(74,1121,22121,22121,0,'2017-11-13 02:28:05'),(75,1121,22121,22121,0,'2017-11-13 02:28:28'),(76,1121,22121,22121,0,'2017-11-13 02:28:57');

UNLOCK TABLES;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
