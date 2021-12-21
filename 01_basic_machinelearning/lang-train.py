from sklearn import svm, metrics
import glob, os.path, re, json

# 텍스트를 읽어들이고 출현 빈도 조사하기
def check_freq(fname):
    name = os.path.basename(fname)
    lang = re.match(r'^[a-z]{2,}', name).group()
    with open (fname, "r", encoding="utf-8") as f:
        text = f.read()
    text = text.lower()

    #숫자 세기 변수(cnt) 초기화 하기
    cnt = [0 for n in range(0,26)]
    code_a = ord("a")
    code_z = ord("z")

    #알파벳 출현 횟수 구하기
    for ch in text:
        n = ord(ch)
        if code_a <= n <=code_z:
            cnt[n-code_a]+=1
    
    #정규화하기
    total = sum(cnt)
    freq = list(map(lambda n:n / total, cnt))
    return (freq, lang)

# 각 파일 처리하기
def load_files(path):
    freqs=[]
    labels=[]
    # 파라미터를 리스트로 반환한다.
    file_list=glob.glob(path)
    for fname in file_list:
        r=check_freq(fname)
        freqs.append(r[0])
        labels.append(r[1])
    return {"freqs":freqs, "labels":labels}

data=load_files("./python-for-machine-learning_20190826/ch4/lang/train/*.txt")
test=load_files("./python-for-machine-learning_20190826/ch4/lang/test/*.txt")

# 이후를 대비해서 JSON으로 결과 저장하기
with open("./python-for-machine-learning_20190826/ch4/lang/freq.json", "w", encoding="utf-8") as fp:
    json.dump([data, test], fp)

# 학습하기
clf = svm.SVC()
clf.fit(data["freqs"], data["labels"])

# 예측하기
predict = clf.predict(test["freqs"])

# 결과 테스트하기
ac_score = metrics.accuracy_score(test["labels"], predict)
cl_report = metrics.classification_report(test["labels"], predict)
print("정답률 : ", ac_score)
print("리포트 = ")
print(cl_report)