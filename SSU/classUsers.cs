using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
/* |==| Libraries used */
using System.Data.SqlClient;
using System.IO;
using System.Data;

namespace SSU
{
    // Creamos clase que permite la conexión con la base de datos.
    public class ConnectionDB
    {
        public static SqlConnection StartConn()
        {
            // Configuración de los parámetros para conectar con la base de datos.
            string[] Config = { "Data Source = srv0.glassesfriends.com;",
            /*                 */"Initial Catalog=dbStockTest;",
            /*                 */"User Id=SA;",
            /*                 */"Password=1187739908Binet"};
            string Connection = Config[0] + Config[1] + Config[2] + Config[3];
            SqlConnection Conn = new SqlConnection(Connection);
            Conn.Open();
            return Conn;
        }
    }
    internal class classUsers
    {
        public string Username { get; set; }
        public string Fname { get; set; }
        public string Lname { get; set; }
        public DateTime Birth { get; set; }
        public char Sex { get; set; }
        public string Paswrd { get; set; }
        public string Email { get; set; }
        // Constructor genérico.
        public classUsers() { }

        // Constructor sobrecargado.
        public classUsers(string Username, string Fname, string Lname, DateTime Birth, char Sex, string Email, string Paswrd)
        {
            this.Username = Username;
            this.Fname = Fname;
            this.Lname = Lname;
            this.Birth = Birth;
            this.Sex = Sex;
            this.Email = Email;
            this.Paswrd = Paswrd;
        }
        public int requestUser(classUsers UsuarioReg)
        {
            using (SqlConnection Conn = ConnectionDB.StartConn())
            {
                // Variable para formato de la base de datos año, mes y día.
                string Format = "yyyy-MM-dd";

                SqlCommand Comando = new SqlCommand(
                    string.Format("INSERT INTO Users (usrUsrname, usrFname, usrLname, usrBirth, usrSex, usrEmail, usrPswrd, usrRegDate) " +
                    "VALUES ('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}')",
                    UsuarioReg.Username,
                    UsuarioReg.Fname,
                    UsuarioReg.Lname,
                    //* Fecha de nacimiento a string con formato de base de datos.
                    UsuarioReg.Birth.ToString(Format),
                    UsuarioReg.Sex,
                    UsuarioReg.Email,
                    UsuarioReg.Paswrd,
                    //* Fecha de día de registro a string con formato de la base de datos.
                    DateTime.Today.ToString(Format)), Conn);
                return Comando.ExecuteNonQuery();
            }
        }
        public bool Validar(string Username)
        {
            string Consulta = @"SELECT COUNT(*) FROM Users WHERE usrUsrname = @usrUsrname ; ";
            using (SqlConnection Conn = ConnectionDB.StartConn())
            {
                SqlCommand cmd = new SqlCommand(Consulta, Conn);
                cmd.Parameters.AddWithValue("@usrUsrname ", Username);
                int Count = Convert.ToInt32(cmd.ExecuteScalar());
                return Count == 0;
            }
        }
        public int Login(string parUsername, string parPassword)
        {
            using (SqlConnection Conn = ConnectionDB.StartConn())
            {
                // Variable para formato de la base de datos año, mes y día.
                string Format = "yyyy-MM-dd";

                SqlCommand Comando = new SqlCommand(
                    string.Format("EXEC procLogin'{0}','{1}';",
                    parUsername, parPassword), Conn);
                SqlDataReader usersRegistered = Comando.ExecuteReader(); // Lee los elementos de la tabla de la BD de Departamento
                int cntUsers = 0;
                while (usersRegistered.Read())
                {
                    cntUsers++;
                }
                return cntUsers;
            }
        }
    }
}
