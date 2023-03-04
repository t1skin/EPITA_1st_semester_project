const pie_config = {
    type: "pie",
    data: {
        labels: pie_labels,
        datasets: [{
            data: pie_data,
            borderWidth: 2,
            hoverOffset: 30,
            hoverBorderWidth: 0,  
        }]
    },
    options: {
        responsive: false,   
        layout: { padding: 10 },
        plugins: {
            legend: {
                position: "right",
                labels: {
                    padding: 20,                
                    boxWidth: 20,
                    boxHeight: 20,
                    color: "greenyellow",
                    font: { size: 18 }
                }
            }
        }
    }
}

new Chart(document.getElementById("pie-chart"), pie_config);