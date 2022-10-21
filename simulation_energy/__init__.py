from otree.api import *


doc = """
Simulation boost
"""


class C(BaseConstants):
    NAME_IN_URL = 'simulation_energy'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
     q1 = models.IntegerField(
     choices=[[1, 'Vero'], [2, 'Falso']],
     widget=widgets.RadioSelect)
     q2 = models.IntegerField()
     q3 = models.IntegerField()
     q4 = models.IntegerField(
     choices=[[1, 'Vero'], [2, 'Falso']],
     widget=widgets.RadioSelect)
# left column
     choice_pr=models.StringField()
# right column
     choice_r=models.StringField()
     errors=models.IntegerField(initial=0)

#functions
def creating_session(subsession: Subsession):
    session = subsession.session
    for p in subsession.get_players():
            p.participant.vars['choice_r']=[]# lista scelta right
            p.participant.vars['choice_pr']=[]# lista scelta left


class Instructions(Page):
    pass

class Control(Page):
    form_model = 'player'
    form_fields = ['q1', 'q2', 'q3', 'q4']
    def is_displayed(player: Player):
        ## ultimo round mostra risultati
        return player.subsession.round_number == 1

    def error_message(player: Player, values):
        if values['q1'] != 2 and values['q2'] != 40 and values['q3'] != 75 and values['q4'] !=1: #All the answers are wrong
            player.errors += 1
            return 'Tutte le risposte sono sbagliate'

        if values['q1'] != 2 and values['q2'] == 40 and values['q3'] == 75 and values['q4'] ==1: # The answer to question 1 is wrong
            player.errors += 1
            return 'La risposta alla domanda 1 è sbagliata'

        if values['q1'] == 2 and values['q2'] != 40 and values['q3'] == 75 and values['q4'] ==1: #sThe answer to question 2 is wrong
            player.errors += 1
            return 'La risposta alla domanda 2 è sbagliata'

        if values['q1'] == 2 and values['q2'] == 40 and  values['q3'] != 75 and values['q4'] ==1: # The answer to question 3 is wrong
            player.errors += 1
            return 'La risposta alla domanda 3 è sbagliata'

        if values['q1'] == 2 and values['q2'] == 40 and  values['q3'] == 75 and values['q4'] !=1: # The answer to question 4 is wrong
            player.errors += 1
            return 'La risposta alla domanda 4 è sbagliata'


        if values['q1'] != 2 and values['q2'] != 40 and  values['q3'] == 75 and values['q4'] ==1: # The answers to question 1 and 2 are wrong
            player.errors += 1
            return 'Le risposte alle domande 1 e 2 sono sbagliate'

        if values['q1'] != 2 and values['q2'] == 40 and values['q3'] != 75 and values['q4'] ==1: # he answers to question 1 and 3 are wrong
            player.errors += 1
            return 'Le risposte alle domande 1 e 3 sono sbagliate'

        if values['q1'] != 2 and values['q2'] == 40 and values['q3'] == 75 and values['q4'] !=1: # The answers to question 1 and 4 are wrong
            player.errors += 1
            return 'Le risposte alle domande 1 e 4 sono sbagliate'


        if values['q1'] == 2 and values['q2'] != 40 and  values['q3'] != 75 and values['q4'] ==1:  # The answers to question 2 and 3 are wrong
            player.errors += 1
            return 'Le risposte alle domande 2 e 3 sono sbagliate'

        if values['q1'] == 2 and values['q2'] != 40 and  values['q3'] == 75  and values['q4'] !=1: # The answers to question 2 and 4 are wrong
            player.errors += 1
            return 'Le risposte alle domande 2 e 4 sono sbagliate'


        if values['q1'] == 2 and values['q2'] == 40 and  values['q3'] != 75  and values['q4'] !=1: # The answers to question 3 and 4 are wrong
            player.errors += 1
            return 'Le risposte alle domande 3 e 4 sono sbagliate'

        if values['q1'] != 2 and values['q2'] != 40 and  values['q3'] != 75 and values['q4'] ==1: # The answers to question 1,2 and 3 are wrong
            player.errors += 1
            return 'Le risposte alle domande 1,2 e 3 sono sbagliate'

        if values['q1'] == 2 and values['q2'] != 40 and  values['q3'] != 75  and values['q4'] !=1: # The answers to question 2,3 and 4 are wrong
            player.errors += 1
            return 'Le risposte alle domande 2,3 e 4 sono sbagliate'

        if values['q1'] != 2 and values['q2'] == 40 and  values['q3'] != 75  and values['q4'] !=1: # The answers to question 1,3 and 4 are wrong
            player.errors += 1
            return 'Le risposte alle domande 1,3 e 4 sono sbagliate'

        if values['q1'] != 2 and values['q2'] != 40 and  values['q3'] == 75  and values['q4'] !=1: # The answers to question 1,2 and 4 are wrong
            player.errors += 1
            return 'Le risposte alle domande 1,2 e 4 sono sbagliate'

class Start (Page):
    pass

# PAGES
class Simulation(Page):
    timeout_seconds = 600
    form_model = 'player'
    def live_method(player, data):
        t=data['type']
        if t == 'choice_r':
            player.participant.vars['choice_r']=data['value']
        if t == 'choice_pr':
            player.participant.vars['choice_pr']=data['value']

        # print('received a choice',player.participant.vars['choice_r'])
        # with open('readme.txt', 'w') as f:
        #     f.write(str(player.participant.vars['choice_r']))
    @staticmethod
    def before_next_page(player, timeout_happened):
            player.choice_r=str(player.participant.vars['choice_r']) #stringhe per salvare scelte _r
            player.choice_pr=str(player.participant.vars['choice_pr']) #stringhe per salvare scelte _pr
            print('received a choice r',player.choice_r)
            print('received a choice pr',player.choice_pr)

class WaitPage0(WaitPage):
    wait_for_all_groups=True
    body_text = "Attendi che gli altri partecipanti facciano le loro scelte"


class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass


page_sequence = [Instructions, Control, WaitPage0,Start, Simulation]
