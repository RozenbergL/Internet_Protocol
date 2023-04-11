import socket
import struct
import time

def get_ntp_time(server_address):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.sendto(b'', server_address)
        data, _ = s.recvfrom(1024)
        ntp_time_bytes = data[:8]
        return ntp_time_bytes

def parse_ntp_time(ntp_time_bytes):
    ntp_time_int = struct.unpack('>I', ntp_time_bytes[:4])[0] - 2208988800
    ntp_time_str = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(ntp_time_int))
    return f"{ntp_time_str}"

if __name__ == '__main__':
    server_address = ('localhost', 123)
    ntp_time = get_ntp_time(server_address)
    ntp_time_str = parse_ntp_time(ntp_time)
    print(f"Текущее время на сервере {server_address}: {ntp_time_str}")
