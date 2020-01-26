import logging 

from model.random_generation_utils import generate_number, generate_operation


logger = logging.getLogger(__name__)

class Model:
    '''
        The calculator of the library:
    Its role is to generate randomly new challenge which respects the parameters given by the user, to assess the answers, 
    and to test if the game is finished, or not. 
    '''
    
    def __init__(self, limit_score, born_sup, nbr_dec, operations_allowed):
        self.limit_score = int(limit_score)
        self.born_sup = float(born_sup)
        self.nbr_dec = int(nbr_dec)
        self.operations_allowed = operations_allowed
        self.score = 0
        self.nbr_rounds_played = 0
        # initialize states
        self.success = False
        self.still_playing = True
        
    def generate_challenge(self):
        ''' Updates the current calculation, and returns it for the Controller. '''
        ope = generate_operation(self.operations_allowed)
        nbr1 = generate_number(self.born_sup, self.nbr_dec)
        nbr2 = generate_number(self.born_sup, self.nbr_dec)
        self.current_calculation = nbr1 + ' ' + ope + ' ' + nbr2   
        return self.current_calculation
    
    def assess_answer(self, user_answer):
        '''Assess the answer of the user and if the game is finished or not
        user_answer (string) value entered by the user and collected by the
        Controller.'''
        self.nbr_rounds_played += 1 # keep records of the number of rounds for the performance statistic  
        
        solution = round(eval(self.current_calculation.replace('x', '*')), self.nbr_dec)   # round is needed in case of division 
        try:
            if float(solution) == float(user_answer): # The user gave a correct answer
                self.score += 1
                self.success = True
            else:
                self.success = False
        except ValueError:  # The user has entered a wrong format as answer 
            logger.warning('The answer has a wrong format')
            self.success = False

        if self.score == self.limit_score:  # The game is now finished
            self.still_playing = False

        return self.success, self.still_playing  # returns new states for the controller
    
    @property 
    def percentage_success(self):
        '''Returns the percentage of rounds succeeded by the user'''
        return round(self.score / self.nbr_rounds_played * 100, 1)