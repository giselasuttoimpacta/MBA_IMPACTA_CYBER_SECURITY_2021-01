#! /usr/bin/python

import shodan

key = PNnViMbW4TLO7BV66HNjv9ghmpZnMYdf
api = shodan.Shopdan(key)
target = '179.191.78.194'
host = api.host(target)

def info():
    print('Informacoes genericas do alvo:')
    print('IP albo: ',host['ip_str'])
    print('organizacao', host.get('org','n/a'))
    print('sistema operacional:', host.get('os','n/a'))
    print('-' * 60)

def portscan():
    print('identificacao de portas abertas')
    for line in host['data']:
        print('porta aberta: ',line['port'])
    print('+'*60)

print("+"*60)
info()
portscan()
