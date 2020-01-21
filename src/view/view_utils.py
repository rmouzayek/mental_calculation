import tkinter as tk

def init_root(root):
    ''' Initializes the fixed size root. '''
    root.title("Mental calculations")
    root.geometry('772x600')
    root.minsize(width=772, height=600)
    root.maxsize(width=772, height=600)
    return root
    
def change_page(old_frame, new_frame):
    ''' Switches frame. '''
    old_frame.grid_forget()
    new_frame.grid(row=0)
    
class TableCheckb:
    ''' Compound Widget composed of several Checkbuttons. '''
    def __init__(self, main_frame, dict_labels):
        self.frame = tk.Frame(main_frame)
        self.dict_labels = dict_labels
        self.Variables = [tk.IntVar(value=default_val) for default_val in dict_labels.values()]
        self.checkb = []
        for index, item in enumerate(self.dict_labels.keys()):
            new_checkb = tk.Checkbutton(self.frame, text = item, variable=self.Variables[index])
            self.checkb.append(new_checkb)
            new_checkb.grid(row=index)
            
    def get(self):
        ''' Get the value of the different Checkbuttons. '''
        return dict(zip(self.dict_labels.keys(), [var.get() for var in self.Variables]))

class LabelledSpinb:
    ''' Compound widget composed of a Label and a Spinbox. '''
    def __init__(self, parent, text, from_, to, init_value):
        self.var = tk.IntVar(value = init_value)
        self.spinb = tk.Spinbox(parent, from_=from_, to=to, textvariable=self.var)
        self.lab = tk.Label(parent, text=text, font=("Helvetica", 20), fg = "light blue", width=25, height=3)
        
    def get(self):
        ''' To get the value of the Spinbox. '''
        return self.var.get()
    
    def grid(self, row):
        ''' Overloads grid method. '''
        self.lab.grid(row=row, column=0)
        self.spinb.grid(row=row, column=1)
        

class RecordScreen(tk.Label):
    ''' Special Label for the record. '''
    def __init__(self, parent):
        self.parent = parent
        self.var_record = tk.StringVar(value='Record: -')
        self.record = None 
        super().__init__(parent, textvariable=self.var_record, font=("Helvetica", 20), fg = "red", width=15, height=2)
        
    def update(self, new_record):
        ''' To update the record.'''
        self.record = new_record
        self.var_record.set('Record: ' + str(new_record))
        
    def get(self):
        ''' To get the value of the current record. '''
        return self.record 
    
    
            
            