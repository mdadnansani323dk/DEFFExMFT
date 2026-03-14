#!/usr/bin/env python3

import os

TOOL_NAME = "DEFFEx MFTv1"
VERSION = "1.1"

def banner():
    os.system("clear" if os.name == "posix" else "cls")
    print(r"""
██████╗ ███████╗███████╗███████╗███████╗██╗  ██╗
██╔══██╗██╔════╝██╔════╝██╔════╝██╔════╝╚██╗██╔╝
██║  ██║█████╗  █████╗  █████╗  █████╗   ╚███╔╝ 
██║  ██║██╔══╝  ██╔══╝  ██╔══╝  ██╔══╝   ██╔██╗ 
██████╔╝███████╗██║     ██║     ███████╗██╔╝ ██╗
╚═════╝ ╚══════╝╚═╝     ╚═╝     ╚══════╝╚═╝  ╚═╝

        DEFFEx MFTv1
   Android Motherboard Framework Tool
        dev by - DEFFEX
------------------------------------------------
""")

soc_protocols = [
    "MIPI CSI (Camera)",
    "MIPI DSI (Display)",
    "LPDDR Bus (RAM)",
    "UFS Storage",
    "PCIe (Modem / WiFi)",
    "I2C (Sensors / PMIC)",
    "SPI (Fingerprint)",
    "USB 3.x",
    "UART Debug"
]

components = {
    "SoC": "Main processor (CPU/GPU/AI)",
    "PMIC": "Power management IC",
    "LPDDR RAM": "Mobile DRAM memory",
    "UFS Storage": "Flash storage chip",
    "Modem IC": "5G cellular communication",
    "WiFi/Bluetooth IC": "Wireless connectivity",
    "Audio Codec": "Speaker & microphone control",
    "Camera Sensor": "Image sensor module",
    "Charging IC": "Battery charging controller",
    "Sensor Hub": "Accelerometer, gyro etc"
}

basic_components = {
    "Resistor": "Limits current",
    "Capacitor": "Stores electric charge",
    "Inductor / Coil": "Magnetic energy storage",
    "Diode": "One-direction current flow",
    "Zener Diode": "Voltage regulation",
    "Transistor": "Electronic switch/amplifier",
    "MOSFET": "High-speed switching transistor",
    "Crystal Oscillator": "Clock signal generator",
    "Fuse": "Overcurrent protection",
    "Connector": "Connects modules",
    "Voltage Regulator": "Stable voltage output"
}

signal_flow = """
BATTERY
   │
   ▼
PMIC ─────► Power Rails
   │
   ▼
SOC
 │ │ │ │
 │ │ │ └── UFS STORAGE
 │ │ └──── RAM
 │ └────── CAMERA
 └──────── DISPLAY

SOC ── PCIe ── MODEM
SOC ── SDIO ── WIFI
SOC ── I2C ── SENSORS
SOC ── I2S ── AUDIO
SOC ── USB ── CHARGER
"""

def show_architecture():
    print("\nAndroid Motherboard Architecture\n")
    print(signal_flow)

def list_components():
    print("\nMain IC Components\n")
    for k,v in components.items():
        print(f"{k}  ->  {v}")

def show_protocols():
    print("\nSoC Communication Protocols\n")
    for p in soc_protocols:
        print("-", p)

def show_basic_components():
    print("\nBasic Electronic Components\n")
    for k,v in basic_components.items():
        print(f"{k}  ->  {v}")

def search_component():
    name = input("Enter component name: ").lower()

    for comp in components:
        if name in comp.lower():
            print(f"\nFound: {comp}")
            print("Function:", components[comp])
            return

    for comp in basic_components:
        if name in comp.lower():
            print(f"\nFound: {comp}")
            print("Function:", basic_components[comp])
            return

    print("Component not found.")

def menu():
    while True:
        print("\nMenu")
        print("1. Motherboard Architecture")
        print("2. List IC Components")
        print("3. Show Protocol Lines")
        print("4. Show Signal Flow")
        print("5. Search Component")
        print("6. Show Basic Electronic Components")
        print("7. Exit")

        choice = input("\nSelect option: ")

        if choice == "1":
            show_architecture()
        elif choice == "2":
            list_components()
        elif choice == "3":
            show_protocols()
        elif choice == "4":
            print(signal_flow)
        elif choice == "5":
            search_component()
        elif choice == "6":
            show_basic_components()
        elif choice == "7":
            print("\nThanks for using DEFFEx MFTv1")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    banner()
    menu()