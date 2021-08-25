---
title: Assignments
layout: page
assignments:
  - date: 2021-08-21
    number: 1
    path: assignment1.pdf
---

<ol>
{% for assignment in page.assignments %}
    <li>
        <a href="{{ assignment.url }}"> Assignment {{assignment.number}} ({{assignment.date | date: '%B %d' }})</a>
    </li>
{% endfor %}
</ol>
