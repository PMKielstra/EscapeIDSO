from dataclasses import dataclass
import random
from hackdata import firewalls, passwords, fuzzes

@dataclass
class Instance:
    time: int
    msgs: list
    sols: list
    final_lines: list

def make_generator(msg, data, command):
    def generate():
        name, sol = random.choice(data)
        return msg.format(name), f"{command} {sol}"
    return generate

gen_firewall = make_generator("Model {} firewall", firewalls, "knock")
gen_passwords = make_generator("Hashed password: {}", passwords, "pword")
gen_fuzzes = make_generator("Black box -- suggested fuzz \"{}\"", fuzzes, "fuzz")

ips = {
    "127.0.0.1": (120, 2, [gen_firewall], ["Competence verified.", "Instructions to recover the final code are in 0258.txt."]),
    "192.168.2.32": (80, 2, [gen_firewall, gen_passwords], ["The number you need is 942."]),
    "102.153.223.125": (90, 3, [gen_firewall, gen_passwords, gen_fuzzes], ["SELF-DESTRUCT CODE UNLOCKED", "ENTER THE FOLLOWING CODE INTO THE AI:", "MAIMONIDES"])
}

def get_instance(ip):
    if ip not in ips: return None
    time, stage_multiplier, gens, final_lines = ips[ip]
    gens *= stage_multiplier
    random.shuffle(gens)
    msgs = []
    sols = []
    for g in gens:
        msg, sol = g()
        msgs.append(msg)
        sols.append(sol)
    return Instance(time, msgs, sols, final_lines)
