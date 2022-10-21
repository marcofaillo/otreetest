from otree.api import *
c = Currency
import random as r

doc = """
Energy poverty experiment
"""

#subjects are assigned to three groups: poor (endowment always 50) , poor-rich (endowment 50 for the first n periods and then 100)
#rich (endowment always 100).
#treatment: 1 poor; 2 poor-rich; 3 rich

class Constants(BaseConstants):
    name_in_url = 'energy_boost'
    players_per_group = 4
    num_rounds = 1
    # instructions_template = 'public_goods/instructions.html'
    # """Amount allocated to each player"""
    selected_round=r.randint(1,num_rounds)
    round_poor=num_rounds/2 # poor_rich become rich starting from this round
    endowment_p = 50 #endowment poor and poor_rich (fist n/2 rounds)
    endowment_r= 100  #endowment rich
    alpha = 1.5
    alpha_me = 1.38
    costs_list=[20,40,80,60]
    prices_list=[20,40,80,90]
    benefits_list=[30,60,120,120]
    # beta = 1
    # beta_me = 10/13
    n = 4
    exchange_rate = 0.1 #tasso di cambio 10 punti = 0.50 €
    showup= 3






class Subsession(BaseSubsession):
    pass

def creating_session(subsession):
    subsession.group_randomly()
    print(subsession.get_group_matrix())

class Group(BaseGroup):
    total_consumption = models.IntegerField()
    total_externality = models.FloatField()
    per_capita_externality= models.FloatField()

    f_20 =models.IntegerField()
    f_40 =models.IntegerField()
    f_80 =models.IntegerField()
    f_60 =models.IntegerField()
    per_capita_externality= models.FloatField()
    # individual_share = models.CurrencyField()


