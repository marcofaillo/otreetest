from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)

import random as r
author = 'Marco Faillo'

doc = """
Replication of Barrtling et al.
"""


class Constants(BaseConstants):
    test=0 #dummy per test
    name_in_url = 'bartling'
    players_per_group = 16
    num_rounds = 24
    value = 50
    damage = 60 #damage to class
    endowment = 100 #endowment per round (all the players)
    cost_d = 0 #costo per produrre bene che genera danno a C
    cost_nd = 10 #costo per produrre bene che non genera danno a C
    selected_round =r.randint(1,num_rounds)
    exchange_rate = 0.05 #tasso di cambio 10 punti = 0.50 €
    showup= 5


class Subsession(BaseSubsession):

    def creating_session(self):
        for player in self.get_players():
            player.participant.vars['prices']=[[1,0,-1,-1],[2,0,-1,-1],[3,0,-1,-1],[4,0,-1,-1],[5,0,-1,-1],[6,0,-1,-1]] #  [seller Id, price, product, order]
            player.participant.vars['order']=[7,8,9,10,11]   # buyers entry order
            player.participant.vars['products']=[-1,-1,-1,-1,-1] #prodotti acquistati per matching con dummy





class Group(BaseGroup):
    turno = models.IntegerField(initial=0)  #contatore per scorrere nel vettore ordine
    c1 =models.IntegerField(initial=0)   # dummy per offerte accettate
    c2 =models.IntegerField(initial=0)
    c3 =models.IntegerField(initial=0)
    c4 =models.IntegerField(initial=0)
    c5 =models.IntegerField(initial=0)
    c6 =models.IntegerField(initial=0)

    c12 =models.IntegerField(initial=0)
    c13 =models.IntegerField(initial=0)
    c14 =models.IntegerField(initial=0)
    c15 =models.IntegerField(initial=0)
    c16 =models.IntegerField(initial=0)
#salva le offerte dei venditori

    def save_offers(self):
            s1 = self.get_player_by_id(1)
            s2 = self.get_player_by_id(2)
            s3 = self.get_player_by_id(3)
            s4 = self.get_player_by_id(4)
            s5 = self.get_player_by_id(5)
            s6 = self.get_player_by_id(6)


            for player in self.get_players():

                player.participant.vars['prices'][0][1]= s1.seller_price#
                player.participant.vars['prices'][1][1]= s2.seller_price#
                player.participant.vars['prices'][2][1]= s3.seller_price#
                player.participant.vars['prices'][3][1]= s4.seller_price#
                player.participant.vars['prices'][4][1]= s5.seller_price#
                player.participant.vars['prices'][5][1]= s6.seller_price#

                player.participant.vars['prices'][0][2]= s1.seller_product#
                player.participant.vars['prices'][1][2]= s2.seller_product#
                player.participant.vars['prices'][2][2]= s3.seller_product#
                player.participant.vars['prices'][3][2]= s4.seller_product#
                player.participant.vars['prices'][4][2]= s5.seller_product#
                player.participant.vars['prices'][5][2]= s6.seller_product#

                r.shuffle(s1.participant.vars['prices'])   # shuffle del vettore prize per un venditore
                r.shuffle(s1.participant.vars['order'])   # shuffle del vettore order
            for player in self.get_players():
                player.participant.vars['prices']=s1.participant.vars['prices'] # copia del vettore rimescolato per tutti
                player.participant.vars['order']=s1.participant.vars['order'] # copia del vettore rimescolato per tutti

    def save_accepted(self): #salva lo status delle offerte
            c7 = self.get_player_by_id(7)
            c8 = self.get_player_by_id(8)
            c9 = self.get_player_by_id(9)
            c10 = self.get_player_by_id(10)
            c11 = self.get_player_by_id(11)

            for player in self.get_players():
                if c7.buyer_choice != 0:
                    player.participant.vars['prices'][c7.buyer_choice-1][3]= c7.accepted_order#scrive l'ordine di accettazione nella casella del venditore
                    c7.product_bought=player.participant.vars['prices'][c7.buyer_choice-1][2]
                    player.participant.vars['products'][player.participant.vars['order'].index(7)]=c7.product_bought
                if c8.buyer_choice != 0:
                    player.participant.vars['prices'][c8.buyer_choice-1][3]= c8.accepted_order#scrive l'ordine di accettazione nella casella del venditore
                    c8.product_bought=player.participant.vars['prices'][c8.buyer_choice-1][2]
                    player.participant.vars['products'][player.participant.vars['order'].index(8)]=c8.product_bought
                if c9.buyer_choice != 0:
                    player.participant.vars['prices'][c9.buyer_choice-1][3]= c9.accepted_order#scrive l'ordine di accettazione nella casella del venditore
                    c9.product_bought=player.participant.vars['prices'][c9.buyer_choice-1][2]
                    player.participant.vars['products'][player.participant.vars['order'].index(9)]=c9.product_bought
                if c10.buyer_choice != 0:
                    player.participant.vars['prices'][c10.buyer_choice-1][3]= c10.accepted_order#scrive l'ordine di accettazione nella casella del venditore
                    c10.product_bought=player.participant.vars['prices'][c10.buyer_choice-1][2]
                    player.participant.vars['products'][player.participant.vars['order'].index(10)]=c10.product_bought
                if c11.buyer_choice != 0:
                    player.participant.vars['prices'][c11.buyer_choice-1][3]= c11.accepted_order#scrive l'ordine di accettazione nella casella del venditore
                    c11.product_bought=player.participant.vars['prices'][c11.buyer_choice-1][2]
                    player.participant.vars['products'][player.participant.vars['order'].index(11)]=c11.product_bought
                print('prodotto salvato', player.participant.vars['products'])




