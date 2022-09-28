import datetime

LOGGING = True


def log(text: str, mode="info"):
    if LOGGING:
        print(f"{'[+]' if mode == 'info' else '[-]' if mode == 'error' else '[!]' if mode == 'warning' else '[ ]'} {datetime.datetime.now()} {text}")
