from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService
from manim import *

class MyAwesomeScene(VoiceoverScene):
    def construct(self):
        self.set_speech_service(GTTSService())

        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency

        with self.voiceover(text="This circle is drawn as I speak.") as tracker:
            self.play(Create(circle))