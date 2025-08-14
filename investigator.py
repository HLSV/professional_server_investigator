#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import whois
import tldextract
import socket
import nmap

def get_ip(url):
    try:
        domain = tldextract.extract(url).fqdn
        return socket.gethostbyname(domain)
    except:
        return "Não encontrado"

def check_ports(ip, ports=[21,22,23,25,53,80,443,110,143,3306]):
    nm = nmap.PortScanner()
    open_ports = []
    try:
        nm_scan = nm.scan(hosts=ip, arguments='-Pn -p '+','.join(map(str,ports)))
        for port in ports:
            if ip in nm_scan['scan'] and 'tcp' in nm_scan['scan'][ip] and port in nm_scan['scan'][ip]['tcp']:
                if nm_scan['scan'][ip]['tcp'][port]['state'] == 'open':
                    open_ports.append(str(port))
    except:
        open_ports.append("Erro Nmap")
    return ','.join(open_ports) if open_ports else "Nenhuma aberta"

def detect_technologies(headers):
    techs = []
    if 'Server' in headers:
        techs.append(headers['Server'])
    if 'X-Powered-By' in headers:
        techs.append(headers['X-Powered-By'])
    return ', '.join(techs) if techs else "Desconhecido"

def investigate(url):
    if not url.startswith("http"):
        url = "http://" + url
    ip = get_ip(url)
    try:
        response = requests.get(url, timeout=5)
        status = response.status_code
        headers = response.headers
        techs = detect_technologies(headers)
    except:
        status = "Erro"
        headers = {}
        techs = "Desconhecido"
    try:
        domain_info = whois.whois(url)
    except:
        domain_info = "Não disponível"
    open_ports = check_ports(ip)

    report = f"""
URL: {url}
IP do Servidor: {ip}
Status HTTP: {status}
Cabeçalhos: {headers}
Tecnologias Detectadas: {techs}
Portas Abertas: {open_ports}
Informações WHOIS: {domain_info}
"""
    print(report)
    with open("server_report.txt", "w", encoding="utf-8") as f:
        f.write(report)
    print("[INFO] Relatório salvo como server_report.txt")

if __name__ == "__main__":
    target = input("Digite a URL ou domínio: ")
    investigate(target)
