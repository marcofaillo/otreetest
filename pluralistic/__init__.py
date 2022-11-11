from otree.api import *
import random as r
doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'pluralistic'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1



class Subsession(BaseSubsession):
    mode=models.IntegerField()
    n_ten=models.IntegerField()
    n_five=models.IntegerField()
    draw1=models.IntegerField()
    draw2=models.IntegerField()





class Group(BaseGroup):
    p1 =models.IntegerField(initial=0)
    p2 =models.IntegerField(initial=0)
    p3 =models.IntegerField(initial=0)

class Player(BasePlayer):
    choice= models.IntegerField(choices=[[170, 'Option A. You get 170 CZK and the charity will receive 100 CZK with a probability of 10% and 0 with a probability of 90% '], [100, 'Option B. You get 100 CZK and the carity will receive 80 CZK']])
    pay_1=models.IntegerField(initial=0) #player's payoff from first choice
    pay_2=models.IntegerField(initial=0) #player's payoff from second choice
    donation_1=models.FloatField(initial=0) #money given to the charity
    donation_2=models.FloatField(initial=0) #money given to the charity
    choice2= models.IntegerField(choices=[[170, 'Option A. You get 170 CZK and the charity will receive 100 CZK with a probability of 10% and 0 with a probability of 90% '], [100, 'Option B. You get 100 CZK and the carity will receive 80 CZK']])
    pers_belief=models.IntegerField(choices=[[170, 'Option A. You get 170 CZK and the charity will receive 100 CZK with a probability of 10% and 0 with a probability of 90% '], [100, 'Option B. You get 100 CZK and the carity will receive 80 CZK']])
    norm_belief=models.IntegerField(choices=[[170, 'Option A. You get 170 CZK and the charity will receive 100 CZK with a probability of 10% and 0 with a probability of 90% '], [100, 'Option B. You get 100 CZK and the carity will receive 80 CZK']]) #personal Beliefs
    emp_belief=models.IntegerField(choices=[[270, 'One chose Option A and the other chose Option B'], [340, 'They both chose Option A'], [200, 'They both chose Option B']]) #empirical expectations
    norm_belief=models.IntegerField(choices=[[270, 'One chose answered Option A and the other answered Option B'], [340, 'They both answered Option A'], [200, 'They both answered Option B']]) #normative believes
    pay_belief_q1 =models.FloatField(initial=0) #payment for question 1
    pay_belief_q2 =models.FloatField(initial=0) #payment for question 2
    pay_2_final=models.FloatField(initial=0) #final payoff after punishment
    agree =models.FloatField(initial=-1)  # = 1 if they chose the same choice2 and 0 otherwise
    final_payoff=models.FloatField(initial=0) #final payoff
    total_donation=models.FloatField(initial=0) #final total donatio
    pun_1=models.IntegerField(choices=[[0, 'Assign 0 points '], [1,'Assign 1 point']]) #first member punished  (p2 for p1, p1 for p2, p2 for p3)
    pun_2=models.IntegerField(choices=[[0, 'Assign 0 points '], [1,'Assign 1 point']])#first member punished  (p2 for p1, p1 for p2, p2 for p3)
    cost_pun=models.IntegerField(initial=0) #cost paid by the punisher
    red_pun=models.IntegerField(initial=0) #reduction for punished players
    change=models.IntegerField(initial=0)  #=1 if choice2 is changed because of punishment
    choice2_old=models.IntegerField(initial=0) #old choice2 in case of change
    final_agree=models.IntegerField(initial=0)#final agreement
    burn =models.IntegerField(initial=0) # =1 if the first donation is reduced
    burn_2 =models.IntegerField(initial=0) # =1 if the second donation is reduced

 #second  member punished (p3 for p1, p1 for p2, p2 for p3)
#functions

def creating_session(subsession: Subsession):
    session = subsession.session
    for p in subsession.get_players():
                p.participant.vars['goods']=[]# id soggetti che scelgono 10
                p.participant.vars['bads']=[]## id soggetti che scelgono 5
                p.participant.vars['group_mat']=[]# matrice dei gruppi
                p.participant.vars['choices']=[]  #other's choices in choice 2

                print("hello")


def store_choice(group: Group): #writes the choices of the members of the group as [p1.choice, p2.choice, p3.choice]
        p1=group.get_player_by_id(1)
        p2=group.get_player_by_id(2)
        p3=group.get_player_by_id(3)
        for p in group.get_players():
            p.participant.vars['choices'].append(p1.choice2)
            p.participant.vars['choices'].append(p2.choice2)
            p.participant.vars['choices'].append(p3.choice2)
        print(p.participant.vars['choices'])


