from mycroft import MycroftSkill, intent_file_handler


class Hazillar(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('hazillar.intent')
    def handle_hazillar(self, message):
        self.speak_dialog('hazillar')


def create_skill():
    return Hazillar()

