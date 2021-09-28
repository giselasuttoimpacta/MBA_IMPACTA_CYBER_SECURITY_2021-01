#! /usr/bin/python

import shodan

shodan_key = "PNnViMbW4TLO7BV66HNjv9ghmpZnMYdf"
shodan_api = shodan.Shodan(shodan_key)
shodan_target = '179.191.78.194'
shodan_host = shodan_api.host(shodan_target)

print("IP alvo: ", shodan_host["ip_str"])
print("Organizacao: " , shodan_host.get('org','n/a'))
print("Sistena operacional: ", shodan_host.get('os','n/a'))
