from spo.spofrag_epic.page_object.track_pom import TrackPOM as track_pom
from spo.spofrag_common_handler.ui_action_handler import UIActionHandler as ui_handler


class TrackPage(track_pom):
    driver_factory = None

    def __init__(self, driver_factory):
        super().__init__(driver_factory)
        self.driver_factory = driver_factory

    def click_on_btn_play_track(self):
        ui_handler.click_on_element(self, track_pom.get_btn_play_track(self))
