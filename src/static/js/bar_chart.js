const bar_config = {
    type: "bar",
    data: {
        labels: bar_labels,
        datasets: [{
            data: bar_data,
            hoverBorderWidth: 2,
            hoverBorderColor: "white",
            backgroundColor: 'greenyellow'
        }]
    },
    options: {
        responsive: false,
        layout: { padding: 10 },
        scales: {
            x: {ticks: {color: "white" }},
            y: {
                min: 50,
                ticks: {
                    stepSize: 5,
                    color: "white"
                }
            }
        },
        plugins: {legend: {display: false}}
    }
}

new Chart(document.getElementById("bar-chart"), bar_config);