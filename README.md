# Yff_prosjektuke21



alle libraries:
import os
from dotenv import find_dotenv, load_dotenv, set_key
from cryptography.fernet import Fernet
import random
import string

Downloads for libraries som ikke er integrert:
pip install python-dotenv
pip install cryptography



Hvordan buke programmet

Etter at du har opprettet en .env-fil i samme mappe som Python-filen, kan du åpne prosjektet i VS Code og kjøre programmet. Når du blir bedt om å skrive inn brukernavn og passord, har du også muligheten til å få generert et tilfeldig passord dersom du ønsker det. Programmet vil deretter kryptere passordet og brukernavnet så dekryptere det. Hvis du åpner .env-filen etter kjøringen, vil du se både den krypterte og den dekrypterte versjonen av passordet lagret der.



Hvordan programmet funker 
programmet krypterer passord og brukernavn derreter decoder programmet passord og brukernavn til en string så sendes dette til .env filen og til slutt blir passord og brukernavn dekryptert og sendt til en .env fil 

her er et eksempel resultat

USERNAME1='Eksempel_brukernavn'
PASSWORD='K2Zr7A2NzvGK6Pkf'
SECRET_KEY='37yvX8avcYYfXFcCUs47_YZrOlIFxx006cguo1BOrvc='
ENCRYPTED_USERNAME1='gAAAAABoLXjmUyNBD1r59ekKbD081pABrnm3yjjlhFBYhcj8BC_47YmRSl1RaALSkOpr1kZVrUHGGX1HOUFahSKlDUTk9XRrO-4W6hD2VClpfeV5nFPmnUw='
ENCRYPTED_PASSWORD='gAAAAABoLXjmb1j0alKl9KlvZ0IlRehZKV1ZOMwHZY9pECUcUBYCUbk_SM7zIoEgJlUSPNmtRLjPxsFec1Dgyu2ln9oM6pmAzhoaSPpZCXxYAienGtipmpk='
