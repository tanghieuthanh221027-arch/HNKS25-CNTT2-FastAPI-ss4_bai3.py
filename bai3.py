from fastapi import FastAPI, HTTPException

app = FastAPI()

products = [
    {"id": 1, "name": "Laptop", "price": 15000000},
    {"id": 2, "name": "Mouse", "price": 200000},
    {"id": 3, "name": "Keyboard", "price": 500000},
    {"id": 4, "name": "Monitor", "price": 3000000}
]

@app.get("/products")
def get_products(keyword: str = None, max_price: float = None):

    if max_price is not None and max_price < 0:
        raise HTTPException(
            status_code=400,
            detail="max_price không được âm"
        )

    result = products

    if keyword:
        found = []

        for product in result:
            if keyword.lower() in product["name"].lower():
                found.append(product)

        result = found

    if max_price is not None:
        filtered = []

        for product in result:
            if product["price"] <= max_price:
                filtered.append(product)

        result = filtered

    return {
        "data": result
    }

# input : API sử dụng : GET / products , 2 query parameter là keyword và max_price và danh sách sản phẩm
# output mong muốn : 
# #Nếu không truyền query parameter nào, hệ thống trả về toàn bộ sản phẩm
# #Nếu truyền keyword, hệ thống chỉ trả về sản phẩm có tên chứa từ khóa đó
# #Việc tìm kiếm theo keyword không phân biệt chữ hoa, chữ thường
# #Nếu truyền max_price, hệ thống chỉ trả về sản phẩm có price <= max_price , có kiểm tra và bắt lỗi
# #Nếu truyền cả keyword và max_price, sản phẩm trả về phải thỏa mãn cả hai điều kiện

# đề xuất và các bước giải quyết bài toán : kiểm tra max_price <0 ? có thì trả lỗi , không thì trả về toàn bộ danh sách -> nếu người dùng truyền keyword thì xử lý tìm không phân biệt hoa thường -> nếu người dùng truyền vào max_price hợp lệ thì xử lý lọc theo giá <= max_price -> hiển thị kết quả