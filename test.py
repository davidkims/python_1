import requests

# 상품 데이터베이스
products = [
    {"id": 1, "name": "컴퓨터", "price": 1000000, "stock": 10},
    {"id": 2, "name": "스마트폰", "price": 500000, "stock": 20},
    {"id": 3, "name": "태블릿", "price": 700000, "stock": 5},
]

# 장바구니
cart = []

def search_product():
    """
    상품을 검색하는 함수
    """
    keyword = input("검색어를 입력하세요: ")
    result = []
    for product in products:
        if keyword in product['name']:
            result.append(product)
    if len(result) == 0:
        print("검색 결과가 없습니다.")
    else:
        for product in result:
            print(product)

def add_to_cart():
    """
    장바구니에 상품을 추가하는 함수
    """
    product_id = int(input("상품 ID를 입력하세요: "))
    product = None
    for p in products:
        if p['id'] == product_id:
            product = p
            break
    if product is None:
        print("상품을 찾을 수 없습니다.")
        return
    if product['stock'] == 0:
        print("상품의 재고가 없습니다.")
        return
    cart.append(product)
    product['stock'] -= 1
    print("장바구니에 추가되었습니다.")

def view_cart():
    """
    장바구니를 보여주는 함수
    """
    if len(cart) == 0:
        print("장바구니가 비어 있습니다.")
    else:
        for product in cart:
            print(product)

def checkout():
    """
    결제 처리 함수
    """
    total_price = 0
    for product in cart:
        total_price += product['price']
    print("총 결제 금액: ", total_price)
    answer = input("결제를 진행하시겠습니까? (Y/N)")
    if answer == 'Y':
        response = requests.post('http://payment-api.com/pay', {'amount': total_price})
        if response.status_code == 200:
            print("결제가 완료되었습니다.")
            cart.clear()
        else:
            print("결제에 실패하였습니다.")

# 메인 메뉴
while True:
    print("1. 상품 검색")
    print("2. 장바구니 보기")
    print("3. 결제하기")
