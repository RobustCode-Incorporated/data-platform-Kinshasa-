import csv

def read_csv(file_path):
    people = []

    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            people.append({
                "nom": row["nom"].strip(),
                "postnom": row["postnom"].strip(),
                "prenom": row["prenom"].strip()
            })

    return people