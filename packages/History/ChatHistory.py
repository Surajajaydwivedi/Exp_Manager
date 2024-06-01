import json
from ..Utils.constants import CHAT_HISTORY_FILE, NAME_KEY, LAST_MESSAGE_ID_KEY, UNKNOWN_NAME,ID, IS_EXP

class ChatHistory:
    def __init__(self):
        try:
            with open(CHAT_HISTORY_FILE, 'r') as file:
                self.history = json.load(file)
        except FileNotFoundError:
            self.history = {}

    def update_user_list(self, user_list):
        for user in user_list:
            user_id = str(user[ID])
            user_name = user[NAME_KEY]
            if user_id not in self.history:
                self.history[user_id] = {NAME_KEY: user_name, LAST_MESSAGE_ID_KEY: None, IS_EXP: False}
            elif str(user_id) in self.history:
                print(user_id)

    def get_id(self, name):
        for user_id, user_data in self.history.items():
            if user_data[NAME_KEY] == name:
                return user_id
        return None

    def get_last_message(self, identifier):
        if isinstance(identifier, str):
            user_id = self.get_id(identifier)
        else:
            user_id = identifier
        if user_id in self.history:
            return self.history[user_id][LAST_MESSAGE_ID_KEY]
        else:
            return None

    def get_name(self, user_id):
        if user_id in self.history:
            return self.history[user_id][NAME_KEY]
        else:
            return UNKNOWN_NAME

    def update_last_message(self, user_id, last_message_id):
        if user_id in self.history:
            self.history[user_id][LAST_MESSAGE_ID_KEY] = last_message_id
        else:
            self.history[user_id] = {NAME_KEY: '', LAST_MESSAGE_ID_KEY: last_message_id, IS_EXP: False}

    def save_to_data(self):
        print()
        print()
        print()
        print()
        print()
        print()
        print(self.history)
        with open(CHAT_HISTORY_FILE, 'w') as file:
            json.dump(self.history, file, indent=4)

    def print_data(self):
        for user_id, user_data in self.history.items():
            print(f"ID: {user_id}, Name: {user_data[NAME_KEY]}, Last Message ID: {user_data[LAST_MESSAGE_ID_KEY]}, Is Expert: {user_data[IS_EXP]}")

    def get_is_exp(self, identifier):
        if isinstance(identifier, str):
            user_id = self.get_id(identifier)
        else:
            user_id = identifier
        if user_id in self.history:
            return self.history[user_id][IS_EXP]
        else:
            return None

    def set_is_exp(self, identifier, is_exp=True):
        if isinstance(identifier, str):
            user_id = self.get_id(identifier)
        else:
            user_id = identifier
        if user_id in self.history:
            self.history[user_id][IS_EXP] = is_exp
        else:
            print("User not found in history.")

# Example usage:
# chat_history = ChatHistory()
# chat_history.set_is_exp('John', True)
# print(chat_history.get_is_exp('John'))
# chat_history.set_is_exp(12345, True)
# print(chat_history.get_is_exp(12345))
