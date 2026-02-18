from scapy.all import ARP, Ether, srp

def scan(ip):
    # 1. ARP сұранысын жасау (Желідегілерге "Сен кімсің?" деп сұрау салу)
    arp = ARP(pdst=ip)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether/arp

    # 2. Пакетті жіберу және жауап алу
    result = srp(packet, timeout=3, verbose=False)[0]

    # 3. Нәтижені шығару
    clients = []
    for sent, received in result:
        clients.append({'ip': received.psrc, 'mac': received.hwsrc})
    
    return clients

# Өз желіңнің IP диапазонын жаз (көбіне 192.168.1.1/24 болады)
ip_range = "192.168.1.1/24"
print(f"{ip_range} желісі сканерленуде...")
devices = scan(ip_range)

print("Табылған құрылғылар:")
print("IP Мекенжайы\t\tMAC Мекенжайы")
for device in devices:
    print(f"{device['ip']}\t\t{device['mac']}")
