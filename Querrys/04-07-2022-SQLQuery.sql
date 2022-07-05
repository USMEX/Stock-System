/* |=====|+|=====|+|=====|+|=====| DROP area	|=====|+|=====|+|=====|+|=====|*/
DROP DATABASE dbStockTest;
DROP TABLE Departments;
DROP TABLE Users;
DROP TABLE AddressBook;
DROP TABLE Contacts;
/* |=====|-|=====|-|=====|-|=====| DROP area	|=====|-|=====|-|=====|-|=====|*/
/* |=====|+|=====|+|=====|+|=====| USE area		|=====|+|=====|+|=====|+|=====|*/
USE dbStockTest;
/* |=====|-|=====|-|=====|-|=====| USE area		|=====|-|=====|-|=====|-|=====|*/
/* |=====|+|=====|+|=====|+|=====| CREATE area	|=====|+|=====|+|=====|+|=====|*/
CREATE DATABASE dbStockTest;

/* | Tabla de departamentos | */
CREATE TABLE Departments(
	dptoId 		INT IDENTITY(1,1) PRIMARY KEY,		/* Identificador �nico*/
	dptoName 	NVARCHAR(45) 	NOT NULL UNIQUE,	/* Nombre del departamento */
	dptoDescr 	NVARCHAR(45) 						/* Descripci�n (Opcional) */
);

/* | Tabla de usuarios | */
CREATE TABLE Users(
	usrId 		INT IDENTITY(1,1) PRIMARY KEY,		/* Identificador �nico*/
	usrEId 		INT	NOT			NULL UNIQUE,		/* Identificador de n�mero de trabajador */
	usrFname 	NVARCHAR(45) 	NOT NULL,			/* Nombre(s) */
	usrLname 	NVARCHAR(45) 	NOT NULL,			/* Apellido(s) */
	usrBirth 	DATE,								/* Fecha de nacimiento */
	usrSex 		NVARCHAR(1) 	NOT NULL,			/* Sexo, puede definirse con (F)emale o (M)ale */
	usrEmail	NVARCHAR(45) 	NOT NULL UNIQUE,	/* Correo electr�nico del usuario */
	usrPswrd 	NVARCHAR(45) 	NOT NULL,			/* Contrase�a del usuario */
	usrRegDate 	DATE,								/* Fecha de registro del usuario */
	dptoId		INT REFERENCES Departments(dptoId) NOT NULL /* Referencia a agenda */
);

/* | Tabla de Agenda | */
CREATE TABLE AddressBook(
	addrId	 		INT IDENTITY(1,1) PRIMARY KEY,			/* Idetificador de la agenda */
	addrName	 	NVARCHAR(45) 	NOT NULL,				/* Nombre o alias de la agenda */
	addrDescr	 	NVARCHAR(900),							/* Descripci�n de la agenda */
	usrId			INT REFERENCES Users(usrId) NOT NULL	/* Usuario al que est� asociado la agenda */
);

/* | Tabla de contactos asociados a agenda | */
CREATE TABLE Contacts(
	contactId 			INT IDENTITY(1,1) PRIMARY KEY,	/* Identificador del contacto */
	contactFName		NVARCHAR(45),				/* Nombre(s) del contacto */
	contactLName		NVARCHAR(45),				/* Apellido(s) del contacto */
	contactAlias		NVARCHAR(45),				/* Alias del contacto */
	contactPhonePers	NVARCHAR(16),				/* Tel�fono personal de contacto */
	contactPhoneWork	NVARCHAR(16),				/* Tel�fono del trabajo del contacto */
	contactPhoneOther	NVARCHAR(16),				/* Telefono opcional del contacto */
	contactEmail		NVARCHAR(64),				/* Email del contacto */
	addrId				INT REFERENCES AddressBook(addrId) NOT NULL /* Referencia a agenda */
);
/* |=====|-|=====|-|=====|-|=====| CREATE area	|=====|-|=====|-|=====|-|=====|*/
/* |=====|+|=====|+|=====|+|=====| INSERT area	|=====|+|=====|+|=====|+|=====|*/
INSERT INTO Departments(dptoName, dptoDescr) VALUES('Contabilidad', 'Departamento de contabilidad.');	
INSERT INTO Departments(dptoName, dptoDescr) VALUES('Recursos Humanos', 'Departamento de recursos humanos.');	
INSERT INTO Departments(dptoName, dptoDescr) VALUES('Finanzas', 'Departamento de finanzas.');
INSERT INTO Departments(dptoName, dptoDescr) VALUES('Compras', 'Departamento de compras.');
INSERT INTO Departments(dptoName, dptoDescr) VALUES('Ingenier�a', 'Departamento de ingenieria.');
INSERT INTO Departments(dptoName, dptoDescr) VALUES('Producci�n', 'Departamento de producci�n.');
INSERT INTO Departments(dptoName, dptoDescr) VALUES('Comercio exterior', 'Departamento de comercio exterior.');
INSERT INTO Departments(dptoName, dptoDescr) VALUES('Servicio al cliente', 'Departamento de servicio al cliente.');
INSERT INTO Departments(dptoName, dptoDescr) VALUES('Control de calidad', 'Departamento de control de calidad.');
INSERT INTO Departments(dptoName, dptoDescr) VALUES('Ventas', 'Departamento de ventas.');
INSERT INTO Departments(dptoName, dptoDescr) VALUES('Mantenimiento', 'Departamento de mantenimiento.');
INSERT INTO Departments(dptoName, dptoDescr) VALUES('Limpieza', 'Departamento de limpieza.');
INSERT INTO Departments(dptoName, dptoDescr) VALUES('Sistemas', 'Departamento de sistemas.');
INSERT INTO Departments(dptoName, dptoDescr) VALUES('Mercadot�cnia', 'Departamento de mercadot�cnia.');

/* |((| Procedimientos |)))| */
procNewUser 24, '�lvaro', 'Gonz�lez', '01/05/1994', 'M', 'a.gonzalez@usmex.mx', 'TiburoncinUhaha',  GETDATE, 13;
/* |=====|-|=====|-|=====|-|=====| INSERT area	|=====|-|=====|-|=====|-|=====|*/