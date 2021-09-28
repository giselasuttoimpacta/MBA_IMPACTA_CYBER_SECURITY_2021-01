#! /usr/bin/python

import whois

target = "google.com"

def func_whois(_domain):
    qw = whois.query(_domain)
    print("[+] - nome do dominio:", qw.name)
    print("[+] - data da criacao:", qw.creation_date)
    print("[+] - data de expiracao:",qw.expiration_date)
    print("[+] - data da ultima atualizacao:",qw.last_update)
    print("[+] - servidor whois registrado:",qw.registrar)

    for _domain in qw.name_servers:
        print (_domain)

func_whois(target)
