from otree.api import *
import random as r

doc = """
Degli Antoni, Faillo and Menegatti 2024
Risk taking risky benefit - Baseline scenario 1 + Second-order risk change
"""


class C(BaseConstants):
    NAME_IN_URL = 'Risk_Second_Order'
    EXCHANGE_RATE=0.02
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    ENDOWMENT=50
    PAID_DECISION = r.randint(1, 2) #select the payoff relevant decision
    LOTTERY_1=r.randint(1,3) #random draw for the payment in case in which decision_1 is selected
    LOTTERY_2 =r.randint(1, 2) #random draw for the payment in case in which decision_2 is selected

class Subsession(BaseSubsession):
     pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    proceed = models.IntegerField()
    decision_1 = models.IntegerField(
        min=0, max=C.ENDOWMENT)
    decision_2 = models.IntegerField(
        min=0, max=C.ENDOWMENT)
    paid_decision=models.IntegerField()
    lottery_1= models.IntegerField()
    lottery_2= models.IntegerField()
    q1_1 = models.IntegerField(choices=[[1, '50 tokens x £0.05 = £2.5.'], [2, '50 tokens x £0.00 = £0.'], [3, '50 tokens x £0.15 = £7.5.']], initial=0)
    q1_2 = models.IntegerField(choices=[[1, '£0 (50 tokens x £0.00) or £7.5 (50 tokens x £0.15) depending on the extracted return.'], [2, '£0 (50 tokens x £0.00) or £3.75 (50 tokens x £0.075) depending on the extracted return'], [3, '£0 (50 tokens x £0.00), £3.75 (50 tokens x £0.075), or £7.5 (50 tokens x £0.15) depending on the extracted return']], initial=0)
    q1_3 = models.IntegerField(choices=[[1, 'definitely yields more than a token invested in the activity with a certain return.'], [2, 'may yield more or less than a token invested in the activity with a certain return'], [3, 'definitely yields less than a token invested in the activity with a certain return']],initial=0)
    q2_1 = models.IntegerField(choices=[[1, '50 tokens x £0.05 = £2.5.'], [2, '50 tokens x £0.00 = £0.'], [3, '50 tokens x £0.15 = £7.5.']], initial=0)
    q2_2 = models.IntegerField(choices=[[1, '£0 (50 tokens x £0.00)'], [2, '£7.5 (50 tokens x £0.15)'], [3, '£0 (50 tokens x £0.00) or £7.5 (50 tokens x £0.15) depending on the extracted return']], initial=0)
    q2_3 = models.IntegerField(choices=[[1, 'definitely yields more than a token invested in the activity with a certain return.'], [2, 'may yield more or less than a token invested in the activity with a certain return'], [3, 'definitely yields less than a token invested in the activity with a certain return']],initial=0)

    errors_1=models.IntegerField(initial = 0)
    errors_2=models.IntegerField(initial = 0)


# def set_payoff(player: Player):
#     player.paid_decision = r.randint(1, 2) #select the payoff relevant decision
#     player.lottery_1=r.randint(1, 2,3) #random draw for the payment in case in which decision_1 is selected
#     player.lottery_2=r.randint(1, 2) #random draw for the payment in case in which decision_2 is selected
#
#     if player.paid_decision == 1: #decision 1 is selected
#         if player.lottery ==1: #uncertain income token value=0
#            player.payoff=player.decision_1*0.0+(50-player.decision_1)*0.05
#         if player.lottery ==2: #uncertain income token value=0.075
#            player.payoff=player.decision_1*0.075+(50-player.decision_1)*0.05
#         if player.lottery ==3: #uncertain income token value=0.15
#            player.payoff=player.decision_1*0.15+(50-player.decision_1)*0.05
#     if player.paid_decision == 2: #decision 2 is selected
#         if player.lottery ==1: #uncertain income token value=0
#            player.payoff=player.decision_2*0.0+(50-player.decision_2)*0.05
#         if player.lottery ==3: #uncertain income token value=0.15
#            player.payoff=player.decision_2*0.15+(50-player.Decision_2)*0.05


def set_payoff(player: Player):

    if C.PAID_DECISION == 1: #decision 1 is selected
        if C.LOTTERY_1 ==1: #uncertain income token value=0
           player.payoff=player.decision_1*0.0+(50-player.decision_1)*0.05
        if C.LOTTERY_1 ==2: #uncertain income token value=0.075
           player.payoff=player.decision_1*0.075+(50-player.decision_1)*0.05
        if C.LOTTERY_1 ==3: #uncertain income token value=0.15
           player.payoff=player.decision_1*0.15+(50-player.decision_1)*0.05
    if C.PAID_DECISION == 2: #decision 2 is selected
        if C.LOTTERY_2==1: #uncertain income token value=0
           player.payoff=player.decision_2*0.0+(50-player.decision_2)*0.05
           print("check")
        if C.LOTTERY_2 ==2: #uncertain income token value=0.15
           player.payoff=player.decision_2*0.15+(50-player.decision_2)*0.05
    print("paid", C.PAID_DECISION, "lottery_1", C.LOTTERY_1, "lottery_2", C.LOTTERY_2, "payoff", player.payoff)

def check_proceed(player:Player):
    if player.proceed != 1:
        player.payoff=-1

class Instructions_1(Page):
        form_model = 'player'
        form_fields = ['proceed']
        @staticmethod
        def before_next_page(player: Player, timeout_happened):
            check_proceed(player)

