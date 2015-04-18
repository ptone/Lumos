"""
Client/Source

Generates and sends E1.31 packets over UDP
"""

import socket
import struct

from packet import E131Packet


def ip_from_universe(universe):
    # derive multicast IP address from Universe
    high_byte = (universe >> 8) & 0xff
    low_byte = universe & 0xff
    return "239.255.{}.{}".format(high_byte, low_byte)


class DMXSource(object):
    """
    bind_ip is the IP address assigned to a specific HW interface
    """

    def __init__(self, universe=1, network_segment=1, bind_ip=None):
        self.universe = universe
        self.ip = ip_from_universe(universe)
        self.sequence = 0
        # open UDP socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        if bind_ip:
            self.sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_IF,
                    socket.inet_aton(bind_ip))
        # set ttl to limit network segment reach
        ttl = struct.pack('b', network_segment)
        self.sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)

    def send_data(self, data):
        packet = E131Packet(universe=self.universe, data=data, sequence=self.sequence)
        if self.sequence == 255:
            self.sequence = 0
        else:
            self.sequence += 1
        self.sock.sendto(packet.packet_data, (self.ip, 5568))
