CREATE DATABASE  IF NOT EXISTS `taller_python` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `taller_python`;
-- MySQL dump 10.13  Distrib 5.7.17, for Win64 (x86_64)
--
-- Host: localhost    Database: taller_python
-- ------------------------------------------------------
-- Server version	5.7.21-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `autos`
--

DROP TABLE IF EXISTS `autos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `autos` (
  `id_patente` varchar(30) NOT NULL,
  `id_usuario` int(11) NOT NULL,
  `marca` varchar(30) NOT NULL,
  `modelo` varchar(30) NOT NULL,
  `color` varchar(30) NOT NULL,
  PRIMARY KEY (`id_patente`),
  KEY `id_usuario` (`id_usuario`),
  CONSTRAINT `autos_ibfk_1` FOREIGN KEY (`id_usuario`) REFERENCES `usuarios` (`id_usuario`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `autos`
--

LOCK TABLES `autos` WRITE;
/*!40000 ALTER TABLE `autos` DISABLE KEYS */;
INSERT INTO `autos` VALUES ('AB555CC',3,'Toyota','Hilux','Verde'),('WE333EE',4,'WW','Suran','Rojo');
/*!40000 ALTER TABLE `autos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `facturas`
--

DROP TABLE IF EXISTS `facturas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `facturas` (
  `id_factura` int(11) NOT NULL AUTO_INCREMENT,
  `id_usuario` int(11) DEFAULT NULL,
  `fecha_emision` date DEFAULT NULL,
  `importe_total` float NOT NULL,
  PRIMARY KEY (`id_factura`),
  KEY `id_usuario` (`id_usuario`),
  CONSTRAINT `facturas_ibfk_1` FOREIGN KEY (`id_usuario`) REFERENCES `usuarios` (`id_usuario`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `facturas`
--

LOCK TABLES `facturas` WRITE;
/*!40000 ALTER TABLE `facturas` DISABLE KEYS */;
INSERT INTO `facturas` VALUES (1,3,NULL,36525);
/*!40000 ALTER TABLE `facturas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `hojarepuesto`
--

DROP TABLE IF EXISTS `hojarepuesto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `hojarepuesto` (
  `id_repuesto` int(11) NOT NULL,
  `id_hoja` int(11) NOT NULL,
  `cantidad` int(11) DEFAULT NULL,
  `precio_total` float DEFAULT NULL,
  PRIMARY KEY (`id_repuesto`,`id_hoja`),
  KEY `id_hoja` (`id_hoja`),
  CONSTRAINT `hojarepuesto_ibfk_1` FOREIGN KEY (`id_repuesto`) REFERENCES `repuestos` (`id_repuesto`),
  CONSTRAINT `hojarepuesto_ibfk_2` FOREIGN KEY (`id_hoja`) REFERENCES `hojasdeparte` (`id_hoja`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hojarepuesto`
--

