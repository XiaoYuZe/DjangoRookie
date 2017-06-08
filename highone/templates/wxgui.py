#coding:utf8
import wx
app = wx.App()
frame = wx.Frame(None,-1,u'hollo')
btn = wx.Button(frame,label='ok',pos=(200,100),size=(50,25))
frame.Show()
app.MainLoop()