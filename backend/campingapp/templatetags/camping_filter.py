from django import template

register = template.Library()


@register.filter(name="ground_on")
def re_ground_on(value):
    if value == "T":
        return "접지"
    elif value == "F":
        return "접지x"
    elif value == "ETC":
        return "모름"


# 반려동물: [("T", "가능"), ("F", "불가"), ("ETC", "모름")]
@register.filter(name="with_animal")
def re_with_animal(value):
    if value == "T":
        return "가능"
    elif value == "F":
        return "불가능"
    elif value == "ETC":
        return "모름"


# 뷰 종류
@register.filter(name="kind_of_view")
def re_kind_of_view(value):
    if value == "forest":
        return "숲쀼"
    elif value == "ocean":
        return "오션뷰~~~ ~"
    elif value == "lake":
        return "호수뷰~~~!!!"
    elif value == "simple":
        return "시설맛집!!!"
    elif value == "shit":
        return "똥뷰!!"
    elif value == "etc":
        return "그외!"


# 캠퍼 타입
@register.filter(name="kind_of_camper")
def re_kind_of_camper(value):
    if value == "roud":
        return "시끄러워 아오 눈치 보이네"
    elif value == "quiet":
        return "굿 아주 조용해"
    elif value == "normal":
        return "이정도면 꽤 괜찮네"


# 캠프파이어 가능
@register.filter(name="can_fire")
def re_can_fire(value):
    if value == "T":
        return "오얘 불피우기 가능"
    elif value == "F":
        return "아오 불피우기 안되네"
    elif value == "etc":
        return "모르겠네"


# 날짜
@register.filter(name="visited_at")
def re_visited_at(value):
    date = value.strftime("%Y년 %m월 %d일")
    return date
