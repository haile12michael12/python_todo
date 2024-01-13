import tkinter as tk
from tkinter import messagebox
from tkinter import font

def add_task():
  task = entry.get()
  if task:
   task_listboxx.insert(tk.END,task)
   entry.delete(0,tk.END)
  else:
    messagebox.showwarning("warning","please enter a task.")

# remove selected task
def remove_task():
  selected_task_index=task_listbox.curselection()
  if selected_task_index:
    tsk_listbox_delete(selected_task_index)
  else:
    messagebox.showwarning("warning", "please select a task to remove")

# main window
root=tk.TK()
root.title("To-do app")
root.geometry("400X250")
custom_font=font.nametofont("TkDefaultfont")
custom_font.configure(size=14)
entry=tk.Entry(root,font=custom_font,width=30)
entry.pack(pady=10)
#create button
add_button =tk.Button(root,
text="Add Task",
font =custom_font,
command=add_task)

remove_button =tk.Button(root,
text="remove Task",
font =custom_font,
command=remove_task)
add_button.pack()
remove_remove.pack()
#create a list box of the task

task_listbox =tk.listbox(root,
font=custom_font,
selectmode=tk.SINGLE,
width=30,
height=10)
task_listbox.pack()
  

#main loop
root.mainloop()