class Player(BasePlayer):
    choice = models.IntegerField(
                    choices=[[1, 'Opzione A '], [2, ' Opzione B '], [3, 'Opzione C '], [4, 'Opzione D']],
        label="Scegli una delle opzioni",
    )
    price=models.IntegerField(initial=0) # price of option
    benefit=models.IntegerField() # benefic from the option
    cost=models.IntegerField(initial=0)# cost from the option
    rich=models.IntegerField(initial=0) # =1 if rich
    poor_rich=models.IntegerField(initial=0) # =1 if poor and then rich
    poor= models.IntegerField(initial=0) # =1 if poor and then rich
    profit= models.FloatField()
    profit_av=models.FloatField() #average payoff of others
    finalpoints =models.FloatField()
    finalpay =models.FloatField() #final payoff in UMS
    finalpay_euro =models.FloatField() #final payoff in euros
    #control questions
    q1 = models.IntegerField(
         choices=[[1, 'Vero'], [2, 'Falso']],
         widget=widgets.RadioSelect)
    q2 = models.IntegerField()
    q3 = models.IntegerField()
    q4 = models.IntegerField(
         choices=[[1, 'Vero'], [2, 'Falso']],
         widget=widgets.RadioSelect)

    #questionnaire variables.

    gender = models.IntegerField(
         choices=[[1, 'Uomo'], [2, 'Donna']],)
    age = models.IntegerField()
    nat =  models.StringField()
    major = models.StringField()
    vol =  models.IntegerField(
         choices=[[1, 'Sì'], [2, 'No']],)
    errors=models.IntegerField(initial=0)
    quest1 = models.IntegerField(
         choices=[[1, "Molto d'accordo"], [2, "D'accordo"],[3, "Più d'accordo che in disaccordo"], [4, "Né d'accordo né in disaccordo"] ,[5, "Più in disaccordo che d'accordo"],[6, "In disaccordo che d'accordo"],[7, "Molto in disaccordo"]])
    quest2 = models.IntegerField(
         choices=[[1, "Molto d'accordo"], [2, "D'accordo"],[3, "Più d'accordo che in disaccordo"], [4, "Né d'accordo né in disaccordo"] ,[5, "Più in disaccordo che d'accordo"],[6, "In disaccordo che d'accordo"],[7, "Molto in disaccordo"]])
    quest3 = models.IntegerField(
         choices=[[1, "Molto d'accordo"], [2, "D'accordo"],[3, "Più d'accordo che in disaccordo"], [4, "Né d'accordo né in disaccordo"] ,[5, "Più in disaccordo che d'accordo"],[6, "In disaccordo che d'accordo"],[7, "Molto in disaccordo"]])
    quest4 = models.IntegerField(
         choices=[[1, "Molto d'accordo"], [2, "D'accordo"],[3, "Più d'accordo che in disaccordo"], [4, "Né d'accordo né in disaccordo"] ,[5, "Più in disaccordo che d'accordo"],[6, "In disaccordo che d'accordo"],[7, "Molto in disaccordo"]])
    quest5 = models.IntegerField(
         choices=[[1, "Molto d'accordo"], [2, "D'accordo"],[3, "Né d'accordo né in disaccordo"], [4, "Poco d'accordo"] ,[5, "Per niente d'accordo"]])
    quest6 = models.IntegerField(
         choices=[[1, "Molto d'accordo"], [2, "D'accordo"],[3, "Più d'accordo che in disaccordo"], [4, "Né d'accordo né in disaccordo"] ,[5, "Più in disaccordo che d'accordo"],[6, "In disaccordo che d'accordo"],[7, "Molto in disaccordo"]])
    quest7 = models.IntegerField(
         choices=[[1, "Molto d'accordo"], [2, "D'accordo"],[3, "Più d'accordo che in disaccordo"], [4, "Né d'accordo né in disaccordo"] ,[5, "Più in disaccordo che d'accordo"],[6, "In disaccordo che d'accordo"],[7, "Molto in disaccordo"]])
    quest8 = models.IntegerField(
         choices=[[1, "Molto d'accordo"], [2, "D'accordo"],[3, "Più d'accordo che in disaccordo"], [4, "Né d'accordo né in disaccordo"] ,[5, "Più in disaccordo che d'accordo"],[6, "In disaccordo che d'accordo"],[7, "Molto in disaccordo"]])
    quest9 = models.IntegerField(
         choices=[[1, "Molto d'accordo"], [2, "D'accordo"],[3, "Più d'accordo che in disaccordo"], [4, "Né d'accordo né in disaccordo"] ,[5, "Più in disaccordo che d'accordo"],[6, "In disaccordo che d'accordo"],[7, "Molto in disaccordo"]])
    quest10 = models.IntegerField(
         choices=[[1, "Molto d'accordo"], [2, "D'accordo"],[3, "Più d'accordo che in disaccordo"], [4, "Né d'accordo né in disaccordo"] ,[5, "Più in disaccordo che d'accordo"],[6, "In disaccordo che d'accordo"],[7, "Molto in disaccordo"]])
    quest11 = models.IntegerField(
         choices=[[1, "Molto d'accordo"], [2, "D'accordo"],[3, "Più d'accordo che in disaccordo"], [4, "Né d'accordo né in disaccordo"] ,[5, "Più in disaccordo che d'accordo"],[6, "In disaccordo che d'accordo"],[7, "Molto in disaccordo"]])
    quest12 = models.IntegerField(
         choices=[[1, "Molto d'accordo"], [2, "D'accordo"],[3, "Più d'accordo che in disaccordo"], [4, "Né d'accordo né in disaccordo"] ,[5, "Più in disaccordo che d'accordo"],[6, "In disaccordo che d'accordo"],[7, "Molto in disaccordo"]])
    quest13 = models.IntegerField(
         choices=[[1, "Molto d'accordo"], [2, "D'accordo"],[3, "Più d'accordo che in disaccordo"], [4, "Né d'accordo né in disaccordo"] ,[5, "Più in disaccordo che d'accordo"],[6, "In disaccordo che d'accordo"],[7, "Molto in disaccordo"]])
    quest14 = models.IntegerField(
         choices=[[1, "Molto d'accordo"], [2, "D'accordo"],[3, "Più d'accordo che in disaccordo"], [4, "Né d'accordo né in disaccordo"] ,[5, "Più in disaccordo che d'accordo"],[6, "In disaccordo che d'accordo"],[7, "Molto in disaccordo"]])
    quest15 = models.IntegerField(
         choices=[[1, "Molto d'accordo"], [2, "D'accordo"],[3, "Più d'accordo che in disaccordo"], [4, "Né d'accordo né in disaccordo"] ,[5, "Più in disaccordo che d'accordo"],[6, "In disaccordo che d'accordo"],[7, "Molto in disaccordo"]])
    quest16 = models.IntegerField(
         choices=[[1, "Molto d'accordo"], [2, "D'accordo"],[3, "Più d'accordo che in disaccordo"], [4, "Né d'accordo né in disaccordo"] ,[5, "Più in disaccordo che d'accordo"],[6, "In disaccordo che d'accordo"],[7, "Molto in disaccordo"]])
    quest17 = models.IntegerField(
         choices=[[1, "Molto d'accordo"], [2, "D'accordo"],[3, "Più d'accordo che in disaccordo"], [4, "Né d'accordo né in disaccordo"] ,[5, "Più in disaccordo che d'accordo"],[6, "In disaccordo che d'accordo"],[7, "Molto in disaccordo"]])
    quest18 = models.IntegerField(
         choices=[[1, "Molto d'accordo"], [2, "D'accordo"],[3, "Più d'accordo che in disaccordo"], [4, "Né d'accordo né in disaccordo"] ,[5, "Più in disaccordo che d'accordo"],[6, "In disaccordo che d'accordo"],[7, "Molto in disaccordo"]])
    deb_1= models.StringField()
    deb_2 = models.StringField()
    deb_3 = models.StringField()


