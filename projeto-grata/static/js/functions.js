function justNumbers(num) {

    var er = /[^0-9.]/;
    var field = num;

    er.lastIndex = 0;

    if (er.test(field.value)) {

          field.value = "";
    }
}

$(document).ready(function(){
    $('select').formSelect();
});

$(document).ready(function(){

    $('.sidenav').sidenav();
});

document.addEventListener('DOMContentLoaded', function() {

    var elems = document.querySelectorAll('.dropdown-trigger');
    var instances = M.Dropdown.init(elems, options);
});

$('.dropdown-trigger').dropdown({
      inDuration: 500,
      outDuration: 1025,
      constrain_width: false,
      hover: true,
      gutter: 0,
      belowOrigin: false,
    }
);

$('.datepicker').datepicker({
        i18n: {
            months: ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho',
                    'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'],
            monthsShort: ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'],
            weekdays: ['Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sabádo'],
            weekdaysShort: ['Dom', 'Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sab'],
            weekdaysAbbrev: ['D', 'S', 'T', 'Q', 'Q', 'S', 'S'],
            today: 'Hoje',
            clear: 'Limpar',
            cancel: 'Sair',
            done: 'Confirmar',
        },
        format: 'dd/mm/yyyy',
        container: 'body',
        minDate: new Date(),
        onSet: function (ele) {

           if(ele.select){

                this.close();
           }

            var inicial_date = $('#inicial_date').val();
            var final_date = $('#final_date').val();

            var inicial_date_date1 = new Date(inicial_date);
            var inicial_date_date2 = new Date(final_date);

            var inicial_date_ms = inicial_date_date1.getTime();
            var final_date_ms = inicial_date_date2.getTime();

            if((final_date_ms - inicial_date_ms) < 0 ) {
              alert('A Data final tem que ser maior que a data inicial!');
              $('#inicial_date').val(final_date);
            }
        }
    });

$(function(){

	$('#id_final_hour').timepicker({
		showCleanBtn: true,
		autoClose: false,
		twelveHour: false,
		i18n: {
			today: 'Hoje',
			clear: 'Limpar',
			cancel: 'Sair',
			done: 'Confirmar',
		}
	});
});

$(function(){

	$('#id_first_hour').timepicker({
		showCleanBtn: true,
		autoClose: false,
		twelveHour: false,
		i18n: {
			today: 'Hoje',
			clear: 'Limpar',
			cancel: 'Sair',
			done: 'Confirmar',
		}
	});
});

$(document).ready(function(){
    $('input.autocomplete').autocomplete({
      data: {
        "jQuery": null,
        "JavaScriptextsmstextsmstextsmstextsmstextsmstextsmstextsmst": 'https://www.jquery-az.com/wp-content/uploads/2017/12/favicon-32x32.png',
        "CSS": null,
        "HTML": null,
        "Bootstrap": 'https://www.jquery-az.com/wp-content/uploads/2017/12/favicon-32x32.png',
        "Java": null,
        "Python": null,
      },
    });
});