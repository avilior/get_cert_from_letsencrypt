# Project in support of obtaining a certificate from Let's Encrypt

## Introduction

This project creates an environment for obtaining a certificate from [Let's Encrypt](https://letsencrypt.org)

In order to acquire a certificate for a domain from [Let's Encrypt](https://letsencrypt.org) as the owner of the domain you have to demonstrate that you have control over that domains.
This entails proving that a file containing some specific stuff can be serverd from that domain.


[Let's Encrypt](https://letsencrypt.org) use the [ACME Protocol](https://en.wikipedia.org/wiki/Automated_Certificate_Management_Environment) to acquire and renew certificates.

The ACME protocol is implemented by a client which can be installed as follows;

For ubuntu:

$ sudo apt-get update

$ sudo apt-get install software-properties-common

$ sudo add-apt-repository ppa:certbot/certbot

$ sudo apt-get update

$ sudo apt-get install certbot

Note that an earlier (?) version can also be obtained by sudo apt-get install letsencrypt


## Settting up a webserver

In order to prove that we control the domain we need to setup a webserver that will be used by [Let's Encrypt](https://letsencrypt.org) to fetch a file.

The file will be placed in the webservers static location.  In our case there is a static directory.

run the webserver as follows:

cd webserver
sudo python3 webserver.py --port 80 --static <......>/lets_encrypt/static/

Note may have to setup a forwarding rule on the router if the machine is on the LAN.

## Run ACME Client -- Certbot

sudo certbot certonly --webroot -w ./static -d example.com -d www.example.com

Certbot will place a file in the static directory  which will be fetched by [Let's Encrypt](https://letsencrypt.org) thus proving your control over the domain.

Once the exchange is successful certbot will place several files in the /etc/letsencrypt directory.  These files include the account files and also the certificate generated.

The account files are used for subsequent operations such as renew and key revocation.

## Testing

In order to test the certificate we can run the secure webserver

cd secure_webserver
sudo python3 secure_webserver.py --port 443 --static <...>/lets_encrypt/static/  --cert "/etc/letsencrypt/live/example.com/fullchain.pem"  --key "/etc/letsencrypt/live/example.org/privkey.pem"

The static directory contains a hello.txt file.  Lets see if we can fetch it:

curl https://example.com/hello.txt

Note we may have to setup a forwarding rule for port 443 if the machine is on the LAN.