def check_beliefs (group: Group): #check beliefs and compute payments
        p1=group.get_player_by_id(1)
        p2=group.get_player_by_id(2)
        p3=group.get_player_by_id(3)
        for p in group.get_players():
            #check agreement on choice2
            if (p1.choice2 == p2.choice2) and (p1.choice2 == p3.choice2):
               p.agree=1
            else:
               p.agree=0
            print("agree", p.agree)

            #check empirical beliefs
            if p1.emp_belief == p2.choice2 + p3.choice2:
                  p1.pay_belief_q1 = 20

            if p2.emp_belief == p1.choice2 + p3.choice2:
                  p2.pay_belief_q1 = 20

            if p3.emp_belief == p1.choice2 + p2.choice2:
                  p3.pay_belief_q1 = 20


            #check normative beliefs
            if p1.norm_belief == p2.pers_belief + p3.pers_belief:
                  p1.pay_belief_q2 = 20

            if p2.norm_belief == p1.pers_belief + p3.pers_belief:
                  p2.pay_belief_q2 = 20

            if p3.norm_belief == p1.choice2 + p2.choice2:
                  p3.pay_belief_q2 = 20


            print("pay empirical belief",p1.pay_belief_q1, p2.pay_belief_q1,p3.pay_belief_q1)
            print("pay normative belief",p1.pay_belief_q2, p2.pay_belief_q2,p3.pay_belief_q2)

def compute_payoff (group: Group): #final payoff agreement
        p1=group.get_player_by_id(1)
        p2=group.get_player_by_id(2)
        p3=group.get_player_by_id(3)
        for p in group.get_players():
            p.choice2_old=p.choice2
            if p.agree==1: #agreement no punishment
                p.cost_pun =0;
                p.red_pun =0;
            if p.agree == 0: #no agreement punishment
               p.cost_pun = 10*(p.pun_1+p.pun_2) #cost if he punishes
               if p.id_in_group == 1: #p1
                  p.red_pun = 50*(p2.pun_1+p3.pun_1)
               if p.id_in_group == 2: #p2
                  p.red_pun = 50*(p1.pun_1+p3.pun_2)
               if p.id_in_group == 3:#p3
                  p.red_pun = 50*(p1.pun_2+p2.pun_2)
               if p.red_pun == 100: #change choice2
                  p.change=1
                  if p.choice2 == 170:
                     p.choice2 = 100
                  else:
                     p.choice2 = 170

            p.pay_2=p.choice2
            if p.choice2 == 100:
               p.donation_2 = 80
            else:
                if p.subsession.draw2 ==1:
                    p.donation_2 = 100
                else:
                    p.donation_2 = 0
                    p.burn_2=1
        for p in group.get_players():
            if (p1.choice2 == p2.choice2) and (p1.choice2 == p3.choice2): #agree
                print("ID",p.id_in_group,"p1",p1.choice2,"p2",p2.choice2, "p3",p3.choice2, )
                p.final_agree=1
                p.final_payoff = p.pay_1+p.pay_2+p.pay_belief_q1+p.pay_belief_q2-p.cost_pun-p.red_pun
                p.total_donation = p.donation_1 + p.donation_2
            else:
                p.final_agree=0
                p.final_payoff =p.pay_1+p.pay_belief_q1+p.pay_belief_q2
                p.total_donation =p.donation_1

# PAGES
class Choice(Page):
    form_model = 'player'
    form_fields = ['choice']
    def vars_for_template(player: Player):
        print("ruolo", player.id_in_group )
        return dict(label=player.id_in_subsession)

#creazione vettore buoni e cattivi
    def before_next_page (player,timeout_happened):
        for p in player.subsession.get_players():
            if player.choice==170:
                p.participant.vars['goods'].append(player.id_in_subsession)#
            else:
                p.participant.vars['bads'].append(player.id_in_subsession)

        print(p.participant.vars['goods'],p.participant.vars['bads'])
        total=player.participant.vars['goods']+player.participant.vars['bads']
        print("total",total)
        group_mat=[]
        lenght=int(len(total)/3)
#creazione matrice dei gruppi da tre giocatori
        for i in range(0, len(total), 3):
            group_mat.append(total[i:i + 3])
        print("group_mat", group_mat)
        choices=[]
        for p in player.subsession.get_players():
            p.participant.vars['group_mat']=group_mat


