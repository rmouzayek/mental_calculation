import tkinter as tk


class Chronometer(tk.Label):
    '''Class which implements a chronometer'''
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller 
        self.time_displayed = tk.StringVar(value='0') # the dynamic variable storing the current time
        super().__init__(root, textvariable=self.time_displayed, font=("Helvetica", 35), fg = "red", width=15, height=2)
       
    def update_chrono():
        '''Adds a second'''
        seconds = int(self.time_displayed.get())
        self.time_displayed.set(str(seconds + 1))
        
    def start(self):
        '''Launchs the chronometer'''
        if self.controller.still_playing: # Checks that the game is still on going
            seconds = int(self.time_displayed.get())
            self.time_displayed.set(str(seconds + 1))
            self.root.after(1000, self.start) # after waiting one second 
        
    def get(self): 
        '''Returns the value displayed by the chronometer'''
        return int(self.time_displayed.get())
    
    def restart(self):
        '''Restart the chronometer'''
        self.time_displayed.set('0')
        
        

        