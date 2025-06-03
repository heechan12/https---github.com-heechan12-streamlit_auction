def format_real_price(price: float) -> int:
    """
    소수점으로 입력받은 가격을 실제 가격 및 정수로 변환
    """
    if price is None:
        return 0
    return int(price * 100000000)


def format_comma_price(price: int) -> str:
    """
    입력받은 가격을 실제 가격으로 변경 및 콤마 추가
    """
    if price is None:
        print("입력 값이 없습니다")
        return "입력 값이 없습니다."
    formatted_price = format(int(price), ",")

    return formatted_price


def format_korean_won(price: int) -> str:
    """
    입력받은 가격을 한글로 변환
    """
    if price is None:
        print("입력 값이 없습니다")
        return "입력 값이 없습니다"
    price = price / 100000000
    eok = int(price)  # 정수부: 억
    cheon = int(round((price - eok), 3) * 10000)  # 소수부: 천 단위 계산

    result = ""
    if eok > 0:
        result += f"{eok}억"
    if cheon > 0:
        if result:
            result += " "
        result += f"{cheon:,}만원"  # 천 단위 콤마 추가 가능

    return result or "0 원"
