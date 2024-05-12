from manim import *


# "The"=791, " quick"=4062, " brown"=14198, " fox"=39935, " jumps"=35308, " over"=927, " the"=279, " lazy"=16053, " dog"=5679, "."=13
class Tokenization(Scene):
    def construct(self):
        # Sentence and its tokenization
        sentence = "The quick brown fox jumps over the lazy dog."
        tokens = ["The", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog", "."]
        token_ids = [791, 4062, 14198, 39935, 35308, 927, 279, 16053, 5679, 13]

        # Create text objects
        sentence_text = Text(sentence, font_size=36)
        self.play(Write(sentence_text))
        self.wait(1)

        # Process each word
        token_texts = [Text(word, font_size=36) for word in tokens]
        id_texts = [Text(str(id), font_size=36, color=BLUE) for id in token_ids]

        # Positioning
        sentence_text.to_edge(UP)
        group_tokens = VGroup(*token_texts).arrange(DOWN, aligned_edge=LEFT)
        group_ids = VGroup(*id_texts).arrange(DOWN, aligned_edge=RIGHT)

        group_tokens.next_to(sentence_text, DOWN, buff=1)
        group_ids.next_to(group_tokens, RIGHT, buff=1)

        # Animate tokenization
        for token_text, id_text in zip(token_texts, id_texts):
            self.play(ReplacementTransform(sentence_text.copy(), token_text))
            self.play(TransformMatchingShapes(token_text.copy(), id_text))
            self.wait(0.5)

        # Show final transformation
        self.play(
            ReplacementTransform(group_tokens, sentence_text),
            ReplacementTransform(group_ids, sentence_text)
        )
        self.wait(1)