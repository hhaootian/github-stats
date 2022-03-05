#!/usr/bin/env python
import json
import params


excluded = params.EXCLUDED
excluded = excluded.split(";")

lang_file = open("everything.lang").readlines()
langs = []
total = 0

for line in lang_file[4:]:
    if line[0] == "-":
        break

    lang_name = line[:25].strip()
    if lang_name in excluded:
        continue

    line = line[25:].split()
    num = sum(list(map(int, line[1:])))
    total += num
    langs.append([lang_name, num])

    # only use top 10
    if len(langs) == 10:
        break

langs = sorted(langs, key=lambda x: x[1], reverse=True)


def human_format(num):
    """convert number to human format
    e.g., 1000 to 1k
    """
    num = float('{:.3g}'.format(num))
    magnitude = 0
    while abs(num) >= 1000:
        magnitude += 1
        num /= 1000.0
    return '{}{}'.format(
        '{:f}'.format(num).rstrip('0').rstrip('.'),
        ['', 'K', 'M', 'B', 'T'][magnitude]
    )


with open('colors.json') as f:
    color_map = json.load(f)

# write to svg
lang_lists = []
with open("languages_template.svg", "r") as f:
    output = f.read()
    output = output.replace("XXX", human_format(total))

    delay_between = 150

    for i, (lang, num) in enumerate(langs):
        color = color_map[lang]['color'] if lang in color_map else "#000000"
        progress = (
            f'<span style="background-color: {color};'
            f'width: {num / total * 100:0.3f}%;" '
            f'class="progress-item"></span>'
        )
        lang_list = f"""
<li style="animation-delay: {i * delay_between}ms;">
<svg xmlns="http://www.w3.org/2000/svg" class="octicon" style="fill:{color};"
viewBox="0 0 16 16" version="1.1" width="16" height="16"><path
fill-rule="evenodd" d="M8 4a4 4 0 100 8 4 4 0 000-8z"></path></svg>
<span class="lang">{lang}</span>
<span class="percent">{num / total * 100:0.2f}%</span>
</li>
"""
        lang_lists.append(lang_list)
        output += progress

    output += "</span>\n</div>\n<ul>\n"
    for lang_list in lang_lists:
        output += lang_list

    output += "</ul>\n</div>\n</foreignObject>\n</g>\n</g>\n</svg>\n"

    with open("languages.svg", "w") as f:
        f.write(output)
