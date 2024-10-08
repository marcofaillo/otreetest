
// var disegni = ["fab fa-affiliatetheme fa-3x","fas fa-bars fa-3x","fas fa-share-alt fa-3x","fas fa-paragraph fa-3x","fas fa-sign-in-alt fa-3x","fas fa-clone fa-3x","fas fa-rss fa-3x","fas fa-fire fa-3x","fas fa-chart-area fa-3x","fas fa-circle fa-3x"];
var disegni = ["fab fa-affiliatetheme","fas fa-bars","fas fa-share-alt","fas fa-paragraph","fas fa-sign-in-alt","fas fa-clone","fas fa-rss","fas fa-fire","fas fa-chart-area","fas fa-circle"];

var num_righe = parseInt($("#numero_righe").val());
var current_riga = $("#riga_corrente").val();
var current_status = $("#stato_corrente").val();
var num_righe_show = current_riga;
var guadagni =  JSON.parse($("#guadagni").val());
var altri = JSON.parse($("#altro_stato_corrente").val());
var guadagni_altri = JSON.parse($("#altro_guadagni").val());
var numero_giocatori = JSON.parse($("#numero_giocatori").val());
var guad_cum = (JSON.parse($("#guadagno_cumulato").val()));
var errore_imitazione = (JSON.parse($("#id_errore_imitazione").val()));;

jQuery(document).ready(function ($) {

	$( "#vendi" ).hide();
	var status = JSON.parse($("#stato_totale").val());

	if (numero_giocatori == 0){
		$("#panel_scelte_altri").hide();
	}
	else{
		$("#panel_scelte_altri").show();
	}
	// alert(altri);
	current_status = status[current_riga - 1]
	$('#id_player_stato_corrente').val(current_status);

	aggiungi_primariga();
	for (var n=1;n<num_righe + 1;n++){
		aggiungi_riga(n);
	}
	for (var nr=num_righe;nr>num_righe_show;nr--){
		$("#"+String(nr)).hide();
	}
	n=parseInt(num_righe_show) + 1;
	for (sst=1;sst<parseInt(num_righe_show) + 1;sst++){
		// alert(sst+'***'+'***'+n+'****'+status[sst-1]);
		set_riga(sst,status[sst-1]);
	}
	var diff1 = 0;
	var diff2 = 0;
	try {
		for (i=0;i<10;i++){
			if (current_status[i] != altri[0][i]) { diff1 = diff1 + 1; }
			if (current_status[i] != altri[1][i]) { diff2 = diff2 + 1; }
		}
	}
	catch (e) {

	}

	aggiungi_altri(altri[0],1,guadagni_altri[0],diff1);
	aggiungi_altri(altri[1],2,guadagni_altri[1],diff2);

	if (current_riga == 1){
		$("#form").submit();
	}

	$( "#vendi" ).show();

	// Bottone Imitazione
	$(document).on('click','.myclassimita',function(){
		if (this.id == "bt_imita_1"){
				v = altri[0];
				$("#id_imita_1").val(1);
		}
		else{
			v = altri[1];
			$("#id_imita_2").val(1)
		}
		// ####### Parte aggiunta per errore in imitazione

		var modifiche_bit = 0;
		try {
			for (i=0;i<10;i++){
				if (current_status[i] != v[i]) {
					random_number = Math.floor(Math.random() * 100) + 1;
					if (random_number <= errore_imitazione) {
						modifiche_bit = modifiche_bit + 1;
						if (v[i] == 0) {v[i] = 1;} else {v[i]=0};
					}
				}
			}

		} catch (e) {

		}
		$('#id_error_imita').val(modifiche_bit);


		// ###########

		set_riga(num_righe_show,v);
		current_status = v.slice();
		$('#id_player_stato_corrente').val(current_status);
		if (modifiche_bit > 0) {
			alert("Un errore è intervenuto nel processo di imitazione e l' immagine dell’altro/a partecipante è stata imitata in maniera imperfetta.\n\nIl viaggiatore dello spazio ha acquistato l'immagine che hai prodotto imitando un/a altro/a partecipante");
		}
		else{
			if (errore_imitazione > 0){
					alert( "Nessun errore è intervenuto nel processo di imitazione e l' immagine dell’altro/a partecipante è stata imitata in maniera perfetta.\n\nIl viaggiatore dello spazio ha acquistato l'immagine che hai prodotto imitando un/a altro/a partecipante" );
			}
			else {
				alert( "Il viaggiatore dello spazio ha acquistato l'immagine che hai prodotto imitando un/a altro/a partecipante" );
			}

		}
		$("#form").submit();
	});

});




