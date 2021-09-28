#! /usr/bin/python

import shodan
sho_key = PNnViMbW4LTO7BV66HNjv9ghmpZnMYdf
sho_api = shodan.Shodan(sho_key)
sho_target = '179.191.78.194'
shodan_host = sho_api.host(sho_target)

def shodan_info():
    print ('IP alvo:' , sho_host['ip_str'])
    print('organizacao : ', sho_host.get('org','n/a'))
    print('sistema operacional :', sho_host.get('os','n/a'))





shodan_info()
