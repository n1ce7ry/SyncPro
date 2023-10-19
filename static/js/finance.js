var speedCanvas = document.getElementById("speedChart");

var speedData = {
    labels: ["Пн", "Вт", "Ср", "Чт", "Пт", "Сб"],
    datasets: [{
        label: "Доходы за неделю",
        data: [1000, 5000, 12000, 10000, 5000, 8000],
    }]
};

var chartOptions = {
    legend: {
        display: true,
        position: 'top',
        labels: {
            boxWidth: 80,
            fontColor: 'black'
        }
    }
};

var lineChart = new Chart(speedCanvas, {
    type: 'line',
    data: speedData,
    options: chartOptions
});
