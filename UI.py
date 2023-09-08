import wx


FONT_STYLE='微软雅黑'

class MyFrame(wx.Frame):
    def __init__(self, parent, title, handle):
        super(MyFrame, self).__init__(parent, title=title, size=(300, 200))

        panel = wx.Panel(self)

        st = wx.StaticText(panel, -1, '请确认是否已登录',
                            style=wx.ALIGN_CENTER_HORIZONTAL)  # 生成静态文本控件，水平居中
        st.SetFont(wx.Font(20, wx.DEFAULT, wx.NORMAL,
                    wx.NORMAL, False, FONT_STYLE))  # 设置字体字号

        # 创建一个水平和垂直居中的BoxSizer来容纳文本控件
        sizer = wx.BoxSizer(wx.VERTICAL)
        # 方法用于在 sizer 中添加一个可伸缩的空白空间。这个空白空间会根据布局的需要自动调整大小，以填充剩余的空白区域。它可以用来控制布局中的间距和对齐。
        # sizer.AddStretchSpacer()
        sizer.Add(st, 0, wx.ALIGN_CENTER_HORIZONTAL)
        # sizer.AddStretchSpacer()

        panel.SetSizer(sizer)

        button = wx.Button(panel, label="已登录", pos=(100, 50), size=(100, 50))
        button.SetFont(wx.Font(16, wx.DEFAULT, wx.NORMAL, wx.NORMAL, False, FONT_STYLE))
        button.Bind(wx.EVT_BUTTON, lambda event,
                    handle=handle: self.onclick(event, handle))  # 绑定按钮点击事件

        sizer.Add(button, 0, wx.ALIGN_CENTER_HORIZONTAL)

    def onclick(self, event, handle):
        # self.Close()



        handle()
        return True


def handle():
    print('handle')


def initUI(title, onclick):
    app = wx.App()
    frame = MyFrame(None, title, onclick)
    frame.Center()
    frame.Show()
    app.MainLoop()


if __name__ == '__main__':
    initUI('请扫码登录', handle)
