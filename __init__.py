from mycroft import MycroftSkill, intent_file_handler


class PlayLms(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('lms.play.intent')
    def handle_lms_play(self, message):
        self.speak_dialog('lms.play')


def create_skill():
    return PlayLms()

