from enum import Enum
import operator
from functools import reduce

hex2bin = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111",
}


def to_bitstream(hexstream):
    return "".join(list(map(hex2bin.__getitem__, hexstream)))


class Stream:
    def __init__(self, bitstream):
        self._bitstream = bitstream

    def read(self, nbits):
        head = self._bitstream[:nbits]
        self._bitstream = self._bitstream[nbits:]
        return head

    def __repr__(self):
        return str(self._bitstream)


with open("input.txt", "r") as fo:
    l = fo.readline()
    stream = Stream(to_bitstream(l))


class State(Enum):
    READ_VERSION = 1
    READ_TYPE = 2
    READ_LITERAL = 3
    READ_MODE = 4
    READ_SUBPACKET_BITS = 5
    READ_SUBPACKET_NUM = 6
    FINISH = 7


def parse_subpackets_bitcounts(stream: Stream, subpacket_bitcounts: int):
    curbits = 0
    children = []
    while curbits < subpacket_bitcounts:
        packet = parse(stream)
        curbits += packet["length"]
        children.append(packet)
    return children


def parse_subpackets_numcounts(stream: Stream, subpacket_numcounts: int):
    children = []
    bits_in_children = 0
    for _ in range(subpacket_numcounts):
        packet = parse(stream)
        bits_in_children += packet["length"]
        children.append(packet)
    return children, bits_in_children


def parse(stream: Stream):
    state = State.READ_VERSION
    packet = {"length": 0}
    while state != State.FINISH:
        if state == State.READ_VERSION:
            vbits = stream.read(3)
            packet["version"] = int(vbits, base=2)
            packet["length"] += 3
            state = State.READ_TYPE
        elif state == State.READ_TYPE:
            tbits = stream.read(3)
            packet["type"] = int(tbits, base=2)
            packet["length"] += 3
            if packet["type"] == 4:
                state = State.READ_LITERAL
            else:
                state = State.READ_MODE
        elif state == State.READ_LITERAL:
            lbits = stream.read(5)
            if not "value_bits" in packet:
                packet["value_bits"] = ""
            packet["value_bits"] += lbits[1:]
            packet["length"] += 5
            if lbits[0] == "0":
                packet["value"] = int(packet["value_bits"], base=2)
                state = State.FINISH
        elif state == State.READ_MODE:
            mbits = stream.read(1)
            packet["mode"] = int(mbits, base=2)
            packet["length"] += 1
            if packet["mode"] == 0:
                state = State.READ_SUBPACKET_BITS
            else:
                state = State.READ_SUBPACKET_NUM
        elif state == State.READ_SUBPACKET_BITS:
            sbits = stream.read(15)
            packet["subpacket_bits"] = int(sbits, base=2)
            packet["length"] += 15
            packet["children"] = parse_subpackets_bitcounts(
                stream, packet["subpacket_bits"]
            )
            packet["length"] += packet["subpacket_bits"]
            state = State.FINISH
        elif state == State.READ_SUBPACKET_NUM:
            sbits = stream.read(11)
            packet["subpacket_num"] = int(sbits, base=2)
            packet["length"] += 11
            packet["children"], bits_in_children = parse_subpackets_numcounts(
                stream, packet["subpacket_num"]
            )
            packet["length"] += bits_in_children
            state = State.FINISH
    return packet


packet = parse(stream)

reduction_op = {
    0: operator.add,
    1: operator.mul,
    2: min,
    3: max,
}

comp_op = {
    5: lambda x, y: 1 if x > y else 0,
    6: lambda x, y: 1 if x < y else 0,
    7: lambda x, y: 1 if x == y else 0,
}


def traverse(packet):
    if packet["type"] == 4:
        return packet["value"]
    elif packet["type"] in reduction_op:
        values = [traverse(child) for child in packet["children"]]
        return reduce(reduction_op[packet["type"]], values)
    elif packet["type"] in comp_op:
        lhs = traverse(packet["children"][0])
        rhs = traverse(packet["children"][1])
        return comp_op[packet["type"]](lhs, rhs)


res = traverse(packet)
print(res)
