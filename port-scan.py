#!/usr/bin/env python3
import nmap

def main():
    nm = nmap.PortScanner()

    alvo = "45.33.32.156"     
    opcoes = "-sV -sC"         
    try:
        nm.scan(hosts=alvo, arguments=opcoes)
    except nmap.PortScannerError as e:
        print("Erro do Nmap:", e)
        return
    except Exception as e:
        print("Erro inesperado:", e)
        return

    for host in nm.all_hosts():
        print(f"\nHost: {host} ({nm[host].hostname()})")
        print(f"Estado: {nm[host].state()}")

        for protocolo in nm[host].all_protocols():
            print(f"Protocolo: {protocolo}")
            portas = nm[host][protocolo].keys()
            
            for porta in sorted(portas):
                info = nm[host][protocolo][porta]
                estado = info.get('state', 'desconhecido')
                nome = info.get('name', '')
                produto = info.get('product', '')
                versao = info.get('version', '')
                extra = info.get('extrainfo', '')

                print(f"  Porta: {porta}\tEstado: {estado}\tServiço: {nome}\tProduto: {produto} {versao}\tExtra: {extra}")

if __name__ == "__main__":
    main()





