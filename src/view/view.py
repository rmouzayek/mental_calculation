import tkinter as tk

from view.view_utils import init_root, change_page
from view.config_frame import ConfigFrame
from view.main_frame import MainFrame


class View:
    ''' 
        Component of the library in charge of what the user can see. Every action of the user are communicated to the controller. 
    No direct interaction with the Model part. 
    Essentially composed of two frames:
    - the main_frame with which the user can start a new game, and play as well
    - the config_frame to change the parameters of the game.
    '''
    
    def __init__(self, root, controller):
        self.root = init_root(root)
        self.controller = controller
        self.main_frame = MainFrame(self.controller, self, self.root)
        self.config_frame = ConfigFrame(self.controller, self, self.root)
        self.main_frame.grid(row=0) # display the main_frame at the beginning
        
    def go_to_config(self):
        ''' To go to the config_frame. '''
        change_page(self.main_frame, self.config_frame)
    
    def go_to_main(self):
        ''' To go to the main_frame. '''
        change_page(self.config_frame, self.main_frame)
    
    def display_message(self, text, delay=0):
        ''' To display a message on the main_frame; delay is the time, in seconds, before the change occurs. '''
        self.main_frame.display_message(text, delay)
        
    def collect_parameters(self):
        ''' To pick up the parameters chosen by the user on the configuration frame. '''
        return self.config_frame.LabelledSpinb_nbr_games.get(), self.config_frame.LabelledSpinb_born_sup.get(), self.config_frame.LabelledSpinb_nbr_dec.get(), self.config_frame.tablecheckb.get() 
        
    def restart(self):
        ''' Restart the game. '''
        self.main_frame.restart()
    
    def get_time(self):
        ''' To pick up the time displayed by the chronometer. '''
        return self.main_frame.chrono.get()
    
    def get_record(self):
        ''' To pick up the current record. '''
        return self.main_frame.record_screen.get()
    
    def update_record(self, new_record):
        ''' Update the record on the main_frame '''
        self.main_frame.record_screen.update(new_record)