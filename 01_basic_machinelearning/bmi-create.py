import random

"""
 BMI = [몸무게] / [키]*[키]
    +저체중 : 18.5 미만
    +일반 : 18.5~25
    +비만 : 25 이상
"""

# BMI를 계산해서 레이블을 리턴하는 함수
def calc_bmi(h, w):
    bmi = w / (h/100)**2
    if bmi < 18.5 : return "Thin"
    if bmi < 25 : return "Normal"
    return "Fat"

# 출력 파일 준비하기

fp = open("bmi.csv", "w", encoding="utf-8")
fp.write("height,weight,label\r\n")

# 무작위로 데이터 생성하기
cnt = {"Thin":0, "Normal":0, "Fat":0}
for i in range(10000):
    h = random.randint(120,200)
    w = random.randint(35,80)
    label = calc_bmi(h, w)
    cnt[label] += 1
    fp.write("{0},{1},{2}\r\n".format(h,w,label))
fp.close()
print("ok", cnt)