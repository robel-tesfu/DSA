class Solution:
    def fullJustify(self, words, maxWidth):
        result = []
        i = 0

        while i < len(words):
            # Find how many words fit in the current line
            line_length = len(words[i])
            j = i + 1

            while j < len(words) and line_length + 1 + len(words[j]) <= maxWidth:
                line_length += 1 + len(words[j])
                j += 1

            line_words = words[i:j]

            # Total letters (without spaces)
            letters = sum(len(word) for word in line_words)

            # Last line or single word
            if j == len(words) or len(line_words) == 1:
                line = " ".join(line_words)
                line += " " * (maxWidth - len(line))

            else:
                gaps = len(line_words) - 1
                total_spaces = maxWidth - letters

                even_spaces = total_spaces // gaps
                extra_spaces = total_spaces % gaps

                line = ""

                for k in range(gaps):
                    line += line_words[k]
                    line += " " * even_spaces

                    if k < extra_spaces:
                        line += " "

                line += line_words[-1]

            result.append(line)
            i = j

        return result