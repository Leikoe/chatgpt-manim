from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService
# from manim_voiceover.services.recorder import RecorderService


class ChatGPTVideo(VoiceoverScene):
    def construct(self):
        self.set_speech_service(GTTSService()) # set the speech service, will be replacing with RecorderService()

        # # Create title
        # title = Text("Large Language Models (LLMs)", font_size=48)
        # self.play(Write(title))
        # self.wait(1)
        # self.play(FadeOut(title))

        # with self.voiceover(text="You might have heard of chatGPT. ChatGPT is an assistant which can help you with a variety of tasks. \
        #                     It can generate text, answer questions, and even write code.") as tracker:
        #     image = ImageMobject("assets\ChatGPT_logo.svg.png")  # Replace with your image file name
        #     self.play(FadeIn(image.scale(0.5)))
        #     chatgpt_label = Text("ChatGPT", font_size=24).next_to(image, DOWN)
        #     self.play(Write(chatgpt_label))
        # self.play(FadeOut(image))
        # self.play(FadeOut(chatgpt_label))

        # with self.voiceover(text="In this video, we are going to see how ChatGPT and other Large Language Models work on a high level.") as tracker:
        #     title = Text("Large Language Models (LLMs)", font_size=48)
        #     self.play(Write(title))
        # self.play(title.animate.to_edge(UP))

        # with self.voiceover(text="GPT stands for Generative Pretrained Transformer. It's a machine learning model whose goal is to predict the next token in a sentence.") as tracker:
        #     text = Text("Generative Pretrained Transformer", font_size=36)
        #     self.play(Write(text))
        # self.play(FadeOut(text))

        # # Create GPT model representation
        # with self.voiceover(text="This is our GPT model.") as tracker:
        #     model = Rectangle(width=4, height=2, color=BLUE)
        #     model_label = Text("GPT Model", font_size=24).next_to(model, DOWN)
        #     self.play(Create(model), Write(model_label))

        # # Create initial incomplete sentence
        # with self.voiceover(text="And this is our prompt. Prompt is the initial text to complete using the model.") as tracker:
        #     sentence = Text("The quick brown fox jumps over the", font_size=32)
        #     sentence.next_to(model, UP, buff=0.5)
        #     self.play(Write(sentence))

        # # Iterate token generation
        # with self.voiceover(text="We pass the prompt through the model, the model then predicts the next word. We then concatenate this new word to the end of our prompt and repeat the process until satisfied.") as tracker:
        #     for next_token_str in [" lazy", " dog", "."]:
        #         # Highlight the current sentence
        #         self.play(sentence.animate.set_color(YELLOW))

        #         # Move the sentence into the model
        #         self.play(sentence.animate.move_to(model))

        #         # Generate the next token
        #         next_token = Text(f" {next_token_str}", font_size=32, color=GREEN)
        #         next_token.next_to(model, DR, buff=0.5)
        #         self.play(TransformFromCopy(model, next_token))

        #         # Add the next token to the sentence
        #         self.play(sentence.animate.next_to(next_token, LEFT, buff=0.1))
        #         sentence_copy = sentence.copy()
        #         sentence_copy.set_color(WHITE)
        #         self.add(sentence_copy)
        #         self.remove(sentence)
        #         sentence = VGroup(sentence_copy, next_token)

        #         # Move the updated sentence back to the left of the model
        #         self.play(sentence.animate.next_to(model, UP, buff=0.5))

        # # Final sentence
        # with self.voiceover(text="We then end up with our finished sentence or text.") as tracker:
        #     final_sentence = Text("The quick brown fox jumps over the lazy dog.", font_size=32)
        #     final_sentence.next_to(model, UP, buff=0.5)
        #     self.play(TransformMatchingShapes(sentence, final_sentence))
        #     self.wait(1)


        #     # Fade out everything except the final sentence
        #     self.play(
        #         *[FadeOut(mob) for mob in self.mobjects if mob != final_sentence],
        #         final_sentence.animate.move_to(ORIGIN)
        #     )
        #     self.wait(2)
        # self.play(FadeOut(final_sentence))
        
        # tokenization
        # with self.voiceover(text="Well, I might have lied a little bit. In reality each token is passed as a whole number to the model. The process of transforming the sentence into a list of tokens is called Tokenization.") as tracker:
        #     sowy = Text("Well, I might have lied a little bit.", font_size=36)
        #     self.play(Write(sowy))
        #     self.wait(2)
        #     self.play(FadeOut(sowy))

        #     # take a sentence and display the list of token ids under the sentence with an arrow
        #     sentence = "The quick brown fox jumps over the lazy dog."
        #     # "The"=791, " quick"=4062, " brown"=14198, " fox"=39935, " jumps"=35308, " over"=927, " the"=279, " lazy"=16053, " dog"=5679, "."=13
        #     tokens = ["The", " quick", " brown", " fox", " jumps", " over", " the", " lazy", " dog", "."]
        #     token_ids = [791, 4062, 14198, 39935, 35308, 927, 279, 16053, 5679, 13]

        #     # Process each word
        #     token_texts = [Text(word, font_size=32) for word in tokens]
        #     id_texts = [Text(str(id), font_size=32, color=BLUE) for id in token_ids]

        #     sentence = VGroup(*token_texts).arrange(RIGHT, center=False, aligned_edge=LEFT, buff=1)
        #     self.play(Write(sentence.move_to(ORIGIN + UP*0.5)))

        #     ids = VGroup(*id_texts).arrange(RIGHT, center=False, aligned_edge=LEFT, buff=1)
        #     ids.next_to(sentence, DOWN, buff=1)

        #     # Animate tokenization
        #     for token_text, id_text in zip(token_texts, id_texts):
        #         self.play(TransformMatchingShapes(token_text.copy(), id_text))

        #     self.play(FadeOut(sentence))
        #     self.play(ids.animate.next_to(ids, UP, buff=1))
        #     self.play(FadeOut(ids))

        #     tokenization = Text("Tokenization", font_size=36)
        #     self.play(Write(tokenization))
        #     self.wait(1)
        #     self.play(FadeOut(tokenization))


        # Instruct Finetuning
        with self.voiceover(text="Let's talk about the finetuning process of these models. To take the model from being able to complete text to being a usefult assistant, we train the model on question answer pairs.") as tracker:
            title = Text("Finetuning", font_size=48)
            self.play(Write(title))
        self.play(FadeOut(title))

        json = """
{
    "instruction": "Natalia sold clips to 48 of her friends in April, and then she sold half as many clips in May.\n\t\tHow many clips did Natalia sell altogether in April and May?",
    "input": "",
    "output": "Natalia sold 48/2 = 24 clips in May.\n\t\tNatalia sold 48+24 = 72 clips altogether in April and May."
}
"""

        with self.voiceover(text="This is an example of such a Q/A pair from the gsm_8k dataset.") as tracker:
            example = Text(json, font_size=18)
            self.play(Write(example.move_to(ORIGIN)))
        self.play(FadeOut(example))


        