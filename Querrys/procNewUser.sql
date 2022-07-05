SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
-- =============================================
-- Author:		Álvaro González
-- Create date: 04-07-2022
-- Description:	Procedimiento a utilizar para registrar un nuevo usuario asociado a una agenda.
-- =============================================
CREATE PROCEDURE procNewUser
	-- Parametros
	@usrEId 	INT,			/* Identificador de número de trabajador */
	@usrFname 	NVARCHAR(45),	/* Nombre(s) */
	@usrLname 	NVARCHAR(45),	/* Apellido(s) */
	@usrBirth 	DATE,			/* Fecha de nacimiento */
	@usrSex 	NVARCHAR(1),	/* Sexo, puede definirse con (F)emale o (M)ale */
	@usrEmail	NVARCHAR(45),	/* Correo electrónico del usuario */
	@usrPswrd 	NVARCHAR(45),	/* Contraseña del usuario */
	@usrRegDate DATE,			/* Fecha de registro del usuario */
	@dptoId		INT				/* Referencia a agenda */
AS
BEGIN
	SET NOCOUNT ON;
	IF EXISTS(SELECT usrEId FROM Users WHERE usrEId = @usrEId)
		BEGIN
			/* Impresión de usuario registrado con el EId que se ingreso */
			SELECT DISTINCT usrFname AS 'Nombre', usrLname AS 'Apellido', usrEId as 'Num de empleado'	/*¨Elementos que se mostraran en la consulta */
			/* ==== Tablas a consultar	   ==== */	FROM Users											/* Las tablas de referencia */
			/* ==== con base en las marcas ==== */	WHERE usrEId = @usrEId								/* Comienzan las condiciones */
			RETURN 0
		END
	ELSE
	IF EXISTS(SELECT usrEId FROM Users WHERE usrEmail = @usrEmail)
		BEGIN
			/* Impresión de usuario registrado con el Email que se ingreso */
			SELECT DISTINCT usrFname AS 'Nombre', usrLname AS 'Apellido', usrEmail as 'Email'			/*¨Elementos que se mostraran en la consulta */
			/* ==== Tablas a consultar	   ==== */	FROM Users											/* Las tablas de referencia */
			/* ==== con base en las marcas ==== */	WHERE usrEmail = @usrEmail							/* Comienzan las condiciones */
			RETURN 0
		END
	ELSE
		BEGIN
			INSERT INTO Users		VALUES (@usrEId, @usrFname, @usrLname, @usrBirth, @usrSex, @usrEmail, HASHBYTES('SHA2_256', @usrPswrd), @usrRegDate, @dptoId);
			INSERT INTO AddressBook VALUES (@usrFname+' s address book', @usrFname+' s address book', IDENT_CURRENT('Users'));
			INSERT INTO Contacts(contactFName, contactLName, contactAlias, addrId)
									VALUES (@usrFname, @usrLname, 'Me', IDENT_CURRENT('AddressBook'));
			RETURN 1
		END
END
GO
