from _04_dialog_manager.listeners.stop_skill_listener import setup_stop_event_handlers
from _04_dialog_manager.listeners.wikipedia_skill_listener import setup_wikipedia_event_handlers
from _04_dialog_manager.listeners.none_skill_listener import setup_none_event_handlers
from _04_dialog_manager.listeners.music_skill_listener import setup_music_event_handlers
from _04_dialog_manager.listeners.mensa_skill_listener import setup_mensa_event_handlers
from _04_dialog_manager.listeners.bot_listener import setup_bot_event_handlers

def setup_event_handlers():
    """
    calls all setup functions of available listeners
    """
    setup_none_event_handlers()
    setup_stop_event_handlers()
    setup_wikipedia_event_handlers()
    setup_music_event_handlers()
    setup_mensa_event_handlers()
    setup_bot_event_handlers()
