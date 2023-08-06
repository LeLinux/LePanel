import json5 as json
from screeninfo import get_monitors




class Config:
    def __init__(self):
        panel_width = 0
        panel_height = 0
        panel_radius = 0
        active_widgets = {}
        


    def createDefaultConfig(self):
        display_size = get_monitors()

        config = {
            "panel_width" : display_size[0].width - 10,
            "panel_height" : 25,
            "panel_radius" : 12,
            "panel_position" : 0,
            "active_widgets": {
                "appmenu" : 1
            },
            "widgets_position":{
                "appmenu" : 850
            },
            "background_color" : "#FFFFFF",
            "text_color" : "#000000"
        }

        with open("config.json", "w") as write_file:
            json.dump(config, write_file)

    def readConfig(self):
        with open("config.json", "r") as read_file:
            config = json.load(read_file)

c = Config()
c.createDefaultConfig()
