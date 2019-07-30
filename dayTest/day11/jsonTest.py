import json

def main():
    mydict = {
        'name': 'hupingan',
        'age': '33',
        'qq': 70807080,
        'frineds': [u'模压', u'白于', u'朥不'],
        'cars': [
            {'brand': 'byd', 'max_speed': 180},
            {'brand': 'de',  'max_speed': 456},
            {'brand': 'afa', 'max_speed': 695}
        ]
    }
    try:
        with open('d:\\git\\data.json', 'w') as fs:
            json.dump(mydict, fs)
    except IOError as e:
        print(e)
    print("json写入成功")


if __name__ == '__main__':
    main()