$( "#vendi" ).click(function() {
	$( "#vendi" ).hide();
			alert( "Il viaggiatore dello spazio ha acquistato l'immagine da te prodotta." );
			$("#form").submit();
  });

$( "#intest" ).click(function() {
	$( "#vendi" ).show();
});



// Nasconde le righe
function nascondi_righe(){
	$(".row_choice").hide();
}


// Aggiunge le righe
function aggiungi_primariga(){
	var num_riga = 0;
	var nuova_riga = "<div class=\"row bordi_intestazione\" id='" + num_riga + "'>";
	for (i=0;i<10;i++){
		var imgnome = 'imgnome' + String(num_riga) + '-' + String(i+1);
		var cellnome = 'cellnome' + String(num_riga) + '-' + String(i+1);
		nuova_riga = nuova_riga + "<div class=\"col-md-1 bordi_celle_intestazione\" id = \"" +  cellnome  +   "\"><i class=\"" + disegni[i] +" img_choice \" id=\"" + imgnome +  "\"></i></div>";
	}
	nuova_riga = nuova_riga + "<div class=\"col-md-2 bordi_celle_intestazione\"><p>Payoff</p></div> </div>";
	// alert(nuova_riga);
	$('#panel_scelte').append(nuova_riga);
}


// Aggiunge le righe
function aggiungi_riga(numrow){
	var num_riga = numrow;
	var guadnome = 'guadnome' + String(num_riga);
	var nuova_riga = "<div class=\"row row_choice\" id='" + num_riga + "'>";
	for (i=0;i<10;i++){
		var imgnome = 'imgnome' + String(num_riga) + '-' + String(i+1);
		var cellnome = 'cellnome' + String(num_riga) + '-' + String(i+1);
		if (numrow == num_righe_show)
			nuova_riga = nuova_riga + "<div class=\"col-md-1 bordi_celle sfondo cellchoice\" id = \"" +  cellnome  +   "\"><i class=\"" + disegni[i] +" img_choice \" id=\"" + imgnome +  "\"></i></div>";
		else
			nuova_riga = nuova_riga + "<div class=\"col-md-1 bordi_celle cellchoice\" id = \"" +  cellnome  +   "\"><i class=\"" + disegni[i] +" img_choice \" id=\"" + imgnome +  "\"></i></div>";
	}
	nuova_riga = nuova_riga + "<div class=\"col-md-2 bordi_celle bordi_celle_intestazione>\"><p id=\""+ guadnome + "\">&nbsp;</p></div> </div>";
	// alert(nuova_riga);
	$('#panel_scelte').append(nuova_riga);
}

// Scelta immagine
$(document).on('click', ".cellchoice" , function() {
	var nome = this.id;
	var imgnome = "imgnome" + nome.substring(8,nome.length);
	var riga_corrente = nome.substring(8,nome.length - 1);
	var whereischar = nome.indexOf('-');
	if (nome.length >= 11) {riga_corrente = nome.substring(8,nome.length - 2);}
	riga_corrente = nome.substring(8,whereischar);
	// alert(nome + '..' + imgnome + '..' + riga_corrente + '..' + nome.length + '..' + current_status +  '..' + whereischar);
	var isVisible = $('#'+imgnome).is(':visible');

	if (riga_corrente == current_riga){
		var num_element = parseInt(nome.substring(whereischar + 1,nome.length)) - 1;
		// alert(num_element);
		if (isVisible) {
			$('#'+imgnome).hide();
			current_status[num_element] = 0;
		}
		else {
			$('#'+imgnome).show();
			current_status[num_element] = 1;
		}
		// alert(current_status +'*' + String(whereischar) + '*' + nome + '*' + nome.substring(whereischar,nome.length));
		$('#id_player_stato_corrente').val(current_status);
	}
});

