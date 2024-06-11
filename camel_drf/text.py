import re

CAMEL_REGEX = re.compile('(?<=.)_(\\w)')
SNAKE_REGEX = re.compile('(?<=[a-z])([A-Z])')


def match_camel(match):
    return match.group(1).upper()


def match_snake(match):
    return f'_{match.group(1).lower()}'

def convert_data(regex, processor):
    def convert(data):
        if isinstance(data, dict):
            return {regex.sub(processor, k): convert(v) for k, v in data.items()}
        elif isinstance(data, list):
            return [convert(datum) for datum in data]
        else:
            return data
    return convert

to_snake_data = convert_data(SNAKE_REGEX, match_snake)
to_camel_data = convert_data(CAMEL_REGEX, match_camel)