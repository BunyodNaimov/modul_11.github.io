let tg = window.Telegram.WebApp;
tg.expand();

tg.MainButton.textColor = "#FFFFFF"
tg.MainButton.color = "#FC3005"

let rbtn1 = document.getElementById("rbtn1");
let abtn1 = document.getElementById("abtn1");

let rbtn2 = document.getElementById("rbtn2");
let abtn2 = document.getElementById("abtn2");

let rbtn3 = document.getElementById("rbtn3");
let abtn3 = document.getElementById("abtn3");

let rbtn4 = document.getElementById("rbtn4");
let abtn4 = document.getElementById("abtn4");

let item = " "
let num_count = 0

number = document.getElementById("count");

abtn1.addEventListener("click", function () {

    number.innerText = num_count += 1;
    number.style.display = "block";
})


btn1.addEventListener("click", function () {
    tg.MainButton.setText("Burger " + num);
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

