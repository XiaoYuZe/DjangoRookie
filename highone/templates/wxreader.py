#!/usr/bin/env python
import wx
def catfile(event):
    file=open(filename.GetValue(),'r')
    contents.SetValue(file.read())
    file.close()
 
app=wx.App()
win=wx.Frame(None,title='txt reader',size=(500,350))
bkg=wx.Panel(win)
catfileButton=wx.Button(bkg,label='Open')
catfileButton.Bind(wx.EVT_BUTTON,catfile)
 
filename=wx.TextCtrl(bkg)
contents=wx.TextCtrl(bkg,style=wx.TE_MULTILINE|wx.HSCROLL)
 
hbox=wx.BoxSizer()
hbox.Add(filename,proportion=1,flag=wx.EXPAND|wx.LEFT|wx.RIGHT,border=10)
hbox.Add(catfileButton,proportion=0,flag=wx.LEFT)
 
vbox=wx.BoxSizer(wx.VERTICAL)
vbox.Add(hbox,proportion=0,flag=wx.EXPAND|wx.ALL)
vbox.Add(contents,proportion=1,flag=wx.EXPAND|wx.LEFT|wx.BOTTOM|wx.RIGHT)
bkg.SetSizer(vbox)
win.Show()
app.MainLoop()