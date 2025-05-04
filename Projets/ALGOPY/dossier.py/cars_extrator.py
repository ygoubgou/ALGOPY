from pathlib import Path
import os
from typing import List
from lxml.html import fromstring
from models_dataclasses import voiture
import re

root = Path(__file__).parent
cars_file = root / "cars-html"

def extraire_numeriques(chaine):
    return ''.join(caractere for caractere in chaine if caractere.isdigit())

def clean_int(text) -> int:
    if extraire_numeriques(text) == '':
        return 0
    return int(extraire_numeriques(text))

def extraire_nombre_chevaux(texte: str) -> int:
    return ''.join(caractere for caractere in texte if caractere.isdigit())

def extract_cars_data(filename: str) -> List[voiture]:
    with open(filename, "r", encoding="utf-8") as f:
        content = fromstring(f.read())

    marque_modele_elements = content.xpath("//span[starts-with(@class,'VehicleTile_make__')]")
    marques = [m.text_content().strip().split(" ", 1)[0] for m in marque_modele_elements]
    modeles = [m.text_content().strip().split(" ", 1)[1] if len(m.text_content().strip().split(" ", 1)) > 1 else "" for m in marque_modele_elements]

    prix_elements = content.xpath("//p[@class='Typography_typography____Fzs Typography_h3__jih9Z TotalPrice_totalPrice__JlRFp']")
    prix_v = [clean_int(p.text_content()) for p in prix_elements]

    infos_elements = content.xpath("//div[starts-with(@class, 'typography-subheading-3 Pill_pill')]")
    infos_text = [e.text_content().strip() for e in infos_elements]

    chevaux_bruts = [cheval.text for cheval in content.xpath("//span[starts-with(@class,'VehicleTile_model__WztVg')]")]
    chevaux = [extraire_nombre_chevaux(txt) for txt in chevaux_bruts]

    codes_postaux = [span.text_content().strip() for span in content.xpath("//span[contains(@class, 'Typography_caption1')]")]

    # 🔧 Correction ici : filtrer les triplets valides [année, km, énergie]
    infos_valides = []
    temp = []

    for info in infos_text:
        temp.append(info)
        if len(temp) == 3:
            try:
                annee_test = int(temp[0])
                km_test = clean_int(temp[1])
                energie_test = temp[2].lower()
                if annee_test >= 1990 and any(kw in energie_test for kw in ['essence', 'diesel', 'électrique', 'hybride']):
                    infos_valides.append(tuple(temp))
            except:
                pass
            temp = []

    total_voitures = min(len(marques), len(prix_v), len(infos_valides), len(chevaux), len(codes_postaux))
    voitures = []

    for i in range(total_voitures):
        try:
            annee, kilometrage_str, energie = infos_valides[i]
            annee = clean_int(annee)
            kilometrage = clean_int(kilometrage_str)

            voiture_obj = voiture(
                marque=marques[i],
                modele=modeles[i],
                prix=prix_v[i],
                annee=annee,
                kilometrage=kilometrage,
                energie=energie,
                nb_chevaux=chevaux[i],
                code_postal=codes_postaux[i]
            )
            voitures.append(voiture_obj)
        except Exception as e:
            print(f"Erreur à l’index {i}: {e}")
            continue

    return voitures

def export_to_csv(data: List[voiture], filename: str, sep=";"):
    header = sep.join(["marque", "modele", "prix", "annee", "kilometrage", "energie", "nombre chevaux", "code postal"])

    with open(filename, "w", encoding="utf-8") as f:
        f.write(header + "\n")
        for v in data:
            line = sep.join([
                v.marque,
                v.modele,
                str(v.prix),
                str(v.annee),
                str(v.kilometrage),
                v.energie,
                str(v.nb_chevaux),
                v.code_postal
            ])
            f.write(line + "\n")

if os.path.exists(cars_file):
    files = [cars_file / file for file in os.listdir(cars_file) if file.endswith(".html")]
    all_voitures = []
    for file in files:
        all_voitures += extract_cars_data(file)

    export_to_csv(all_voitures, root / "voitures.csv", sep=";")
else:
    print("Le dossier 'cars-html' n'existe pas.")
