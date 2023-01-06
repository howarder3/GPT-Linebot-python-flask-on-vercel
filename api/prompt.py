import os
import variables

chat_language = variables.INIT_LANGUAGE

MSG_LIST_LIMIT = variables.MSG_LIST_LIMIT
LANGUAGE_TABLE = {
  "zh": "哈囉！",
  "en": "Hello!"
}

class Prompt:
    def __init__(self):
        self.msg_list = []
        self.msg_list.append(f"AI:{LANGUAGE_TABLE[chat_language]}")
    
    def add_msg(self, new_msg):
        if len(self.msg_list) >= MSG_LIST_LIMIT:
            self.remove_msg()
        self.msg_list.append(new_msg)

    def remove_msg(self):
        self.msg_list.pop(0)

    def generate_prompt(self):
        return '\n'.join(self.msg_list)