// Visualizza o meno gli elementi di una riga
function set_riga(riga,st){
	var elementi = st;
	var riga_to_set = riga;
	var guadnome = 'guadnome' + String(riga_to_set);
	for (var rs=0;rs<10;rs++){
		var imgnome = 'imgnome' + String(riga_to_set) + '-' + String(rs+1);
		if (elementi[rs] == 0){
			$('#'+imgnome).hide();
		}
		else {
			$('#'+imgnome).show();
		}
	}
	// alert(guadagni[riga_to_set - 1]);
	 if (guadagni[riga_to_set - 1] != -1) {
	// alert(String(guadagni[riga_to_set - 1]));
		$('#'+guadnome).html(String(guadagni[riga_to_set - 1]));
	}
}


// Aggiunge le righe degli altri giocatori
function aggiungi_altri(others,ng,guad,diff){
	var nuova_riga = "<div class=\"row bordi_celle_altri\">";
	// for (i=0;i<10;i++){
	// 	if (others[i] == 1){
	// 		nuova_riga = nuova_riga + "<div class=\"col-md-1 bordi_celle\">" +  "<i class=\"" + disegni[i] +"\"></i></div>";
	// 	}
	// 	else{
	// 		nuova_riga = nuova_riga + "<div class=\"col-md-1 bordi_celle\">&nbsp;</div>";
	// 	}
	// }

	if (errore_imitazione > 0){

		nuova_riga = nuova_riga + "<div class=\"col-md-10 col-md-1sx bordi_celle_gray\">Un partecipante selezionato casualmente ha ottenuto un pagamento di </div>";

	}
	else {

		nuova_riga = nuova_riga + "<div class=\"col-md-10 col-md-1sx bordi_celle_gray\">Un partecipante selezionato casualmente ha ottenuto un pagamento di </div>";

	}
	if (guad!=-1){
		// nuova_riga = nuova_riga + "<div class=\"col-md-2 bordi_celle\"><p><small>gioc. " + String(ng) + ": " + String(guad) + "</small></p></div> </div>";
		nuova_riga = nuova_riga + "<div class=\"col-md-2 col-md-1sx bordi_celle\">&nbsp &nbsp &nbsp &nbsp" + String(guad) + "</div>";
	}
	else {
			nuova_riga = nuova_riga + "<div class=\"col-md-2 bordi_celle\"><p> " + String("") + " " + String("") + "</p></div> </div>";
	}
	if (errore_imitazione == 0){
		// nuova_riga = nuova_riga + "<div class=\"row bordi_celle_altri\">";
		nuova_riga = nuova_riga + "<div class=\"col-md-10 col-md-1sx bordi_celle_gray\">Il numero di simboli differenti rispetto all'ultima immagine da te prodotta è </div>";
		nuova_riga = nuova_riga + "<div class=\"col-md-2 col-md-1sx bordi_celle\">&nbsp &nbsp &nbsp &nbsp" + String(diff) + "</div>";
		$('#id_difference').val(diff);
	}

	if (guad!=-1){
		name_button = "bt_imita_" + String(ng );
		nb = "<i class=\"fas fa-cloud-download-alt myclassb\" id=\"" + name_button + "\"></i>";
		nb = "<button class=\"btn btn-outline-primary myclassimita \" id=\"" + name_button + "\">Imita l'immagine prodotta da questo partecipante</button>";
		nuova_riga = nuova_riga + "<div class=\"col-md-10 bordi_celle_imita\" style=\"padding-left:5px\">"  + nb + "&nbsp;</div>";

		nuova_riga = nuova_riga + " </div>";
	}
	else {
			nuova_riga = nuova_riga + "<div class=\"col-md-2 bordi_celle\"><p> " + String("") + " " + String("") + "</p></div> </div>";
	}
	nuova_riga = nuova_riga + "<div class=\"col-md-12 col-md-1sx \">&nbsp;</div>";
	// alert(nuova_riga);
	$('#panel_scelte_altri').append(nuova_riga);
}
