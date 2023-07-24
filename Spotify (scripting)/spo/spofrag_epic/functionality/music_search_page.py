from spo.spofrag_epic.page_object.music_search_pom import MusicSearchPOM as music_search_pom
from spo.spofrag_common_handler.ui_action_handler import UIActionHandler as ui_handler


class MusicSearchPage(music_search_pom):
    driver_factory = None

    def __init__(self, driver_factory):
        super().__init__(driver_factory)
        self.driver_factory = driver_factory

    def search_by_term(self, search_term: str):
        ui_handler.send_key_to_element(self, music_search_pom.get_txt_search(self), search_term)

    def click_on_play_btn_at_top_result(self):
        ui_handler.hover_over_element(self, music_search_pom.get_btn_play_at_top_result(self))
        ui_handler.click_on_element(self, music_search_pom.get_btn_play_at_top_result(self))
