const faker = require('faker');

// Hàm để tạo URL thumb nail ngẫu nhiên
function generateThumbnailUrl() {
    const thumbnailUrls = [
        'https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.pinterest.com%2Fpin%2F302163456232813900%2F&psig=AOvVaw2_upTevL-wdVBpNHWDD9dh&ust=1716225867623000&source=images&cd=vfe&opi=89978449&ved=0CBIQjRxqFwoTCOiv-tqdmoYDFQAAAAAdAAAAABAE',
        'https://www.google.com/url?sa=i&url=https%3A%2F%2Fsec.edu.vn%2Fcung-nhin-90-bia-sach-dep-cute-nhat%2F&psig=AOvVaw2_upTevL-wdVBpNHWDD9dh&ust=1716225867623000&source=images&cd=vfe&opi=89978449&ved=0CBIQjRxqFwoTCOiv-tqdmoYDFQAAAAAdAAAAABAJ',
        'https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.canva.com%2Fvi_vn%2Fbia-sach%2Fmau%2F&psig=AOvVaw2_upTevL-wdVBpNHWDD9dh&ust=1716225867623000&source=images&cd=vfe&opi=89978449&ved=0CBIQjRxqFwoTCOiv-tqdmoYDFQAAAAAdAAAAABAU',
    ];
    // Chọn ngẫu nhiên một URL từ danh sách
    const randomIndex = Math.floor(Math.random() * thumbnailUrls.length);
    return thumbnailUrls[randomIndex];
}

// Hàm tạo lượt bán hàng tháng ngẫu nhiên
function generateMonthlySales() {
    const sales = {};
    const months = [
        'January', 'February', 'March', 'April', 'May', 'June', 
        'July', 'August', 'September', 'October', 'November', 'December'
    ];
    months.forEach(month => {
        sales[month] = faker.datatype.number({ min: 0, max: 100 });
    });
    return sales;
}

//Fake thông tin
function generateFakeBookData(id) {
    return {
        id: id,
        name: faker.lorem.words(),
        sales: faker.datatype.number({ min: 50, max: 500 }),
        price: faker.datatype.float({ min: 5, max: 20, precision: 0.01 }),
        publishDate: faker.date.past(5, new Date()).toISOString().split('T')[0],
        publisher: faker.company.companyName(),
        thumbnail_url: generateThumbnailUrl(),
        review_count: faker.datatype.number({ min: 10, max: 600 }),
        discount_rate: faker.datatype.number({ min: 0, max: 100 }),
        monthly_sales: generateMonthlySales() 
    };
}

// Số lượng sách
function generateFakeBooks(numBooks) {
    const books = [];
    for (let i = 1; i <= numBooks; i++) {
        books.push(generateFakeBookData(i));
    }
    return books;
}

// Generate 10 fake books
const books = generateFakeBooks(10);
// Hiển thị dữ liệu giả lập

module.exports = books;
