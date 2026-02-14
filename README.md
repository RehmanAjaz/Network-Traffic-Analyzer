Network Traffic Analyzer – Python Packet Sniffer
Overview

This project implements a real-time network packet sniffer using Python and the Scapy library. The tool captures live IP traffic from a network interface, identifies transport-layer protocols (TCP, UDP, ICMP), and extracts structured metadata such as source/destination IP addresses and port numbers.

The objective of this project is to demonstrate practical understanding of packet structure, protocol hierarchy, and network traffic inspection within a controlled lab environment.

Features

Real-time packet capture

IP layer inspection

TCP, UDP, and ICMP protocol identification

Source and destination IP extraction

Port number analysis (TCP/UDP)

Structured console output

Controlled and ethical implementation

Technologies Used

Python 3

Scapy

Kali Linux (Lab Environment)

How It Works

The application follows this logical flow:

Network Interface
↓
Packet Capture (Scapy sniff)
↓
Layer Detection (IP Layer Check)
↓
Protocol Identification (TCP/UDP/ICMP)
↓
Metadata Extraction
↓
Formatted Output to Console

The program inspects packet headers only and does not attempt to decrypt encrypted traffic or manipulate packet contents.
