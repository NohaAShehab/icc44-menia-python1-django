spans = document.querySelectorAll('span');
for (var j = 0; j < spans.length; j++) {
    spans[j].classList.add('d-block');
}


labels = document.querySelectorAll('label');

for (var i = 0; i < labels.length; i++) {
    labels[i].classList.add('form-label');
}

inputs = document.querySelectorAll('input');
for (var i = 0; i < inputs.length; i++) {
    inputs[i].classList.add('form-control');
}
selects= document.querySelectorAll('select');
console.log(selects);
for(var j=0; j< selects.length; j++) {
    selects[j].classList.add('form-control');
}

divs = document.getElementsByClassName("form_element")
for (var d =0; d < divs.length; d++){
    divs[d].classList.add('mb-3')
}

checkboxex=document.querySelectorAll('input[type="checkbox"]')
for (var d =0; d < checkboxex.length; d++){
    checkboxex[d].classList.remove('form-control')
}

// document.querySelector("form").addEventListener("submit", function () {
//
// });


    errors = document.querySelectorAll('ul.errorlist')
for (var m=0 ; m < errors.length; m ++){
    errors[m].style = 'color:red; font-weight: bold';
}