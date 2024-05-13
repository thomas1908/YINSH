import wx

class Case:
    def __init__(self, x, y, value=1):
        self.x = x
        self.y = y
        self.value = value  # 0 for empty, 1 for one player, 2 for another player

    def set__Value(self, value):
        self.value = value

    def get__Value(self):
        return self.value

class BoardPanel(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)
        self.board = [
            [0, 0, 0, 0, Case(4, 0), 0, Case(6, 0), 0, 0, 0, 0],
            [0, 0, 0, Case(3, 1), 0, Case(5, 1), 0, Case(7, 1), 0, 0, 0],
            [0, 0, Case(2, 2), 0, Case(4, 2), 0, Case(6, 2), 0, Case(8, 2), 0, 0],
            [0, Case(1, 3), 0, Case(3, 3), 0, Case(5, 3), 0, Case(7, 3), 0, Case(9, 3), 0],
            [0, 0, Case(2, 4), 0, Case(4, 4), 0, Case(6, 4), 0, Case(8, 4), 0, 0],
            [0, Case(1, 5), 0, Case(3, 5), 0, Case(5, 5), 0, Case(7, 5), 0, Case(9, 5), 0],
            [Case(0, 6), 0, Case(2, 6), 0, Case(4, 6), 0, Case(6, 6), 0, Case(8, 6), 0, Case(10, 6)],
            [0, Case(1, 7), 0, Case(3, 7), 0, Case(5, 7), 0, Case(7, 7), 0, Case(9, 7), 0],
            [Case(0, 8), 0, Case(2, 8), 0, Case(4, 8), 0, Case(6, 8), 0, Case(8, 8), 0, Case(10, 8)],
            [0, Case(1, 9), 0, Case(3, 9), 0, Case(5, 9), 0, Case(7, 9), 0, Case(9, 9), 0],
            [Case(0, 10), 0, Case(2, 10), 0, Case(4, 10), 0, Case(6, 10), 0, Case(8, 10), 0, Case(10, 10)],
            [0, Case(1, 11), 0, Case(3, 11), 0, Case(5, 11), 0, Case(7, 11), 0, Case(9, 11), 0],
            [Case(0, 12), 0, Case(2, 12), 0, Case(4, 12), 0, Case(6, 12), 0, Case(8, 12), 0, Case(10, 12)],
            [0, Case(1, 13), 0, Case(3, 13), 0, Case(5, 13), 0, Case(7, 13), 0, Case(9, 13), 0],
            [0, 0, Case(2, 14), 0, Case(4, 14), 0, Case(6, 14), 0, Case(8, 14), 0, 0],
            [0, Case(1, 15), 0, Case(3, 15), 0, Case(5, 15), 0, Case(7, 15), 0, Case(9, 15), 0],
            [0, 0, Case(2, 16), 0, Case(4, 16), 0, Case(6, 16), 0, Case(8, 16), 0, 0],
            [0, 0, 0, Case(3, 17), 0, Case(5, 17), 0, Case(7, 17), 0, 0, 0],
            [0, 0, 0, 0, Case(4, 18), 0, Case(6, 18), 0, 0, 0, 0]
        ]
        self.Bind(wx.EVT_PAINT, self.on_paint)
        self.Bind(wx.EVT_LEFT_DOWN, self.on_left_down)

    def on_paint(self, event):
        dc = wx.PaintDC(self)
        dc.Clear()
        for row in self.board:
            for case in row:
                if case != 0:
                    if case.get__Value() == 1:
                        dc.SetBrush(wx.Brush("black"))
                    elif case.get__Value() == 2:
                        dc.SetBrush(wx.Brush("white"))
                    else:
                        dc.SetBrush(wx.Brush("grey"))
                    dc.DrawCircle(case.x * 40 + 20, case.y * 40 + 20, 15)

    def on_left_down(self, event):
        pos = event.GetPosition()
        x = pos.x // 40
        y = pos.y // 40
        if 0 <= x < 11 and 0 <= y < 19:
            self.board[y][x].set__Value(2)
            self.Refresh()

class MainFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title="YINSH Board", size=(500, 800))
        panel = BoardPanel(self)

if __name__ == '__main__':
    app = wx.App(False)
    frame = MainFrame()
    frame.Show()
    app.MainLoop()