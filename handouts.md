---
title: Handouts
layout: page
handouts:
  - date: 2021-08-21
    path: handout1.pdf
    title: foobar
---

<!-- <ul>
  {% for handout in site.handouts %}
    <li>
      Handout {{handout.number}} ({{handout.date | date: '%B %d'}}): <a href="/assets/handouts/{{ handout.basename }}">{{handout.title}}</a>
    </li>
  {% endfor %}
</ul> -->

<ol>
{% for handout in page.handouts %}
    <li>
      {{handout.date | date: '%B %d'}}: <a href="/assets/handouts/{{ handout.basename }}">{{handout.title}}</a>
      </li>
{% endfor %}
</ol>
