#----------------------------------------------------------Headers-------------------------------------------------------
import tkinter as tk

#-----------------------------------------------------------Globals-----------------------------------------------------------

_bgcolor = '#d9d9d9'  # X11 color: 'gray85'
_fgcolor = '#000000'  # X11 color: 'black'
_compcolor = '#d9d9d9' # X11 color: 'gray85'
_ana1color = '#d9d9d9' # X11 color: 'gray85'
_ana2color = '#ececec' # Closest X11 color: 'gray92'
font10 = "-family {Lucida Sans Unicode} -size 18 -weight bold "  \
    "-underline 1"
font11 = "-family {Microsoft YaHei Light} -size 14 -weight "  \
    "bold"
#----------------------------------------------------------Functions------------------------------------------------------
def Trees():
    import BinaryTreeVisualization
    root.destroy()
    
def Graphs():
    import graphViz
    root.destroy()
    return
#----------------------------------------------------------GUI Window-----------------------------------------------------
root = tk.Tk()
photo1 = tk.PhotoImage(file = r"images\trees.png")
photo2 = tk.PhotoImage(file = r"images\graphs.png")
root.geometry("600x450+374+181")
root.minsize(120, 1)
root.maxsize(4100, 893)
root.resizable(1, 1)
root.title("New Toplevel")
root.configure(background="#000000")
root.configure(highlightbackground="#000000")

Label1 = tk.Label(root)
Label1.place(relx=0.2, rely=0.044, height=41, width=394)
Label1.configure(activebackground="#00ff00")
Label1.configure(activeforeground="#008000")
Label1.configure(background="#000000")
Label1.configure(disabledforeground="#a3a3a3")
Label1.configure(font=font10)
Label1.configure(foreground="#008000")
Label1.configure(text='''Algorithms Visualizer''')

Button1 = tk.Button(root, image=photo1,relief="raised")
Button1.place(relx=0.033, rely=0.267, height=234, width=267)
Button1.configure(activebackground="#ececec")
Button1.configure(activeforeground="#000000")
Button1.configure(background="#d9d9d9")
Button1.configure(disabledforeground="#a3a3a3")
Button1.configure(foreground="#000000")
Button1.configure(highlightbackground="#d9d9d9")
Button1.configure(highlightcolor="black")
Button1.configure(highlightthickness="2")
Button1.configure(pady="0")
Button1.configure(text='''Button''')
Button1.configure(command=Trees)

Label2 = tk.Label(root)
Label2.place(relx=0.117, rely=0.8, height=31, width=174)
Label2.configure(background="#000000")
Label2.configure(disabledforeground="#a3a3a3")
Label2.configure(font=font11)
Label2.configure(foreground="#ff0080")
Label2.configure(text='''Tree Algorithms''')

Button1_9 = tk.Button(root ,image=photo2 ,relief="raised")
Button1_9.place(relx=0.517, rely=0.267, height=234, width=267)
Button1_9.configure(activebackground="#ececec")
Button1_9.configure(activeforeground="#000000")
Button1_9.configure(background="#d9d9d9")
Button1_9.configure(disabledforeground="#a3a3a3")
Button1_9.configure(foreground="#000000")
Button1_9.configure(highlightbackground="#d9d9d9")
Button1_9.configure(highlightcolor="black")
Button1_9.configure(highlightthickness="2")
Button1_9.configure(pady="0")
Button1_9.configure(text='''Button''')
Button1_9.configure(command=Graphs)

Label2_10 = tk.Label(root)
Label2_10.place(relx=0.583, rely=0.8, height=31, width=184)
Label2_10.configure(activebackground="#f9f9f9")
Label2_10.configure(activeforeground="black")
Label2_10.configure(background="#000000")
Label2_10.configure(disabledforeground="#a3a3a3")
Label2_10.configure(font="-family {Microsoft YaHei Light} -size 14 -weight bold")
Label2_10.configure(foreground="#ff0080")
Label2_10.configure(highlightbackground="#d9d9d9")
Label2_10.configure(highlightcolor="black")
Label2_10.configure(text='''Graph Algorithms''')


root.mainloop()