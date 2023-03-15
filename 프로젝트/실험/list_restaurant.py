def select_genre():
    while True:
        var = input("\n한식, 중식, 일식, 양식, 기타 중에 입력하세요:")
        if var in ("한식", "중식", "일식", "양식", "기타"):
            break
        else:
            print("다시 입력해주세요.")
    return var
​
def view_menu_list():
    while True:
        var = input("""
메뉴를 보고 싶으시다면 Y, y, 예를 써주시고
안 봐도 되시면 N, n, 아니오를 써주세요.""")
        if var == "Y" or var == "y" or var == "예":
            print("\n한식은 ", ', '.join(menu_list["한식"]), "이 있습니다.\n")
            print("중식은 ", ', '.join(menu_list["중식"]), "이 있습니다.\n")
            print("일식은 ", ', '.join(menu_list["일식"]), "이 있습니다.\n")
            print("양식은 ", ', '.join(menu_list["양식"]), "이 있습니다.\n")
            print("기타는 ", ', '.join(menu_list["기타"]),"이 있습니다.")
            break
        elif var == "N" or var == "n" or var == "아니오":
            break
        else:
            print("다시 입력해주세요")
​
​
menu_list = {"한식":["덮밥", "비빔밥", "볶음밥", "김치찌개", "부대찌개", 
                    "생선찜", "생선구이", "냉면", "설렁탕", 
                   "분식(김밥&떡볶이&순대)"],
              "중식":["짜장&짬뽕", "마라탕"],
             "일식":["돈까스", "우동", "초밥", "회", "샤브샤브", "라멘"],
             "양식":["피자", "치킨", "햄버거"],
             "기타":["고기", "곱창", "밥버거"]}