from .commands import register_commands_handlers
from .messages import register_messages_handlers

def register_all_handlers(dp):
    register_commands_handlers(dp)
    register_messages_handlers(dp)