# fa avanzare il prossimo consumatore aggiornando il puntatore turno e
    def next_buyer(self):
            for player in self.get_players():
                print(player.participant.vars['prices'])
                print(player.participant.vars['order'])
                #il codice sotto non funziona.

            self.turno+= 1

            print("turno",self.turno)




class Player(BasePlayer):
    q1 = models.IntegerField() # domande di controllo
    q2 = models.IntegerField()
    q3 = models.IntegerField()
    q4 = models.IntegerField()
    q5 = models.IntegerField()
    q6 = models.IntegerField()
    q7 = models.IntegerField()
    q8 = models.IntegerField()
    q9 = models.IntegerField()
    q10 = models.IntegerField()
    q11 = models.IntegerField()
    q12 = models.IntegerField()

                                #domande questionario
    # d1 = models.IntegerField(choices=[[0, 'Per niente'],[1],[2],[3],[4],[5,'del tutto']])
    d1 = models.IntegerField(choices=[[1, '1. (Per nulla)'], [2,'2.'],[3,'3.'],[4,'4.'],[5, '5. (Del tutto)']])
    d2 = models.IntegerField()
    d3 = models.IntegerField()
    d4 = models.IntegerField(choices=[[1, 'F'], [2,'M']])
    d5 = models.StringField()
    d6 = models.StringField()
    d7 = models.StringField()
    d8 = models.IntegerField(choices=[[1, '1. (Per nulla disposto a prendere rischi)'], [2,'2.'],[3,'3.'],[4,'4.'],[5,'5.'],[6,'6.'],[7,'7.'],[8,'8.'],[9,'9.'],[10, '10. (Del tutto disposto a prendere rischi)']])
    d91 =models.IntegerField(choices=[[-5, "-5. (Per nulla d'accordo)"], [-4,'-4.'], [-3,'-3.'], [-2,'-2.'], [-1,'-1.'], [0,'0.'] , [1,'1.'], [2,'2.'], [3,'3.'], [4,'4.'], [5,"5. (Completamente d'accordo)"]            ])
    d92 =models.IntegerField(choices=[[-5, "-5. (Per nulla d'accordo)"], [-4,'-4.'], [-3,'-3.'], [-2,'-2.'], [-1,'-1.'], [0,'0.'] , [1,'1.'], [2,'2.'], [3,'3.'], [4,'4.'], [5,"5. (Completamente d'accordo)"]            ])
    d93 =models.IntegerField(choices=[[-5, "-5. (Per nulla d'accordo)"], [-4,'-4.'], [-3,'-3.'], [-2,'-2.'], [-1,'-1.'], [0,'0.'] , [1,'1.'], [2,'2.'], [3,'3.'], [4,'4.'], [5,"5. (Completamente d'accordo)"]            ])
    d94 =models.IntegerField(choices=[[-5, "-5. (Per nulla d'accordo)"], [-4,'-4.'], [-3,'-3.'], [-2,'-2.'], [-1,'-1.'], [0,'0.'] , [1,'1.'], [2,'2.'], [3,'3.'], [4,'4.'], [5,"5. (Completamente d'accordo)"]            ])
    d95 =models.IntegerField(choices=[[-5, "-5. (Per nulla d'accordo)"], [-4,'-4.'], [-3,'-3.'], [-2,'-2.'], [-1,'-1.'], [0,'0.'] , [1,'1.'], [2,'2.'], [3,'3.'], [4,'4.'], [5,"5. (Completamente d'accordo)"]            ])
    d96 =models.IntegerField(choices=[[-5, "-5. (Per nulla d'accordo)"], [-4,'-4.'], [-3,'-3.'], [-2,'-2.'], [-1,'-1.'], [0,'0.'] , [1,'1.'], [2,'2.'], [3,'3.'], [4,'4.'], [5,"5. (Completamente d'accordo)"]            ])
    d97 =models.IntegerField(choices=[[-5, "-5. (Per nulla d'accordo)"], [-4,'-4.'], [-3,'-3.'], [-2,'-2.'], [-1,'-1.'], [0,'0.'] , [1,'1.'], [2,'2.'], [3,'3.'], [4,'4.'], [5,"5. (Completamente d'accordo)"]            ])
    d98 =models.IntegerField(choices=[[-5, "-5. (Per nulla d'accordo)"], [-4,'-4.'], [-3,'-3.'], [-2,'-2.'], [-1,'-1.'], [0,'0.'] , [1,'1.'], [2,'2.'], [3,'3.'], [4,'4.'], [5,"5. (Completamente d'accordo)"]            ])
    d99 =models.IntegerField(choices=[[-5, "-5. (Per nulla d'accordo)"], [-4,'-4.'], [-3,'-3.'], [-2,'-2.'], [-1,'-1.'], [0,'0.'] , [1,'1.'], [2,'2.'], [3,'3.'], [4,'4.'], [5,"5. (Completamente d'accordo)"]            ])
    d910 =models.IntegerField(choices=[[-5, "-5. (Per nulla d'accordo)"], [-4,'-4.'], [-3,'-3.'], [-2,'-2.'], [-1,'-1.'], [0,'0.'] , [1,'1.'], [2,'2.'], [3,'3.'], [4,'4.'], [5,"5. (Completamente d'accordo)"]            ])
    d911 =models.IntegerField(choices=[[-5, "-5. (Per nulla d'accordo)"], [-4,'-4.'], [-3,'-3.'], [-2,'-2.'], [-1,'-1.'], [0,'0.'] , [1,'1.'], [2,'2.'], [3,'3.'], [4,'4.'], [5,"5. (Completamente d'accordo)"]            ])
    d912 =models.IntegerField(choices=[[-5, "-5. (Per nulla d'accordo)"], [-4,'-4.'], [-3,'-3.'], [-2,'-2.'], [-1,'-1.'], [0,'0.'] , [1,'1.'], [2,'2.'], [3,'3.'], [4,'4.'], [5,"5. (Completamente d'accordo)"]            ])
    d913 =models.IntegerField(choices=[[-5, "-5. (Per nulla d'accordo)"], [-4,'-4.'], [-3,'-3.'], [-2,'-2.'], [-1,'-1.'], [0,'0.'] , [1,'1.'], [2,'2.'], [3,'3.'], [4,'4.'], [5,"5. (Completamente d'accordo)"]            ])
    d914 =models.IntegerField(choices=[[-5, "-5. (Per nulla d'accordo)"], [-4,'-4.'], [-3,'-3.'], [-2,'-2.'], [-1,'-1.'], [0,'0.'] , [1,'1.'], [2,'2.'], [3,'3.'], [4,'4.'], [5,"5. (Completamente d'accordo)"]            ])
    d915 =models.IntegerField(choices=[[-5, "-5. (Per nulla d'accordo)"], [-4,'-4.'], [-3,'-3.'], [-2,'-2.'], [-1,'-1.'], [0,'0.'] , [1,'1.'], [2,'2.'], [3,'3.'], [4,'4.'], [5,"5. (Completamente d'accordo)"]            ])
    d10 =models.IntegerField(choices=[[-1, "NA"],[0, "0. (Per niente)"], [1,'1.'], [2,'2.'], [3,'3.'], [4,'4.'], [5,'5.'] , [6,'6.'], [7,'7.'], [8,'8.'], [9,'9.'], [10,"10. (Del tutto)"]            ])
    d11 =models.IntegerField(choices=[[-1, "NA"],[0, "0. (Per niente)"], [1,'1.'], [2,'2.'], [3,'3.'], [4,'4.'], [5,'5.'] , [6,'6.'], [7,'7.'], [8,'8.'], [9,'9.'], [10,"10. (Del tutto)"]            ])
    d12 =models.IntegerField(choices=[[-1, "NA"],[0, "0. (Per niente)"], [1,'1.'], [2,'2.'], [3,'3.'], [4,'4.'], [5,'5.'] , [6,'6.'], [7,'7.'], [8,'8.'], [9,'9.'], [10,"10. (Del tutto)"]            ])
    d13 =models.IntegerField(choices=[[-1, "NA"],[0, "0. (Per niente)"], [1,'1.'], [2,'2.'], [3,'3.'], [4,'4.'], [5,'5.'] , [6,'6.'], [7,'7.'], [8,'8.'], [9,'9.'], [10,"10. (Del tutto)"]            ])
    d141 =models.IntegerField(choices=[[1, "1. Completamente in disaccordo"], [2,'2. Molto in disaccordo.'], [3,'3. Un po’ in disaccordo.'], [4,'4. Né d’accordo né in disaccordo.'], [5,'5. Un po’ d’accordo.'] , [6,'6. Molto d’accordo.'], [7,'7. Completamente d’accordo.']            ])
    d142 =models.IntegerField(choices=[[1, "1. Completamente in disaccordo"], [2,'2. Molto in disaccordo.'], [3,'3. Un po’ in disaccordo.'], [4,'4. Né d’accordo né in disaccordo.'], [5,'5. Un po’ d’accordo.'] , [6,'6. Molto d’accordo.'], [7,'7. Completamente d’accordo.']            ])
    d143 =models.IntegerField(choices=[[1, "1. Completamente in disaccordo"], [2,'2. Molto in disaccordo.'], [3,'3. Un po’ in disaccordo.'], [4,'4. Né d’accordo né in disaccordo.'], [5,'5. Un po’ d’accordo.'] , [6,'6. Molto d’accordo.'], [7,'7. Completamente d’accordo.']            ])
    d144 =models.IntegerField(choices=[[1, "1. Completamente in disaccordo"], [2,'2. Molto in disaccordo.'], [3,'3. Un po’ in disaccordo.'], [4,'4. Né d’accordo né in disaccordo.'], [5,'5. Un po’ d’accordo.'] , [6,'6. Molto d’accordo.'], [7,'7. Completamente d’accordo.']            ])
    d145 =models.IntegerField(choices=[[1, "1. Completamente in disaccordo"], [2,'2. Molto in disaccordo.'], [3,'3. Un po’ in disaccordo.'], [4,'4. Né d’accordo né in disaccordo.'], [5,'5. Un po’ d’accordo.'] , [6,'6. Molto d’accordo.'], [7,'7. Completamente d’accordo.']            ])
    d146 =models.IntegerField(choices=[[1, "1. Completamente in disaccordo"], [2,'2. Molto in disaccordo.'], [3,'3. Un po’ in disaccordo.'], [4,'4. Né d’accordo né in disaccordo.'], [5,'5. Un po’ d’accordo.'] , [6,'6. Molto d’accordo.'], [7,'7. Completamente d’accordo.']            ])
    d147 =models.IntegerField(choices=[[1, "1. Completamente in disaccordo"], [2,'2. Molto in disaccordo.'], [3,'3. Un po’ in disaccordo.'], [4,'4. Né d’accordo né in disaccordo.'], [5,'5. Un po’ d’accordo.'] , [6,'6. Molto d’accordo.'], [7,'7. Completamente d’accordo.']            ])
    d148 =models.IntegerField(choices=[[1, "1. Completamente in disaccordo"], [2,'2. Molto in disaccordo.'], [3,'3. Un po’ in disaccordo.'], [4,'4. Né d’accordo né in disaccordo.'], [5,'5. Un po’ d’accordo.'] , [6,'6. Molto d’accordo.'], [7,'7. Completamente d’accordo.']            ])
    d149 =models.IntegerField(choices=[[1, "1. Completamente in disaccordo"], [2,'2. Molto in disaccordo.'], [3,'3. Un po’ in disaccordo.'], [4,'4. Né d’accordo né in disaccordo.'], [5,'5. Un po’ d’accordo.'] , [6,'6. Molto d’accordo.'], [7,'7. Completamente d’accordo.']            ])
    d1410 =models.IntegerField(choices=[[1, "1. Completamente in disaccordo"], [2,'2. Molto in disaccordo.'], [3,'3. Un po’ in disaccordo.'], [4,'4. Né d’accordo né in disaccordo.'], [5,'5. Un po’ d’accordo.'] , [6,'6. Molto d’accordo.'], [7,'7. Completamente d’accordo.']            ])
    d15 =models.IntegerField(choices=[[1, "Vivi in modo agiato."], [2,'Vivi in modo accettabile.'], [3,'Riesci appena a tirare avanti.'], [4,'Te la passi davvero male.']      ])
    d16 =models.IntegerField(choices=[[1, "Fino a €15.000. "], [2,'Da €15.000,01 a €28.000.'], [3,'Da €28.000,01 a €55.000.'], [4,'Da €55.000,01 a €75.000.'], [5,'Oltre €75.000.']      ])
    d17 =models.IntegerField(choices=[[1, "Nessuna"], [2,'Impiegato/a.'], [3,'Insegnante.'], [4,'Libero Professionista.'], [5,'Operaio/a.'], [6,'Consulente.'],  [7,'Altro.']     ])
    d18 =models.IntegerField(choices=[[1, "Nessuna"], [2,'Sì, come impiegato/a.'], [3,'Sì, come insegnante.'], [4,'Sì, come libero Professionista.'], [5,'Sì. come operaio/a.'], [6,'Sì, come consulente'],  [7,'Sì, altra professione.']     ])




    errors=models.IntegerField(initial = 0)
    seller_product = models.IntegerField(choices=[[0, 'Prodotto senza conseguenze per il partecipante C'], [1, 'Prodotto che causa una perdita al partecipante C']],widget=widgets.RadioSelect)
    seller_price = models.IntegerField(min=0, max=50)
    dummy_belief_seller=models.IntegerField(min=0, max=6)
    dummy_belief_buyer=models.IntegerField(min=0, max=5)
    turno= models.IntegerField(initial=0)  #contatore per scorrere nel vettore ordine
