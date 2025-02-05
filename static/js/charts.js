document.addEventListener('DOMContentLoaded', function () {
    const historyData = window.historyData;
    console.log('Charts.js - History Data:', historyData);

    if (!historyData || !historyData.dates || !historyData.stock_data || !historyData.price_data) {
        console.error('Invalid history data structure:', historyData);
        return;
    }

    // Stock History Chart
    const stockCtx = document.getElementById('stockChart');
    if (!stockCtx) {
        console.error('Stock chart canvas not found');
        return;
    }

    new Chart(stockCtx, {
        type: 'line',
        data: {
            labels: historyData.dates,
            datasets: [{
                label: 'Stock Level',
                data: historyData.stock_data,
                borderColor: '#0d6efd',
                backgroundColor: 'rgba(13, 110, 253, 0.1)',
                tension: 0.1,
                fill: true
            }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: {
                    position: 'top',
                }
            },
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });

    // Price History Chart
    const priceCtx = document.getElementById('priceChart');
    if (!priceCtx) {
        console.error('Price chart canvas not found');
        return;
    }

    new Chart(priceCtx, {
        type: 'line',
        data: {
            labels: historyData.dates,
            datasets: [{
                label: 'Price ($)',
                data: historyData.price_data,
                borderColor: '#20c997',
                backgroundColor: 'rgba(32, 201, 151, 0.1)',
                tension: 0.1,
                fill: true
            }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: {
                    position: 'top',
                }
            },
            scales: {
                y: {
                    beginAtZero: true,
                    ticks: {
                        callback: function (value) {
                            return '$' + value.toFixed(2);
                        }
                    }
                }
            }
        }
    });
});

