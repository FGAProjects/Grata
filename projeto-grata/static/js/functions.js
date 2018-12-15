function justNumbers(num) {
    var er = /[^0-9.]/;
    var field = num;

    er.lastIndex = 0;

    if (er.test(field.value)) {

          field.value = "";
    }
}