# install libraries pip install wxPython

import wx

class LoginFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='Login Form', size=(300, 360))

        panel = wx.Panel(self)

        # Create a vertical box sizer
        main_sizer = wx.BoxSizer(wx.VERTICAL)

        # Logo
        self.logo = wx.StaticBitmap(panel, bitmap=wx.Bitmap('resources/images/login.png'))
        main_sizer.Add(self.logo, 0, wx.ALIGN_CENTER | wx.TOP, 10)  # Centered with some top margin

        # Create a second vertical sizer for the input fields and labels
        input_sizer = wx.BoxSizer(wx.VERTICAL)

        # Username label and text box
        username_label = wx.StaticText(panel, label='Username:')
        input_sizer.Add(username_label, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        self.username = wx.TextCtrl(panel, size=(200, -1))
        input_sizer.Add(self.username, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        # Password label and text box
        password_label = wx.StaticText(panel, label='Password:')
        input_sizer.Add(password_label, 0, wx.ALIGN_CENTER | wx.ALL, 5)
        self.password = wx.TextCtrl(panel, style=wx.TE_PASSWORD, size=(200, -1))
        input_sizer.Add(self.password, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        # Login button
        self.login_button = wx.Button(panel, label='Login')
        self.login_button.Bind(wx.EVT_BUTTON, self.on_login)
        input_sizer.Add(self.login_button, 0, wx.ALIGN_CENTER | wx.ALL, 10)

        # Add the input sizer to the main sizer and center it
        main_sizer.Add(input_sizer, 0, wx.ALIGN_CENTER)

        # Set the sizer for the panel
        panel.SetSizer(main_sizer)

        self.Show()

    def on_login(self, event):
        valid_username = "admin"
        valid_password = "password123"

        username = self.username.GetValue()
        password = self.password.GetValue()

        if username == valid_username and password == valid_password:
            wx.MessageBox('Access Granted', 'Info', wx.OK | wx.ICON_INFORMATION)
        else:
            wx.MessageBox('Access Denied', 'Error', wx.OK | wx.ICON_ERROR)

        self.clear_fields()
        
    def clear_fields(self):
        self.username.SetValue("")
        self.password.SetValue("")
        self.username.SetFocus()

if __name__ == '__main__':
    app = wx.App(False)
    frame = LoginFrame()
    app.MainLoop()
