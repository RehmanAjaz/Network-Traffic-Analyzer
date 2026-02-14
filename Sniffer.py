from scapy.all import sniff
from scapy.layers.inet import IP, TCP, UDP, ICMP

def analyze_packet(packet):
    if IP in packet:
        src = packet[IP].src
        dst = packet[IP].dst

        if packet.haslayer(TCP):
            print(f"[TCP] {src} -> {dst} | {packet[TCP].sport} -> {packet[TCP].dport}")

        elif packet.haslayer(UDP):
            print(f"[UDP] {src} -> {dst} | {packet[UDP].sport} -> {packet[UDP].dport}")

        elif packet.haslayer(ICMP):
            print(f"[ICMP] {src} -> {dst}")

        else:
            print(f"[IP] {src} -> {dst}")

print("Sniffer started... Press CTRL+C to stop.")
sniff(prn=analyze_packet, store=False)
