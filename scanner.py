import socket

OPEN_PORTS = [] #lista porte aperte

def get_host_ip_addr(target): #converte il dominio in ip
    try:
        ip_addr = socket.gethostbyname(target)
    except socket.gaierror as e: #errore
        print(f"C'è stato un errore {e}")
    else: #altrimenti printo l'ip
        return ip_addr

def scan_port(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Iimposto il socket con ip ipv4 e tcp
    sock.settimeout(1.0) #imposto il timeout
    conn_status = sock.connect_ex((ip, port)) #0 --> connessione buon fine 1--> no
    if conn_status == 0: #se la connessione va a buon fine aggiungo alla lista porte aperte
        OPEN_PORTS.append(port)
    sock.close() #chiudo la connessione 

if __name__ == "__main__": #incomincia il programma --> come il main
    print("programma scritto per solo scopo educativo")
    target = input ("Inserire target: ") #dominio da provare
    ip_addr = get_host_ip_addr(target) #prende l'ip dal dominio e lo manda alla funzione per prendere il dominio dall ip
    while True:
        try:
            port = int(input("Inserire porta: ")) 
            scan_port(ip_addr, port) #manda ip e porta da provare alla funzione
            print(OPEN_PORTS) #stampa la lista di porte
        except KeyboardInterrupt:
            print("\n Exit...")
            break