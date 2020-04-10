from data import data

answerDelimiter = "&nbsp;" * 20
anchorDelimiter = "<br>" * 40

markdown = ""

for key in data.keys():
    block = data[key]
    question = block[0]
    markdown += "## {}".format(question)
    markdown += """
"""

    answers = block[1:]

    for answer in answers:
        if len(answer) > 1:
            # This is the anchorLink
            try:
                # TODO change to regex later
                anchorLink = data[answer[1]][0].lower().replace(" ", "-").replace("?", "").replace(".", "").replace(":", "")
            except KeyError:
                raise KeyError("Could not find key ({}) in data.".format(answer[1]))

            # Create the answer text that points to the other section anchor link
            markdown += "[{}](#{})".format(answer[0], anchorLink)
            markdown += answerDelimiter
        else:
            try:
                markdown += answer[0]
            except IndexError:
                raise IndexError("There was no answer in the \"{}\" section".format(block[0]))

    markdown += anchorDelimiter
    markdown += """
"""

# Write to file and then we can copy/paste it
with open('./markdown.md','w') as f:
    f.write(markdown)
