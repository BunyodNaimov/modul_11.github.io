let tg = window.Telegram.WebApp;
tg.expand();

tg.MainButton.textColor = "#FFFFFF"
tg.MainButton.color = "#FC3005"

let rbtn1 = document.getElementById("rbtn1");
let abtn1 = document.getElementById("abtn1");


let item = " "
let n_count1 = 0


count1 = document.getElementById("count1");

abtn1.addEventListener("click", function () {
    count1.innerText = n_count1 += 1;
    count1.style.display = "inline-block";
    tg.MainButton.setText("Burger");
    tg.MainButton.show();
    item = "Burger/3$/"+count1.innerText;

})
rbtn1.addEventListener("click", function () {
    count1.innerText = n_count1 -= 1;
    count1.style.display = "inline-block";
    item = "Burger/3$/"+count1;
})


Telegram.WebApp.onEvent("mainButtonClicked", function () {
    tg.sendData(item);
});

