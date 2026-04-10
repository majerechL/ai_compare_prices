class PriceScraper:
    
    def get_product_prices(self, product_name):
        offers = []
    
        alza_offer = {
            "product_name": product_name,
            "shop": "Alza",
            "price": 249,
            "url": "https://www.alza.sk/apple-airpods-pro-3-d13078758.htm"
        }
        offers.append(alza_offer)

        nay_offer = {
            "product_name": product_name,
            "shop": "Nay",
            "price": 240.80,
            "url": "https://www.nay.sk/sluchadla-apple-airpods-pro-3-mfhp4zm-a?gad_source=1&gad_campaignid=22510022551&gbraid=0AAAAADwlKdu_8br_aLDJPMaQZOEusITpB&gclid=Cj0KCQjwgr_NBhDFARIsAHiUWr63D3625UqsUofbcwhj469FMRCUE3FaZ0Tq8BGWM8l61F5xgW7Tk4IaAoqWEALw_wcB"
        }
        offers.append(nay_offer)

        smarty_offer = {
            "product_name": product_name,
            "shop": "Smarty",
            "price": 249,
            "url": "https://www.smarty.sk/apple-airpods-pro-3-generacia-s-magsafe-puzdrom-usb-c-4p240051?utm_source=google&utm_medium=cpc&utm_campaign=pMax_Brand&utm_adgroup=&utm_term=pla&tracking=Cj0KCQjwgr_NBhDFARIsAHiUWr6Of6R-Yb1pO8JtJ8vsyYZQVuFrdufOn77YQW-CFaAtFu8QtiffaCsaAlgREALw_wcB&gad_source=1&gad_campaignid=22128862043&gbraid=0AAAAApHQpnMxb_MtT8lpUip-jVfADCc2Z&gclid=Cj0KCQjwgr_NBhDFARIsAHiUWr6Of6R-Yb1pO8JtJ8vsyYZQVuFrdufOn77YQW-CFaAtFu8QtiffaCsaAlgREALw_wcB"
        }
        offers.append(smarty_offer)

        return offers
    