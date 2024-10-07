playlist = dict(title='patagonia bus',
                author='colt steele',
                songs=[
                        {'title': 'song1', 'artists': ['blue'], 'duration': 2.5},
                        {'title': 'low', 'artists': ['nike, adidas'], 'duration': 2.5},
                        {'title': 'song2', 'artists': ['levi'], 'duration': 2.5},
                      ]
                )


for song in playlist['songs']:
    print(f"""song: {song['title']}
artists: {' '.join(song['artists'])}
duration: {song['duration']}
""")


