import matplotlib.pyplot as plt
import pandas as pd

# Pandas로 CSV 파일 읽어들이기
tbl=pd.read_csv("bmi.csv", index_col=2)

# 그래프 그리기 시작
fig = plt.figure()
ax = fig.add_subplot(1,1,1)

# 서브 플롯 전용 - 지정한 레이블을 임의색으로 칠하기
def scatter(lbl, color):
    b = tbl.loc[lbl]
    ax.scatter(b["weight"], b["height"], c=color, label=lbl)

scatter("Fat", "red")
scatter("Normal", "green")
scatter("Thin", "yellow")

ax.legend()
plt.savefig("bmi-test.png")
plt.show()
