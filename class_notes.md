---
title: Class notes
layout: page
class_notes:
  - date: 2021-08-21
    number: 1
    title: foobar
    path: notes1.pdf
  - date: 2021-08-22
    number: 1
    path: notes1.pdf
---

<ol>
{% for notes in page.class_notes %}
    <li>
        <a href="{{ notes.url }}">{{notes.date | date: '%B %d' }}</a>{% if notes.title %}: {{notes.title}} {% endif %}
    </li>
{% endfor %}
</ol>
