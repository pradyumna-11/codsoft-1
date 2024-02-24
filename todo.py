from tkinter import *
import customtkinter
from CTkListbox import *

customtkinter.set_appearance_mode("dark")  
customtkinter.set_default_color_theme("green")

def add_tasks():
    task_entered = input_box.get()
    input_box.delete(0,customtkinter.END)
    tasks_list_box.insert(END, task_entered)
    
def delete_task():
    selected_tasks = tasks_list_box.get()
    selected_tasks_indexes = tasks_list_box.curselection()
    for i in selected_tasks_indexes:
        tasks_list_box.delete(i)
        
def update_task():
    modified_value = input_box.get()
    selected_tasks_indexes = tasks_list_box.curselection()
    tasks_list_box.delete(selected_tasks_indexes[0])
    tasks_list_box.insert(selected_tasks_indexes[0],modified_value)
    input_box.delete(0,customtkinter.END)
        
def delete_all_task():
    tasks_list_box.delete("all")


root = customtkinter.CTk()
root.title("Todo's Application-Pradyumna")
root.geometry('600x600')
label = customtkinter.CTkLabel(root, text="Pradyumna's Todo Application", fg_color="transparent",font = ('Bree Serif',30))
label.pack(pady="20")

input_box = customtkinter.CTkEntry(root,placeholder_text="Enter a task",border_width=0,fg_color="white",corner_radius=2,width=500,text_color="black")
input_box.pack(pady = "10")

tasks_list_box = CTkListbox(root,height=350,width=500,button_fg_color = "red",highlight_color = "green",multiple_selection = True)
tasks_list_box.pack(pady="40")

buttons_frame = customtkinter.CTkFrame(root, width=200, height=200)
buttons_frame.pack(pady="20")

add_task_button = customtkinter.CTkButton(buttons_frame,text="Add Task",hover_color="black",command = add_tasks)
add_task_button.grid(row = 0,column = 0,padx= "5")

delete_task_button = customtkinter.CTkButton(buttons_frame,text="Delete Task",hover_color="black",command=delete_task)
delete_task_button.grid(row = 0,column = 1,padx = "5")

update_task_button = customtkinter.CTkButton(buttons_frame,text="Update Task",hover_color="black",command = update_task)
update_task_button.grid(row = 0,column = 2,padx = "5")

delete_all_task_button = customtkinter.CTkButton(buttons_frame,text="Delete All Task",hover_color="black",command=delete_all_task)
delete_all_task_button.grid(row = 0,column = 3,padx = "5")

root.mainloop()