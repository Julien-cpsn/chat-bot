#! /usr/bin/env python
# -*- encoding: UTF-8 -*-

"""Example: A Simple class to test dialogue and media"""
import os

import qi
import time
import sys
import argparse
import glob

class LanguageManager:
    def __init__(self, session):
        ### Topics ###

        self.ALDialog = session.service("ALDialog")
        self.ALDialog.resetAll()
        self.ALDialog.setLanguage("English")

        self.test_topic = self.ALDialog.loadTopic(
            "/home/nao/.local/share/PackageManager/apps/chat_bot/dialogs/introduction_en.top")
        self.ALDialog.activateTopic(self.test_topic)
        self.ALDialog.subscribe('Introduction')

    def setLanguage(self, language):
        print "Change language >", language
        self.ALDialog.setLanguage(language)

        print glob.glob("/home/nao/.local/share/PackageManager/apps/chat_bot/dialogs/*.top")


class AlignmentMatrix:
    def __init__(self, session):
        self.audio_player = session.service("ALAudioPlayer")
        self.tts = session.service("ALTextToSpeech")
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

            alignment_matrix = AlignmentMatrix(session)
            self.alignment_matrix = session.registerService("AlignmentMatrix", alignment_matrix)

            language_manager = LanguageManager(session)
            self.language_manager = session.registerService("LanguageManager", language_manager)

            ### Subscribers ###

            self.play_sfr_subscriber = self.memory.subscriber("play_sfr")
            self.play_sfr_subscriber.signal.connect(self.play_sfr)

            ### Settings ###

            self.tablet_service.setBrightness(1.0)
            self.tablet_service.setVolume(10)

            ### Web view ###

            self.tablet_service.showWebview("http://198.18.0.1/apps/chat_bot/index.html")

        except Exception, e:
            print "Error was: ", e

    def run(self):
        """
        Main runtime
        """
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            # stopping the dialog engine
            self.ALDialog.unsubscribe("Introduction")

            # Deactivating the topic
            self.ALDialog.deactivateTopic(self.test_topic)
            self.ALDialog.unloadTopic(self.test_topic)

            sys.exit(0)

    def play_sfr(self, _):
        print "Clicked on SFR"
        self.tablet_service.playVideo("http://198.18.0.1/apps/chat_bot/SFR.mp4")
        time.sleep(4)
        self.tablet_service.stopVideo()


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
