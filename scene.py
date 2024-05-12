from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService
# from manim_voiceover.services.recorder import RecorderService


class ChatGPTVideo(VoiceoverScene):
    def construct(self):
        self.set_speech_service(GTTSService()) # set the speech service, will be replacing with RecorderService()

        # Create title
        title = Text("Large Language Models (LLMs)", font_size=48)
        self.play(Write(title))
        self.wait(1)
        self.play(FadeOut(title))

        with self.voiceover(text="You might have heard of chatGPT. ChatGPT is an assistant which can help you with a variety of tasks. \
                            It can generate text, answer questions, and even write code.") as tracker:
            image = ImageMobject("assets\ChatGPT_logo.svg.png")  # Replace with your image file name
            self.play(FadeIn(image.scale(0.5)))
            chatgpt_label = Text("ChatGPT", font_size=24).next_to(image, DOWN)
            self.play(Write(chatgpt_label))
        self.play(FadeOut(image))
        self.play(FadeOut(chatgpt_label))

        with self.voiceover(text="In this video, we are going to see how ChatGPT and other Large Language Models work on a high level.") as tracker:
            title = Text("Large Language Models (LLMs)", font_size=48)
            self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        with self.voiceover(text="GPT stands for Generative Pretrained Transformer. It's a machine learning model whose goal is to predict the next token in a sentence.") as tracker:
            text = Text("Generative Pretrained Transformer", font_size=36)
            self.play(Write(text))
        self.play(FadeOut(text))

        # Create GPT model representation
        with self.voiceover(text="This is our GPT model.") as tracker:
            model = Rectangle(width=4, height=2, color=BLUE)
            model_label = Text("GPT Model", font_size=24).next_to(model, DOWN)
            self.play(Create(model), Write(model_label))

        # Create initial incomplete sentence
        with self.voiceover(text="And this is our prompt. Prompt is the initial text to complete using the model.") as tracker:
            sentence = Text("The quick brown fox jumps over the", font_size=32)
            sentence.next_to(model, UP, buff=0.5)
            self.play(Write(sentence))

        # Iterate token generation
        with self.voiceover(text="We pass the prompt through the model, the model then predicts the next word. We then concatenate this new word to the end of our prompt and repeat the process until satisfied.") as tracker:
            for next_token_str in [" lazy", " dog", "."]:
                # Highlight the current sentence
                self.play(sentence.animate.set_color(YELLOW))

                # Move the sentence into the model
                self.play(sentence.animate.move_to(model))

                # Generate the next token
                next_token = Text(f" {next_token_str}", font_size=32, color=GREEN)
                next_token.next_to(model, DR, buff=0.5)
                self.play(TransformFromCopy(model, next_token))

                # Add the next token to the sentence
                self.play(sentence.animate.next_to(next_token, LEFT, buff=0.1))
                sentence_copy = sentence.copy()
                sentence_copy.set_color(WHITE)
                self.add(sentence_copy)
                self.remove(sentence)
                sentence = VGroup(sentence_copy, next_token)

                # Move the updated sentence back to the left of the model
                self.play(sentence.animate.next_to(model, UP, buff=0.5))

        return

        # Final sentence
        final_sentence = Text("The quick brown fox jumps over the lazy dog.", font_size=32)
        final_sentence.next_to(model, UP, buff=0.5)
        self.play(TransformMatchingShapes(sentence, final_sentence))
        self.wait(1)


        # Fade out everything except the final sentence
        self.play(
            *[FadeOut(mob) for mob in self.mobjects if mob != final_sentence],
            final_sentence.animate.move_to(ORIGIN)
        )
        self.wait(2)