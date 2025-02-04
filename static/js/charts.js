document.addEventListener('DOMContentLoaded', function() {
    // Sample data for charts
    const dates = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'];
    const stockData = [100, 85, 120, 75, 90, 110];
    const priceData = [9.99, 9.99, 10.99, 10.99, 11.99, 11.99];

    // Stock History Chart
    const stockCtx = document.getElementById('stockChart').getContext('2d');
    new Chart(stockCtx, {
        type: 'line',
        data: {
            labels: dates,
            datasets: [{
                label: 'Stock Level',
                data: stockData,
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
    const priceCtx = document.getElementById('priceChart').getContext('2d');
    new Chart(priceCtx, {
        type: 'line',
        data: {
            labels: dates,
            datasets: [{
                label: 'Price ($)',
                data: priceData,
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
                        callback: function(value) {
                            return '$' + value.toFixed(2);
                        }
                    }
                }
            }
        }
    });
});
