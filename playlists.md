---
title: Playlists
layout: page
playlists:
  - date: 2021-09-09
    url: https://open.spotify.com/playlist/0FCp6ihXYtka08X3JVjs6Q?si=28c8feec552f4296
  - date: 2021-09-16
    url: https://open.spotify.com/playlist/7p79JCm0z9uB8U7SxY3nLD?si=d56e80ea68aa4118
  - date: 2021-09-23
    url: https://open.spotify.com/playlist/7y0EYbMTH7JtEN0EoJFOuD?si=159954882cbc4342
  - date: 2021-09-30
    url: https://open.spotify.com/playlist/25RtbUTxIEsb6td48R2wsh?si=5b18f05a6fcb4c23
  - date: 2021-10-7
    url: https://open.spotify.com/playlist/4lv1PfvsnZCuFKNwGggTTH?si=3494f6d27e074ec2
  - date: 2021-10-14
    url: https://open.spotify.com/playlist/56n3N5YgEc26sKBgdojgy7?si=804351c04f344758
  - date: 2021-10-21
    url: https://open.spotify.com/playlist/4mkHOPsFJHT7VQknikOAFo?si=e391828455a94730
  - date: 2021-11-04
    url: https://open.spotify.com/playlist/2t8gjR6SMRNv9kqz81EIkx?si=9cbc05331e124bcf
  - date: 2021-11-11
    url: https://open.spotify.com/playlist/0b2RmWbvlATLW7sI8YBjNT?si=dc5bac385cf74126
  - date: 2021-12-02
    url: https://open.spotify.com/playlist/6n66JILouy3GkunU7D33am?si=2a15db1478e44f01
---

Links open in Spotify. There is also a [playlist containing the tracks from all weeks](https://open.spotify.com/playlist/5LFat7Qmw1ZC7gaaytLaxX?si=ee3f9faa5cd84c55){:target="\_blank" rel="noreferrer noopener"}.

The playlist of versions of the B-flat major fugue from WTC 1 is [here](https://open.spotify.com/track/63Hj3FZGGLuBxpWv44Aqpw?si=058526f2ffb84e83).

{% if page.playlists %}

<ol>
{% for playlist in page.playlists %}
    <li>
        <a href="{{ playlist.url }}" target="_blank" rel="noreferrer noopener">{{playlist.date | date: '%B %d' }}</a>
    </li>
{% endfor %}
</ol>
{% else %}

### Coming soon...

{% endif %}
