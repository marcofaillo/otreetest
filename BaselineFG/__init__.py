from otree.api import *
import random as r

doc = """
Public goods with punishment, roughly based on Fehr & Gaechter 2000.
"""


class C(BaseConstants):
    NAME_IN_URL = 'BaselineFG'
    EXCHANGE_RATE=0.02
    PLAYERS_PER_GROUP = 4
    NUM_ROUNDS = 3
    ENDOWMENT = 10
    MPCR = 0.4
    MAX_PUNISHMENT = 10
    ORDER=[1,2,3,4]
    PUNISHMENT_SCHEDULE = {
        0: 0,
        1: 1,
        2: 2,
        3: 4,
        4: 6,
        5: 9,
        6: 12,
        7: 16,
        8: 20,
        9: 25,
        10: 30,
    }


class Subsession(BaseSubsession):
        pass


class Group(BaseGroup):
    total_contribution = models.FloatField()
    average_contribution=models.FloatField()
    individual_share = models.FloatField()



class Player(BasePlayer):
    contribution = models.FloatField(
        min=0, max=C.ENDOWMENT, label="Qual è la tua contribuzione (tra 0 e 10)?"
    )
    punish_p1 = models.IntegerField(choices=[[0, '0 (0)'],[1, '1 (1)'], [2, '2 (2)'], [3, ' 3 (4)'], [4, '4 (6)'],[5, '5 (9)'], [6, '6 (12)'],[7, '7 (16)'],[8, '8 (16)'],[9, '9 (20)'],[10, '10 (30)']], label="", blank=True,)
    punish_p2 = models.IntegerField(choices=[[0, '0 (0)'],[1, '1 (1)'], [2, '2 (2)'], [3, ' 3 (4)'], [4, '4 (6)'], [5, '5 (9)'],[6, '6 (12)'],[7, '7 (16)'],[8, '8 (20)'],[9, '9 (25)'],[10, '10 (30)']], label="", blank=True,)
    punish_p3 = models.IntegerField(choices=[[0, '0 (0)'],[1, '1 (1)'], [2, '2 (2)'], [3, ' 3 (4)'], [4, '4 (6)'], [5, '5 (9)'],[6, '6 (12)'],[7, '7 (16)'],[8, '8 (20)'],[9, '9 (25)'],[10, '10 (30)']], label="", blank=True,)
    punish_p4 = models.IntegerField(choices=[[0, '0 (0)'],[1, '1 (1)'], [2, '2 (2)'], [3, ' 3 (4)'], [4, '4 (6)'], [5, '5 (9)'],[6, '6 (12)'],[7, '7 (16)'],[8, '8 (20)'],[9, '9 (25)'],[10, '10 (30)']], label="", blank=True,)
    total_punishment= models.IntegerField()
    cost_of_punishment = models.IntegerField()
    punishment_received = models.IntegerField()
    contribution_p1=models.FloatField()
    contribution_p2=models.FloatField()
    contribution_p3=models.FloatField()
    contribution_p4=models.FloatField()
    payoff_1=models.FloatField(initial=0)
    payoff_2=models.FloatField(initial=0)
    cumul_payoff=models.FloatField(initial=0)
    player_name=models.IntegerField()
    show=models.IntegerField()
    final_payoff_euro=models.FloatField(initial=0)


def players_names(group: Group):
    shuffled_order = C.ORDER.copy()
    r.shuffle(shuffled_order)


    p1=group.get_player_by_id(1)
    p2=group.get_player_by_id(2)
    p3=group.get_player_by_id(3)
    p4=group.get_player_by_id(4)

    for p in group.get_players():
        p.show=shuffled_order[0]

        p1.player_name = 1
        p2.player_name = 2
        p3.player_name =3
        p4.player_name = 4
        if p.round_number >1:
            p.cumul_payoff=p.in_round(p.round_number - 1).cumul_payoff

def save_contributions(group: Group):
    p1=group.get_player_by_id(1)
    p2=group.get_player_by_id(2)
    p3=group.get_player_by_id(3)
    p4=group.get_player_by_id(4)

    for p in group.get_players():
            p.contribution_p1=p1.contribution
            p.contribution_p2=p2.contribution
            p.contribution_p3=p3.contribution
            p.contribution_p4=p4.contribution
            p1.player_name = 1
            p2.player_name = 2
            p3.player_name =3
            p4.player_name = 4
    group.total_contribution=sum([p.contribution for p in group.get_players()])
    group.average_contribution=group.total_contribution/4
    group.individual_share=group.total_contribution*C.MPCR
    print(group.individual_share)

def set_playoff_1(group: Group):
    for p in group.get_players():
        p.payoff_1=C.ENDOWMENT-p.contribution+group.individual_share

