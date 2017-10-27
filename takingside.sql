/*
Navicat MySQL Data Transfer

Source Server         : 本地
Source Server Version : 50719
Source Host           : localhost:3306
Source Database       : takingside

Target Server Type    : MYSQL
Target Server Version : 50719
File Encoding         : 65001

Date: 2017-10-27 12:23:26
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `debatetopic`
-- ----------------------------
DROP TABLE IF EXISTS `debatetopic`;
CREATE TABLE `debatetopic` (
  `Topic` char(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of debatetopic
-- ----------------------------
INSERT INTO `debatetopic` VALUES ('abc');

-- ----------------------------
-- Table structure for `user`
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `AccountNumber` char(30) NOT NULL,
  `Password` char(20) NOT NULL,
  `Nickname` char(30) NOT NULL,
  `TelephoneNumber` int(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO `user` VALUES ('test1', '123', 'jiang', '1378888888');
INSERT INTO `user` VALUES ('test2', '1234', 'jiang1', '1377777777');
INSERT INTO `user` VALUES ('test4', '123456', 'jiang3', '1375555555');
INSERT INTO `user` VALUES ('test3', '12345', 'jiang2', '1376666666');
INSERT INTO `user` VALUES ('test5', '1234567', 'jiang4', '1374444444');
