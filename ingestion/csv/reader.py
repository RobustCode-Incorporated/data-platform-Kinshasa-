import csv
import unicodedata


def normalize_key(key: str) -> str:
    if key is None:
        return ""

    key = key.strip().lower()

    # 🔥 supprime accents (Prénom → prenom)
    key = unicodedata.normalize('NFKD', key)
    key = ''.join(c for c in key if not unicodedata.combining(c))

    return key.replace("-", "").replace(" ", "")


def read_csv(file_path):
    people = []

    with open(file_path, newline='', encoding='utf-8-sig') as csvfile:

        # 🔍 détecte séparateur automatiquement
        sample = csvfile.read(2048)
        csvfile.seek(0)

        try:
            dialect = csv.Sniffer().sniff(sample)
        except:
            dialect = csv.excel

        reader = csv.DictReader(csvfile, dialect=dialect)

        print("📌 Headers détectés:", reader.fieldnames)

        for row in reader:

            normalized = {
                normalize_key(k): (v.strip() if v else "")
                for k, v in row.items()
                if k
            }

            nom = normalized.get("nom", "")
            postnom = normalized.get("postnom", "")
            prenom = normalized.get("prenom", "")

            # 🧠 debug utile
            if not nom and not prenom:
                continue

            people.append({
                "nom": nom,
                "postnom": postnom,
                "prenom": prenom
            })

    print(f"📊 {len(people)} lignes valides après nettoyage")

    return people