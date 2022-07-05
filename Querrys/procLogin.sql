SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
-- =============================================
-- Author:		Álvaro González
-- Create date: 05-07-2022
-- Description:	Procedimiento a utilizar para validar usuario.
-- =============================================
CREATE PROCEDURE procLogin
	-- Parametros
	@usrEmail	NVARCHAR(45),	/* Correo electrónico del usuario */
	@usrPswrd 	NVARCHAR(45)	/* Contraseña del usuario */
AS
BEGIN
	SET NOCOUNT ON;
	IF EXISTS(SELECT usrEId FROM Users WHERE usrEmail = @usrEmail AND usrPswrd = HASHBYTES('SHA2_256', @usrPswrd))
	BEGIN
		/* Impresión de usuario registrado con el EId que se ingreso */
		SELECT DISTINCT usrFname AS 'Nombre', usrLname AS 'Apellido', usrEId as 'Num de empleado'	/*¨Elementos que se mostraran en la consulta */
		/* ==== Tablas a consultar	   ==== */	FROM Users											/* Las tablas de referencia */
		/* ==== con base en las marcas ==== */	WHERE usrEmail = @usrEmail							/* Comienzan las condiciones */
	END
END
GO
