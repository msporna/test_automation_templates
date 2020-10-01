import os


class Config:
    """
    it attempts to take each configurable value from env variables
    if not found, default is used (usable for local testing - don't specify env variables, just use defaults
    however-remember that this file goes to git, so mind other team members when doing changes to defaults)
    """
    app_host = os.getenv("API_HOST","http://localhost:3000")
