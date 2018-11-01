#encoding=utf-8
# Hello World
import tkinter as tk

# root = tk.Tk()
# label = tk.Label(root, text="Hello World", padx = 10, pady = 20)
# label.pack()

# root.mainloop()

class Root(tk.Tk):
	def __init__(self):
		super().__init__()

		self.label = tk.Label(self, text = "Hello World!", padx = 5, pady = 5)

		self.label.pack()

if __name__ == "__main__":
	root = Root()
	root.mainloop()