class WaitPage1(WaitPage):
    wait_for_all_groups = True
    #assegnazione ai gruppi
    def after_all_players_arrive(subsession: Subsession):
        subsession.draw1=r.randint(1,10)
        subsession.draw2=r.randint(1,10)
        print ("random", subsession.draw1,subsession.draw2 )

        for p in subsession.get_players():
            subsession.set_group_matrix(p.participant.vars['group_mat'])
            print("gruppi",subsession.get_group_matrix())

            #calcolo payoff
            p.pay_1=p.choice
            if p.choice == 100:
                p.donation_1 = 80

            else:
                if p.subsession.draw1 ==1:
                    p.donation_1 = 100
                else:
                    p.donation_1 = 0
                    p.burn = 1
            print("payoff", p.pay_1, "donation", p.donation_1)
        subsession.n_ten=[p.choice for p in subsession.get_players()].count(170)
        subsession.n_five=[p.choice for p in subsession.get_players()].count(100)
        print(subsession.n_ten,subsession.n_five)
        # calcolo della moda
        if subsession.n_ten>subsession.n_five:
            subsession.mode=170
        elif subsession.n_ten<subsession.n_five:
            subsession.mode=100
        else:
            subsession.mode=-1
        print("moda", subsession.mode)
    body_text = "Please wait for other participants"



class Results(Page):

    def vars_for_template(player: Player):
        return dict(moda=player.subsession.mode, group=player.group.id_in_subsession, label=player.id_in_group, payoff=player.pay_1, donation=player.donation_1)


class Choice2(Page):
    form_model = 'player'
    form_fields = ['choice2']
    def vars_for_template(player: Player):
        print("ruolo", player.id_in_group )
        return dict(group=player.group.id_in_subsession, label=player.id_in_group)




class Beliefs(Page):
    form_model = 'player'
    form_fields = ['pers_belief','emp_belief','norm_belief']
    def vars_for_template(player: Player):

        return dict(group=player.group.id_in_subsession, label=player.id_in_group, choice2=player.choice2)


class WaitPage2(WaitPage):
	wait_for_all_groups = False
	after_all_players_arrive = store_choice

class WaitPage3(WaitPage):
	wait_for_all_groups = False
	after_all_players_arrive = check_beliefs

class WaitPage4(WaitPage):
	wait_for_all_groups = False
	after_all_players_arrive = compute_payoff

class Agreement(Page):
    wait_for_all_groups = False
    def is_displayed(player):
        return player.agree== 1
    def vars_for_template(player: Player):
        return dict(group=player.group.id_in_subsession, burn=player.burn,burn_2=player.burn_2,label=player.id_in_group,choice2=player.choice2, choice=player.choice, pay_1=player.pay_1,  pay_2=player.pay_2,donation_1=player.donation_1,donation_2=player.donation_2, pay_belief_q1=player.pay_belief_q1, pay_belief_q2=player.pay_belief_q2, finalpay=player.final_payoff, total_donation=player.total_donation)

class Punishment (Page):
    form_model = 'player'
    form_fields = ['pun_1','pun_2']
    def error_message(player: Player, values):
          if values['pun_1'] == 1 and values['pun_2'] == 1: #punish both
             return 'You cannot assign points to both the members'
    def is_displayed(player):
        return player.agree== 0
    def vars_for_template(player: Player):
        return dict(group=player.group.id_in_subsession, label=player.id_in_group,choice2=player.choice2, c1=player.participant.vars['choices'][0], c2=player.participant.vars['choices'][1], c3=player.participant.vars['choices'][2])

class FinalPunishment(Page):
    wait_for_all_groups = False
    def is_displayed(player):
        return player.agree== 0
    def vars_for_template(player: Player):
        return dict(group=player.group.id_in_subsession, burn=player.burn, burn_2=player.burn_2,label=player.id_in_group,choice2=player.choice2,choice2_old=player.choice2_old, choice=player.choice, pay_1=player.pay_1,  pay_2=player.pay_2,donation_1=player.donation_1,donation_2=player.donation_2, pay_belief_q1=player.pay_belief_q1, pay_belief_q2=player.pay_belief_q2, red_pun=player.red_pun, point_pun= player.red_pun/50, cost_pun=player.cost_pun/10, finalpay=player.final_payoff, total_donation=player.total_donation, final_agree=player.final_agree)


page_sequence = [Choice, WaitPage1, Results, Choice2, Beliefs, WaitPage2,WaitPage3, Punishment, WaitPage4,Agreement,FinalPunishment ]
