import json
import socket

OPEN_PORTS = [] #lista porte aperte
PORTS_DATA_FILE = "./commons_ports.json"

def extract_json_data(filename):
    with open(filename, "r") as file: #r = sola lettura come file
        data = json.load(file) #mettiamo in data il file json
    return data

def get_ports_info():
    data = extract_json_data(PORTS_DATA_FILE)
    ports_info = {int(k): v for (k, v) in data.items()} #dizionario int k e valore v per ciascuna chiave e valore presente in data.items
    return ports_info

def get_host_ip_addr(target): #converte il dominio in ip
    try:
        ip_addr = socket.gethostbyname(target)
    except socket.gaierror as e: #errore
        print(f"C'è stato un errore {e}")
    else: #altrimenti printo l'ip
        return ip_addr

def scan_port(ip, port): #effettua la connessione per vedere se è aperta o no
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
    ports_info = get_ports_info() #richiamo la funzione

    for port in ports_info.keys(): #otteniamo le porte dal dizionario col for  
        try:
            print(f"Scanning: {ip_addr}:{port}")
            scan_port(ip_addr, port) #manda ip e porta da provare alla funzione
        except KeyboardInterrupt:
            print("\n Exit...")
            break
    print("Porte aperte:")
    for port in OPEN_PORTS:
        print(str(port), ports_info[port])