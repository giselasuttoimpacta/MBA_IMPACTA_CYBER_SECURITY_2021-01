#! /usr/bin/python

import whois
msg = "informe o nome do dominio alvo"
target = "google.com"
#qw = whois.query(target)

qw = whois.query(target)

def fun_whois():
    print(" Nome do dominio: ",qw.name)
    print(" Data de criacao: ",qw.creation_date)
    print(" Data de expiracao: ", qw.expiration_date)
    print(" data da ultima atualizacao: ",qw.last_update)
    print(" Servidor Whois registrado: ", qw.registrar)

    for _domain in qw.name_servers:
        print (" servidor de nome: ", _domain)

fun_whois


