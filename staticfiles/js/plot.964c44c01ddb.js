var jumiaCanvas = $("#jumiaChart");
// jumiaCanvas.resize(function(){
//   this.width=100;
//   this.height=100;
// })
var avechiCanvas = $("#avechiChart");
var killmallCanvas = $("#killmallChart");
var jumiaPrice= document.getElementsByClassName('jumia-price');
var jumiaTime= document.getElementsByClassName('jumia-time');
var killmallPrice= document.getElementsByClassName('killmall-price');
var killmallTime= document.getElementsByClassName('killmall-time');
var avechiPrice= document.getElementsByClassName('avechi-price');
var avechiTime= document.getElementsByClassName('avechi-time');
jumia_price = [];jumia_time = [];killmall_price=[];killmall_time=[];
avechi_price = [];avechi_time=[];
for(i=0;i<jumiaPrice.length;i++){
  jumia_price.push(parseInt(jumiaPrice[i].innerHTML));
  jumia_time.push(jumiaTime[i].innerHTML);
}
for(i=0;i<killmallPrice.length;i++){
  killmall_price.push(parseInt(killmallPrice[i].innerHTML));
  killmall_time.push(killmallTime[i].innerHTML);
}
for(i=0;i<avechiPrice.length;i++){
  avechi_price.push(parseInt(avechiPrice[i].innerHTML));
  avechi_time.push(avechiTime[i].innerHTML);
}
/**median and other probabilistic distribution properties*/
if (jumia_price.length>0){
var jumia_median = math.median(jumia_price);
var jumia_mean = math.mean(jumia_price);
var jumia_std = math.std(jumia_price);
$('.mean').text(jumia_mean);
$('.median').text(jumia_median);
$('.std').text(jumia_std);


}
if (avechi_price.length>0){
var avechi_median = math.median(avechi_price);
var avechi_mean = math.mean(avechi_price);
var avechi_std = math.std(avechi_price);
$('.avechi-mean').text(avechi_mean);
$('.avechi-median').text(avechi_median);
$('.avechi-std').text(avechi_std);

}
if (killmall_price.length>0){
var killmall_median = math.median(killmall_price);
var killmall_mean = math.mean(killmall_price);
var killmall_std = math.std(killmall_price);
$('.killmall-mean').text(killmall_mean);
$('.killmall-median').text(killmall_median);
$('.killmall-std').text(killmall_std);

  
}




Chart.defaults.global.defaultFontFamily = "Lato";
Chart.defaults.global.defaultFontSize = 18;
var killmallData= {
    labels: killmall_time.reverse(),
  datasets: [{
    label: "Prices Shift at Killmall",
    data:killmall_price.reverse(),
    lineTension: 0.3,
    fill: false,
    borderColor: 'green',
    backgroundColor: 'transparent',
    pointBorderColor: 'green',
    pointBackgroundColor: 'lightgreen',
    pointRadius: 5,
    pointHoverRadius: 15,
    pointHitRadius: 30,
    pointBorderWidth: 2,
    pointStyle: 'rect'
    
  }]
  };

var avechiData = {
     labels: avechi_time.reverse(),
  datasets: [{
    label: "Prices Shift at Avechi",
    data:avechi_price.reverse(),
    lineTension: 0.3,
    fill: false,
    borderColor: 'red',
    backgroundColor: 'transparent',
    pointBorderColor: 'red',
    pointBackgroundColor: 'lightgreen',
    pointRadius: 5,
    pointHoverRadius: 15,
    pointHitRadius: 30,
    pointBorderWidth: 2,
    pointStyle: 'rect'
    
  }]
  };

// var speedData = {
//     label: "Car c - Speed (mph)",
//     data: [20, 23, 60, 60, 65, 30, 45],
//     lineTension: 0.3,   
//     fill: false,    
//     borderColor: 'purple',    
//     backgroundColor: 'transparent',    
//     pointBorderColor: 'purple',    
//     pointBackgroundColor: 'lightgreen',    
//     pointRadius: 5,    
//     pointHoverRadius: 15,    
//     pointHitRadius: 30,    
//     pointBorderWidth: 2
//   };

  var jumiaData = {
  labels: jumia_time.reverse(),
  datasets: [{
    label: "Prices Shift at Jumia",
    data: jumia_price.reverse(),
    lineTension: 0.3,   
    fill: true,  
    fillColor:'white',  
    borderColor: 'purple',    
    backgroundColor: 'transparent',    
    pointBorderColor: 'purple',    
    pointBackgroundColor: 'lightgreen',    
    pointRadius: 5,    
    pointHoverRadius: 15,    
    pointHitRadius: 30,    
    pointBorderWidth: 2,
    pointStyle: 'rect'
    
  }]
};

// var speedData = {
//   labels: jumia_time,
//   dataset: jumia_price
// };

var chartOptions = {
  legend: {
    display: true,
    position: 'top',
    labels: {
      boxWidth: 20,
      fontColor: 'black'
    }

  }
  // responsive: true,
  // maintainAspectRatio: true
};

var jumiaChart = new Chart(jumiaCanvas, {
  type: 'line',
  data: jumiaData,
  options: chartOptions
});
var killmallChart = new Chart(killmallCanvas, {
  type: 'line',
  data: killmallData,
  options: chartOptions
});
var avechiChart = new Chart(avechiCanvas, {
  type: 'line',
  data: avechiData,
  options: chartOptions
});
// function beforePrintHandler () {
//   for (var id in Chart.instances) {
//     Chart.instances[id].resize()
//   }
// }

// beforePrintHandler()