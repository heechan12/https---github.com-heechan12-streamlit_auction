from enum import Enum

class UserType(Enum):
    BUSINESS_GENERAL = "부동산 매매 사업자(일반)"
    BUSINESS_DUTY_FREE = "부동산 매매 사업자(면세)"
    NORMAL = "일반 매매"

class EstateLocation(Enum):
    NON_REGULATED = "비조정 지역"
    REGULATED = "조정 지역"

class RetentionPeriod(Enum):
    UNDER_1_YEAR = "1년 미만"
    BETWEEN_1_AND_2_YEARS = "1년 이상 2년 미만"
    OVER_2_YEARS = "2년 이상"