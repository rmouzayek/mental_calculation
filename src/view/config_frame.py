import tkinter as tk


from view.view_utils import TableCheckb, LabelledSpinb


class ConfigFrame(tk.Frame):
    ''' Class implementing the configuration frame. '''
    
    def __init__(self, controller, view, root):
        super(ConfigFrame, self).__init__(root)
        self.controller = controller
        self.view = view
        self.root = root
        
        # Widgets creation
        self.button_return = tk.Button(self, text='Return', command=self.go_to_main, bg='grey', width=15, height=3, font=("Helvetica", 25))
        self.LabelledSpinb_nbr_games = LabelledSpinb(self, text="Number of halves:", from_=1, to=100, init_value=5)
        self.LabelledSpinb_born_sup = LabelledSpinb(self, text="Biggest number:", from_=1, to=100000, init_value=10)
        self.LabelledSpinb_nbr_dec = LabelledSpinb(self, "Number of decimals:", from_=0, to=5, init_value=0)
        self.lab_operations = tk.Label(self, text="Operations:", font=("Helvetica", 20), fg = "light blue", width=0, height=3)
        self.tablecheckb = TableCheckb(self, {'+': 1, '-': 1, 'x': 1, '/': 0})      
        self.operation_frame = self.tablecheckb.frame

        # Widgets layout
        self.LabelledSpinb_nbr_games.grid(row=0)
        self.LabelledSpinb_born_sup.grid(row=1)
        self.LabelledSpinb_nbr_dec.grid(row=2)
        self.lab_operations.grid(row=3, column=0)
        self.operation_frame.grid(row=3, column=1)
        self.button_return.grid(row=7, column=0)
        
    def go_to_main(self):
        ''' To go to the main_frame. '''
        self.view.go_to_main()
    
