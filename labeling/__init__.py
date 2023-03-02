from otree.api import *
c = Currency
import random as r

doc = """
Labeling experiment v 1.1
author: Marco Faillo
data: 8/2/2023
"""



class Constants(BaseConstants):
    name_in_url = 'labeling'
    players_per_group = None
    num_rounds = 1
    # instructions_template = 'public_goods/instructions.html'
    # """Amount allocated to each player"""
    exchange_rate = 0.1 #tasso di cambio 10 punti = 0.50 €
    showup= 1
    endowment =10
    estratto_tab=r.randint(0, 50) #bid number nutritional table
    estratto_nutri=r.randint(0, 50) #bid number nutriscore
    estratto_eco=r.randint(0, 50) #bid number footprint
    estratto_tipic=r.randint(0, 50) #bid number typicity
    p_mezzipaccheri = 6.40
    p_tagliatelle = 4.40
    p_passata = 4.90
    p_olio = 9.80
    p_riso = 4.30
    p_parmigiano = 5.50
    p_cioccolato = 3.40
    p_burro = 3.50







class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass

class Player(BasePlayer):
    bid_info_nutri= models.IntegerField(initial=0) #bid for info on nutrients
    bid_info_tab= models.IntegerField(initial=0) #bid for info on addictives
    bid_info_eco= models.IntegerField(initial=0) #bid for info on eco footprint
    bid_info_tipic= models.IntegerField(initial=0) #bid for info on typicity.
    money_from_info=models.IntegerField(initial=0) #money saved after bidding.
    give_info_nutri= models.IntegerField(initial=0) #=1 if bid_info_nutri > estratto
    give_info_tab= models.IntegerField(initial=0) #=1 if bid_info_addit > estratto
    give_info_eco= models.IntegerField(initial=0) #=1 if bid_info_eco > estratto
    give_info_tipic= models.IntegerField(initial=0)#=1 if bid_info_tipic> estratto
    no_bid_made=models.IntegerField(initial=0)#=1 if no bid
    no_info_given= models.IntegerField(initial=0)#=1 if no information will be given
    mezzipaccheri=models.IntegerField(initial=0)  #1 if chosen
    tagliatelle=models.IntegerField(initial=0)  #1 if chosen
    passata=models.IntegerField(initial=0)  #1 if chosen
    olio=models.IntegerField(initial=0)  #1 if chosen
    riso=models.IntegerField(initial=0)  #1 if chosen
    cioccolato=models.IntegerField(initial=0)  #1 if chosen
    parmigiano=models.IntegerField(initial=0)  #1 if chosen
    burro=models.IntegerField(initial=0)  #1 if chosen
    risparmio_info=models.FloatField(initial=0) #money not used to buy information
    spesa_totale=models.FloatField(initial=0)
    residuo=models.FloatField(initial=0)  #money saved
    payoff_prolific=models.FloatField(initial=0)  # amount to be paid in Prolific


## functions
# check for info to be given

class Instructions(Page):
    pass

class Information(Page):
    form_model = 'player'
    form_fields = ['bid_info_nutri', 'bid_info_tab', 'bid_info_eco', 'bid_info_tipic']
    def error_message(player: Player, values):
        if values['bid_info_tab'] > 50:
           return 'Attenzione, il numero massimo che puoi inserire per vedere la scheda con i valori nutrizionali è 50'
        if values['bid_info_nutri'] > 50:
           return 'Attenzione, il numero massimo che puoi inserire per vedere il punteggio nutriscore è 50'
        if values['bid_info_eco'] > 50:
           return 'Attenzione, il numero massimo che puoi inserire per avere informazioni sull\'impronta ecologica  è 50'
        if values['bid_info_tipic'] > 50:
           return 'Attenzione, il numero massimo che puoi inserire per avere informazioni sulla tipicità è 50'






class Results_Information(Page):

    def vars_for_template(player: Player):
        player.risparmio_info = (200 - (player.bid_info_nutri+player.bid_info_tab+player.bid_info_eco+ player.bid_info_tipic))/100
        print(player.risparmio_info)
        if player.bid_info_nutri+player.bid_info_tab+player.bid_info_eco+ player.bid_info_tipic ==0:
           player.no_bid_made =1 # no bid made
        if Constants.estratto_nutri <  player.bid_info_nutri:
           player.give_info_nutri =1
        if Constants.estratto_tab <  player.bid_info_tab:
           player.give_info_tab =1
        if Constants.estratto_eco <  player.bid_info_eco:
           player.give_info_eco =1
        if Constants.estratto_tipic<  player.bid_info_tipic:
           player.give_info_tipic =1
        if player.give_info_nutri+player.give_info_tab+player.give_info_eco+ player.give_info_tipic ==0:
           player.no_info_given =1 # receive no information

        return dict(bid_info_nutri=player.bid_info_nutri, bid_info_tab=player.bid_info_tab, bid_info_eco=player.bid_info_eco, bid_info_tipic=player.bid_info_tipic,no_bid_made= player.no_bid_made, no_info_given= player.no_info_given, estratto_tab=Constants.estratto_tab, estratto_nutri= Constants.estratto_nutri, estratto_eco= Constants.estratto_eco,estratto_tipic= Constants.estratto_tipic,give_info_nutri=player.give_info_nutri, give_info_tab=player.give_info_tab,give_info_eco=player.give_info_eco,give_info_tipic=player.give_info_tipic)

class Products_noinfo(Page):
    form_model = 'player'
    form_fields = ['mezzipaccheri', 'tagliatelle', 'passata', 'olio', 'riso', 'parmigiano', 'cioccolato','burro']
    def vars_for_template(player: Player):
        return dict(give_info_nutri=player.give_info_nutri, give_info_tab=player.give_info_tab,give_info_eco=player.give_info_eco,give_info_tipic=player.give_info_tipic)




class Final(Page):
    def vars_for_template(player: Player):
        player.spesa_totale = player.mezzipaccheri*Constants.p_mezzipaccheri + player.tagliatelle*Constants.p_tagliatelle + player.passata*Constants.p_passata + player.olio*Constants.p_olio+player.riso*Constants.p_riso+player.parmigiano*Constants.p_parmigiano+player.cioccolato*Constants.p_cioccolato+player.burro*Constants.p_burro
        print (player.mezzipaccheri,player.spesa_totale)
        player.residuo=round(10-player.spesa_totale,2)
        player.payoff_prolific =player.residuo+ player.risparmio_info

        return dict(risparmio_info=player.risparmio_info,spesa_totale=player.spesa_totale,residuo=player.residuo, mezzipaccheri= player.mezzipaccheri, tagliatelle= player.tagliatelle, passata=player.passata, olio=player.olio, riso=player.riso, parmigiano=player.parmigiano, cioccolato=player.cioccolato, burro=player.burro)



page_sequence = [ Instructions,Information, Results_Information,Products_noinfo,Final]
