let tg = window.Telegram.WebApp;
tg.expand();

tg.MainButton.textColor = "#FFFFFF"
tg.MainButton.color = "#FC3005"

let btn1 = document.getElementById("btn1");
let btn2 = document.getElementById("btn2");
let btn3 = document.getElementById("btn3");
let btn4 = document.getElementById("btn4");
let btn5 = document.getElementById("btn5");
let btn6 = document.getElementById("btn6");


btn1.addEventListener("click", function () {
    tg.MainButton.setText("btn1 bosildi");
    tg.MainButton.show();
});


btn1.addEventListener("click", function () {
    tg.MainButton.setText("btn1 bosildi");
    tg.MainButton.show();
});
btn1.addEventListener("click", function () {
    tg.MainButton.setText("btn1 bosildi");
    tg.MainButton.show();
});
btn2.addEventListener("click", function () {
    tg.MainButton.setText("btn2 bosildi");
    tg.MainButton.show();
});
btn3.addEventListener("click", function () {
    tg.MainButton.setText("btn3 bosildi");
    tg.MainButton.show();
});
btn4.addEventListener("click", function () {
    tg.MainButton.setText("btn4 bosildi");
    tg.MainButton.show();
});
btn5.addEventListener("click", function () {
    tg.MainButton.setText("btn5 bosildi");
    tg.MainButton.show();
});
btn6.addEventListener("click", function () {
    tg.MainButton.setText("btn6 bosildi");
    tg.MainButton.show();
});

Telegram.WebApp.onEvent("mainButtonClicked", function () {
    tg.sendData("TestMessage")
});

