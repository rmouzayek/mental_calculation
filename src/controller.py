import tkinter as tk
import logging

from view.view import View
from model.model import Model


logger = logging.getLogger(__name__)

class Controller:
    def __init__(self):
        self.root = tk.Tk()
        self.view = View(self.root, self)
        # initialize states:
        self.still_playing = True
        self.parameters_game = None
        self.success = True

    def run(self):
        ''' Starts running out the tkinter application. '''
        self.root.mainloop()

    def start_game(self):
        ''' Starts the game.
        Start by collecting the parameters of the game chosen by the user.
        If these are new parameters then the current record is restarted.
        The model is then initialized, and the first round launched. '''
        logger.info('The game starts')
        if self.parameters_game != self.view.collect_parameters():  # new parameters => new record
            self.view.update_record('-')
        self.parameters_game = self.view.collect_parameters()
        self.model = Model(*self.parameters_game)  # init the model   
        self.launch_round()  # first round

    def launch_round(self):
        ''' Launchs a new round. 
        If the user failed the last round, then self.success is False and the current challenge remains the same: 
        the user has to succeed the calculation to get a new one. '''
        logger.info('New rounds launched.')
        if self.success:
            self.current_challenge = self.model.generate_challenge()
        logger.info('The current challenge is {}.'.format(self.current_challenge))
        self.view.display_message(self.current_challenge, 1)
        
    def _check_answer(self, user_answer):
        ''' Sends the user answer to the Model in order to assess it. '''
        self.success, self.still_playing = self.model.assess_answer(user_answer)
        if self.success:
            logger.info('The player succeeded the round.')
            self.view.display_message('congratulations!')
        else:
            logger.info('The player failed the round.')
            self.view.display_message('sorry bro ...  you failed!')
    
    def handle_answer(self, user_answer):
        logger.info('The player user answer is {}.'.format(user_answer))
        self._check_answer(user_answer)
        if self.still_playing: 
            self.launch_round()
        else:
            time_played = self.view.get_time()
            current_record = self.view.get_record()
            if current_record == '-' or time_played < current_record:  # new record 
                self.view.update_record(time_played)
                self.view.display_message('The game is now finished. \nYour time performance is {}! NEW RECORD ! \nYour percentage of success is {}%'.format(time_played, self.model.percentage_success))    
            else:
                self.view.display_message('The game is now finished. \nYour time performance is {}! \nYour percentage of success is {}%'.format(time_played, self.model.percentage_success))
            self.view.restart()