#consumatore
    buyer_choice=models.IntegerField(initial=0) #accepted offer by the buyer
    price_paid=models.IntegerField(initial=-1) #prezzo pagato dal consumatore
    price_received=models.IntegerField(initial=-1) #prezzo ottenuto dal venditore
    accepted_order=models.IntegerField(initial=0) #ordine con cui accetta
    seller_id=models.IntegerField(initial=-1)  #id del venditore da cui compra
    product_bought=models.IntegerField(initial=-1) #tipo di prodotto comprato
    position=models.IntegerField(initial=-1) # posizione del venditore nel vettore price
    accepted=models.IntegerField(initial=-1)  #dummy per venditore 1 = accettata 0= non accettata
    profit=models.IntegerField(initial=0) #profitto del soggetto
    profit_C=models.IntegerField(initial=0) #profitto del dummy
    profit_B= models.IntegerField(initial=0) #profitto del compratore
    contatore=models.IntegerField(initial=0)
    product_d = models.IntegerField(initial=0)
    finalpay = models.IntegerField(initial=0)
    finalpoints = models.IntegerField(initial=0)
    finalpay_euro = models.FloatField(initial=0)

#roles s1...s6, b1...b5, d1...d5
    def role(self):
            for i in self.subsession.get_players():
                if self.id_in_group <= 6:
                  return 'seller'
                elif self.id_in_group >6 and self.id_in_group <=11:
                    return 'buyer'
                else:
                    return 'dummy'


    def azzera(self):
        self.participant.vars['prices']=[[1,0,-1,-1],[2,0,-1,-1],[3,0,-1,-1],[4,0,-1,-1],[5,0,-1,-1],[6,0,-1,-1]]

    def write_offers(self):
                if self.buyer_choice == 1:
                        self.group.c1=1
                elif self.buyer_choice == 2:
                        self.group.c2=1
                if self.buyer_choice == 3:
                        self.group.c3=1
                elif self.buyer_choice == 4:
                        self.group.c4=1
                elif self.buyer_choice == 5:
                        self.group.c5=1
                elif self.buyer_choice == 6:
                        self.group.c6=1

                if self.buyer_choice != 0:
                    self.accepted_order = self.contatore+1
                    print('scelta', self.buyer_choice)
                    print('ordine accettazione', self.accepted_order)
                    for player in self.group.get_players():
                        player.contatore += 1
                        print('contatore', player.contatore)

    def compute_payoff_b(self):
                #consumatore
                if self.id_in_group >6 and self.id_in_group <=11:
                    #acquista
                    if self.buyer_choice != 0:
                        self.price_paid=self.participant.vars['prices'][self.buyer_choice-1][1]
                        self.product_bought=self.participant.vars['prices'][self.buyer_choice-1][2]
                        self.seller_id=self.participant.vars['prices'][self.buyer_choice-1][0]
                        self.profit = Constants.endowment + Constants.value - self.price_paid
                        if self.product_bought == 1: #prodotto con perdita
                            self.profit_C = Constants.endowment -Constants.damage
                        elif self.product_bought == 0:
                            self.profit_C = Constants.endowment
                    else:
                        profit = Constants.endowment
    def compute_payoff_s(self):
                #venditore
                if self.id_in_group <=6:
                        print ('prezzi', self.participant.vars['prices'])
                        self.participant.vars['prices'].sort()
                        print ('prezzi ordinati', self.participant.vars['prices'])
                        self.accepted= self.participant.vars['prices'][self.id_in_group-1][3]
                        self.price_received= self.participant.vars['prices'][self.id_in_group-1][1]
                        print ('id in group',self.id_in_group, 'accepted', self.accepted) #controlla se l'offerta è stata accettata
                    #vende
                        if self.accepted != -1:
                           self.profit_B=Constants.endowment + Constants.value - self.price_received
                           #esternalità
                           if self.seller_product == 1:
                              self.profit = Constants.endowment -Constants.cost_d + self.price_received
                              print ('profit', self.profit)
                              self.profit_C = Constants.endowment -Constants.damage
                          #non esternalità
                           else:
                              self.profit = Constants.endowment -Constants.cost_nd + self.price_received
                              self.profit_C = Constants.endowment
                    #non vende
                        else:
                            self.profit_B=Constants.endowment
                            self.profit = Constants.endowment
                            self.profit_C = Constants.endowment
# payoff dummy
    def compute_payoff_d (self):
                        if self.id_in_group >11:
                            print('prodotti', self.participant.vars['products'])
                            self.product_d=self.participant.vars['products'][self.id_in_group-12]
                            print('prodotto per C', self.product_d)
                        if self.product_d == 1:
                            self.profit = Constants.endowment - 60
                        else:
                            self.profit = Constants.endowment

    #calcola il pagamento finale corrispondente al pagamento del round estratto
    def finalpay (self):
        self.finalpay = self.in_round(Constants.selected_round).profit
        self.finalpoints = self.finalpay
        print('final pay', self.finalpay)
        self.finalpay_euro =self.finalpay * Constants.exchange_rate
