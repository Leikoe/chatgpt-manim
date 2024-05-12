from manim import *

class Generation(Scene):
    def construct(self):
        # Create title
        title = Text("Large Language Models (LLMs)", font_size=48)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))

        # Create GPT model representation
        model = Rectangle(width=4, height=2, color=BLUE)
        model_label = Text("GPT Model", font_size=24).next_to(model, DOWN)
        self.play(Create(model), Write(model_label))

        # Create initial incomplete sentence
        sentence = Text("The quick brown fox", font_size=32)
        sentence.next_to(model, UP, buff=0.5)
        self.play(Write(sentence))

        # Iterate token generation
        for next_token_str in [" jumps", " over", " the", " lazy", " dog", "."]:
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
