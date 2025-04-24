from enum import Enum
from logger import Logger
from util.mock_emulator_data import switched_off, login, main_menu, first_workflow_queue, record_details, claim_details, select_options, workflow_images

class ScreenNames(Enum):
    OFF = "off"
    LOGIN = "login"
    MAIN_MENU = "main_menu"
    FIRST_WORKFLOW_QUEUE = "first_workflow_queue"
    RECORD_DETAILS = "record_details"
    CLAIM_DETAILS = "claim_details"
    SELECT_OPTIONS = "select_options"
    WORKFLOW_IMAGES = "workflow_images"
    SDS_LOADING = "sds_loading"

screens = {
    ScreenNames.OFF: {
        "image_url": "off.jpg",
        "navigations": {
            "START": ScreenNames.LOGIN
        },
        "extra_data": switched_off
    },
    ScreenNames.LOGIN: {
        "image_url": "login.jpg",
        "navigations": {
            "1": ScreenNames.MAIN_MENU,
            "9": ScreenNames.OFF
        },
        "extra_data": login
    },
    ScreenNames.MAIN_MENU: {
        "image_url": "main-menu.jpg",
        "navigations": {
            "1": ScreenNames.FIRST_WORKFLOW_QUEUE,
            "2": ScreenNames.MAIN_MENU,
            "3": ScreenNames.MAIN_MENU,
            "4": ScreenNames.MAIN_MENU,
            "5": ScreenNames.MAIN_MENU,
            "BACK": ScreenNames.LOGIN
        },
        "extra_data": main_menu
    },
    ScreenNames.FIRST_WORKFLOW_QUEUE: {
        "image_url": "first_workflow_queue.jpg",
        "navigations": {
            "1": ScreenNames.RECORD_DETAILS,
            "2": ScreenNames.FIRST_WORKFLOW_QUEUE,
            "3": ScreenNames.FIRST_WORKFLOW_QUEUE,
            "4": ScreenNames.FIRST_WORKFLOW_QUEUE,
            "5": ScreenNames.FIRST_WORKFLOW_QUEUE,
            "BACK": ScreenNames.MAIN_MENU
        },
        "extra_data": first_workflow_queue
    },
    ScreenNames.RECORD_DETAILS: {
        "image_url": "record_details.jpg",
        "navigations": {
            "A": ScreenNames.RECORD_DETAILS,
            "B": ScreenNames.RECORD_DETAILS,
            "C": ScreenNames.RECORD_DETAILS,
            "D": ScreenNames.CLAIM_DETAILS,
            "E": ScreenNames.RECORD_DETAILS,
            "F": ScreenNames.RECORD_DETAILS,
            "G": ScreenNames.RECORD_DETAILS,
            "H": ScreenNames.RECORD_DETAILS,
            "I": ScreenNames.RECORD_DETAILS,
            "J": ScreenNames.RECORD_DETAILS,
            "K": ScreenNames.RECORD_DETAILS,
            "L": ScreenNames.RECORD_DETAILS,
            "M": ScreenNames.RECORD_DETAILS,
            "N": ScreenNames.RECORD_DETAILS,
            "O": ScreenNames.RECORD_DETAILS,
            "BACK": ScreenNames.FIRST_WORKFLOW_QUEUE
        },
        "extra_data": record_details
    },
    ScreenNames.CLAIM_DETAILS: {
        "image_url": "claim_details.jpg",
        "navigations": {
            "M": ScreenNames.CLAIM_DETAILS,
            "P": ScreenNames.CLAIM_DETAILS,
            "R": ScreenNames.CLAIM_DETAILS,
            "F": ScreenNames.CLAIM_DETAILS,
            "V": ScreenNames.SELECT_OPTIONS,
            "O": ScreenNames.CLAIM_DETAILS,
            "BACK": ScreenNames.RECORD_DETAILS
        },
        "extra_data": None  # Will be populated from claim_details based on ID
    },
    ScreenNames.SELECT_OPTIONS: {
        "image_url": "select_options.jpg",
        "navigations": {
            "S": ScreenNames.SELECT_OPTIONS,
            "G": ScreenNames.SELECT_OPTIONS,
            "E": ScreenNames.SELECT_OPTIONS,
            "B": ScreenNames.SELECT_OPTIONS,
            "P": ScreenNames.SELECT_OPTIONS,
            "R": ScreenNames.SELECT_OPTIONS,
            "I": ScreenNames.WORKFLOW_IMAGES,
            "L": ScreenNames.SELECT_OPTIONS,
            "H": ScreenNames.SELECT_OPTIONS,
            "N": ScreenNames.SELECT_OPTIONS,
            "A": ScreenNames.SELECT_OPTIONS,
            "V": ScreenNames.SELECT_OPTIONS,
            "U": ScreenNames.SELECT_OPTIONS,
            "Y": ScreenNames.SELECT_OPTIONS,
            "BACK": ScreenNames.CLAIM_DETAILS
        },
        "extra_data": select_options
    },
    ScreenNames.WORKFLOW_IMAGES: {
        "image_url": "workflow_images.jpg",
        "navigations": {
            "A": ScreenNames.SDS_LOADING,
            "BACK": ScreenNames.SELECT_OPTIONS
        },
        "extra_data": workflow_images
    },
    ScreenNames.SDS_LOADING: {
        "image_url": "sds_loading.jpg",
        "navigations": {},
        "extra_data": {"status": "loading"}
    }
}

