var myChartObject = document.getElementById("myChart");

var chart = new Chart(myChartObject,{

    type: "pie",
    data: {
        labels:["Red", "Blue"],
        dataset: [{
            label: "Nummer 1",
        }]
    }
})