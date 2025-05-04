def scraping():
    import re
    from playwright.sync_api import Playwright, sync_playwright, expect
    from utils import save_html

    def run(playwright: Playwright) -> None:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://heycar.com/fr/autos/gearbox/automatic_gear?utm_campaign=fr_sea_pmax_shopping_vehicles_cls&utm_source=google&utm_medium=cpc&hsa_acc=9963670215&hsa_cam=21239546280&hsa_src=x&hsa_net=adwords&hsa_ver=3&gad_source=5&gclid=EAIaIQobChMIruKW2KPojAMV2jcGAB1BbAM4EAAYAyAAEgIuavD_BwE&sort=i15_fr_elo")
        page.get_by_role("button", name="partenaires").click()
        page.get_by_role("button", name="ENREGISTRER ET QUITTER").click()
        for i in range(100):
            save_html(page.content())
            page.get_by_role("link", name="Aller à la page suivante").click()

        # ---------------------
        context.close()
        browser.close()

    with sync_playwright() as playwright:
        run(playwright)        