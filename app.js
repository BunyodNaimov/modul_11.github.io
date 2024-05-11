let tg = window.Telegram.WebApp;
tg.expand();

tg.MainButton.textColor = "#FFFFFF"
tg.MainButton.color = "#FC3005"

let btn1 = document.getElementById("btn1");
let btn2 = document.getElementById("btn2");
let btn3 = document.getElementById("btn3");
let btn4 = document.getElementById("btn4");

let item = " "
let num = 1


btn1.addEventListener("click", function () {
    tg.MainButton.setText("Burger "+ num);
    item = "Burger/3$";
    tg.MainButton.show();
});
btn2.addEventListener("click", function () {
    tg.MainButton.setText("KFC");
    item = "KFC/10$";
    tg.MainButton.show();
});
btn3.addEventListener("click", function () {
    tg.MainButton.setText("LAVASH");
    item = "LAVASH/4$";
    tg.MainButton.show();
});
btn4.addEventListener("click", function () {
    tg.MainButton.setText("Pizza");
    item = "Pizza/5$";

    tg.MainButton.show();
});

Telegram.WebApp.onEvent("mainButtonClicked", function () {
    tg.sendData(item);
});

