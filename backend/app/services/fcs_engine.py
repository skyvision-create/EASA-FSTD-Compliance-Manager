from typing import Dict, List, Tuple

FIDELITY_ORDER = {"N": 0, "G": 1, "R": 2, "S": 3}

FCS_FEATURES = [
    "fdk", "clh", "clo", "sys", "gnd", "ige", "oge",
    "snd", "vib", "mtn", "vis", "nav", "atm", "ost"
]


def check_fcs_compliance(task_fcs: Dict[str, str], fstd_fcs: Dict[str, str]) -> Tuple[bool, List[str]]:
    shortfalls = []

    for feature in FCS_FEATURES:
        required = task_fcs.get(feature, "N")
        available = fstd_fcs.get(feature, "N")

        if FIDELITY_ORDER.get(available, 0) < FIDELITY_ORDER.get(required, 0):
            shortfalls.append(f"{feature.upper()}: requires {required}, available {available}")

    return len(shortfalls) == 0, shortfalls
