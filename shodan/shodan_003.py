#!/usr/bin/python

import shodan
key = PNnVimMbW4TLI7BV66HNjv9ghmpZnMYdf
api = shodan.Shodan(key)
target = '179.191.78.194'
host = api.host(target)

def shodan_portscan():
    for _line in host['data']:
        print("Porta aberta: ",_line['port'])

shodan_portscan()