def set_rich(self):
    #subject is assign to one of the three groups: poor, poor-rich or rich
    for p in self.group.get_players():
        #poor
        if  p.session.config['treatment'] == 1:
            p.poor=1

            print("povero")
        #poor_rich
        #and p.subsession.round_number<=Constants.round_povero
        elif  p.session.config['treatment'] == 2 :
            p.poor_rich=1
            print("povero_ricco")
        #rich
        else:
            p.rich=1
            print("ricco")


def set_payoffs(group: Group):
    for p in group.get_players():
        p.price=Constants.prices_list[p.choice-1]
        p.benefit=Constants.benefits_list[p.choice-1]
        p.cost=Constants.costs_list[p.choice-1]


    group.total_externality = sum([p.cost for p in group.get_players()])
    group.f_20=[p.choice for p in group.get_players()].count(1)
    group.f_40=[p.choice for p in group.get_players()].count(2)
    group.f_80=[p.choice for p in group.get_players()].count(3)
    group.f_60=[p.choice for p in group.get_players()].count(4)


    # for p in group.get_players():
    #     group.total_externality = group.total_consumption
    # # for p in group.get_players():
    #     if p.choice != 90: # non autoelettrica
    #         group.total_externality = Constants.beta*group.total_consumption
    #     else:
    #         group.total_externality = Constants.beta_me*group.total_consumption
    group.per_capita_externality=  group.total_externality/4

    for p in group.get_players():

        if p.rich==1 or (p.poor_rich==1 and p.subsession.round_number>Constants.round_poor): # ricchi o poveri ricchi
            p.profit= Constants.endowment_r  - p.price + p.benefit  -  group.total_externality/(Constants.n)
        elif p.poor==1 or (p.poor_rich==1 and p.subsession.round_number<=Constants.round_poor): # poveri o poveri_ricchi
            p.profit= Constants.endowment_p  - p.price + p.benefit  -  group.total_externality/(Constants.n)
        print("profit", p.profit)
        print("gruppo", p.group.id_in_subsession)


def set_av_payoffs(group: Group):

    for p in group.get_players():
        p.profit_av=(sum([p.profit for p in group.get_players()])-p.profit)/3
        print("average",p.profit_av)

