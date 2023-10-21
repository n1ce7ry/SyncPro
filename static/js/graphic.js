function getRandomColor() {
    var letters = '0123456789ABCDEF';
    var color = '#';
    for (var i = 0; i < 6; i++) {
        color += letters[Math.floor(Math.random() * 16)];
    }
    return color;
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

    var oilCanvas = document.getElementById("oilChart");

    var ctx = document.getElementById('myChart');


    var oilData = {
        labels: [
            "Пн",
            "Вт",
            "Ср",
            "Чт",
            "Пт",
            "Сб"
        ],
        datasets: [
            {
                data: [10, 2, 3, 4, 7, 9],
                backgroundColor: [
                    "#FF6384",
                    "#63FF84",
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
            labels: ['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб'],
            datasets: [{
                label: 'Заявки за неделю',
                data: [12, 19, 3, 5, 2, 3],
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