#!/usr/bin/python

# commondialogs.py

import wx
import os, sys

class MyFrame(wx.Frame):
    def __init__(self, parent, id, title):

        wx.Frame.__init__(self, parent, id, title)

        #self.CreateStatusBar()
        menuBar = wx.MenuBar()
        menu = wx.Menu()
        menu.Append(99, "&Select", "Choose Directory")
        menuBar.Append(menu, "&Directory")
        self.SetMenuBar(menuBar)
        self.Bind(wx.EVT_MENU, self.opendir, id=99)

    def opendir(self, event):
         dlg = wx.DirDialog(self, "Choose a directory:", style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)

         if dlg.ShowModal() == wx.ID_OK:
             dlg.GetPath();
             self.SetStatusText('You selected: %s\n' % dlg.GetPath())
         dlg.Destroy()
         self.Close()

  
class MyApp(wx.App):
    def OnInit(self):
        myframe = MyFrame(None, -1, "SpiderWeb")
        myframe.CenterOnScreen()
        myframe.Show(True)
        return True
app = MyApp(0)
app.MainLoop();
