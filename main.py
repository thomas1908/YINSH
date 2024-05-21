import wx
from GameScene import GameScene

class MainFrame(wx.Frame):
    def __init__(self, *args, **kw):
        super(MainFrame, self).__init__(*args, **kw)
        self.InitUI()

    def InitUI(self):
        self.panel = wx.Panel(self)
        self.vbox = wx.BoxSizer(wx.VERTICAL)

        # Define button size
        button_size = (200, 60)

        # Add buttons with gaps in between
        button1 = wx.Button(self.panel, label='Jouer a 2 Joueur', size=button_size)
        button2 = wx.Button(self.panel, label='Jouer vs ai', size=button_size)
        button3 = wx.Button(self.panel, label='Jouer en réseau', size=button_size)
        button4 = wx.Button(self.panel, label='Mode Blitz', size=button_size)

        self.vbox.Add(button1, 0, wx.ALIGN_CENTER | wx.TOP, 20)  # Add top gap for the first button
        self.vbox.Add(button2, 0, wx.ALIGN_CENTER | wx.TOP, 20)  # Add top gap for the second button
        self.vbox.Add(button3, 0, wx.ALIGN_CENTER | wx.TOP, 20)  # Add top gap for the third button
        self.vbox.Add(button4, 0, wx.ALIGN_CENTER | wx.TOP, 20)

        self.hbox = wx.BoxSizer(wx.HORIZONTAL)
        self.hbox.Add(self.vbox, 1, wx.ALIGN_CENTER)


        self.panel.SetSizer(self.hbox)

        self.SetSize((500, 700))
        self.SetTitle('Menu Screen')
        self.Centre()

        button1.Bind(wx.EVT_BUTTON, self.OnButton1Click)
        #button2.Bind(wx.EVT_BUTTON, self.OnButton2Click)
        #button3.Bind(wx.EVT_BUTTON, self.OnButton3Click)
        button4.Bind(wx.EVT_BUTTON, self.OnButton4Click)


    def OnButton1Click(self, event):
        self.ShowGame()

    def ShowGame(self):
        self.panel.Destroy()  # Remove the panel with the buttons
        game_panel = GameScene(self,3 )
        self.SetTitle('Game Scene YNISH')
        self.SetSize((700, 900))
        self.Centre()
        self.Layout()

    def ShowMainMenu(self):
        self.DestroyChildren()  # Remove all children components
        self.InitUI()  # Reinitialize the main menu UI

    def OnButton4Click(self, event):
        self.ShowGameBlitzs()

    def ShowGameBlitzs(self):
        self.panel.Destroy()  # Remove the panel with the buttons
        game_panel = GameScene(self,1 )
        self.SetTitle('Game Scene YNISH')
        self.SetSize((700, 900))
        self.Centre()
        self.Layout()

    def ShowMainMenu(self):
        self.DestroyChildren()  # Remove all children components
        self.InitUI()  # Reinitialize the main menu UI

def main():
    app = wx.App()
    frm = MainFrame(None)
    frm.Show()
    app.MainLoop()

if __name__ == '__main__':
    main()