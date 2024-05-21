let data = []; // Khai báo biến data ở ngoài phạm vi hàm

document.addEventListener('DOMContentLoaded', function() {
  fetch('/data')
    .then(response => response.json())
    .then(fetchedData => {
      data = fetchedData; // Gán giá trị từ server vào biến data
      updateTable(data); // Cập nhật bảng với dữ liệu từ server
    })
    .catch(error => console.error('Error fetching data:', error));

  // Function to update table with given data
  const updateTable = (data) => {
    const table = document.getElementById('data-table');
    // Clear existing table data
    table.innerHTML = '';
    // Populate table with new data
    data.forEach(item => {
      const row = table.insertRow();
      const cellId = row.insertCell(0);
      const cellProductId = row.insertCell(1);
      cellId.textContent = item.id;
      cellProductId.textContent = item.product_id;
    });
  };

  // Function to handle search
  const handleSearch = (query) => {
    // Lọc dữ liệu theo query
    const filteredData = data.filter(item => {
      const productId = item.product_id.toLowerCase();
      return productId.includes(query.toLowerCase());
    });

    // Hiển thị danh sách ID tìm kiếm
    const searchResultsDiv = document.getElementById('search-results');
    searchResultsDiv.innerHTML = ''; // Xóa danh sách cũ trước khi hiển thị danh sách mới

    // Duyệt qua các sản phẩm đã lọc và hiển thị chúng trong dropdown list
    filteredData.forEach(item => {
      const resultItem = document.createElement('div');
      resultItem.textContent = item.product_id;
      resultItem.addEventListener('click', () => {
        document.getElementById('search-input').value = item.product_id; // Gán giá trị của sản phẩm đã chọn vào input search
        searchResultsDiv.innerHTML = ''; // Xóa danh sách kết quả tìm kiếm

        // Thực hiện tìm kiếm và cập nhật bảng
        updateTable(filteredData);

        // Ẩn danh sách kết quả tìm kiếm sau khi chọn sản phẩm
        searchResultsDiv.style.display = 'none';
      });
      searchResultsDiv.appendChild(resultItem);
    });
  };

  // Event listener for search input
  const searchInput = document.getElementById('search-input');
  searchInput.addEventListener('input', () => handleSearch(searchInput.value));

  // Event listener to hide search results when mouse leaves the search results list
  const searchResultsDiv = document.getElementById('search-results');
  searchResultsDiv.addEventListener('mouseleave', () => {
    searchResultsDiv.innerHTML = ''; // Ẩn danh sách kết quả tìm kiếm
  });
});
