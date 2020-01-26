import tkinter as tk


from view.chronometer import Chronometer 
from view.view_utils import RecordScreen


class MainFrame(tk.Frame):
    ''' Class implementing the main frame of the application. '''
    
    def __init__(self, controller, view, root):
        super(MainFrame, self).__init__(root)
        self.controller = controller
        self.view = view
        self.root = root
        
        # Widgets creation:
        self.main_screen = tk.Label(self, text="Let's play!", font=("Helvetica", 25), fg = "light blue", borderwidth=4, width=40, height=4, relief="ridge")
        self.answer_screen = tk.Entry(self, width=30, font=("Helvetica", 25))
        self.main_button = tk.Button(self, text='Start', command=self.start_game, bg='red', width=15, height=3, font=("Helvetica", 25))
        self.config_button = tk.Button(self, text='Configuration', command=self.go_to_config, bg='grey', width=15, height=3, font=("Helvetica", 25))
        self.chrono = Chronometer(self, self.controller)
        self.record_screen = RecordScreen(self)
        
        # Widgets Layout:
        self.record_screen.grid(column=0, row=0)
        self.main_screen.grid(row=1, column=0, columnspan=2)
        self.answer_screen.grid(row=2, pady=60, columnspan=2)
        self.main_button.grid(column=0, row=3)
        self.config_button.grid(column=1, row=3)
    
        # Shortcut: 
        self.root.bind('<Return>', self.start_game)
        
    def display_message(self, text, delay=0):
        ''' To display a message on the main screen; delay is the time, in seconds, before the change occurs. '''
        def update_main_screen():
            self.main_screen['text'] = text
        self.root.after(delay * 1000, update_main_screen) # <=> time sleep, without buffer problem

    def start_game(self, event=None):
        ''' The user has triggered the beggining of the game.
        Updates of the main frame and Controller informed. '''
        # Change the screen 
        self.display_message('Go!')
        self.main_button.grid_forget()  # update start button becomes the next button
        self.config_button.grid_forget()
        self.main_button = tk.Button(self, text='Next', command=self.answer, bg='red', width=15, height=3, font=("Helvetica", 25))
        self.main_button.grid(column=0, row=3, columnspan=2)
        self.chrono.grid(column=1, row=0)
        self.controller.still_playing = True  # restart
        self.chrono.start()
        self.root.bind('<Return>', self.answer)
        
        # Call the controller to launch the game 
        self.controller.start_game()
    
    def go_to_config(self):
        ''' To go to the config_frame. '''
        self.view.go_to_config()
    
    def answer(self, event=None):
        ''' Sends the new user answer to the Controller. '''
        user_answer = self.answer_screen.get()
        self.answer_screen.delete(0, tk.END)  # clearn user screen 
        
        self.controller.handle_answer(user_answer)
        
    def restart(self):
        ''' Update the main_frame to restart the game. '''
        self.main_button.grid_forget()
        self.chrono.restart()
        self.main_button = tk.Button(self, text='Start again', command=self.start_game, bg='red', width=15, height=3, font=("Helvetica", 25))
        self.config_button = tk.Button(self, text='Configuration', command=self.go_to_config, bg='grey', width=15, height=3, font=("Helvetica", 25))
        self.main_button.grid(column=0, row=3)
        self.config_button.grid(column=1, row=3)
        self.root.bind('<Return>', self.start_game)