from wsgiref.simple_server import make_server
from urllib.parse import parse_qs
import json


def application(environ, start_response):
    params = parse_qs(environ['QUERY_STRING'])
    species = params.get('species', [''])[0]
    print(type(species))
    print(species)
    credentials = get_credentials(species)
    print(type(credentials))
    print(credentials)
    headers = [('Content-Type', 'application/json')]

    if credentials is None:
        start_response('404 Not Found', headers)
        return [json.dumps({'credentials': 'Unknown'}).encode()]
    else:
        start_response('200 OK', headers)
        return [json.dumps({'credentials': credentials}).encode()]


def get_credentials(species):
    credentials = {
        'Cyberman': 'John Lumic',
        'Dalek': 'Davros',
        'Judoon': 'Shadow Proclamation Convention 15 Enforcer',
        'Human': 'Leonardo da Vinci',
        'Ood': 'Klineman Halpen',
        'Silence': 'Tasha Lem',
        'Slitheen': 'Coca-Cola salesman',
        'Sontaran': 'General Staal',
        'Time Lord': 'Rassilon',
        'Weeping Angel': 'The Division Representative',
        'Zygon': 'Broton'
    }
    return credentials.get(species)


if __name__ == '__main__':
    serv = make_server('localhost', 8888, application)
    serv.serve_forever()
