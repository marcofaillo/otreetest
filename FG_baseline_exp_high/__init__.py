from otree.api import *
import random as r

doc = """
Faillo and Grieco 2023 Baseline high endowment.
"""


class C(BaseConstants):
    NAME_IN_URL = 'FG_baseline_exp_high'
    EXCHANGE_RATE=0.02
    PLAYERS_PER_GROUP = 4
    NUM_ROUNDS = 20
    ENDOWMENT =20
    MPCR = 0.4
    MAX_PUNISHMENT = 10
    PUNISHMENT_SCHEDULE= {
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
    contribution = models.FloatField(min =0, max =20)
    punish_p1 = models.IntegerField(choices=[[0, '0 (0)'],[1, '1 (1)'], [2, '2 (2)'], [3, ' 3 (4)'], [4, '4 (6)'],[5, '5 (9)'], [6, '6 (12)'],[7, '7 (16)'],[8, '8 (20)'],[9, '9 (25)'],[10, '10 (30)']], label="", blank=True, initial=0)
    punish_p2 = models.IntegerField(choices=[[0, '0 (0)'],[1, '1 (1)'], [2, '2 (2)'], [3, ' 3 (4)'], [4, '4 (6)'],[5, '5 (9)'], [6, '6 (12)'],[7, '7 (16)'],[8, '8 (20)'],[9, '9 (25)'],[10, '10 (30)']], label="", blank=True,initial=0)
    punish_p3 = models.IntegerField(choices=[[0, '0 (0)'],[1, '1 (1)'], [2, '2 (2)'], [3, ' 3 (4)'], [4, '4 (6)'],[5, '5 (9)'], [6, '6 (12)'],[7, '7 (16)'],[8, '8 (20)'],[9, '9 (25)'],[10, '10 (30)']], label="", blank=True,initial=0)
    punish_p4 = models.IntegerField(choices=[[0, '0 (0)'],[1, '1 (1)'], [2, '2 (2)'], [3, ' 3 (4)'], [4, '4 (6)'],[5, '5 (9)'], [6, '6 (12)'],[7, '7 (16)'],[8, '8 (20)'],[9, '9 (25)'],[10, '10 (30)']], label="", blank=True,initial=0)
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
    final_payoff_euro=models.FloatField(initial=0)
    #control questions
    q1=models.IntegerField()
    q2=models.IntegerField()
    q3=models.IntegerField(choices=[[1, 'A. Il tuo pagamento è calcolato come: 20-8 + 0,4*(8+5+2+10) =12+0,4*25=12+10=22 '], [2, 'B.Il tuo pagamento è calcolato come: 10-8 + 0,4*(8+5+2+10) =2+0,4*25=2+10=2']])
    q4=models.IntegerField()#cost
    q5=models.IntegerField()#cost
    q6=models.IntegerField()#cost
    q7=models.IntegerField()#cost
    q8=models.IntegerField()
    q9=models.IntegerField()
    errors=models.IntegerField(initial=0) #n. of errors in control questions
    #Questionnaire
    closeness_before=models.IntegerField(min = 1, max =7)
    closeness_after=models.IntegerField(min = 1, max =7)
    female= models.IntegerField(choices=[[0,'Maschio'], [1, 'Femmina'], [2, 'Altro'],[3, 'Non rispondo']])
    age= models.IntegerField()
    major=models.StringField()
    exp=models.IntegerField()

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

class Instructions_1(Page):
    def is_displayed(player: Player):
        return player.subsession.round_number ==  1

class WaitPage_intructions(WaitPage):
    wait_for_all_groups=True
    pass

class Instructions_2(Page):
    def is_displayed(player: Player):
        return player.subsession.round_number ==  1

class Control(Page):
    wait_for_all_groups=True
    form_model = 'player'
    form_fields = ['q1', 'q2', 'q3', 'q4','q5', 'q6','q7', 'q8','q9']
    def is_displayed(player: Player):
        ## ultimo round mostra risultati
        return player.subsession.round_number == 1

    def error_message(player: Player, values):
        if values['q1'] != 0:
            player.errors += 1
            return 'La risposta alla domanda 1 è sbagliata'
        if values['q2'] != 32:
            player.errors += 1
            return 'La risposta alla domanda 2 è sbagliata'
        if values['q3'] != 1:
            player.errors += 1
            return 'La risposta alla domanda 3 è sbagliata'
        if values['q4'] != 25:
            player.errors += 1
            return 'La risposta alla domanda 4 è sbagliata'
        if values['q5'] != 9:
            player.errors += 1
            return 'La risposta alla domanda 5 è sbagliata'
        if values['q6'] != 0:
            player.errors += 1
            return 'La risposta alla domanda 6 è sbagliata'
        if values['q7'] != 34:
            player.errors += 1
            return 'La risposta alla domanda 7 è sbagliata'
        if values['q8'] != 0:
            player.errors += 1
            return 'La risposta alla domanda 8 è sbagliata'
        if values['q9'] != 40:
            player.errors += 1
            return 'La risposta alla domanda 9 è sbagliata'


class WaitPage0(WaitPage):
    after_all_players_arrive = players_names

class Contribute(Page):
    form_model = 'player'
    form_fields = ['contribution']
    def error_message(player: Player, values):
        if values['contribution'] > C.ENDOWMENT:
                return 'La contribuzione massima è 20 UMS'
    def vars_for_template(player: Player):
        return dict(tot_round=C.NUM_ROUNDS,round=player.subsession.round_number,player_name=player.player_name, cumul_payoff=player.cumul_payoff)

class Rematch(Page):
    def is_displayed(player: Player):
        return player.subsession.round_number == C.NUM_ROUNDS/2+1


class WaitPage1(WaitPage):
    after_all_players_arrive = save_contributions


class WaitPage2(WaitPage):
    after_all_players_arrive = set_playoff_1

class Punish(Page):
    form_model = 'player'
    form_fields = ['punish_p1','punish_p2','punish_p3','punish_p4', ]
    def vars_for_template(player: Player):
        return dict(tot_round=C.NUM_ROUNDS,round=player.subsession.round_number,total_contribution=player.group.total_contribution, individual_share=player.group.individual_share, contribution_p1=player.contribution_p1,contribution_p2=player.contribution_p2, contribution_p3=player.contribution_p3, contribution_p4=player.contribution_p4, player_name=player.player_name, payoff_1=player.payoff_1, contribution=player.contribution)

class Feedback(Page):
    def vars_for_template(player: Player):
        return dict(tot_round=C.NUM_ROUNDS,round=player.subsession.round_number, total_punishment=player.total_punishment,cost_of_punishment=player.cost_of_punishment, punishment_received=player.punishment_received, reduction=player.punishment_received*0.10*player.payoff_1, payoff_2=player.payoff_2,player_name=player.player_name )

class WaitPage3(WaitPage):
    after_all_players_arrive = set_playoff_2

class Final(Page):
    def is_displayed(player: Player):
        ## ultimo round mostra risultati
        player.final_payoff_euro=C.EXCHANGE_RATE*player.cumul_payoff
        return player.subsession.round_number == C.NUM_ROUNDS
    def vars_for_template(player: Player):
        return dict(player_name=player.player_name, cumul_payoff=player.cumul_payoff, euro=player.final_payoff_euro)

class Questionnaire(Page):
    form_model = 'player'
    form_fields = ['closeness_before','closeness_after','female','age','major','exp', ]

    def is_displayed(player: Player):
        return player.subsession.round_number ==  C.NUM_ROUNDS

page_sequence = [Instructions_1,WaitPage_intructions,Instructions_2,WaitPage0,Control, WaitPage_intructions, Rematch, Contribute,WaitPage1, WaitPage2, Punish,WaitPage3, Feedback,Final, Questionnaire,]
