def recite(start, take=1):
    nums = (
        "no",
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
        "ten",
    )

    verses = []

    for i in range(start, start - take, -1):
        h_col = nums[i].title()  # Current number of bottles (in words)
        l_col = nums[i - 1]  # Next number of bottles (in words)

        # Determine singular/plural for "bottle"
        bottle_word = "bottle" if i == 1 else "bottles"
        next_bottle_word = "bottle" if i - 1 == 1 else "bottles"

        # Add the verse for the current number of bottles
        verses.append(f"{h_col} green {bottle_word} hanging on the wall,")
        verses.append(f"{h_col} green {bottle_word} hanging on the wall,")
        verses.append("And if one green bottle should accidentally fall,")
        verses.append(
            f"There'll be {l_col} green {next_bottle_word} hanging on the wall."
        )

        # Add an empty line after the verse, except after the last one
        if i - 1 > start - take:
            verses.append("")

    return verses
