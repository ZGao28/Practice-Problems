class Solution:
    def entityParser(self, text: str) -> str:
        converter = {
            "&quot;": "\"",
            "&apos;": "'",
            "&amp;": "&",
            "&gt;": ">",
            "&lt;": "<",
            "&frasl;": "/"
        }
        i = 0
        while i < len(text): 
            if text[i] == '&':
                j = i + 1
                while j < len(text):
                    if text[j] == ';' and text[i:j+1] in converter:
                        text = text[:i] + converter[text[i:j+1]] + text[j+1:]
                        break
                    if text[j] == '&':
                        break
                    j += 1
            i += 1
        return text