# PAGES
def set_playoff_2(group: Group):
    p1=group.get_player_by_id(1)
    p2=group.get_player_by_id(2)
    p3=group.get_player_by_id(3)
    p4=group.get_player_by_id(4)
    for p in group.get_players():
        p1.total_punishment=p1.punish_p2+p1.punish_p3+p1.punish_p4
        p1.cost_of_punishment=C.PUNISHMENT_SCHEDULE[p1.punish_p2] + C.PUNISHMENT_SCHEDULE[p1.punish_p3] + C.PUNISHMENT_SCHEDULE[p1.punish_p4]
        p2.total_punishment=p2.punish_p1+p2.punish_p3+p2.punish_p4
        p2.cost_of_punishment=C.PUNISHMENT_SCHEDULE[p2.punish_p1] + C.PUNISHMENT_SCHEDULE[p2.punish_p3] + C.PUNISHMENT_SCHEDULE[p2.punish_p4]
        p3.total_punishment=p3.punish_p1+p3.punish_p2+p3.punish_p4
        p3.cost_of_punishment=C.PUNISHMENT_SCHEDULE[p3.punish_p1] + C.PUNISHMENT_SCHEDULE[p3.punish_p2] + C.PUNISHMENT_SCHEDULE[p3.punish_p4]
        p4.total_punishment=p4.punish_p1+p4.punish_p2+p4.punish_p3
        p4.cost_of_punishment=C.PUNISHMENT_SCHEDULE[p4.punish_p1] + C.PUNISHMENT_SCHEDULE[p4.punish_p2] + C.PUNISHMENT_SCHEDULE[p4.punish_p3]
        p1.punishment_received=p2.punish_p1+p3.punish_p1+p4.punish_p1
        p2.punishment_received=p1.punish_p2+p3.punish_p2+p4.punish_p2
        p3.punishment_received=p1.punish_p3+p2.punish_p3+p4.punish_p3
        p4.punishment_received=p1.punish_p4+p2.punish_p4+p3.punish_p4
        p1.payoff_2=p1.payoff_1-p1.payoff_1*0.10*p1.punishment_received-p1.cost_of_punishment
        p2.payoff_2=p2.payoff_1-p2.payoff_1*0.10*p2.punishment_received-p2.cost_of_punishment
        p3.payoff_2=p3.payoff_1-p3.payoff_1*0.10*p3.punishment_received-p3.cost_of_punishment
        p4.payoff_2=p4.payoff_1-p4.payoff_1*0.10*p4.punishment_received-p4.cost_of_punishment
    #cumulative payoff:
        if p.subsession.round_number == 1:
           p.cumul_payoff=p.payoff_2
        if p.subsession.round_number > 1:
            p.cumul_payoff=p.in_round(p.round_number - 1).cumul_payoff+p.payoff_2
            print('cumul_payoff',p.cumul_payoff)
class WaitPage0(WaitPage):
    after_all_players_arrive = players_names

class Contribute(Page):
    form_model = 'player'
    form_fields = ['contribution']

    def vars_for_template(player: Player):
        return dict(round=player.subsession.round_number,player_name=player.player_name, cumul_payoff=player.cumul_payoff)

class WaitPage1(WaitPage):
    after_all_players_arrive = save_contributions


class WaitPage2(WaitPage):
    after_all_players_arrive = set_playoff_1

class Punish(Page):
    form_model = 'player'
    form_fields = ['punish_p1','punish_p2','punish_p3','punish_p4', ]
    def vars_for_template(player: Player):
        return dict(round=player.subsession.round_number, total_contribution=player.group.total_contribution, individual_share=player.group.individual_share, contribution_p1=player.contribution_p1,contribution_p2=player.contribution_p2, contribution_p3=player.contribution_p3, contribution_p4=player.contribution_p4, player_name=player.player_name, payoff_1=player.payoff_1, contribution=player.contribution, show=player.show)

class Feedback(Page):
    def vars_for_template(player: Player):
        return dict(round=player.subsession.round_number, total_punishment=player.total_punishment,cost_of_punishment=player.cost_of_punishment, punishment_received=player.punishment_received, reduction=player.punishment_received*0.10*player.payoff_1, payoff_2=player.payoff_2,player_name=player.player_name )

class WaitPage3(WaitPage):
    after_all_players_arrive = set_playoff_2

class Final(Page):
    def is_displayed(player: Player):
        ## ultimo round mostra risultati
        player.final_payoff_euro=C.EXCHANGE_RATE*player.cumul_payoff
        return player.subsession.round_number == C.NUM_ROUNDS
    def vars_for_template(player: Player):
        return dict(player_name=player.player_name, cumul_payoff=player.cumul_payoff, euro=player.final_payoff_euro)



page_sequence = [WaitPage0,Contribute,WaitPage1, WaitPage2, Punish,WaitPage3, Feedback, Final]
