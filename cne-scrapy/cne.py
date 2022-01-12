import time
import asyncio
import aiohttp
from bs4 import BeautifulSoup
import data_selectors
from logger import logger
from utils import get_dni_from_query

BASE_URL = "http://www.cne.gob.ve/"
CNE_DNI_URL = BASE_URL + "web/registro_electoral/ce.php?nacionalidad={}&cedula={}"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
}
VENEZUELAN = 'V'
FOREIGN = 'E'


class Cne:
    def __init__(self, dni_list):
        self.dni_list = dni_list
        self.results = []

    def get_url_by_nacionality(self, dni):
        nacionality = VENEZUELAN
        if (dni.startswith('e')):
            nacionality = FOREIGN
        if (not dni.isdigit()):
            current_nacionality = dni[0]
            _, dni = dni.split(current_nacionality)
        return CNE_DNI_URL.format(nacionality, dni)

    def _get_task(self, session):
        return [
            asyncio.create_task(
                session.get(self.get_url_by_nacionality(dni), headers=HEADERS, ssl=False)
            )
            for dni in self.dni_list
        ]

    async def run_extraction(self):
        async with aiohttp.ClientSession() as session:
            tasks = self._get_task(session)
            responses = await asyncio.gather(*tasks)
            for res in responses:
                html_content = await res.text()
                dni = get_dni_from_query(res.url.query)
                payload = (html_content, dni)
                self.results.append(payload)

    def start(self):
        start = time.time()
        asyncio.run(self.run_extraction())
        end = time.time()
        total_time = end - start
        logger.info(f" Time to extract {len(self.dni_list)} dni, it took: {total_time}")


class CneParser:

    def __init__(self, html_content, dni):
        self.html_content = BeautifulSoup(html_content, "html.parser")
        self.dni = dni

    def get_name(self):
        return self.html_content.select_one(data_selectors.name).text

    def get_state(self):
        return self.html_content.select_one(data_selectors.state).text

    def get_municipality(self):
        return self.html_content.select_one(data_selectors.municipality).text

    def get_parish(self):
        return self.html_content.select_one(data_selectors.parish).text

    def get_data(self):
        data = {"name": None, "state": None, "municipality": None, "parish": None}
        try:
            data["name"] = self.get_name()
            data["state"] = self.get_state()
            data["municipality"] = self.get_municipality()
            data["parish"] = self.get_parish()
            return data
        except:
            logger.warning(f" Dni {self.dni} not found")
            return None
