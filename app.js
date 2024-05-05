let tg = window.Telegram.WebApp;
tg.expand();

tg.MainButton.textColor = '#FFFFFF';
tg.MainButton.color = '#2cab37';


let btn = document.getElementById('btn')

btn.addEventListener("click", function () {
    tg.MainButton.setText("SMS jo'naytildi");
    tg.MainButton.show();

})