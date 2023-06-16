from otree.api import *
import random as r

doc = """
Faillo and Grieco 2023 Baseline high endowment.
"""


class C(BaseConstants):
    NAME_IN_URL = 'FG_mix_no_norm'
    EXCHANGE_RATE=0.02
    PLAYERS_PER_GROUP = 4
    NUM_ROUNDS = 20
    # ENDOWMENT =20
    MPCR = 0.4
    # MAX_PUNISHMENT = 10
    ROUND_CHANGE=(NUM_ROUNDS/2)+1
    PUNISHMENT_SCHEDULE_H= {
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

    # MAX_PUNISHMENT = 10
    PUNISHMENT_SCHEDULE_L= {
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
    high=models.IntegerField(initial =99 )



class Player(BasePlayer):
    #contribution high
    contribution = models.IntegerField(initial=0)


    #punishment high
    punish_h_p1 = models.IntegerField(choices=[[0, '0 (0)'],[1, '1 (1)'], [2, '2 (2)'], [3, ' 3 (4)'], [4, '4 (6)'],[5, '5 (9)'], [6, '6 (12)'],[7, '7 (16)'],[8, '8 (20)'],[9, '9 (25)'],[10, '10 (30)']], label="", blank=True, initial=0)
    punish_h_p2 = models.IntegerField(choices=[[0, '0 (0)'],[1, '1 (1)'], [2, '2 (2)'], [3, ' 3 (4)'], [4, '4 (6)'],[5, '5 (9)'], [6, '6 (12)'],[7, '7 (16)'],[8, '8 (20)'],[9, '9 (25)'],[10, '10 (30)']], label="", blank=True,initial=0)
    punish_h_p3 = models.IntegerField(choices=[[0, '0 (0)'],[1, '1 (1)'], [2, '2 (2)'], [3, ' 3 (4)'], [4, '4 (6)'],[5, '5 (9)'], [6, '6 (12)'],[7, '7 (16)'],[8, '8 (20)'],[9, '9 (25)'],[10, '10 (30)']], label="", blank=True,initial=0)
    punish_h_p4 = models.IntegerField(choices=[[0, '0 (0)'],[1, '1 (1)'], [2, '2 (2)'], [3, ' 3 (4)'], [4, '4 (6)'],[5, '5 (9)'], [6, '6 (12)'],[7, '7 (16)'],[8, '8 (20)'],[9, '9 (25)'],[10, '10 (30)']], label="", blank=True,initial=0)
    #punishment low
    punish_l_p1 = models.IntegerField(choices=[[0, '0 (0)'],[1, '1 (0.5)'], [2, '2 (1)'], [3, ' 3 (2)'], [4, '4 (3)'],[5, '5 (4.5)'], [6, '6 (6)'],[7, '7 (8)'],[8, '8 (10)'],[9, '9 (12.5)'],[10, '10 (15)']], label="", blank=True, initial=0)
    punish_l_p2 = models.IntegerField(choices=[[0, '0 (0)'],[1, '1 (0.5)'], [2, '2 (1)'], [3, ' 3 (2)'], [4, '4 (3)'],[5, '5 (4.5)'], [6, '6 (6)'],[7, '7 (8)'],[8, '8 (10)'],[9, '9 (12.5)'],[10, '10 (15)']], label="", blank=True,initial=0)
    punish_l_p3 = models.IntegerField(choices=[[0, '0 (0)'],[1, '1 (0.5)'], [2, '2 (1)'], [3, ' 3 (2)'], [4, '4 (3)'],[5, '5 (4.5)'], [6, '6 (6)'],[7, '7 (8)'],[8, '8 (10)'],[9, '9 (12.5)'],[10, '10 (15)']], label="", blank=True,initial=0)
    punish_l_p4 = models.IntegerField(choices=[[0, '0 (0)'],[1, '1 (0.5)'], [2, '2 (1)'], [3, ' 3 (2)'], [4, '4 (3)'],[5, '5 (4.5)'], [6, '6 (6)'],[7, '7 (8)'],[8, '8 (10)'],[9, '9 (12.5)'],[10, '10 (15)']], label="", blank=True,initial=0)


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
    #control questions
    q1=models.IntegerField()
    q2=models.IntegerField()
    q3=models.IntegerField(choices=[[1, 'A. Il tuo pagamento è calcolato come: 20-8 + 0,4*(8+5+2+10) =12+0,4*25=12+10=22 '], [2, 'B.Il tuo pagamento è calcolato come: 10-8 + 0,4*(8+5+2+10) =2+0,4*25=2+10=2']])
    q4=models.FloatField()#cost
    q5=models.FloatField()#cost
    q6=models.FloatField()#cost
    q7=models.FloatField()#cost
    q8=models.FloatField()
    q9=models.FloatField()
    q1_l=models.IntegerField()
    q2_l=models.IntegerField()
    q3_l=models.IntegerField(choices=[[1, 'A. Il tuo pagamento è calcolato come: 20-8 + 0,4*(8+5+2+10) =12+0,4*25=12+10=22 '], [2, 'B.Il tuo pagamento è calcolato come: 10-8 + 0,4*(8+5+2+10) =2+0,4*25=2+10=2']])
    q4_l=models.FloatField()#cost
    q5_l=models.FloatField()#cost
    q6_l=models.FloatField()#cost
    q7_l=models.FloatField()#cost
    q8_l=models.FloatField()
    q9_L=models.FloatField()

    errors=models.IntegerField(initial=0) #n. of errors in control questions
    #Questionnaire
    closeness_before=models.IntegerField(min = 1, max =7)
    closeness_after=models.IntegerField(min = 1, max =7)
    female= models.IntegerField(choices=[[0,'Maschio'], [1, 'Femmina'], [2, 'Altro'],[3, 'Non rispondo']])
    age= models.IntegerField()
    major=models.StringField()
    exp=models.IntegerField()
    mygroup=models.IntegerField()
    immigrant_high=models.IntegerField(initial=0)
    immigrant_low=models.IntegerField(initial = 0)

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





# PAGES

def set_playoff_1(group: Group):
    for p in group.get_players():

        if  p.group.high==1: #high
            p.payoff_1=20-p.contribution+group.individual_share
        else:
            p.payoff_1=10-p.contribution+group.individual_share


# PAGES
def set_playoff_2(group: Group):
    p1=group.get_player_by_id(1)
    p2=group.get_player_by_id(2)
    p3=group.get_player_by_id(3)
    p4=group.get_player_by_id(4)
    for p in group.get_players():
            if p.group.high==0: #low

                p1.total_punishment=p1.punish_l_p2+p1.punish_l_p3+p1.punish_l_p4
                p2.total_punishment=p2.punish_l_p1+p2.punish_l_p3+p2.punish_l_p4
                p3.total_punishment=p3.punish_l_p1+p3.punish_l_p2+p3.punish_l_p4
                p4.total_punishment=p4.punish_l_p1+p4.punish_l_p2+p4.punish_l_p3
                p1.cost_of_punishment=C.PUNISHMENT_SCHEDULE_L[p1.punish_l_p2] + C.PUNISHMENT_SCHEDULE_L[p1.punish_l_p3] + C.PUNISHMENT_SCHEDULE_L[p1.punish_l_p4]
                p2.cost_of_punishment=C.PUNISHMENT_SCHEDULE_L[p2.punish_l_p1] + C.PUNISHMENT_SCHEDULE_L[p2.punish_l_p3] + C.PUNISHMENT_SCHEDULE_L[p2.punish_l_p4]
                p3.cost_of_punishment=C.PUNISHMENT_SCHEDULE_L[p3.punish_l_p1] + C.PUNISHMENT_SCHEDULE_L[p3.punish_l_p2] + C.PUNISHMENT_SCHEDULE_L[p3.punish_l_p4]
                p4.cost_of_punishment=C.PUNISHMENT_SCHEDULE_L[p4.punish_l_p1] + C.PUNISHMENT_SCHEDULE_L[p4.punish_l_p2] + C.PUNISHMENT_SCHEDULE_L[p4.punish_l_p3]
                p1.punishment_received=p2.punish_l_p1+p3.punish_l_p1+p4.punish_l_p1
                p2.punishment_received=p1.punish_l_p2+p3.punish_l_p2+p4.punish_l_p2
                p3.punishment_received=p1.punish_l_p3+p2.punish_l_p3+p4.punish_l_p3
                p4.punishment_received=p1.punish_l_p4+p2.punish_l_p4+p3.punish_l_p4
                p1.payoff_2=round(p1.payoff_1-p1.payoff_1*0.10*p1.punishment_received-p1.cost_of_punishment,1)
                p2.payoff_2=round(p2.payoff_1-p2.payoff_1*0.10*p2.punishment_received-p2.cost_of_punishment,1)
                p3.payoff_2=round(p3.payoff_1-p3.payoff_1*0.10*p3.punishment_received-p3.cost_of_punishment,1)
                p4.payoff_2=round(p4.payoff_1-p4.payoff_1*0.10*p4.punishment_received-p4.cost_of_punishment,1)
            #cumulative payoff:
                if p.subsession.round_number == 1:
                   p.cumul_payoff=p.payoff_2
                if p.subsession.round_number > 1:
                    p.cumul_payoff=p.in_round(p.round_number - 1).cumul_payoff+p.payoff_2
            else: #high
                p1.total_punishment=p1.punish_h_p2+p1.punish_h_p3+p1.punish_h_p4
                p2.total_punishment=p2.punish_h_p1+p2.punish_h_p3+p2.punish_h_p4
                p3.total_punishment=p3.punish_h_p1+p3.punish_h_p2+p3.punish_h_p4
                p4.total_punishment=p4.punish_h_p1+p4.punish_h_p2+p4.punish_h_p3
                p1.cost_of_punishment=C.PUNISHMENT_SCHEDULE_H[p1.punish_h_p2] + C.PUNISHMENT_SCHEDULE_H[p1.punish_h_p3] + C.PUNISHMENT_SCHEDULE_H[p1.punish_h_p4]
                p2.cost_of_punishment=C.PUNISHMENT_SCHEDULE_H[p2.punish_h_p1] + C.PUNISHMENT_SCHEDULE_H[p2.punish_h_p3] + C.PUNISHMENT_SCHEDULE_H[p2.punish_h_p4]
                p3.cost_of_punishment=C.PUNISHMENT_SCHEDULE_H[p3.punish_h_p1] + C.PUNISHMENT_SCHEDULE_H[p3.punish_h_p2] + C.PUNISHMENT_SCHEDULE_H[p3.punish_h_p4]
                p4.cost_of_punishment=C.PUNISHMENT_SCHEDULE_H[p4.punish_h_p1] + C.PUNISHMENT_SCHEDULE_H[p4.punish_h_p2] + C.PUNISHMENT_SCHEDULE_H[p4.punish_h_p3]
                p1.punishment_received=p2.punish_h_p1+p3.punish_h_p1+p4.punish_h_p1
                p2.punishment_received=p1.punish_h_p2+p3.punish_h_p2+p4.punish_h_p2
                p3.punishment_received=p1.punish_h_p3+p2.punish_h_p3+p4.punish_h_p3
                p4.punishment_received=p1.punish_h_p4+p2.punish_h_p4+p3.punish_h_p4
                p1.payoff_2=round(p1.payoff_1-p1.payoff_1*0.10*p1.punishment_received-p1.cost_of_punishment,1)
                p2.payoff_2=round(p2.payoff_1-p2.payoff_1*0.10*p2.punishment_received-p2.cost_of_punishment,1)
                p3.payoff_2=round(p3.payoff_1-p3.payoff_1*0.10*p3.punishment_received-p3.cost_of_punishment,1)
                p4.payoff_2=round(p4.payoff_1-p4.payoff_1*0.10*p4.punishment_received-p4.cost_of_punishment,1)
            #cumulative payoff:
                if p.subsession.round_number == 1:
                   p.cumul_payoff=p.payoff_2
                if p.subsession.round_number > 1:
                    p.cumul_payoff=p.in_round(p.round_number - 1).cumul_payoff+p.payoff_2



class Instructions_1(Page):
    def is_displayed(player: Player):
        def after_all_players_arrive(subsession: Subsession):
            for p in subsession.get_players():
                if p.subsession.round_number < C.ROUND_CHANGE:
                    initial_mat=[[1,2,3,4],[5,6,7,8]]
                    subsession.set_group_matrix(initial_mat)
        return player.subsession.round_number ==  1

class WaitPage_intructions(WaitPage):
    wait_for_all_groups = True
    def after_all_players_arrive(subsession: Subsession):
        for g in subsession.get_groups():
            if g.id_in_subsession % 2 == 0:
               g.high=1
            else:
               g.high=0

class WaitPage_intructions2(WaitPage):
    wait_for_all_groups = True
    def after_all_players_arrive(subsession: Subsession):
        for p in subsession.get_players():
                if p.id_in_group == 1 and p.group.high==1: #immigrant high
                   p.immigrant_high=1
                   print(p.immigrant_high)
                if p.id_in_group == 1 and p.group.high==0: #immigrant low
                   p.immigrant_low=1
                   print(p.immigrant_low)
#instructions high
class Instructions_2_h(Page):
    def is_displayed(player: Player):
        return player.subsession.round_number ==  1 and player.group.high==1

#instructions low
class Instructions_2_l(Page):
    def is_displayed(player: Player):
        return player.subsession.round_number ==  1 and  player.group.high==0

#control high
class Control_h(Page):
    form_model = 'player'
    form_fields = ['q1', 'q2', 'q3', 'q4','q5', 'q6','q7', 'q8','q9']
    def is_displayed(player: Player):
        ## ultimo round mostra risultati
        return player.subsession.round_number == 1 and player.group.high==1

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

class Control_l(Page):
    form_model = 'player'
    form_fields = ['q1', 'q2', 'q3', 'q4','q5', 'q6','q7', 'q8','q9']
    def is_displayed(player: Player):
        ## ultimo round mostra risultati
        return player.subsession.round_number ==  1 and player.group.high==0

    def error_message(player: Player, values):
        if values['q1'] != 0:
            player.errors += 1
            return 'La risposta alla domanda 1 è sbagliata'
        if values['q2'] != 16:
            player.errors += 1
            return 'La risposta alla domanda 2 è sbagliata'
        if values['q3'] != 2:
            player.errors += 1
            return 'La risposta alla domanda 3 è sbagliata'
        if values['q4'] != 12.5:
            player.errors += 1
            return 'La risposta alla domanda 4 è sbagliata'
        if values['q5'] != 4.5:
            player.errors += 1
            return 'La risposta alla domanda 5 è sbagliata'
        if values['q6'] != 0:
            player.errors += 1
            return 'La risposta alla domanda 6 è sbagliata'
        if values['q7'] != 17:
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

    # def after_all_players_arrive(subsession: Subsession):
    #     if player.subsession.round_number <= C.ROUND_CHANGE:
    #       for p in subsession.get_players():
    #             new_mat=[[5,2,3,4],[1,6,7,8]]
    #             subsession.set_group_matrix(new_mat)

class Contribute_h(Page):
    form_model = 'player'
    form_fields = ['contribution']
    def is_displayed(player: Player):
        return player.group.high==1
    def error_message(player: Player, values):
        if values['contribution'] > 20:
                return 'La contribuzione massima è 20 UMS'
    def vars_for_template(player: Player):
        return dict(tot_round=C.NUM_ROUNDS,round=player.subsession.round_number,player_name=player.player_name, cumul_payoff=player.cumul_payoff)

class Contribute_l(Page):
    form_model = 'player'
    form_fields = ['contribution']
    def is_displayed(player: Player):
        return player.group.high==0

    def error_message(player: Player, values):
        if values['contribution'] > 10:
                return 'La contribuzione massima è 10 UMS'
    def vars_for_template(player: Player):
        return dict(tot_round=C.NUM_ROUNDS,round=player.subsession.round_number,player_name=player.player_name, cumul_payoff=player.cumul_payoff)


class Rematch(Page):
    def is_displayed(player: Player):
        return player.subsession.round_number == C.NUM_ROUNDS/2+1

    def vars_for_template(player: Player):
        return dict(high=player.group.high, immigrant_high=player.immigrant_high, immigrant_low=player.immigrant_low)


class WaitPage_rematch(WaitPage):
    wait_for_all_groups = True
    def after_all_players_arrive(subsession: Subsession):
        for p in subsession.get_players():
            if p.subsession.round_number >= C.ROUND_CHANGE:
                last_mat=[[5,2,3,4],[1,6,7,8]]
                subsession.set_group_matrix(last_mat)
        for g in subsession.get_groups():
            if g.id_in_subsession % 2 == 0:
               g.high=1
            else:
               g.high=0


class WaitPage1(WaitPage):
    after_all_players_arrive = save_contributions


class WaitPage2(WaitPage):
    after_all_players_arrive = set_playoff_1

class Punish_h(Page):
    form_model = 'player'
    form_fields = ['punish_h_p1','punish_h_p2','punish_h_p3','punish_h_p4', ]
    def is_displayed(player: Player):
        return player.group.high==1
    def vars_for_template(player: Player):
        return dict(id_player=player.id_in_group,round_change=C.ROUND_CHANGE,tot_round=C.NUM_ROUNDS,round=player.subsession.round_number,total_contribution=player.group.total_contribution, individual_share=player.group.individual_share, contribution_p1=player.contribution_p1,contribution_p2=player.contribution_p2, contribution_p3=player.contribution_p3, contribution_p4=player.contribution_p4, player_name=player.player_name, payoff_1=player.payoff_1, contribution=player.contribution)


class Punish_l(Page):
    form_model = 'player'
    form_fields = ['punish_l_p1','punish_l_p2','punish_l_p3','punish_l_p4', ]
    def is_displayed(player: Player):
        return player.group.high==0
    def vars_for_template(player: Player):
        return dict(id_player=player.id_in_group,round_change=C.ROUND_CHANGE,tot_round=C.NUM_ROUNDS,round=player.subsession.round_number,total_contribution=player.group.total_contribution, individual_share=player.group.individual_share, contribution_p1=player.contribution_p1,contribution_p2=player.contribution_p2, contribution_p3=player.contribution_p3, contribution_p4=player.contribution_p4, player_name=player.player_name, payoff_1=player.payoff_1, contribution=player.contribution)

class WaitPageControl(WaitPage):
      wait_for_all_groups = True

class Feedback(Page):

    def vars_for_template(player: Player):
        return dict(high=player.group.high,tot_round=C.NUM_ROUNDS,round=player.subsession.round_number, total_punishment=player.total_punishment,cost_of_punishment=player.cost_of_punishment, punishment_received=player.punishment_received, reduction=player.punishment_received*0.10*player.payoff_1, payoff_2=player.payoff_2,player_name=player.player_name )

class WaitPage3(WaitPage):
    after_all_players_arrive = set_playoff_2

class WaitPageInit(WaitPage):
    pass

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

page_sequence = [Instructions_1,WaitPage_intructions,WaitPage_intructions2,WaitPageInit,Instructions_2_h,Instructions_2_l,WaitPageControl,Control_h, Control_l,WaitPage0, Rematch, WaitPage_rematch, Contribute_h,Contribute_l,WaitPage1, WaitPage2, Punish_h,Punish_l,WaitPage3, Feedback,Final, Questionnaire,]
