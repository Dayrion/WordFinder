import xml.etree.ElementTree as ET

# seekingLetters = ('s', 'q', 'd', 't', 'c', 'u', 'r', 's', 'a', 'o', 'c', 'k')
seekingLetters = ['o', 'd', 'a', 'q', 'r', 't', 'u', 'c']
# seekingLetters = ('d', 'â', 't', 'é', 'g', 'r')
wordLen = 7

if __name__ == '__main__':
    print("Parsing XML file...")
    tree = ET.parse("./words/Morphalou2/Morphalou-2.0.xml")
    print("XML file parsed")
    root = tree.getroot()
    idx = 0
    for category in root:
        if idx == 0:
            idx += 1
            continue
        wordCategory = 0
        for i in range(len(category)):
            if category[i].tag == "formSet":
                wordCategory = i
                break
        for word in category[wordCategory][0]:
            if word.tag == "orthography":
                present = len([letter for letter in seekingLetters for wordLetter in word.text if wordLetter == letter])
                if len(word.text) != wordLen or present != wordLen:
                    continue
                invalid = False
                cpy = seekingLetters
                for validLetter in word.text:
                    found = False
                    # wordIdx = 0
                    for testLetter in cpy:
                        if testLetter == validLetter:
                            found = True
                            # cpy[wordIdx] = ''
                            break
                        # wordIdx += 1
                    if found is False:
                        invalid = True
                        break
                if invalid is False:
                    print("Most probable word:", word.text)
