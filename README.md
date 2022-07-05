# **Stock-System for USMEX - SSU**
A beta of a stock system
![](Readme/USMEX-Logo.jpeg)
## **Prefix**
| Object         | Spanish              | Prefix  | Example                             |
| -------------- | -------------------- | ------- | ----------------------------------- |
| Button         | Botónes              | btn     | btnAccept,   btnCancel, btnRegister |
| CheckBox       | Check Box            | chkbox  | chkboxFemale,   chkboxMale          |
| CheckedListBox | Lista de Check Box   | chklbox | chklboxSex                          |
| ComboBox       | Combo box            | cbox    | cboxDepartaments,   cboxUserMod     |
| Form           | Forms de windows     | frm     | frmLogin,   frmRegister             |
| GroupBox       | Agrupador            | grpb    | grpbPersonalData,   grpbContactData |
| Date           | Fecha                | date    | dateBday,   dateRegDate             |
| Label          | Etiquetas            | lbl     | lblText1, lblText2                  |
| LinkLabels     | Etiquetas con link   | llbl    | llblLinkUSMEX,   llblLinkAboutUs    |
| ListBox        | Lista                | lbox    | lboxUsersRegistered                 |
| PictureBox     | Imagen               | pbox    | pboxLogoUSMEX,   pboxCert1          |
| RadioButtom    | Botones de seleccion | rbtn    | rbtnFemale,   rbtnMale              |
| TextBox        | Cajas de texto       | txt     | txtUsername,   txtPassword          |

## **Variable names**


### **C#** language
Variable names must be named using the camelcase convention, the variable name must be related to its use.

**Example 1**

A variable for age will be called *user**Age*** where _user_ and is the prefix of the instance we are getting the value from and **Age** is the use or value we are going to store in it.

### Microsoft**SQL**
Variables that **refer to a parameter used by taking from a table will use the same name as the table parameter**, otherwise they will be named as a C# variable.