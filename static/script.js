let chart1, chart2, chart3, chart4;
console.log(data);
document.addEventListener("DOMContentLoaded", function() {

    // Km y Prices
    const km = data.training_data.map(pair => pair[0]);
    const prices = data.training_data.map(pair => pair[1]);
    const lr_info = data.regression_line
    const scaling = data.scaling

    loadDataGraphic(km, prices);
    loadPredictionGraphic(km, prices, lr_info, scaling);
    loadLossGraphic(km, prices, lr_info, scaling);
    loadNewPrediction(km, prices, lr_info, scaling);
});

function loadDataGraphic(km, prices) {
    const ctx = document.getElementById("graphic").getContext("2d");

    if (chart1) {
        chart1.destroy();
    }

    chart1 = new Chart(ctx, {
        type: 'scatter',
        data: {
            datasets: [{
                label: data.title,
                data: km.map((k, i) => ({ x: k, y: prices[i] })),
                backgroundColor: 'rgba(75, 192, 192, 0.6)',
                borderColor: 'rgba(75, 192, 192, 1)',
                pointRadius: 5
            }]
        },
        options: {
            responsive: true,
            plugins: {
                tooltip: {
                    callbacks: {
                        label: function(context) {
                            const x = context.raw.x;
                            const y = context.raw.y;
                            return `${data.description.x_title}: ${x}, ${data.description.y_title}${y}`;
                        }
                    }
                },
                legend: {
                    display: false
                }
            },
            scales: {
                x: {
                    title: {
                        display: true,
                        text: data.description.x_title
                    }
                },
                y: {
                    title: {
                        display: true,
                        text: data.description.y_title
                    }
                }
            }
        }
    });
}

function loadPredictionGraphic(km, prices, lr_info, scaling) {
    const ctx2 = document.getElementById("graphic2").getContext("2d");

    let { regressionLine, _ } = computeLinearRegression(km, lr_info, scaling);

    if (chart2) {
        chart2.destroy();
    }

    chart2 =  new Chart(ctx2, {
        type: 'scatter',
        data: {
            datasets: [
                {
                    label: 'Data',
                    data: km.map((k, i) => ({ x: k, y: prices[i] })),
                    backgroundColor: 'rgba(75, 192, 192, 0.6)',
                },
                {
                    label: 'Regression Line',
                    type: 'line',
                    data: regressionLine,
                    borderColor: 'rgba(255, 99, 132, 1)',
                    backgroundColor: 'rgba(255, 99, 132, 0.3)',
                    borderWidth: 2,
                    fill: false,
                    pointRadius: 0
                }
            ]
        },
        options: {
            responsive: true,
            plugins: { legend: { position: 'top' } },
            scales: {
                x: { title: { display: true, text: data.description.x_title } },
                y: { title: { display: true, text: data.description.y_title } }
            }
        }
    });
}

function loadLossGraphic(km, prices, lr_info, scaling) {
    const ctx3 = document.getElementById("graphic3").getContext("2d");

    let { regressionLine, predictedPrices } = computeLinearRegression(km, lr_info, scaling);

    if (chart3) {
        chart3.destroy();
    }
    chart3 = new Chart(ctx3, {
        type: 'scatter',
        data: {
            datasets: [
                {
                    label: 'Datos Reales',
                    data: km.map((k, i) => ({ x: k, y: prices[i] })),
                    backgroundColor: 'rgba(75, 192, 192, 0.6)',
                },
                {
                    label: 'Recta de Regresión',
                    type: 'line',
                    data: regressionLine,
                    borderColor: 'rgba(255, 99, 132, 1)',
                    borderWidth: 2,
                    fill: false,
                    pointRadius: 0
                },
                // Crear líneas verticales como segmentos
                ...km.map((k, i) => ({
                    label: `Error punto ${i+1}`,
                    type: 'line',
                    data: [
                        { x: k, y: prices[i] },
                        { x: k, y: predictedPrices[i] }
                    ],
                    borderColor: 'rgba(255, 205, 86, 0.8)',
                    borderWidth: 1,
                    pointRadius: 0,
                    showLine: true
                }))
            ]
        },
        options: {
            responsive: true,
            plugins: { legend: { display: false } },
            scales: {
                x: { title: { display: true, text: data.description.x_title } },
                y: { title: { display: true, text: data.description.y_title } }
            }
        }
    });
}

function computeLinearRegression(km, lr_info, scaling) {
    const a_scaled = lr_info.intercept;
    const b_scaled = lr_info.slope;

    const a_real = (a_scaled * scaling.y_std) / scaling.x_std;
    const b_real = b_scaled * scaling.y_std + scaling.y_mean - a_real * scaling.x_mean;

    const predictedPrices = km.map(x => a_real * x + b_real);

    const minKm = Math.min(...km);
    const maxKm = Math.max(...km);
    const regressionLine = [
        {x: minKm, y: a_real * minKm + b_real},
        {x: maxKm, y: a_real * maxKm + b_real}
    ]

    return { regressionLine, predictedPrices };
}

function loadNewPrediction(km, prices, lr_info, scaling) {
    const ctx4 = document.getElementById("graphic4").getContext("2d");

    let { regressionLine, _ } = computeLinearRegression(km, lr_info, scaling);

    if (chart4) {
        chart4.destroy();
    }

    // If there's a prediction, get the predicted point
    let predictedPoint = null;
    if (data.predicted_price !== null) {
        predictedPoint = { x: data.input_km, y: data.predicted_price };
    }

    chart4 = new Chart(ctx4, {
        type: 'scatter',
        data: {
            datasets: [
                {
                    label: 'Data',
                    data: km.map((k, i) => ({ x: k, y: prices[i] })),
                    backgroundColor: 'rgba(75, 192, 192, 0.6)',
                },
                {
                    label: 'Regression Line',
                    type: 'line',
                    data: regressionLine,
                    borderColor: 'rgba(255, 99, 132, 1)',
                    backgroundColor: 'rgba(255, 99, 132, 0.3)',
                    borderWidth: 2,
                    fill: false,
                    pointRadius: 0
                },
                // If there is a predicted point, add it to the chart
                predictedPoint ? {
                    label: 'Predicted Point',
                    data: [predictedPoint],
                    backgroundColor: 'rgba(255, 159, 64, 1)',
                    borderColor: 'rgba(255, 159, 64, 1)',
                    pointRadius: 6
                } : {}
            ]
        },
        options: {
            responsive: true,
            plugins: { legend: { position: 'top' } },
            scales: {
                x: { title: { display: true, text: data.description.x_title } },
                y: { title: { display: true, text: data.description.y_title } }
            }
        }
    });
}