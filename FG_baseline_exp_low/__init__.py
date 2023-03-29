from otree.api import *
import random as r

doc = """
Faillo and Grieco 2023 Baseline low endowment.
"""


class C(BaseConstants):
    NAME_IN_URL = 'FG_baseline_exp_low'
    EXCHANGE_RATE=0.02
    PLAYERS_PER_GROUP = 4
    NUM_ROUNDS = 3
    ENDOWMENT =10
    MPCR = 0.4
    MAX_PUNISHMENT = 10
    PUNISHMENT_SCHEDULE= {
        0: 0,
        1: 0.5,
        2: 1,
        3: 2,
        4: 3,
        5: 4.5,
        6: 6,
        7: 8,
        8: 10,
        9: 12.5,
        10: 15,
        }


class Subsession(BaseSubsession):
        pass


class Group(BaseGroup):
    total_contribution = models.FloatField()
    average_contribution=models.FloatField()
    individual_share = models.FloatField()



class Player(BasePlayer):
    contribution = models.FloatField()
    punish_p1 = models.IntegerField(choices=[[0, '0 (0)'],[1, '1 (0.5)'], [2, '2 (1)'], [3, ' 3 (2)'], [4, '4 (3)'],[5, '5 (4.5)'], [6, '6 (6)'],[7, '7 (8)'],[8, '8 (10)'],[9, '9 (12.5)'],[10, '10 (15)']], label="", blank=True, initial=0)
    punish_p2 = models.IntegerField(choices=[[0, '0 (0)'],[1, '1 (0.5)'], [2, '2 (1)'], [3, ' 3 (2)'], [4, '4 (3)'],[5, '5 (4.5)'], [6, '6 (6)'],[7, '7 (8)'],[8, '8 (10)'],[9, '9 (12.5)'],[10, '10 (15)']], label="", blank=True, initial=0)
    punish_p3 = models.IntegerField(choices=[[0, '0 (0)'],[1, '1 (0.5)'], [2, '2 (1)'], [3, ' 3 (2)'], [4, '4 (3)'],[5, '5 (4.5)'], [6, '6 (6)'],[7, '7 (8)'],[8, '8 (10)'],[9, '9 (12.5)'],[10, '10 (15)']], label="", blank=True, initial=0)
    punish_p4 = models.IntegerField(choices=[[0, '0 (0)'],[1, '1 (0.5)'], [2, '2 (1)'], [3, ' 3 (2)'], [4, '4 (3)'],[5, '5 (4.5)'], [6, '6 (6)'],[7, '7 (8)'],[8, '8 (10)'],[9, '9 (12.5)'],[10, '10 (15)']], label="", blank=True, initial=0)
    total_punishment= models.IntegerField()
    cost_of_punishment = models.FloatField()
    punishment_received = models.IntegerField()
    contribution_p1=models.FloatField()
    contribution_p2=models.FloatField()
    contribution_p3=models.FloatField()
    contribution_p4=models.FloatField()
    payoff_1=models.FloatField(initial=0)
    payoff_2=models.FloatField(initial=0)
    cumul_payoff=models.FloatField(initial=0)
    player_name=models.IntegerField()
    final_payoff_euro=models.FloatField(initial=0)


def players_names(group: Group):
    p1=group.get_player_by_id(1)
    p2=group.get_player_by_id(2)
    p3=group.get_player_by_id(3)
    p4=group.get_player_by_id(4)

    for p in group.get_players():
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
        p2.total_punishment=p2.punish_p1+p2.punish_p3+p2.punish_p4
        p3.total_punishment=p3.punish_p1+p3.punish_p2+p3.punish_p4
        p4.total_punishment=p4.punish_p1+p4.punish_p2+p4.punish_p3
        p1.cost_of_punishment=C.PUNISHMENT_SCHEDULE[p1.punish_p2] + C.PUNISHMENT_SCHEDULE[p1.punish_p3] + C.PUNISHMENT_SCHEDULE[p1.punish_p4]
        p2.cost_of_punishment=C.PUNISHMENT_SCHEDULE[p2.punish_p1] + C.PUNISHMENT_SCHEDULE[p2.punish_p3] + C.PUNISHMENT_SCHEDULE[p2.punish_p4]
        p3.cost_of_punishment=C.PUNISHMENT_SCHEDULE[p3.punish_p1] + C.PUNISHMENT_SCHEDULE[p3.punish_p2] + C.PUNISHMENT_SCHEDULE[p3.punish_p4]
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
    def error_message(player: Player, values):
        if values['contribution'] > C.ENDOWMENT:
                return 'La contribuzione massima è 10 UMS'


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
        return dict(round=player.subsession.round_number,total_contribution=player.group.total_contribution, individual_share=player.group.individual_share, contribution_p1=player.contribution_p1,contribution_p2=player.contribution_p2, contribution_p3=player.contribution_p3, contribution_p4=player.contribution_p4, player_name=player.player_name, payoff_1=player.payoff_1, contribution=player.contribution)

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
