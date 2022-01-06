def recite(start, take=1):
    song = [ver(i) + [""] for i in range(start, start - take, -1)]
    return [line for x in song for line in x][:-1]


def ver(n):
    return [f"{beer(n).capitalize()} on the wall, {beer(n)}.",
            (f"Take {'one' if n > 1 else 'it'} down and pass it around" if n else "Go to the store and buy some more") + f", {beer(n-1)} on the wall."]


def beer(x):
    return f"{'99' if x == -1 else x if x else 'no more'} bottle{'s' if x != 1 else ''} of beer"
