document.addEventListener("DOMContentLoaded", () => {
    echarts.init(document.querySelector("#providerChart")).setOption({
      tooltip: {
        trigger: 'item'
      },
      legend: {
        top: '5%',
        left: 'center'
      },
      series: [{
        name: 'Access From',
        type: 'pie',
        radius: ['40%', '70%'],
        avoidLabelOverlap: false,
        label: {
          show: false,
          position: 'center'
        },
        emphasis: {
          label: {
            show: true,
            fontSize: '18',
            fontWeight: 'bold'
          }
        },
        labelLine: {
          show: false
        },
        data: [{
            value: 1048,
            name: 'Nhà sách Fahasa'
          },
          {
            value: 735,
            name: 'Nhà sách Vĩnh Thụy'
          },
          {
            value: 580,
            name: 'Bamboo Books'
          },
          {
            value: 484,
            name: 'Nhà sách ABC'
          },
          {
            value: 300,
            name: 'Khác'
          }
        ]
      }]
    });
  });