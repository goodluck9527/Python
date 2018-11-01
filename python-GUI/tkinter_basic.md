# tkinter学习笔记
## 参考资料
1. [Github上的tkinter简单实例学习](https://github.com/Dvlv/Tkinter-By-Example)
2. [Python3 tkinter 官方文档](https://docs.python.org/2/library/tkinter.html)

## Hello World
### 知识点
1. tkinter的基本函数
```# 导入tkinter包
import tkinter as tk

# tkinter最基本的载体
root = tk.Tk()

# 组件
label = tf.Label("Label_name", padx=10, pady=10)

# 向root里面添加组件
label.pack()

# 运行图形界面
root.mainloop()

```

2. 继承Tk类
```import tkinter as tk

class Todo(tk.Tk):
	def __init__(self, tasks=None):
		super().__init__()
		...

if __name__ == "__main__":
	todo = Todo()
	todo.mainloop()
```