using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
/* Librries used */
using System.Text.RegularExpressions;

namespace SSU
{
    internal class classTextValidation
    {
        // === | INICIO Métodos | === //
        private static string replaceAcentos(string textObjetct)
        {
            Regex ReemplazarA = new Regex("[á|à|ä|â]", RegexOptions.Compiled);
            Regex ReemplazarE = new Regex("[é|è|ë|ê]", RegexOptions.Compiled);
            Regex ReemplazarI = new Regex("[í|ì|ï|î]", RegexOptions.Compiled);
            Regex ReemplazarO = new Regex("[ó|ò|ö|ô]", RegexOptions.Compiled);
            Regex ReemplazarU = new Regex("[ú|ù|ü|û]", RegexOptions.Compiled);
            Regex ReemplazarAMay = new Regex("[Á]", RegexOptions.Compiled);
            Regex ReemplazarEMay = new Regex("[É]", RegexOptions.Compiled);
            Regex ReemplazarIMay = new Regex("[Í]", RegexOptions.Compiled);
            Regex ReemplazarOMay = new Regex("[Ó]", RegexOptions.Compiled);
            Regex ReemplazarUMay = new Regex("[Ú]", RegexOptions.Compiled);
            textObjetct = ReemplazarA.Replace(textObjetct, "a");
            textObjetct = ReemplazarE.Replace(textObjetct, "e");
            textObjetct = ReemplazarI.Replace(textObjetct, "i");
            textObjetct = ReemplazarO.Replace(textObjetct, "o");
            textObjetct = ReemplazarU.Replace(textObjetct, "u");
            textObjetct = ReemplazarAMay.Replace(textObjetct, "A");
            textObjetct = ReemplazarEMay.Replace(textObjetct, "E");
            textObjetct = ReemplazarIMay.Replace(textObjetct, "I");
            textObjetct = ReemplazarOMay.Replace(textObjetct, "O");
            textObjetct = ReemplazarUMay.Replace(textObjetct, "U");
            return textObjetct;
        }
        public bool isvalid(TextBox TextoVerificar, int Case)
        {
            // Función para verificar el formato del Email y la Password.
            switch (Case)
            {
                // Caso 1 - Formato para Email.
                case 1:
                    try
                    {
                        // Validar formato de [Correo electrónico].
                        string expresion = "\\w+([-+.']\\w+)*@\\w+([-.]\\w+)*\\.\\w+([-.]\\w+)*";
                        if (Regex.IsMatch(TextoVerificar.Text, expresion))
                        {
                            if (Regex.Replace(TextoVerificar.Text, expresion, string.Empty).Length == 0)
                                return true;
                            else
                                return false;
                        }
                        else
                            return false;
                    }
                    catch
                    {
                        TextoVerificar.Text = replaceAcentos(TextoVerificar.Text);
                        TextoVerificar.SelectionStart = TextoVerificar.TextLength;
                    }
                    return true;

                // Caso 2 - Formato para Password.
                case 2:
                    try
                    {
                        // Validar formato de la contraseña.
                        string expresion = "^(?=.*[A-Za-z])(?=.*\\d)[A-Za-z\\d]{8,}$";
                        if (Regex.IsMatch(TextoVerificar.Text, expresion))
                        {
                            if (Regex.Replace(TextoVerificar.Text, expresion, string.Empty).Length == 0)
                                return true;
                            else
                                return false;
                        }
                        else
                            return false;
                    }
                    catch
                    {
                        TextoVerificar.Text = replaceAcentos(TextoVerificar.Text);
                        TextoVerificar.SelectionStart = TextoVerificar.TextLength;
                    }
                    return true;

                // Caso 3 - Formato para Username.
                case 3:

                    // Validamos que se usen signos válidos para un usuario.
                    foreach (int Caracter in Encoding.ASCII.GetBytes(TextoVerificar.Text))
                        /*  //-Guión bajo-//    //-----Letras Mayúsculas-----//    //-----Letras Minúsculas-----//     //-----------Números-----------//  */
                        if (Caracter != 95 && (Caracter < 65 || Caracter > 90) && (Caracter < 97 || Caracter > 122) && (Caracter < 48 || Caracter > 57))
                        {
                            try
                            {
                                int AuxUbi = Convert.ToByte(TextoVerificar.Text.IndexOf(Convert.ToChar(Caracter)));
                                TextoVerificar.Text = TextoVerificar.Text.Remove(AuxUbi, 1);
                                TextoVerificar.SelectionStart = AuxUbi;
                                return true;
                            }
                            catch
                            {
                                TextoVerificar.Text = replaceAcentos(TextoVerificar.Text);
                                TextoVerificar.SelectionStart = TextoVerificar.TextLength;
                                return true;
                            }
                        }
                    return true;
            }
            return true;
        }
    }
}
