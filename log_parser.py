#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import csv
import re
import signal

def parse_line(line):
    entry = {}
    for column in line:
        # Champ vide, on saute
        if not "=" in column:
            continue
        key, value = column.split("=", 1)
        if value.startswith('"') and value.endswith('"'):
            # On vire les guillemets doubles
            # quand ils sont présents des deux côtés
            value = re.sub(r'^"|"$', "", value)
        entry[key] = value
    for field, regex in args.grep:
        # Si l'un des champs ne correspond pas ou n'est pas présent, on zappe
        if field not in entry or not re.search(regex, entry[field]):
            return
    # Pas de filtrage
    if not args.fields:
        filtered_entry = entry
    else:
        # On prend tous les champs de la liste s'ils existent pour ce log
        filtered_entry = {k: entry[k] for k in args.fields if k in entry}
    if filtered_entry:
        display_entry(filtered_entry)

def display_entry(entry):
    if args.field_names:
        print(*("{}={}".format(k, v) for k, v in entry.items()), sep = ", ")
    else:
        print(*(entry.values()))

if __name__ == "__main__":
    # Pour éviter BrokenPipeError quand on pipe dans un autre programme
    #signal.signal(signal.SIGPIPE, signal.SIG_DFL)
    parser = argparse.ArgumentParser()
    parser.add_argument("log", nargs="+")
    parser.add_argument("-f", "--fields", default=[], nargs="+",
            help="list des champs a afficher, par defaut tous")
    parser.add_argument("-g", "--grep", default=[], nargs=2, action="append",
            metavar=("FIELD", "REGEX"),
            help="n'afficher que les logs ou le champ FIELD correspond a REGEX")
    parser.add_argument("-n", "--field-names", action="store_true", default=False,
            help="afficher les noms des champs pour chaque log")
    args = parser.parse_args()
    for log_file in args.log:
        with open(log_file) as f:
            reader = csv.reader(f)
            for line in reader:
                parse_line(line)
