---
title: Playlists
layout: page
playlists:
  - date: 2021-08-21
    url: https://open.spotify.com/playlist/73tls5WCPGAeQh5lFGoov2?si=466e5b4245124dab
---

Links open in Spotify.

<ol>
{% for playlist in page.playlists %}
    <li>
        <a href="{{ playlist.url }}">{{playlist.date | date: '%B %d' }}</a>
    </li>
{% endfor %}
</ol>
