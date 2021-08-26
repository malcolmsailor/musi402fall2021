---
title: Playlists
layout: page
playlists:
  - date: 2021-09-09
    url: https://open.spotify.com/playlist/0FCp6ihXYtka08X3JVjs6Q?si=28c8feec552f4296
---

Links open in Spotify. There is also a [playlist containing the tracks from all weeks](https://open.spotify.com/playlist/5LFat7Qmw1ZC7gaaytLaxX?si=ee3f9faa5cd84c55){:target="\_blank" rel="noreferrer noopener"}.

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
