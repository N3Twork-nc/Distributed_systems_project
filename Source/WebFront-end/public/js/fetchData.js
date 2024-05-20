fetch('/fakeData')
  .then(response => response.json())
  .then(data => {
    // Get the corresponding elements on the webpage
    const bookNameElement = document.getElementById('bookName');
    const bookPriceElement = document.getElementById('bookPrice');
    const bookSaleElement = document.getElementById('bookSales')
    const bookPublisherElement = document.getElementById('bookPublisher');
    const bookReviewElement = document.getElementById('bookReview');
    const bookDiscountElement = document.getElementById('bookDiscount');

    const book = data[0];
    bookNameElement.textContent = book.name;
    bookPriceElement.textContent = book.price.toFixed(2) + "₫";
    bookSaleElement.textContent = book.sales;
    bookPublisherElement.textContent = book.publisher;
    bookReviewElement.textContent = book.review_count;
    bookDiscountElement.textContent = book.discount_rate;

  })
  .catch(error => {
    console.error('Error fetching data:', error);
  });
