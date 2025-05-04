import requests
from pathlib import Path
from lxml.html import fromstring


root = Path(__file__).parent

cars = "https://heycar.com/fr/autos/body/suv/color/gris/seats/5/doors/5/gearbox/automatic_gear?utm_campaign=fr_sea_pmax_shopping_vehicles_cls&utm_source=google&utm_medium=cpc&hsa_acc=9963670215&hsa_cam=21239546280&hsa_src=x&hsa_net=adwords&hsa_ver=3&gad_source=5&gclid=EAIaIQobChMIruKW2KPojAMV2jcGAB1BbAM4EAAYAyAAEgIuavD_BwE&sort=i15_fr_elo&emission-sticker=1&engine-power__gte=100&engine-power__lte=200"

res = requests.get(cars)

with open(root / "cars.html", "w", encoding="utf-8") as f:
    f.write(res.text)