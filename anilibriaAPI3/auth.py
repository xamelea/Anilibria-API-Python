import requests
import json
from config import mail, password, auth_url


def connect():
    try:
        f = open('session', 'r')
        f.readline()
        auth_cookie = f.readline()
        f.close()
        print('auth_cookie ' + auth_cookie)

        response = requests.request("POST", url=auth_url,
                                    data={'mail': mail, 'passwd': password}, headers={'Cookie': auth_cookie})
    except Exception as e:
        response = requests.request("POST", url=auth_url,
                                    data={'mail': mail, 'passwd': password})

    parse_json = json.loads(response.text)
    try:
        if parse_json['key'] == 'success':
            print('\nadded new session, connected')
            return parse_json['sessionId']
        elif parse_json['key'] == 'authorized':
            print('\nconnected')
            return 'c'
    except KeyError:
        try:
            print('CONNECTION ERROR: ' + parse_json['error'])
        except KeyError:
            raise Exception('Unknown connection error')


def auth():
    temp = connect()
    if temp != 'c':
        f = open('session', 'w')
        f.write(temp)
        f.write(f'\nPHPSESSID={temp}')
        f.close()
