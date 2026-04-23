import re

def parse_people(lines):
    people = []

    for line in lines:
        line = line.strip()

        # filtre simple (évite numéros / headers)
        if len(line.split()) >= 2 and not re.search(r"\d", line):

            parts = line.split()

            if len(parts) >= 2:
                prenom = parts[0]
                nom = parts[-1]
                postnom = parts[1] if len(parts) > 2 else ""

                people.append({
                    "prenom": prenom,
                    "nom": nom,
                    "postnom": postnom
                })

    return people