import re

all_patterns = {'h1': r'^\s*# (.*)$', 'h2': r'^\s*## (.*)$',
                'h3': r'^\s*### (.*)$', 'h4': r'^\s*#### (.*)$',
                'h5': r'^\s*##### (.*)$', 'h6': r'^\s*###### (.*)$',
                #
                'li': r'^\* (.*)',
                'p': r'^([^<\n].*)',
                'strong': r'__(.*)__',
                'ul': r'(<li>.*?</li>)(?![\n]*<li>)',
                'em': r'_(.*)_'}

duplicate = {'ul': re.DOTALL}


def txt_func(txt, tag): return f'<{tag}>{txt}</{tag}>'


def parse(markdown):
    for tag, pattern in all_patterns.items():

        markdown = re.sub(pattern, txt_func(r'\1', tag),
                          markdown, flags=re.MULTILINE | duplicate.get(tag, 0))

    return markdown.replace('\n', '')
