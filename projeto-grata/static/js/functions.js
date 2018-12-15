function justNumbers(num) {
    var er = /[^0-9.]/;
    var field = num;

    er.lastIndex = 0;

    if (er.test(field.value)) {

          field.value = "";
    }
}

function justUser(word) {

    if(word.value != "Usuário") {

        word.value = "Usuário";
    }
}

document.addEventListener('DOMContentLoaded', function() {

    var elems = document.querySelectorAll('select');
    var instances = M.FormSelect.init(elems, options);
});