class Screens:
    def __init__(self):
        self.screens = screens
        self.current_screen = ScreenNames.OFF
        self.logger = Logger()
        self.claim_data_id = 1
        self.live_data_parsing = False

    def set_claim_data_id(self, id):
        self.claim_data_id = id

    def set_live_data_parsing(self, value):
        self.live_data_parsing = value

    def geturl(self, filename):
        return f'static/screenshots/{filename}'

    def navigate_to(self, screen_name):
        if screen_name in self.screens:
            self.current_screen = screen_name
            screen_data = self.screens[screen_name]
            
            # Handle claim details data based on ID
            extra_data = screen_data["extra_data"]
            if screen_name == ScreenNames.CLAIM_DETAILS:
                extra_data = claim_details
            
            # Convert navigation options to uppercase
            navigation_options = [opt.upper() for opt in screen_data["navigations"].keys()]
            
            return {
                "image_url": f"static/screenshots/{screen_data['image_url']}",
                "navigation_options": navigation_options,
                "screen_data": extra_data,
                "claim_data_id": self.claim_data_id,
                "is_live_data_parsing": self.live_data_parsing,
                "current_screen": screen_name.value
            }
        return None

    def process_navigation(self, key):
        current_screen_data = self.screens[self.current_screen]
        if key.upper() in current_screen_data["navigations"]:
            next_screen = current_screen_data["navigations"][key.upper()]
            return self.navigate_to(next_screen)
        return self.navigate_to(self.current_screen)

    def handle_input(self, input_str):
        input_str = str(input_str).strip().upper()  # Convert to uppercase
        
        # Handle data ID changes
        if input_str.startswith('DATA '):
            try:
                new_id = int(input_str.split()[1])
                self.set_claim_data_id(new_id)
                return self.navigate_to(self.current_screen)
            except:
                pass

        # Handle live data parsing changes
        if input_str.startswith('LIVEDATA '):
            try:
                new_value = bool(int(input_str.split()[1]))
                self.set_live_data_parsing(new_value)
                return self.navigate_to(self.current_screen)
            except:
                pass
        
        if input_str == "OFF":
            return self.navigate_to(ScreenNames.OFF)
        elif input_str == "START" or self.current_screen is None:
            return self.navigate_to(ScreenNames.LOGIN)

        current_screen_data = self.screens[self.current_screen]
        if input_str in current_screen_data["navigations"]:
            next_screen = current_screen_data["navigations"][input_str]
            return self.navigate_to(next_screen)
                
        print("Received invalid keystroke:", input_str)
        return self.navigate_to(self.current_screen)
