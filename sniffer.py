from scapy.all import sniff

def packet_callback(packet):
    # Пакеттің қысқаша мазмұнын шығару
    if packet.haslayer("IP"):
        src = packet["IP"].src
        dst = packet["IP"].dst
        proto = packet["IP"].proto
        print(f"[+] Пакет: {src} -> {dst} | Протокол: {proto}")

print("Желіні тыңдау басталды... (Тоқтату үшін Ctrl+C басыңыз)")
# Желілік пакеттерді ұстау (10 пакетті көрсету)
sniff(prn=packet_callback, count=10)
