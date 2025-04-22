import os

class SessionData:
    """
    Global session data object to store configuration and state across the application.
    This follows the singleton pattern to ensure only one instance exists.
    """
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SessionData, cls).__new__(cls)
            cls._instance._initialize()
        return cls._instance
    
    def _initialize(self):
        """Initialize default values for session data"""
        self.download_path = None;
        self.set_download_path()
        self.current_screen = None
        self.user_id = None
        self.session_id = None
        
    def get_download_path(self):
        """Get the download path"""
        return self.download_path
    
    def set_download_path(self):
        """Set a new download path and create the directory if it doesn't exist"""
        # Get the current file path
        current_file_path = os.path.abspath(__file__)
        # Navigate up from util directory to newEmulator directory
        newEmulator_dir = os.path.dirname(os.path.dirname(current_file_path))
        # Create downloads directory path
        downloads_path = os.path.join(newEmulator_dir, "downloads")
        self.download_path = downloads_path
        # Create the directory if it doesn't exist
        os.makedirs(self.download_path, exist_ok=True)
