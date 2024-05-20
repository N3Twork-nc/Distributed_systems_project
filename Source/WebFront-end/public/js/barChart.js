document.addEventListener("DOMContentLoaded", () => {

  // Biểu đồ cột lượt bán sản phẩm
  new Chart(document.querySelector('#barChart1'), {
    type: 'bar',
    data: {
      labels: ['Art & Photography', 'Biographies & Memoirs', 'Business & Economics', 'How-to - Self Help', 'Childrens Books', 'Dictionary', 'Education-Teaching', 'Fiction-Literature', 'Magazines', 'Medical Books', 'Parenting & Relationships', 'Reference','Science-Technology', 'History, Politics & Social Sciences', 'Travel & Holiday', 'Cookbooks, Food & Wine'],
      datasets: [{
        label: 'Thống kê theo số lượng',
        data:  [65, 59, 80, 81, 56, 55, 40, 72, 66, 75, 64, 60, 66, 75, 64, 60],
        backgroundColor: [
          'rgba(255, 99, 132, 0.2)',
          'rgba(255, 159, 64, 0.2)',
          'rgba(255, 205, 86, 0.2)',
          'rgba(75, 192, 192, 0.2)',
          'rgba(54, 162, 235, 0.2)',
          'rgba(153, 102, 255, 0.2)',
          'rgba(201, 203, 207, 0.2)',
          'rgba(95, 158, 160, 0.2)',
          'rgba(139, 0, 139, 0.2)',
          'rgba(210, 105, 30, 0.2)',
          'rgba(128, 0, 0, 0.2)',
          'rgba(218, 165, 32, 0.2)',
          'rgba(139, 69, 19, 0.2)',
          'rgba(0, 128, 128, 0.2)',
          'rgba(70, 130, 180, 0.2)',
          'rgba(0, 0, 128, 0.2)',
          'rgba(47, 79, 79, 0.2)',
          'rgba(255, 0, 0, 0.2)',
          'rgba(255, 140, 0, 0.2)',
          'rgba(255, 20, 147, 0.2)',
          'rgba(128, 0, 128, 0.2)',
          'rgba(0, 255, 255, 0.2)',
          'rgba(30, 144, 255, 0.2)',
          'rgba(0, 255, 0, 0.2)'
        ],
        borderColor: [
          'rgba(255, 99, 132, 1)',
          'rgba(255, 159, 64, 1)',
          'rgba(255, 205, 86, 1)',
          'rgba(75, 192, 192, 1)',
          'rgba(54, 162, 235, 1)',
          'rgba(153, 102, 255, 1)',
          'rgba(201, 203, 207, 1)',
          'rgba(95, 158, 160, 1)',
          'rgba(139, 0, 139, 1)',
          'rgba(210, 105, 30, 1)',
          'rgba(128, 0, 0, 1)',
          'rgba(218, 165, 32, 1)',
          'rgba(139, 69, 19, 1)',
          'rgba(0, 128, 128, 1)',
          'rgba(70, 130, 180, 1)',
          'rgba(0, 0, 128, 1)',
          'rgba(47, 79, 79, 1)',
          'rgba(255, 0, 0, 1)',
          'rgba(255, 140, 0, 1)',
          'rgba(255, 20, 147, 1)',
          'rgba(128, 0, 128, 1)',
          'rgba(0, 255, 255, 1)',
          'rgba(30, 144, 255, 1)',
          'rgba(0, 255, 0, 1)'
        ],        
        borderWidth: 1
      }]
    },
    options: {
      scales: {
        y: {
          beginAtZero: true
        }
      }
    }
  });

    // Biểu đồ cột lượt truy cập
    new Chart(document.querySelector('#barChart2'), {
      type: 'bar',
      data: {
        labels: ['Sách văn học', 'Sách kinh tế', 'Sách thiếu nhi', 'Sách kỹ năng sống', 'Nuôi dạy con', 'Sách Giáo Khoa-Giáo Trình', 'Sách Học Ngoại Ngữ', 'Sách Tham Khảo', 'Từ Điển', 'Sách Kiến Thức Tổng Hợp', 'Sách Khoa Học-Kỹ Thuật', 'Sách Lịch sử', 'Điện Ảnh-Nhạc-Họa', 'Truyện Tranh, Manga, Comic', 'Sách Tôn Giáo-Tâm Linh', 'Sách Văn Hóa-Địa Lý-Du Lịch', 'Sách Chính Trị-Pháp Lý', 'Sách Nông-Lâm-Ngư Nghiệp', 'Sách Công Nghệ Thông Tin', 'Sách Y Học', 'Tạp Chí-Catalogue', 'Sách Tâm lý-Giới tính', 'Sách Thường Thức-Gia Đình', 'Thể Dục-Thể Thao'],
        datasets: [{
          label: 'Thống kê theo số lượng',
          data: [65, 59, 80, 81, 56, 55, 40, 72, 66, 75, 64, 60, 65, 59, 80, 81, 56, 55, 40, 72, 66, 75, 64, 60],
          backgroundColor: [
            'rgba(255, 99, 132, 0.2)',
            'rgba(255, 159, 64, 0.2)',
            'rgba(255, 205, 86, 0.2)',
            'rgba(75, 192, 192, 0.2)',
            'rgba(54, 162, 235, 0.2)',
            'rgba(153, 102, 255, 0.2)',
            'rgba(201, 203, 207, 0.2)',
            'rgba(95, 158, 160, 0.2)',
            'rgba(139, 0, 139, 0.2)',
            'rgba(210, 105, 30, 0.2)',
            'rgba(128, 0, 0, 0.2)',
            'rgba(218, 165, 32, 0.2)',
            'rgba(139, 69, 19, 0.2)',
            'rgba(0, 128, 128, 0.2)',
            'rgba(70, 130, 180, 0.2)',
            'rgba(0, 0, 128, 0.2)',
            'rgba(47, 79, 79, 0.2)',
            'rgba(255, 0, 0, 0.2)',
            'rgba(255, 140, 0, 0.2)',
            'rgba(255, 20, 147, 0.2)',
            'rgba(128, 0, 128, 0.2)',
            'rgba(0, 255, 255, 0.2)',
            'rgba(30, 144, 255, 0.2)',
            'rgba(0, 255, 0, 0.2)'
          ],
          borderColor: [
            'rgb(255, 99, 132)',
            'rgb(255, 159, 64)',
            'rgb(255, 205, 86)',
            'rgb(75, 192, 192)',
            'rgb(54, 162, 235)',
            'rgb(153, 102, 255)',
            'rgb(201, 203, 207)',
            'rgb(95, 158, 160)',
            'rgb(139, 0, 139)',
            'rgb(210, 105, 30)',
            'rgb(128, 0, 0)',
            'rgb(218, 165, 32)',
            'rgb(139, 69, 19)',
            'rgb(0, 128, 128)',
            'rgb(70, 130, 180)',
            'rgb(0, 0, 128)',
            'rgb(47, 79, 79)',
            'rgb(255, 0, 0)',
            'rgb(255, 140, 0)',
            'rgb(255, 20, 147)',
            'rgb(128, 0, 128)',
            'rgb(0, 255, 255)',
            'rgb(30, 144, 255)',
            'rgb(0, 255, 0)'
          ],          
          borderWidth: 1
        }]
      },
      options: {
        scales: {
          y: {
            beginAtZero: true
          }
        }
      }
    });
  });
  