let opAdded = false;
let dark = true;
let untouched = true;
let negated = false;

document.body.onkeypress( (e) => {
    kbControl(e);
})

function kbControl(event) {
    console.log(event.keyCode);
    var char = event.which || event.keyCode;
    if(char >= 48 && char <= 57){
        btnClick(char - 48);
    } else if(char == 43) {
        btnClick('+'); // +
    } else if(char == 45) {
        btnClick('-'); // -
    } else if(char == 42) {
        btnClick('*'); // *
    } else if(char == 47) {
        btnClick('/');
    }// /
    // else if()
    else if(char == 13){
        document.getElementById("myForm").submit();
    }
}

function clearScreen(){
    console.log("CLEARED");
    document.getElementById("user-input").innerHTML= "";
    document.getElementById("input-form").value= "";
    opAdded = false;
}

function btnClick(digit) {
    if(digit == '+' || digit == '-' || digit == '*' ||digit == '/' || digit == '%') {
        if(untouched){
            return;
        }
        if(opAdded) {
            return;
        }
        opAdded = true;
    } else if(digit == '.'){
        bits = document.querySelector("#input-form").value.split(/([+\-*/%+])/);
        if(bits[bits.length - 1].split('.').length > 1){
            return;
        }
    }
    if(untouched){
        clearScreen();
        untouched = false;
    }
    document.querySelector("#user-input").innerHTML += digit;
    document.querySelector("#input-form").value += digit;
}

function toggleLightDark(e) {

    e.preventDefault();
    
    if(dark){
        document.querySelector('#myForm').className = "calc light";
    } else {
        document.querySelector('#myForm').className = "calc dark";
    }
    dark = !dark;
}

function removeone() {
    let str = document.querySelector("#user-input").innerHTML;
    let digits = str.split('');
    digits.pop();
    document.querySelector("#user-input").innerHTML = digits.join('');
    document.querySelector("#input-form").value = digits.join('');
}

function negate() {
    if(!negated){
        negated = true;
        document.querySelector("#negate").value = true;
        let digits = ['-', '('];
        let str = document.querySelector("#user-input").innerHTML;
        let s = str.split('');
        digits = digits.concat(s);
        digits.push(')');
        document.querySelector("#user-input").innerHTML = digits.join('');
    } else {
        negated = false;
        document.querySelector("#negate").value = false;
        let str = document.querySelector("#user-input").innerHTML;
        let s = str.split('');
        s.shift();
        s.shift();
        s.pop();
        document.querySelector("#user-input").innerHTML = s.join('');
    }
}