LOCK TABLES `hojarepuesto` WRITE;
/*!40000 ALTER TABLE `hojarepuesto` DISABLE KEYS */;
INSERT INTO `hojarepuesto` VALUES (6,1,3,33192);
/*!40000 ALTER TABLE `hojarepuesto` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `hojasdeparte`
--

DROP TABLE IF EXISTS `hojasdeparte`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `hojasdeparte` (
  `id_hoja` int(11) NOT NULL AUTO_INCREMENT,
  `id_factura` int(11) NOT NULL,
  `id_mecanico` int(11) NOT NULL,
  `id_patente` varchar(30) NOT NULL,
  `costo_mano_de_obra` float NOT NULL,
  PRIMARY KEY (`id_hoja`),
  KEY `id_factura` (`id_factura`),
  KEY `id_mecanico` (`id_mecanico`),
  KEY `id_patente` (`id_patente`),
  CONSTRAINT `hojasdeparte_ibfk_1` FOREIGN KEY (`id_factura`) REFERENCES `facturas` (`id_factura`),
  CONSTRAINT `hojasdeparte_ibfk_2` FOREIGN KEY (`id_mecanico`) REFERENCES `usuarios` (`id_usuario`),
  CONSTRAINT `hojasdeparte_ibfk_3` FOREIGN KEY (`id_patente`) REFERENCES `autos` (`id_patente`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hojasdeparte`
--

LOCK TABLES `hojasdeparte` WRITE;
/*!40000 ALTER TABLE `hojasdeparte` DISABLE KEYS */;
INSERT INTO `hojasdeparte` VALUES (1,1,2,'AB555CC',3333);
/*!40000 ALTER TABLE `hojasdeparte` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `proveedores`
--

DROP TABLE IF EXISTS `proveedores`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `proveedores` (
  `id_cuit` int(11) NOT NULL AUTO_INCREMENT,
  `razon_social` varchar(30) NOT NULL,
  `tel` varchar(30) DEFAULT NULL,
  `direccion` varchar(30) DEFAULT NULL,
  `email` varchar(30) NOT NULL,
  PRIMARY KEY (`id_cuit`),
  UNIQUE KEY `id_cuit` (`id_cuit`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `proveedores`
--

LOCK TABLES `proveedores` WRITE;
/*!40000 ALTER TABLE `proveedores` DISABLE KEYS */;
/*!40000 ALTER TABLE `proveedores` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `proveedorrepuesto`
--

DROP TABLE IF EXISTS `proveedorrepuesto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `proveedorrepuesto` (
  `id_cuit` int(11) NOT NULL,
  `id_repuesto` int(11) NOT NULL,
  PRIMARY KEY (`id_cuit`,`id_repuesto`),
  KEY `id_repuesto` (`id_repuesto`),
  CONSTRAINT `proveedorrepuesto_ibfk_1` FOREIGN KEY (`id_cuit`) REFERENCES `proveedores` (`id_cuit`),
  CONSTRAINT `proveedorrepuesto_ibfk_2` FOREIGN KEY (`id_repuesto`) REFERENCES `repuestos` (`id_repuesto`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `proveedorrepuesto`
--

LOCK TABLES `proveedorrepuesto` WRITE;
/*!40000 ALTER TABLE `proveedorrepuesto` DISABLE KEYS */;
/*!40000 ALTER TABLE `proveedorrepuesto` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reparaciones`
--

DROP TABLE IF EXISTS `reparaciones`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `reparaciones` (
  `id_reparacion` int(11) DEFAULT NULL,
  `id_patente` varchar(10) NOT NULL,
  `id_mecanico` int(11) NOT NULL,
  `fecha_ingreso` date NOT NULL,
  `fecha_salida` date NOT NULL,
  `estado_reparacion` varchar(40) NOT NULL,
  PRIMARY KEY (`id_patente`,`id_mecanico`,`fecha_ingreso`),
  UNIQUE KEY `id_reparacion` (`id_reparacion`),
  KEY `id_mecanico` (`id_mecanico`),
  CONSTRAINT `reparaciones_ibfk_1` FOREIGN KEY (`id_patente`) REFERENCES `autos` (`id_patente`),
  CONSTRAINT `reparaciones_ibfk_2` FOREIGN KEY (`id_mecanico`) REFERENCES `usuarios` (`id_usuario`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reparaciones`
--

LOCK TABLES `reparaciones` WRITE;
/*!40000 ALTER TABLE `reparaciones` DISABLE KEYS */;
/*!40000 ALTER TABLE `reparaciones` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `repuestos`
--

DROP TABLE IF EXISTS `repuestos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `repuestos` (
  `id_repuesto` int(11) NOT NULL AUTO_INCREMENT,
  `id_tipo_repuesto` int(11) DEFAULT NULL,
  `descripcion` varchar(30) NOT NULL,
  `stock` int(11) NOT NULL,
  `punto_pedido` int(11) DEFAULT NULL,
  `precio_unitario` float NOT NULL,
  `origen` varchar(30) NOT NULL,
  PRIMARY KEY (`id_repuesto`),
  KEY `id_tipo_repuesto` (`id_tipo_repuesto`),
  CONSTRAINT `repuestos_ibfk_1` FOREIGN KEY (`id_tipo_repuesto`) REFERENCES `tipoderepuestos` (`id_tipoderepuesto`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `repuestos`
--

LOCK TABLES `repuestos` WRITE;
/*!40000 ALTER TABLE `repuestos` DISABLE KEYS */;
INSERT INTO `repuestos` VALUES (1,2,'Llantas1',3,NULL,303.5,'Nacional'),(2,2,'Llantas2',3,NULL,555,'Nacional'),(3,2,'19 inch ho',999,NULL,11380,'Importado'),(4,2,'10168 ford',999,NULL,12581,'Importado'),(5,2,'22.5 x 8.2',999,NULL,11064,'Importado'),(6,2,'22.5 x 8.2',999,NULL,11064,'Importado');
/*!40000 ALTER TABLE `repuestos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `roles`
--

DROP TABLE IF EXISTS `roles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `roles` (
  `id_rol` int(11) NOT NULL AUTO_INCREMENT,
  `descripcion` varchar(80) NOT NULL,
  PRIMARY KEY (`id_rol`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `roles`
--

LOCK TABLES `roles` WRITE;
/*!40000 ALTER TABLE `roles` DISABLE KEYS */;
INSERT INTO `roles` VALUES (1,'admin'),(2,'mecanico'),(3,'cliente');
/*!40000 ALTER TABLE `roles` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tipoderepuestos`
--

DROP TABLE IF EXISTS `tipoderepuestos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tipoderepuestos` (
  `id_tipoderepuesto` int(11) NOT NULL AUTO_INCREMENT,
  `descripcion` varchar(30) NOT NULL,
  PRIMARY KEY (`id_tipoderepuesto`),
  UNIQUE KEY `id_tipoderepuesto` (`id_tipoderepuesto`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tipoderepuestos`
--

LOCK TABLES `tipoderepuestos` WRITE;
/*!40000 ALTER TABLE `tipoderepuestos` DISABLE KEYS */;
INSERT INTO `tipoderepuestos` VALUES (1,'Puerta Delantera'),(2,'Llantas'),(3,'Asientos');
/*!40000 ALTER TABLE `tipoderepuestos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuarios`
--

DROP TABLE IF EXISTS `usuarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `usuarios` (
  `id_usuario` int(11) NOT NULL AUTO_INCREMENT,
  `id_rol` int(11) NOT NULL,
  `nombre` varchar(30) NOT NULL,
  `apellido` varchar(30) NOT NULL,
  `dni` int(11) NOT NULL,
  `email` varchar(30) NOT NULL,
  `password` varchar(30) NOT NULL,
  `tel` int(11) DEFAULT NULL,
  `habilitado` tinyint(1) NOT NULL,
  PRIMARY KEY (`id_usuario`),
  UNIQUE KEY `dni` (`dni`),
  UNIQUE KEY `email` (`email`),
  KEY `id_rol` (`id_rol`),
  CONSTRAINT `usuarios_ibfk_1` FOREIGN KEY (`id_rol`) REFERENCES `roles` (`id_rol`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuarios`
--

LOCK TABLES `usuarios` WRITE;
/*!40000 ALTER TABLE `usuarios` DISABLE KEYS */;
INSERT INTO `usuarios` VALUES (1,1,'Esteban','Quito',39999,'admin@hotmail.com','admin',33333,1),(2,2,'Roberto','Mengano',400000,'mecanico@hotmail.com','asd',3333,1),(3,3,'Esteban','Quito',4000,'cliente@hotmail.com','asd',3434,1),(4,3,'Mengano','Sultano',4000003,'cliene@hotmail.com','ased',3434,1);
/*!40000 ALTER TABLE `usuarios` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-11-08  0:40:51
