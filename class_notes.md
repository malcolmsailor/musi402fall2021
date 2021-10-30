---
title: Class notes
layout: page
class_notes:
  - date: 2021-09-02
    number: 1
    title:
    path: class_1_notes.pdf
  - date: 2021-09-16
    number: 5
    title: Diminutions
    path: class_5_notes.pdf
  - date: 2021-10-26
    number: 15
    title: Example midterm
    path: class_15_notes.pdf
  - date: 2021-10-28
    number: 16
    title: In-class example midterm (fragment)
    path: class_16_notes.pdf
---

{% if page.class_notes %}

<ol>
{% for notes in page.class_notes %}
    <li>
        <a href="assets/class_notes/{{ notes.path }}">{{notes.date | date: '%B %d' }}</a>{% if notes.title %}: {{notes.title}} {% endif %}
    </li>
{% endfor %}
</ol>
{% else %}

### Coming soon...

{% endif %}
