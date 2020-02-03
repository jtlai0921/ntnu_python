import tkinter
from tkinter import ttk  # 匯入資源

win = tkinter.Tk()
tree = ttk.Treeview(win)  #表格

data1 = ['Vincent','12','男']
data2 = ['Anita','13','女']

tree = ttk.Treeview(win, columns=['1','2','3'], show='headings')

tree.heading('1', text='姓名')
tree.heading('2', text='年齡')
tree.heading('3', text='性别')

tree.column('1',width=100, anchor='center')
tree.column('2',width=100, anchor='center')
tree.column('3',width=100, anchor='center')

tree.insert('', 'end', values=data1)  # end 最後一筆，0 第一筆
tree.insert('', 'end', values=data2)  # end 最後一筆，0 第一筆
tree.grid()

tree.pack()
win.mainloop()