class Questions_1(Page):
    form_model = 'player'
    form_fields = ['q1_1', 'q1_2', 'q1_3']
    def is_displayed(player: Player):
        return player.proceed ==  1

    def vars_for_template(player: Player):
        return dict(endowment=C.ENDOWMENT)

    def error_message(player: Player, values):
        if values['q1_1'] != 1 and values['q1_2'] == 3 and values['q1_3'] ==2:
            player.errors_1 += 1
            return 'The answer to question 1 is wrong'
        if values['q1_1'] == 1 and values['q1_2'] != 3 and values['q1_3'] ==2:
            player.errors_1 += 1
            return 'The answer to question 2 is wrong'
        if values['q1_1'] == 1 and values['q1_2'] == 3 and values['q1_3'] !=2:
            player.errors_1 += 1
            return 'The answer to question 3 is wrong'
        if values['q1_1'] != 1 and values['q1_2'] != 3 and values['q1_3'] ==2:
            player.errors_1 += 1
            return 'The answer to questions 1 and 2 are wrong'
        if values['q1_1'] != 1 and values['q1_2'] == 3 and values['q1_3'] !=2:
            player.errors_1 += 1
            return 'The answer to questions 1 and 3 are wrong'
        if values['q1_1'] == 1 and values['q1_2'] != 3 and values['q1_3'] !=2:
            player.errors_1 += 1
            return 'The answer to questions 2 and 3 are wrong'
        if values['q1_1'] != 1 and values['q1_2'] != 3 and values['q1_3'] !=2:
            player.errors_1 += 1
            return 'All the answers are wrong'


class Decision_1(Page):
    form_model = 'player'
    form_fields = ['decision_1']

    @staticmethod
    def js_vars(player: Player):
        return dict(endowment=C.ENDOWMENT)
    def is_displayed(player: Player):
        return player.proceed ==  1 and player.errors_1<2
    def vars_for_template(player: Player):
            return dict(endowment=C.ENDOWMENT)
    def error_message(player: Player, values):
        if values['decision_1'] == None:
            return 'Please make a choice'


class Decision_1(Page):
    form_model = 'player'
    form_fields = ['decision_1']

    @staticmethod
    def js_vars(player: Player):
        return dict(endowment=C.ENDOWMENT)
    def is_displayed(player: Player):
        return player.proceed ==  1 and player.errors_1<2
    def vars_for_template(player: Player):
            return dict(endowment=C.ENDOWMENT)


class Questions_2(Page):
    form_model = 'player'
    form_fields = ['q2_1', 'q2_2', 'q2_3']
    def is_displayed(player: Player):
        return player.proceed ==  1 and player.errors_1<2

    def vars_for_template(player: Player):
        return dict(endowment=C.ENDOWMENT)

    def error_message(player: Player, values):
        if values['q2_1'] != 1 and values['q2_2'] == 3 and values['q2_3'] ==2:
            player.errors_2 += 1
            return 'The answer to question 1 is wrong'
        if values['q2_1'] == 1 and values['q2_2'] != 3 and values['q2_3'] ==2:
            player.errors_2 += 1
            return 'The answer to question 2 is wrong'
        if values['q2_1'] == 1 and values['q2_2'] == 3 and values['q2_3'] !=2:
            player.errors_2 += 1
            return 'The answer to question 3 is wrong'
        if values['q2_1'] != 1 and values['q2_2'] != 3 and values['q2_3'] ==2:
            player.errors_2 += 1
            return 'The answer to questions 1 and 2 are wrong'
        if values['q2_1'] != 1 and values['q2_2'] == 3 and values['q2_3'] !=2:
            player.errors_2 += 1
            return 'The answer to questions 1 and 3 are wrong'
        if values['q2_1'] == 1 and values['q2_2'] != 3 and values['q2_3'] !=2:
            player.errors_2 += 1
            return 'The answer to questions 2 and 3 are wrong'
        if values['q2_1'] != 1 and values['q2_2'] != 3 and values['q2_3'] !=2:
            player.errors_2 += 1
            return 'All the answers are wrong'

class Decision_2(Page):
    form_model = 'player'
    form_fields = ['decision_2']

    @staticmethod
    def js_vars(player: Player):
        return dict(endowment=C.ENDOWMENT)
    def is_displayed(player: Player):
        return player.proceed ==  1 and player.errors_2<2 and player.errors_1<2
    def vars_for_template(player: Player):
            return dict(endowment=C.ENDOWMENT)
    def before_next_page(player: Player, timeout_happened):
        set_payoff(player)


class Results(Page):
    def is_displayed(player: Player):
        return player.proceed ==  1 and player.errors_1<2 and player.errors_2<2

    def vars_for_template(player: Player):
        return dict(decision_1=player.decision_1, decision_2=player.decision_2, paid_decision=C.PAID_DECISION, lottery_1=C.LOTTERY_1, lottery_2=C.LOTTERY_2, payoff= player.payoff)



class Fail (Page):
    def is_displayed(player: Player):
        if (player.proceed ==  1 and player.errors_1>1) or (player.proceed ==  1 and player.errors_2>1):
            player.payoff=-1
        return (player.proceed ==  1 and player.errors_1>1) or (player.proceed ==  1 and player.errors_2>1)


#
#
#
# class Questionnaire(Page):
#     form_model = 'player'
#     form_fields = ['closeness_before','closeness_after','female','age','major','exp', ]
#
#     def is_displayed(player: Player):
#         return player.subsession.round_number ==  C.NUM_ROUNDS

page_sequence = [Instructions_1, Questions_1, Decision_1, Questions_2, Decision_2,Results, Fail]
