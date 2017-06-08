#coding:utf8
import wx
import os,sys
import time
import wx.lib.filebrowsebutton
import wx.media

app = wx.App()
frame = wx.Frame(None,-1,u'mp3player')
dc = wx.ClientDC(frame)
bmp = wx.Bitmap('E:\\cat.jpg')
frame.SetBackgroundColour('cyan')
dc.DrawBitmap(bmp,0,0)

panel = wx.Panel(frame,size=(550,350))
# mp3files = wx.FileDialog(panel,message='Choose a mp3 music',style='wx.OPEN | wx.CHANGE_DIR')
mp3files = wx.lib.filebrowsebutton.FileBrowseButton(panel,labelText='Select a mp3 file',fileMask='*.mp3')
time.sleep(2)
# filename = mp3files.GetValue()
# print 'filename:', filename

play = wx.media.MediaCtrl(panel)
def windows_closed(n):
	os.system('tskill python')

# def playmusic(b):
# 	filename = mp3files.GetValue()
# 	# print 'filename:',filename
# 	sound = wx.Sound(filename)
# 	if sound.IsOk():
# 		sound.Play(wx.SOUND_ASYNC)
# 	else:
# 		wx.MessageBox('invalid file format or file lost','Error')

def playmusic(b):
	filename = mp3files.GetValue()
	# print 'filename:',filename
	sound = wx.Sound(filename)
	# sound = wx.media.MediaCtrl(filename)
	# if sound.IsOk():
	play.Play()
	if play.Load('E:\cyanflower.mp3'):
		play.Load('E:\cyanflower.mp3')
		# play.Play()
		# frame.GetSizer().Layout()
		print 'play',play.Play(),'load'
		play.Play()

		# play.PLAY
		# play.SetInitialSize()
		
		# sound.Play(wx.SOUND_ASYNC)
	else:
		wx.MessageBox('invalid file format or file lost','Error')


btn0 = wx.Button(panel,label='open',pos=(0,0),size=(50,25))
# btn0.Bind(wx.EVT_BUTTON,mp3files)
btn1 = wx.Button(panel,label='PLAY',pos=(60,100),size=(50,25))
# btn1.Bind(wx.EVT_BUTTON,windows_closed)
print play.Load('E:\\cyanflower.mp3')
play.Load('E:\\cyanflower.mp3')
btn1.Bind(wx.EVT_BUTTON,playmusic)
btn2 = wx.Button(panel,label='PAUSE',pos=(112,100),size=(50,25))
btn3 = wx.Button(panel,label='STOP',pos=(164,100),size=(50,25))
btn4 = wx.Button(panel,label='NEXT',pos=(216,100),size=(50,25))
btn5 = wx.Button(panel,label='PREV',pos=(268,100),size=(50,25))
btn5.Bind(wx.EVT_BUTTON,windows_closed)

frame.Show()
app.MainLoop()