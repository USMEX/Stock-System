using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace SSU
{
    public partial class frmLogin : Form
    {
        public frmLogin()
        {
            InitializeComponent();
        }

        private void btnAccept_Click(object sender, EventArgs e)
        {
            // Instance of the classTextValidation
            classTextValidation objValidUsername = new classTextValidation();

            // Email or EID validation
            if (objValidUsername.isvalid(txtUsername, 1) == true)
            {
                classUsers objUser = new classUsers();
                if (objUser.Login(txtUsername.Text, txtPassword.Text) == 1)
                    MessageBox.Show("Los datos ingresados son correctos.", "Usuario validado correctamente", MessageBoxButtons.OK, MessageBoxIcon.Asterisk);
                else
                    MessageBox.Show("Los datos ingresados son incorrectos.", "Usuario no logueado", MessageBoxButtons.OK, MessageBoxIcon.Warning);
            }
            else
            {
                MessageBox.Show("Wrong or invalid Email or Employee ID", "Username error", MessageBoxButtons.OK, MessageBoxIcon.Warning);
            }

        }

        private void txtPassword_TextChanged(object sender, EventArgs e)
        {
            {
                // Instance of the classTextValidation
                classTextValidation objValidUsername = new classTextValidation();
                if (objValidUsername.isvalid(txtPassword, 2) == true)
                    MessageBox.Show("Wrong or invalid password ingresado", "Password", MessageBoxButtons.OK, MessageBoxIcon.Warning);

            }
        }
    }
}
