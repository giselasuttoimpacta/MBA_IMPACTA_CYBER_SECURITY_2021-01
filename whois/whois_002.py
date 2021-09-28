#! /usr/bin/python

import whois

target = "google.com"

qw = whois.query(target)

print(qw.name)
print(qw.creation_date)
print(qw.expiration_date)
print(qw.last_update)
print(qw.registrar)

for _domain in qw.name_servers:
    print(_domain)
