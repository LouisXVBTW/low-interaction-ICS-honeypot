
function makeChart(whatpie, piename, labels, data){
    var ctx = document.getElementById(whatpie);
    new Chart(ctx, {
        type: 'bar',
        data: {
            labels: labels,
            datasets: [{
                label: piename,
                backgroundColor: ['rgb(255, 99, 132)', 'rgb(52, 79, 235)', 'rgb(255, 64, 242)', 'rgb(255, 160, 64)', 'rgb(255, 239, 64)', 'rgb(64, 255, 140)', 'rgb(64, 255, 236)', 'rgb(188, 64, 255)', 'rgb(188, 64, 64)','rgb(46, 138, 0)','rgb(122, 21, 90)',],
                borderColor: ['rgb(255, 99, 132)', 'rgb(52, 79, 235)', 'rgb(255, 64, 242)', 'rgb(255, 160, 64)', 'rgb(255, 239, 64)', 'rgb(64, 255, 140)', 'rgb(64, 255, 236)', 'rgb(188, 64, 255)', 'rgb(188, 64, 64)','rgb(46, 138, 0)','rgb(122, 21, 90)',],
                data: data,
            }]
        },
        options: {
            plugins: {
                legend: {
                    display: true,
                    labels: {
                        color: ['rgb(255, 99, 132)', 'rgb(52, 79, 235)', 'rgb(255, 64, 242)', 'rgb(255, 160, 64)', 'rgb(255, 239, 64)', 'rgb(64, 255, 140)', 'rgb(64, 255, 236)', 'rgb(188, 64, 255)', 'rgb(188, 64, 64)','rgb(46, 138, 0)','rgb(122, 21, 90)',],
                    }
                }
            },
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });

}