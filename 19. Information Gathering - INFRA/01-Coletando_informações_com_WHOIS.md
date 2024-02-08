# Coletando informações com o WHOIS

## IANA WHOIS Service

[IANA WHOIS](https://iana.org/whois)

The IANA WHOIS Service is provided using the WHOIS protocol on port 43. This web gateway will query this             server and return the results. Accepted query arguments are domain names, IP addresses and AS numbers.

### Exemplo:

**Pesquisando "businesscorp.com.br" no WHOIS da IANA**

```

% IANA WHOIS server
% for more information on IANA, visit http://www.iana.org
% This query returned 1 object

refer:        whois.registro.br >dado importante

domain:       BR

organisation: Comite Gestor da Internet no Brasil
address:      Av. das Nações Unidas, 11541, 7. andar
address:      São Paulo SP 04578-000
address:      Brazil

contact:      administrative
name:         Demi Getschko
organisation: Comite Gestor da Internet no Brasil
address:      Av. das Nações Unidas, 11541, 7. andar
address:      São Paulo SP 04578-000
address:      Brazil
phone:        +55 11 5509 3505
fax-no:       +55 11 5509 3501
e-mail:       demi@registro.br

contact:      technical
name:         Frederico Augusto de Carvalho Neves
organisation: Registro .br
address:      Av. das Nações Unidas, 11541, 7. andar
address:      São Paulo SP 04578-000
address:      Brazil
phone:        +55 11 5509 3505
fax-no:       +55 11 5509 3501
e-mail:       fneves@registro.br

nserver:      A.DNS.BR 200.219.148.10 2001:12f8:6:0:0:0:0:10
nserver:      B.DNS.BR 200.189.41.10 2001:12f8:8:0:0:0:0:10
nserver:      C.DNS.BR 200.192.233.10 2001:12f8:a:0:0:0:0:10
nserver:      D.DNS.BR 200.219.154.10 2001:12f8:4:0:0:0:0:10
nserver:      E.DNS.BR 200.229.248.10 2001:12f8:2:0:0:0:0:10
nserver:      F.DNS.BR 200.219.159.10 2001:12f8:c:0:0:0:0:10
ds-rdata:     38298 13 2 9f2d4993f47b0f2751de0007d70a2754ee532fe373761154d9ea7a8cb9d8ea18

whois:        whois.registro.br

status:       ACTIVE
remarks:      Registration information: http://registro.br/

created:      1989-04-18
changed:      2023-11-14
source:       IANA
```

> Note que o campo "refer" na resposta do whois da iana nos mostra quem é o resposável pelo ip, dominio, etc, pesquisado. Nesse caso o responsável é o registro.br, por isso vamos pesquisar novamente, mas dessa vez vamos usar o WHOIS do registro.br
>


**Pesquisando "businesscorp.com.br" no [WHOIS](https://registro.br/tecnologia/ferramentas/whois) do registro.br**

## Domínio **businesscorp.com.br**


| Titular            | Desec Security Segurança da Informação LTDA                                                               |
| ------------------ | ------------------------------------------------------------------------------------------------------------ |
| Documento          | **23.019.510/0001-06**                                                                                       |
| Responsável       | Desec Security                                                                                               |
| País              | BR                                                                                                           |
| Contato do Titular | **JORLO47**                                                                                                  |
| Contato Técnico   | **JORLO47**                                                                                                  |
| Servidor DNS       | **ns1.businesscorp.com.br** 37.59.174.225                                                                   |
| Servidor DNS       | **ns2.businesscorp.com.br** 37.59.174.226                                                                   |
| SACI               | Sim                                                                                                          |
| Criado             | 04/09/2017[#17416766](https://registro.br/tecnologia/ferramentas/whois/?search=17416766 businesscorp.com.br) |
| Expiração        | 04/09/2024                                                                                                   |
| Alterado           | 07/09/2023                                                                                                   |
| Status             | Publicado                                                                                                    |

## Contato (ID) **JORLO47**


| Nome     | José Ricardo Longatto       |
| -------- | ---------------------------- |
| Email    | financeiro@desecsecurity.com |
| País    | BR                           |
| Criado   | 30/01/2012                   |
| Alterado | 15/09/2023                   |

> Note que agora ele traz informações sobre o dono do domínio

### Pesquisando o numero de IP retornado na busca no whois do registro.br no whois da IANA:

```
% IANA WHOIS server
% for more information on IANA, visit http://www.iana.org
% This query returned 1 object

refer:        whois.ripe.net

inetnum:      37.0.0.0 - 37.255.255.255
organisation: RIPE NCC
status:       ALLOCATED

whois:        whois.ripe.net

changed:      2010-11
source:       IANA

```

> Percebe-se que a entidade que controla esse IP é o RIPE NCC, por isso vamos pesquisar esse IP no [WHOIS](https://apps.db.ripe.net/db-web-ui/query) do RIPE

### Pesquisando o numero de IP retornado na busca no whois do registro.br no whois do RIPE:

```
Responsible organisation: OVH Hosting LDA
Abuse contact info: abuse@ovh.net

    inetnum:         37.59.174.224 - 37.59.174.239
    netname:         OVH_134187362
    country:         PT
    descr:           Failover Ips
    org:             ORG-OL44-RIPE
    admin-c:         OTC6-RIPE
    tech-c:          OTC6-RIPE
    status:          ASSIGNED PA
    mnt-by:          OVH-MNT
    created:         2017-03-07T16:27:02Z
    last-modified:   2023-01-09T14:53:20Z
    source:          RIPE

    route:           37.59.0.0/16
    descr:           OVH ISP
    descr:           Paris, France
    origin:          AS16276
    mnt-by:          OVH-MNT
    created:         2012-01-25T17:04:21Z
    last-modified:   2012-01-25T17:04:21Z
    source:          RIPE# Filtered
```

> Note que agora ele retorna informações importantes sobre o bloco de IPs, a empresa que vendeu esses IPs, a localização da empresa responsável e o bloco ASN do qual saiu o bloco de IP da businesscorp

---

## Fazendo consultas pelo terminal do linux:

`whois businesscorp.com.br`

> Esse programa faz uma consulta na IANA, descobre o responsável e faz a busca no whois responsável pelo dominio/ip etc
