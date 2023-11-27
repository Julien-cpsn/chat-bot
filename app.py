#! /usr/bin/env python
# -*- encoding: UTF-8 -*-

"""Example: A Simple class to test dialogue and media"""
import os

import qi
import time
import sys
import argparse
import subprocess
import json

class LanguageManager:
    def __init__(self, session):
        ### Services ###

        print "Loading dialog services..."

        self.ALDialog = session.service("ALDialog")
        self.ALDialog.resetAll()
        self.ALDialog.setLanguage("English")

        self.loaded_topics = {}

        self.loadTopic("Chat")

        #self.loadTopic("Introduction")

        print "Dialog services loaded!"
        pass

    def setLanguage(self, language):
        print "Change language >", language

        topics = self.ALDialog.getAllLoadedTopics()
        self.ALDialog.setLanguage(language)

        for topic_name in topics:
            if topic_name in self.loaded_topics:
                self.loadTopic(topic_name)

    def loadTopic(self, topic_name):
        print "Loading topic >", topic_name

        language = self.ALDialog.getLanguage().lower()[:2]
        file_path = "/home/nao/.local/share/PackageManager/apps/chat_bot/dialogs/" + topic_name.lower() + "_" + language + ".top"

        loaded_topic = self.ALDialog.loadTopic(file_path)

        self.loaded_topics[topic_name] = loaded_topic
        self.ALDialog.activateTopic(self.loaded_topics[topic_name])
        self.ALDialog.subscribe(self.loaded_topics[topic_name])

    def unloadTopic(self, topic_name):
        print "Unloading topic >", topic_name

        # stopping the dialog engine
        self.ALDialog.unsubscribe(topic_name)

        # Deactivating the topic
        topic = self.loaded_topics[topic_name]
        self.ALDialog.deactivateTopic(topic)
        self.ALDialog.unloadTopic(topic)
        del self.loaded_topics[topic_name]

    def unloadAllTopics(self):
        print "Unloading all topics"

        for topic_name in self.ALDialog.getAllLoadedTopics():
            if topic_name in self.loaded_topics:
                try:
                    self.unloadTopic(topic_name)
                except:
                    continue


class AlignmentMatrix:
    def __init__(self, session):
        ### Services ###

        print "Loading alignment matrix services..."

        self.audio_player = session.service("ALAudioPlayer")
        self.tts = session.service("ALTextToSpeech")

        print "Alignment matrix loaded!"
        pass

    def lawful_good(self):
        print "Action > lawful good"

        time.sleep(2)
        audio_file = self.audio_player.loadFile("/home/nao/.local/share/PackageManager/apps/chat_bot/sounds/happy.wav")
        self.audio_player.play(audio_file, _async=True)

        os.system('python animations/hug.py')
        pass

    def neutral_good(self):
        print "Action > neutral good"
        os.system('python animations/wave.py')
        pass

    def chaotic_good(self):
        print "Action > chaotic good"

        self.tts.say("Ciao tutti antifacisti", _async=True)
        os.system('python animations/clap.py')

        pass

    def lawful_neutral(self):
        print "Action > lawful neutral"
        os.system('python animations/bow.py')
        pass

    def true_neutral(self):
        print "Action > true neutral"
        os.system('python animations/stare.py')
        pass

    def chaotic_neutral(self):
        print "Action > chaotic neutral"
        os.system('python animations/1312.py')
        pass

    def lawful_evil(self):
        print "Action > lawful evil"
        os.system('python animations/ring.py')
        pass

    def neutral_evil(self):
        print "Action > neutral evil"
        os.system('python animations/pingpong.py')
        pass

    def chaotic_evil(self):
        print "Action > chaotic evil"
        os.system('python animations/unspeakable.py')
        pass


class Main:
    def __init__(self, session):
        """
        This example uses the showImage method.
        To Test ALTabletService, you need to run the script ON the robot.
        """

        try:
            ### Services ###

            self.tablet_service = session.service("ALTabletService")
            self.memory = session.service("ALMemory")

            self.alignment_matrix = AlignmentMatrix(session)
            self.alignment_matrix_services = session.registerService("AlignmentMatrix", self.alignment_matrix)

            self.language_manager = LanguageManager(session)
            self.language_manager_service = session.registerService("LanguageManager", self.language_manager)

            ### Subscribers ###

            self.play_sfr_subscriber = self.memory.subscriber("play_sfr")
            self.play_sfr_subscriber.signal.connect(self.play_sfr)

            ### Settings ###

            self.tablet_service.setBrightness(1.0)
            self.tablet_service.setVolume(10)

            ### Web view ###

            self.dialog_subscriber = self.memory.subscriber("test")
            self.dialog_subscriber.signal.connect(self.test)

            self.tablet_service.showWebview("http://198.18.0.1/apps/chat_bot/index.html")

        except Exception, e:
            print "Error was: ", e

    def test(self, content):
        print len(content)
        print ">", content
        #self.queryChatGPT(content)

    def run(self):
        """
        Main runtime
        """
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            self.language_manager.unloadAllTopics()
            sys.exit(0)

    def play_sfr(self, _):
        print "Clicked on SFR"
        self.tablet_service.playVideo("http://198.18.0.1/apps/chat_bot/SFR.mp4")
        time.sleep(4)
        self.tablet_service.stopVideo()

    def queryChatGPT(self, query):
        response = subprocess.check_output([
            """curl -s https://api.openai.com/v1/chat/completions \\
              -H \"Content-Type: application/json\" \\
              -H \"Authorization: Bearer ***REMOVED***\" \\
              -d '{
                \"model\": \"gpt-3.5-turbo\",
                \"messages\": [
                  {
                    \"role\": \"system\",
                    \"content\": \"You are a joyful and helpful assistant robot.\"
                  },
                  {
                    \"role\": \"user\",
                    \"content\": \"%s\"
                  }
                ]
              }'""" % query],
            shell=True
        )

        response_data = json.loads(response)

        if 'choices' in response_data:
            text = response_data['choices'][0]['message']['content']

            print text
            return text
        else:
            print response_data
            return "error"


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="127.0.0.1",
                        help="Robot IP address. On robot or Local Naoqi: use '127.0.0.1'.")
    parser.add_argument("--port", type=int, default=9559,
                        help="Naoqi port number")

    args = parser.parse_args()
    qi_session = qi.Session()
    try:
        qi_session.connect("tcp://" + args.ip + ":" + str(args.port))
    except RuntimeError:
        print (
                "Can't connect to Naoqi at ip \"" + args.ip + "\" on port " + str(args.port) + ".\n"
                                                                                               "Please check your script arguments. Run with -h option for help."
        )
        sys.exit(1)

    app = Main(qi_session)
    app.run()
