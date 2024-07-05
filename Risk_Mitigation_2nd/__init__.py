from otree.api import *
import random as r

doc = """
Degli Antoni, Faillo and Menegatti 2024
Risk taking risky benefit - Baseline scenario 1 + Second-order risk change
"""


class C(BaseConstants):
    NAME_IN_URL = 'Risk_Mitigation_2nd'
    EXCHANGE_RATE=0.02
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    ENDOWMENT=50

class Subsession(BaseSubsession):
     pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    proceed = models.IntegerField()
    insure_1 = models.IntegerField(
        min=0, max=C.ENDOWMENT)
    insure_2 = models.IntegerField(
        min=0, max=C.ENDOWMENT)
    decision_1 = models.IntegerField(
         max=C.ENDOWMENT, initial=-1)   #not used in this app but passed to the unique MPL app
    decision_2 = models.IntegerField(
        max=C.ENDOWMENT, initial=-1)   #not used in this app but passed to the unique MPL app
    paid_decision=models.IntegerField()
    lottery_1= models.IntegerField()
    lottery_2= models.IntegerField()
    q1_1 = models.IntegerField(choices=[[1, 'definitely greater than an uninsured token'], [2, 'definitely lower than an uninsured token'], [3, 'which may be lower or greater than an uninsured token']], initial=0)
    q1_2 = models.IntegerField(choices=[[1, '£8 (50 tokens x £0.16)'], [2, '£4 (50 tokens x £0.08)'], [3, '£3 (50 tokens x £0.06)']], initial=0)
    q1_3 = models.IntegerField(choices=[[1, '£8 (50 tokens x £0.16) or £4 (50 tokens x £0.08) depending on the return for uninsured tokens'], [2, '£8 (50 tokens x £0.16), £4 (50 tokens x £0.8) or £0 (50 tokens x £0.00) depending on the return for uninsured tokens'], [3, '0£ (50 tokens x 0.0£) or 4£ (50 tokens x 0.08£) depending on the extracted return for uninsured tokens']],initial=0)

    q2_1 = models.IntegerField(choices=[[1, 'definitely greater than an uninsured token'], [2, 'definitely lower than an uninsured token'], [3, 'which may be lower or greater than an uninsured token']], initial=0)
    q2_2 = models.IntegerField(choices=[[1, '£8 (50 tokens x £0.16)'],[2, '£3 (50 tokens x £0.06)'], [3, '£0 (50 tokens x £0)'], ], initial=0)
    q2_3 = models.IntegerField(choices=[[1, '£8 (50 tokens x £0.16)'], [2, '£8 (50 tokens x £0.16) or £0 (50 tokens x £0) depending on return for uninsured tokens'], [3, '0£ (50 tokens x 0.0£)']],initial=0)

    errors_1=models.IntegerField(initial = 0)
    errors_2=models.IntegerField(initial = 0)
    failed_too_many = models.BooleanField(initial=False)
    second_order=models.IntegerField(initial = 0) # = 1 if treatment = second order (used in MPL app)





def set_payoff(player: Player):
    player.second_order = 1
    player.paid_decision=r.randint(1,2)
    player.lottery_1=r.randint(1,3) #random draw for the payment in case in which decision_1 is selected
    player.lottery_2 =r.randint(1,2) #random draw for the payment in case in which decision_2 is selected

    if player.paid_decision== 1: #decision 1 is selected
        if player.lottery_1 ==1: # loss = 0.16
           player.payoff=(50-player.insure_1)*0.0+(player.insure_1)*0.06
        if player.lottery_1 ==2: # loss = 0.08
           player.payoff=(50-player.insure_1)*0.08+(player.insure_1)*0.06
        if player.lottery_1 ==3: # no loss
           player.payoff=(50-player.insure_1)*0.16+(player.insure_1)*0.06
    if player.paid_decision== 2: #decision 2 is selected
        if player.lottery_2==1: # loss = 0.16
           player.payoff=(50-player.insure_2)*0+(player.insure_2)*0.06
        else: #no loss
           player.payoff=(50-player.insure_2)*0.16+(player.insure_2)*0.06

    participant=player.participant
    participant.vars['decision_1']= player.decision_1
    participant.vars['decision_2']= player.decision_2
    participant.vars['insure_1']= player.insure_1
    participant.vars['insure_2']= player.insure_2
    participant.vars['lottery_1']= player.lottery_1
    participant.vars['lottery_2'] = player.lottery_2
    participant.vars['paid_decision']= player.paid_decision
    participant.vars['second_order']= player.second_order
    print("paid", player.paid_decision, "lottery_1", player.lottery_1, "lottery_2", player.lottery_2, "payoff", player.payoff)

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
    @staticmethod
    def is_displayed(player: Player):
        return player.proceed ==  1

    def vars_for_template(player: Player):
        return dict(endowment=C.ENDOWMENT)

    def error_message(player: Player, values):
        solutions = dict(q1_1=3, q1_2=3, q1_3=2)
        errors = {f: 'Wrong' for f in solutions if values[f] != solutions[f]}
        if errors:
            player.errors_1 += 1
            if player.errors_1>1:
                player.failed_too_many = True
                # we don't return any error here; just let the user proceed to the
                # next page, but the next page is the 'failed' page that boots them
                # from the experiment.
            else:
                return errors


class Decision_1(Page):
    form_model = 'player'
    form_fields = ['insure_1']

    @staticmethod
    def js_vars(player: Player):
        return dict(endowment=C.ENDOWMENT)
    def is_displayed(player: Player):
        return player.proceed ==  1
    def vars_for_template(player: Player):
            return dict(endowment=C.ENDOWMENT)


class Questions_2(Page):
    form_model = 'player'
    form_fields = ['q2_1', 'q2_2', 'q2_3']
    @staticmethod
    def is_displayed(player: Player):
        return player.proceed ==  1

    def vars_for_template(player: Player):
        return dict(endowment=C.ENDOWMENT)

    def error_message(player: Player, values):
        solutions = dict(q2_1=3, q2_2=2, q2_3=2)
        errors = {f: 'Wrong' for f in solutions if values[f] != solutions[f]}
        if errors:
            player.errors_2 += 1
            if player.errors_2>1:
                player.failed_too_many = True
                # we don't return any error here; just let the user proceed to the
                # next page, but the next page is the 'failed' page that boots them
                # from the experiment.
            else:
                return errors

class Decision_2(Page):
    form_model = 'player'
    form_fields = ['insure_2']

    @staticmethod
    def js_vars(player: Player):
        return dict(endowment=C.ENDOWMENT)
    def is_displayed(player: Player):
        return player.proceed ==  1
    def vars_for_template(player: Player):
            return dict(endowment=C.ENDOWMENT)
    def before_next_page(player: Player, timeout_happened):
        set_payoff(player)


class Fail1 (Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.failed_too_many

class Fail2 (Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.failed_too_many
#
#
#
# class Questionnaire(Page):
#     form_model = 'player'
#     form_fields = ['closeness_before','closeness_after','female','age','major','exp', ]
#
#     def is_displayed(player: Player):
#         return player.subsession.round_number ==  C.NUM_ROUNDS

page_sequence = [Instructions_1, Questions_1,  Fail1, Decision_1, Questions_2,  Fail2, Decision_2]
