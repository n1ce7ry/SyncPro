function getRandomColor() {
    var letters = '0123456789ABCDEF';
    var color = '#';
    for (var i = 0; i < 6; i++) {
        color += letters[Math.floor(Math.random() * 16)];
    }
    return color;
}

function loadJson(selector) {
    return JSON.parse(document.querySelector(selector).getAttribute('data-json'));
}

document.addEventListener("DOMContentLoaded", function () {
    var avatars = document.getElementsByClassName("avatar");
    console.log(avatars)
    for (var i = 0; i < avatars.length; i++) {
        var avatar = avatars[i];
        avatar.style.backgroundColor = getRandomColor();
    }
});

window.onload = function () {

    var finance = loadJson('#FinanceJsonData');
    var application = loadJson('#ApplicationJsonData');

    var finance_data = finance.map((item) => item.count);
    var finance_labels = finance.map((item) => item.day);

    var application_data = application.map((item) => item.count);
    var application_labels = application.map((item) => item.day);

    var oilCanvas = document.getElementById("oilChart");

    var ctx = document.getElementById('myChart');

    var oilData = {
        labels: finance_labels,
        datasets: [
            {
                data: finance_data,
                backgroundColor: [
                    "#FF6384",
                    "#524abb",
                    "#84FF63",
                    "#8463FF",
                    "#6384FF",
                    "#c5544d"
                ]
            }]
    };

    var pieChart = new Chart(oilCanvas, {
        type: 'doughnut',
        data: oilData
    });


    new Chart(ctx, {
        type: 'bar',
        data: {
            labels: application_labels,
            datasets: [{
                label: 'Заявки за неделю',
                data: application_data,
                borderWidth: 1,
                backgroundColor: '#524abb',
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
}