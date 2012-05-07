#!/usr/bin/python

# treectrl.py

import wx
import os, sys
from Parser import Parser

PATH = ""
parser = Parser("/home/mahmed/dev/groovy")

class StartUp(wx.Frame):
 def __init__(self, parent, id, title):
     wx.Frame.__init__(self, parent, id, title, wx.DefaultPosition, wx.Size(450, 350))

     hbox = wx.BoxSizer(wx.HORIZONTAL)
     vbox = wx.BoxSizer(wx.VERTICAL)
     panel1 = wx.Panel(self, -1)
     panel2 = wx.Panel(self, -1)

     menuBar = wx.MenuBar()
     menu = wx.Menu()
     menu.Append(99, "&Select", "Choose Directory")
     menuBar.Append(menu, "&Directory")
     self.SetMenuBar(menuBar)
     self.Bind(wx.EVT_MENU, self.opendir, id=99)


     self.tree = wx.TreeCtrl(panel1, 1, wx.DefaultPosition, (-1,-1), wx.TR_HIDE_ROOT|wx.TR_HAS_BUTTONS)
     self.root = self.tree.AddRoot('Project')
   
     self.tree.Bind(wx.EVT_TREE_SEL_CHANGED, self.OnSelChanged, id=1)
     self.display = wx.StaticText(panel2, -1, '',(10,10), style=wx.ALIGN_CENTRE)
     vbox.Add(self.tree, 1, wx.EXPAND)
     hbox.Add(panel1, 1, wx.EXPAND)
     hbox.Add(panel2, 1, wx.EXPAND)
     panel1.SetSizer(vbox)
     self.SetSizer(hbox)
     self.Centre()

 def OnSelChanged(self, event):
     item =  event.GetItem()
     self.display.SetLabel("blah" + self.tree.GetItemText(item))

 def opendir(self, event):
     dlg = wx.DirDialog(self, "Choose a directory:", style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)

     if dlg.ShowModal() == wx.ID_OK:
         PATH = dlg.GetPath();
         parser = Parser(PATH)
         parser.initialize()
         self.populate()
     dlg.Destroy()

 def populate(self):
     for file_name in parser.get_all_file_names():
         name = self.tree.AppendItem(self.root, file_name)
         for targets in parser.get_targets_by_file(file_name):
             self.tree.AppendItem(name, targets.Name)

class MyApp(wx.App):
 def OnInit(self):
     start = StartUp(None, -1, 'SpiderWeb')
     start.Show(True)
     self.SetTopWindow(start)
     return True

app = MyApp(0)
app.MainLoop()
