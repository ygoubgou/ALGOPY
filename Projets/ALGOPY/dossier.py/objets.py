from dataclasses import dataclass

@dataclass
class MLInput:
    marque_Citroën: bool
    marque_Dacia: bool
    marque_Mercedes_Benz: bool
    marque_Nissan: bool
    marque_Peugeot: bool
    marque_Toyota: bool
    modele_2008: bool
    modele_308_SW: bool
    modele_Arkana: bool
    modele_C_HR: bool
    modele_C3: bool
    modele_C4_X: bool
    modele_Captur: bool
    modele_Classe_A: bool
    modele_Classe_C: bool
    modele_GLA: bool
    modele_Megane: bool
    modele_Megane_E_Tech: bool
    modele_Megane_R_S: bool
    modele_Qashqai: bool
    modele_Sandero: bool
    modele_Sandero_Stepway: bool
    modele_Spring: bool
    modele_Yaris: bool
    modele_e_2008: bool
    annee: int
    kilometrage: int
    energie_Diesel: bool
    energie_hybride: bool
    nombre_chevaux: int
    région_Auvergne_Rhône_Alpes: bool
    région_Bourgogne_Franche_Comté: bool
    région_Bretagne: bool
    région_Centre_Val_de_Loire: bool
    région_Grand_Est: bool
    région_Hauts_de_France: bool
    région_Normandie: bool
    région_Occitanie: bool
    région_Pays_de_la_Loire: bool
    région_Provence_Alpes_Côte_d_Azur: bool
    région_Île_de_France: bool

@dataclass
class UserInput:
    marque: str
    modele: str
    annee: int
    kilometrage: int
    energie: str 
    nombre_chevaux: int
    region: str

    def convert_to_mlinput(self):
        return MLInput(
            marque_Citroën=self.marque == "Citroën",
            marque_Dacia=self.marque == "Dacia",
            marque_Mercedes_Benz=self.marque == "Mercedes-Benz",
            marque_Nissan=self.marque == "Nissan",
            marque_Peugeot=self.marque == "Peugeot",
            marque_Toyota=self.marque == "Toyota",
            modele_2008=self.modele == "2008",
            modele_308_SW=self.modele == "308 SW",
            modele_Arkana=self.modele == "Arkana",
            modele_C_HR=self.modele == "C-HR",
            modele_C3=self.modele == "C3",
            modele_C4_X=self.modele == "C4 X",
            modele_Captur=self.modele == "Captur",
            modele_Classe_A=self.modele == "Classe A",
            modele_Classe_C=self.modele == "Classe C",
            modele_GLA=self.modele == "GLA",
            modele_Megane=self.modele == "Megane",
            modele_Megane_E_Tech=self.modele == "Megane E Tech",
            modele_Megane_R_S=self.modele == "Megane R.S.",
            modele_Qashqai=self.modele == "Qashqai",
            modele_Sandero=self.modele == "Sandero",
            modele_Sandero_Stepway=self.modele == "Sandero Stepway",
            modele_Spring=self.modele == "Spring",
            modele_Yaris=self.modele == "Yaris",
            modele_e_2008=self.modele == "e-2008",
            annee=self.annee,
            kilometrage=self.kilometrage,
            energie_Diesel=self.energie == "Diesel",
            energie_hybride=self.energie == "Hybride",
            nombre_chevaux=self.nombre_chevaux,
            région_Auvergne_Rhône_Alpes=self.region == "Auvergne-Rhône-Alpes",
            région_Bourgogne_Franche_Comté=self.region == "Bourgogne-Franche-Comté",
            région_Bretagne=self.region == "Bretagne",
            région_Centre_Val_de_Loire=self.region == "Centre-Val de Loire",
            région_Grand_Est=self.region == "Grand Est",
            région_Hauts_de_France=self.region == "Hauts-de-France",
            région_Normandie=self.region == "Normandie",
            région_Occitanie=self.region == "Occitanie",
            région_Pays_de_la_Loire=self.region == "Pays de la Loire",
            région_Provence_Alpes_Côte_d_Azur=self.region == "Provence-Alpes-Côte d'Azur",
            région_Île_de_France=self.region == "Île-de-France",
        )
