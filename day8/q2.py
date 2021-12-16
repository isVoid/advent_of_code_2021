from itertools import repeat
from functools import reduce

wire_to_number = {
    "abcefg": 0,
    "cf": 1,
    "acdeg": 2,
    "acdfg": 3,
    "bcdf": 4,
    "abdfg": 5,
    "abdefg": 6,
    "acf": 7,
    "abcdefg": 8,
    "abcdfg": 9,
}

with open("input.txt", "r") as fo:
    patterns = []
    digits = []
    for line in fo:
        p, d = line.split("|")
        patterns.append(p.split())
        digits.append(d.split())

final = 0
for ps, ds in zip(patterns, digits):
    num_wires_to_p = {}
    mappings = dict(zip("abcdefg", repeat(set())))
    for p in ps:
        if len(p) not in num_wires_to_p:
            num_wires_to_p[len(p)] = set()
        num_wires_to_p[len(p)].add(p)

    # Digit 1 uses c, f position
    d1_wires = next(iter(num_wires_to_p[2]))
    mappings["c"] = set(d1_wires)
    mappings["f"] = set(d1_wires)

    # Digit 7 uses a, c, f position
    # Since "c", "f" is constrained to the two positions from d1, the third
    # wire in d7 maps to position "a".
    d7_wires = next(iter(num_wires_to_p[3]))
    mappings["a"] = set(d7_wires) - set(d1_wires)

    # Digit 4 uses b, c, d, f position
    # Similarly, we know that b, d maps the the remaining two wires in d4
    d4_wires = next(iter(num_wires_to_p[4]))
    mappings["b"] = set(d4_wires) - set(d1_wires)
    mappings["d"] = set(d4_wires) - set(d1_wires)

    # Digit 2, 3, 5 all have 5 wires, by performing set intersections
    # we know the mappings of position a, d, g; since a is known, we
    # then know possible mapping of d, g
    res = set(next(iter(num_wires_to_p[5])))
    for d_wires in num_wires_to_p[5]:
        res = res.intersection(d_wires)
    res = res - mappings["a"]

    # For position d, combining with knowledge from d4, we can uniquely determine
    mappings["d"] = mappings["d"].intersection(res)
    # This also determines position g
    mappings["g"] = res - mappings["d"]

    # When d is determined, from d4, position b is determined.
    mappings["b"] = mappings["b"] - mappings["d"]

    # So far we determined a, b, d, g. d5 contains position a, b, d, f, g.
    # If we find d5, we can determine f.
    # This is simple because the only digit with 5 wires that contains
    # position b is 5.
    for d_wires in num_wires_to_p[5]:
        if next(iter(mappings["b"])) in d_wires:
            d5_wires = d_wires
            break
    mappings["f"] = (
        set(d5_wires)
        - mappings["a"]
        - mappings["b"]
        - mappings["a"]
        - mappings["d"]
        - mappings["g"]
    )

    # From d1, we can determine c.
    mappings["c"] = mappings["c"] - mappings["f"]

    # The only one missing is e.
    mappings["e"] = set("abcdefg") - reduce(set.union, mappings.values())

    mappings = dict(
        zip(map(lambda x: next(iter(x)), mappings.values()), mappings.keys())
    )

    pres = ""
    for d in ds:
        fixed = "".join(sorted((map(lambda x: mappings[x], d))))
        pres += str(wire_to_number[fixed])
    final += int(pres)
print(final)
