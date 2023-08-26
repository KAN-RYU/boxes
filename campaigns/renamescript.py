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
                newData = data["ObjectStates"]
                with open(f'./{eng}.json', 'w') as newJSON:
                    json.dump(newData, newJSON)
        except Exception as e:
            print(e)
            pass