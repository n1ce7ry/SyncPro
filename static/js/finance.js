function loadJson(selector) {
    return JSON.parse(document.querySelector(selector).getAttribute('data-json'));
}

var jsonData = loadJson('#jsonData');

var data = jsonData.map((item) => item.count);
var labels = jsonData.map((item) => item.day);

var speedCanvas = document.getElementById("speedChart");

var speedData = {
    labels: labels,
    datasets: [{
        label: "Доходы за неделю",
        data: data,
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