def finalpay (group: Group):
    for p in group.get_players():
        p.finalpay = p.in_round(Constants.selected_round).profit
        p.finalpoints = p.finalpay
        print('final pay', p.finalpay)
        p.finalpay_euro =p.finalpay * Constants.exchange_rate



class Start(Page):
    def is_displayed(player: Player):
        ## ultimo round mostra risultati
        return player.subsession.round_number == 1

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

class WaitPage0(WaitPage):
    wait_for_all_groups=True
    body_text = "Attendi che gli altri partecipanti facciano le loro scelte"

class WaitPage1(WaitPage):
    after_all_players_arrive = set_rich
    body_text = "Attendi che gli altri partecipanti facciano le loro scelte"


class Contribute(Page):
    """Player: Choose how much to contribute"""

    form_model = 'player'
    form_fields = ['choice']

    def error_message(player: Player, values):

       if (player.poor==1 or (player.poor_rich==1 and player.subsession.round_number<=Constants.round_poor)) and (values['choice']==3 or values['choice']  == 4):
            return 'La tua dotazione non ti permette di scegliere questa opzione'


    def vars_for_template(player: Player):
        return dict(round_poor=Constants.round_poor, rich = player.rich,poor_rich= player.poor_rich, round=player.subsession.round_number, group=player.group.id_in_subsession)



class ResultsWaitPage(WaitPage):
    after_all_players_arrive = set_payoffs
    body_text = "Attendi che gli altri partecipanti facciano le loro scelte"

class ResultsWaitPage2(WaitPage):
    #calcola payoff medio
    after_all_players_arrive = set_av_payoffs
    body_text = "Attendi che gli altri partecipanti facciano le loro scelte"

class Results(Page):
    """Players payoff: How much each has earned"""

    def vars_for_template(player: Player):

        group = player.group

        return dict(choice = player.choice, price= player.price,cost= player.cost, benefit= player.benefit, total_externality = group.total_externality, per_capita_externality=group.per_capita_externality, gruppo=player.group.id_in_subsession, payoff =player.profit, av_payoff=player.profit_av, f_20= group.f_20,f_40=group.f_40,f_80=group.f_80,f_60=group.f_60)

class WaitPage2(WaitPage):
    wait_for_all_groups = True
    body_text = "Attendi che gli altri partecipanti facciano le loro scelte"

class ResultsWaitPage3(WaitPage):
    def is_displayed(player: Player):
        ## ultimo round mostra risultati
        return player.subsession.round_number == Constants.num_rounds
    after_all_players_arrive = finalpay
    body_text = "Attendi che gli altri partecipanti facciano le loro scelte"

class Diventa_ricco(Page):
    """Players payoff: How much each has earned"""
    def is_displayed(player: Player):
        ## ultimo round mostra risultati
        return player.subsession.round_number == Constants.round_poor and (player.poor_rich==1  or player.poor==1)

    def vars_for_template(player: Player):
        return dict(poor_rich=player.poor_rich, poor=player.poor)

class Final(Page):
    """Players payoff: How much each has earned"""
    def is_displayed(player: Player):
        ## ultimo round mostra risultati
        return player.subsession.round_number == Constants.num_rounds
    def vars_for_template(player: Player):
        return dict(selected_round=Constants.selected_round, finalpay= player.finalpay, gruppo=player.group.id_in_subsession, finalpay_euro= player.finalpay_euro, showup=Constants.showup)


class Questionnaire(Page):
    form_model = 'player'
    form_fields = ['gender', 'age', 'nat', 'major','vol','quest1', 'quest2', 'quest3', 'quest4','quest5','quest6','quest7','quest8','quest9','quest10','quest11','quest12','quest13','quest14','quest15','quest16','quest17','quest18', 'deb_1', 'deb_2', 'deb_3']
    """Players payoff: How much each has earned"""
    def is_displayed(player: Player):
        return player.subsession.round_number == Constants.num_rounds

page_sequence = [WaitPage1,WaitPage0,Start, Contribute, ResultsWaitPage,ResultsWaitPage2, Results, WaitPage2, Diventa_ricco,ResultsWaitPage3,Final, Questionnaire]
