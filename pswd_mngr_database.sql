-- Database for Password Manager

DROP DATABASE IF EXISTS pswd_mngr_database;
CREATE DATABASE pswd_mngr_database;
USE pswd_mngr_database;

-- Contains information to keep track of user login information
CREATE TABLE loginInfo (
	userID INT INVISIBLE COMMENT "userID will be primary key",
    username VARCHAR(50),
    userPassword VARCHAR(50) INVISIBLE,
	CONSTRAINT loginInfo_userID_pk PRIMARY KEY (userID)
	) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Contains list of applications and associated usernames & passwords
CREATE TABLE applicationList (
    applicationName VARCHAR(50) COMMENT "applicationName will be primary key",
	appUsername VARCHAR(50),
	appPassword VARCHAR(50),
    CONSTRAINT applicationList_applicationName_pk PRIMARY KEY (applicationName)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Relation to tie login table and application table together
CREATE TABLE userAppRelation (
    userAppID INT COMMENT "userAppID will be primary key",
    userID INT INVISIBLE,
    applicationName VARCHAR(50),
    CONSTRAINT userAppRelation_userAppID_pk PRIMARY KEY (userAppID)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE USER 'poncho'@'localhost' IDENTIFIED BY 'whatsaponcho'