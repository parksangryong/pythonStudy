import json

# JSON 파일을 딕셔너리로 변환
with open('myinfo.json') as f:
    data = json.load(f)
    print(data)

# 딕셔너리를 JSON 파일로 저장
with open('myinfo.json', 'w') as f:
    data = {
        "name": "박상룡",
        "age": 29,
        "city": "Daegu",
        "birthday": "1996-05-06"
    }
    json.dump(data, f, ensure_ascii=False)

