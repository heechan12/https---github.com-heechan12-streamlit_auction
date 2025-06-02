
def format_real_price(price: float) -> int :
    if price is None :
        return 0
    return int(price * 100000000)

# 가격을 정수 및 , 추가
def format_comma_price(price: float) -> str:
    if price is None:
        print("입력 값이 없습니다")
        return("입력 값이 없습니다.")
    price = price * 100000000
    formatted_price = format(int(price), ',')

    return formatted_price

def format_korean_won(price: float) -> str:
    if price is None:
        print("입력 값이 없습니다")
        return "입력 값이 없습니다"
    eok = int(price)  # 정수부: 억
    cheon = int((price - eok) * 10000)  # 소수부: 천 단위 계산

    result = ""
    if eok > 0:
        result += f"{eok}억"
    if cheon > 0:
        if result: result += " "
        result += f"{cheon:,}만원"  # 천 단위 콤마 추가 가능

    return result or "0원"