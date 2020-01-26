from random import uniform, sample


def generate_number(born_sup, nbr_dec=0):
    ''' Generate (pseudo) randomly a number inferior of born_sup with nbr_dec figures after the dot. '''
    return str(round(uniform(0, born_sup), nbr_dec))

def generate_operation(Operations_allowed):
    ''' Generate (pseudo) randomly an arithmetic operation among the operations allowed in Operations_allowed (dict). '''
    Operations = [operation for operation, boolean in Operations_allowed.items() if boolean == 1]
    return sample(Operations, 1)[0]