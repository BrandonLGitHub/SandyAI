class research_token:
    def __init__(self, feature, num, effect, outcome, description):
        self.feature = feature
        self.num = num
        self.effect = effect
        self.outcome = outcome
        self.description = description


#   TODO checks research tokens to see if they are usable for this round
def use_token(tokens, feature: object = None) -> object:
    return None


#   TODO create function that purchases tokens
def buy_tokens(tokens_held, dice, token_bank):
    if dice >= 2:
        feature = get_feature()
        number = get_num(feature, token_bank)
    return None


def get_feature():
    '''
    Gets an input from the player of what token feature they want to buy for Sandy
    #   TODO docstring
    :return:
    '''
    feature = input('What feature token should I buy?/n(1) Plants/n(2) Crab/n(3) Turtle/n(4) Seal/n(5) Bird/n(6) '
                    'Board').strip()
    if feature == '1':
        return 'Plants'
    elif feature == '2':
        return 'Crab'
    elif feature == '3':
        return 'Turtle'
    elif feature == '4':
        return 'Seal'
    elif feature == '5':
        return 'Bird'
    elif feature == '6':
        return 'Board'
    else:
        print('Invalid response please enter 1, 2, 3, 4, 5, or 6\n')
        get_feature()


def get_num(feature, token_bank):
    '''
    Gets input of what number of the token feature they are buying for Sandy
    TODO Docstring
    :param feature:
    :return:
    '''
    print(f'Which token for {feature} are we buying?\n')
    #   TODO from the token bank exract all the tokens for the feature and list the numbers and their description
    number = input().strip()
    if number == '1' and feature in ('Plants', 'Crab', 'Turtle', 'Seal', 'Bird', 'Board', 'Tectonic'):
        return 1
    elif number == '2' and feature in ('Crab', 'Turtle', 'Seal', 'Bird', 'Board', 'Tectonic'):
        return 2
    elif number == '3' and feature in ('Crab', 'Turtle', 'Bird'):
        return 3
    else:
        print('Invalid response please enter one of the available numbers for your feature\n')
        get_num(feature)

def generate_bank():
    '''
    Generates a list of all the token types
    TODO Docstring
    :return:
    '''
    plants1 = research_token('Plants', 1, 'Tectonic', None,
                             'When you place a 4th tree on an island, grow that island.')

    crab1 = research_token('Crab', 1, 'cost', 1, 'Place a crab for 1 die.')

    crab2 = research_token('Crab', 2, 'cost', None, 'Place 2 Crabs for 3 dice.')

    crab3 = research_token('Crab', 3, 'Tectonic', None,
                           'When you place 2 Crabs in the same round, grow 1 of the islands.')

    turtle1 = research_token('Turtle', 1, 'cost', 2, 'Place a Turtle for 2 dice.')

    turtle2 = research_token('Turtle', 2, 'Tectonic', None,
                             'When you place a Turtle, grow that island.')

    turtle3 = research_token('Turtle', 3, 'Plants', None,
                             'When you place a Turtle on an island, place 1 Tree on that island')

    seal1 = research_token('Seal', 1, 'cost', 3,'Place 1 Seal for 3 dice.')

    seal2 = research_token('Seal', 2, 'Plants', None,
                           'When you place a Seal, place 1 Tree on that island.')

    bird1 = research_token('Bird', 1, 'cost', 2, 'Steal a Bird for 2 dice.')

    bird2 = research_token('Bird', 2, 'Plants', None,
                           'When you steal a Bird, place 2 Trees on the island it lands on.')

    bird3 = research_token('Bird', 3, 'Tectonic', None,
                           'When you steal a Bird, grown the island it lands on.')

    tectonic1 = research_token('Tectonic', 1, 'cost', 2,
                               'Grow a small island into a medium one for 2 dice.')

    tectonic2 = research_token('Tectonic', 2, 'cost', 2,
                               'Grow a medium island into a large one for 3 dice.')

    board1 = research_token('Board', 1, 'dice', None,
                            'Re-roll any number of dice.')

    board2 = research_token('Board', 2, 'mods', None,
                            'Refresh all your Modifier Tiles')

    token_bank = [plants1, crab1, crab2, crab3, turtle1, turtle2, turtle3, seal1, seal2, tectonic1,
                  tectonic2, bird1, bird2, bird3, board1, board2]
    return token_bank
