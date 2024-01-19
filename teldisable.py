import os
import subprocess

def disable_telemetry():
    # Отключение службы телеметрии
    subprocess.run(["sc", "stop", "DiagTrack"])
    subprocess.run(["sc", "config", "DiagTrack", "start=", "disabled"])
    
    subprocess.run(["sc", "stop", "dmwappushservice"])
    subprocess.run(["sc", "config", "dmwappushservice", "start=", "disabled"])

    # Отключение сбора данных телеметрии в реестре
    subprocess.run(["reg", "add", "HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows\\DataCollection", "/v", "AllowTelemetry", "/t", "REG_DWORD", "/d", "0", "/f"])

if __name__ == "__main__":
    disable_telemetry()
    print("Телеметрия успешно отключена!")
