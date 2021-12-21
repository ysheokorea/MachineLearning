import matplotlib.pyplot as plt
import pandas as pd
import json

# 알파벳 출현 빈도 데이터 읽어들이기
with open("./python-for-machine-learning_20190826/ch4/lang/freq.json", "r", encoding="utf-8") as f:
    freq = json.load(f)


# 언어마다 계산하기
lang_dic = {}
for i, lbl in enumerate(freq[0]["labels"]):
    fq=freq[0]["freqs"][i]
    if not(lbl in lang_dic):
        lang_dic[lbl] = fq
        continue
    for idx, v in enumerate(fq):
        lang_dic[lbl][idx] = (lang_dic[lbl][idx]+v) /2
# Pandas의 DataFrame에 데이터 넣기
asclist=[[chr(n) for n in range(97,97+26)]]
df=pd.DataFrame(lang_dic, index=asclist)

# 그래프그리기
plt.style.use('ggplot')
# df.plot(kind="bar", subplots=True, ylim=(0,0.15))
df.plot(kind="line")
plt.savefig("lang-plot.png")
