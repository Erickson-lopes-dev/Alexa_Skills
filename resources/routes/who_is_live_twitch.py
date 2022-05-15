from flask_restful import Resource
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

from resources.webdriver import get_webdriver


def check_live(driver: webdriver, streamer_name) -> dict:
    try:

        driver.get(f"https://www.twitch.tv/{streamer_name}")

        try:
            live = WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.XPATH,
                                                                                    '//*[@id="root"]/div/div[2]/div[1]/main/div[2]/div[3]/div/div/div[1]/div[1]/div[2]/div/div[1]/div/div/div/div[1]/div/div/div/a/div[2]/div/div/div/div/p')))

        except Exception:
            return {streamer_name: False}

    except Exception as error:
        return {"error": str(error)}
    texto = live.text

    if texto == "AO VIVO":
        return {streamer_name: True}
    else:
        return {"error": live.text}


class WhoIsLiveTwitch(Resource):
    @classmethod
    def get(cls):
        list_streamers = ['gaules', 'smurfdomuca']
        dict_streamers = {}

        driver = get_webdriver()

        for streamer in list_streamers:
            dict_streamers.update(check_live(driver, streamer))

        driver.close()

        return dict_streamers
