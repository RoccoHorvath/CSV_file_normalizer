from tkinter import *
import json
from tkinter import messagebox, filedialog
from datetime import datetime
import time
import pandas as pd


def add_column():
    '''Adds another column field as a new row to the bottom of current rows. Column uses the next letter in the alphabet'''
    letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    global column_name_entry_list
    global content_entry_list

    row = master_frame.grid_size()[1]
    if row > 26:
        messagebox.showerror(title="Max number of columns exceeded",message="The current maximum number of columns is 26 (A-Z)")
        return
    label = Label(master_frame,text=f'Column {letters[row-1]}: ')
    label.grid(column=0,row=row)
    column_name_entry =Entry(master_frame)
    column_name_entry.grid(column=1,row=row)
    content_entry =Entry(master_frame)
    content_entry.grid(column=2,row=row)
    column_name_entry_list.append(column_name_entry)
    content_entry_list.append(content_entry)

def create_config():
    '''Takes input from entry field on GUI. Returns: config (dict)'''
    if header_entry.get():
        config = {"header row":int(header_entry.get())}
    else:
        config = {"header row":None}
    for index, colname in enumerate(column_name_entry_list):
        colname = colname.get()
        inputcol = content_entry_list[index].get()
        if colname is None or colname == "":
            continue
        config[colname] = int(inputcol)
    return config

def save_config():
    '''Saves new config to configs.json'''
    config = create_config()
    name = config_name_entry.get()
    if name.strip() == "" or not name:
        messagebox.showerror(title="Invalid name",message="Please enter a valid name before saving configuration.")
        return
    final_config = {name:config}
    try:
        with open("./configs.json",mode="r") as file:
            data = json.load(file)
            if name in data:
                overwrite = messagebox.askyesno(title="Config name already exists",message=f"A file configuration with the name: {name}\nalready exists. Do you want to overwrite it?")
                if overwrite:
                    data.update(final_config)
            else:
                data.update(final_config)
    except FileNotFoundError:
        with open("./configs.json",mode="w") as file:
            json.dump(final_config, file, indent=4)
    else:
        with open("./configs.json",mode="w") as file:
            json.dump(data, file, indent=4)
    config_dropdown['menu'].add_command(label=name)    
    messagebox.showinfo(title="Configuration Saved",message=f'File configuration "{name}" saved')

def browse():
    '''Allows the user to select files. Returns: filenames (tuple)'''
    global filenames
    filenames = filedialog.askopenfilenames(initialdir="/",title="Browse",filetypes=[("CSV Files", ".csv")])
    file_label.delete(0,END)
    file_label.insert(0,filenames)
    return filenames

def process_file():
    '''Saves new CSV file with the column names and values specified in config'''
    start = time.time()
    if clicked.get() == "Select Configuration":
        config = create_config()
    else:
        name = clicked.get()
        with open("./configs.json",mode="r") as file:
            data = json.load(file)
            config = data[name]

    for filename in filenames:
        with open(filename) as file:
            header_row = config.get('header row',None)
            if header_row:
                header_row -=1
            df = pd.read_csv(file,header=header_row,lineterminator='\n')
        updated_df = pd.DataFrame()
        for column, value in config.items():
            if column != "header row":
                updated_df[column] = df.iloc[:,value-1]
        date = datetime.now().strftime("%m_%d_%Y__%H_%M_%S_%f")
        updated_df.to_csv(f"normalized{date}.csv",index=False)
    end = time.time()
    messagebox.showinfo(title="Process Complete",message=f"File normalization complete.\nProcess took {end-start:.4f} seconds")

# Creation of GUI window and frames
root = Tk()
root.title('CSV File Normalizer')
root.geometry("500x665")
root.resizable(False, False)
upper_button_frame = Frame(root,width=5)
upper_button_frame.pack(side="top", fill="x")
second_button_frame = Frame(root,width=5)
second_button_frame.pack(side="top", fill="x")
master_frame = Frame(root,width=500,height=600, padx=10, pady=10)
master_frame.pack(side="top", fill="both")
lower_button_frame = Frame(root,width=5)
lower_button_frame.pack(side="bottom", fill="x")

# Populating dropdown with saved configs if configs.json exists. If not, creates file.
existing_configs = ["Select Configuration"]
try:
    with open("./configs.json",mode='r') as file:
        data = json.load(file)
        for name in data:
            existing_configs.append(name)
except FileNotFoundError:
    with open("./configs.json",mode='w') as file:
        json.dump({}, file, indent=4)
column_name_entry_list = []
content_entry_list = []

# Layout for top row
clicked = StringVar()
clicked.set("Select Configuration")
config_dropdown = OptionMenu(upper_button_frame,clicked,*existing_configs)
config_dropdown.config(width=17)
config_dropdown.grid(column=0,row=0)
file_label = Entry(upper_button_frame,width=38)
file_label.config(bg="white")
file_label.grid(column=4,row=0,sticky='ew')
browse_button = Button(upper_button_frame,text="Browse",command=browse)
browse_button.grid(column=5,row=0)
process_button = Button(upper_button_frame,text="Process File",anchor='e',command=process_file)
process_button.grid(column=6,row=0,sticky=E)

# Layout for second row
headers_label = Label(second_button_frame,text="Header row:")
headers_label.grid(row=1,column=0)
header_entry = Entry(second_button_frame,width=5)
header_entry.grid(column=1,row=1)        

# Layout for master frame and creates first input rows
column__name_label = Label(master_frame,text="Column Name:")
column__name_label.grid(column=1,row=0)
contents_label = Label(master_frame,text="Column # from file:")
contents_label.grid(column=2,row=0)
for n in range(5):
    add_column()

# Layout for lower frame
add_column_label = Label(lower_button_frame,text="Add Column", anchor='w')
add_column_label.grid(column=0,row=0,sticky=W)
add_column_button = Button(lower_button_frame,text="➕",anchor='w',command=add_column)
add_column_button.grid(column=1,row=0,sticky=W)
config_label = Label(lower_button_frame,text="Configuration name:")
config_label.grid(column=2,row=0)
config_name_entry = Entry(lower_button_frame)
config_name_entry.grid(column=3,row=0)
save_button = Button(lower_button_frame,text="Save",command=save_config)
save_button.grid(column=4,row=0)

# Allow window to always be on top and keeps window open until the user closes it
root.attributes('-topmost',True)
root.mainloop()
