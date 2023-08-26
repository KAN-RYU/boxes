import json

if __name__ == "__main__":
    FILENAMES = []
    with open('./naming.txt', encoding='utf-8') as nameFile:
        while True:
            line = nameFile.readline().rstrip()
            if not line:
                break
            FILENAMES.append(line.split(','))
    for eng, kor in FILENAMES:
        try:
            with open(f'./{kor}.json', encoding='utf-8') as korJSON:
                data = json.load(korJSON)
                newData = data["ObjectStates"][0]
                with open(f'./{eng}.json', 'w', encoding='utf-8') as newJSON:
                    json.dump(newData, newJSON, ensure_ascii=False, indent=2)
        except Exception as e:
            print(e)
            pass