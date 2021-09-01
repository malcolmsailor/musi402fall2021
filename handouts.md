---
title: Handouts
layout: page
---

{% if site.data.handouts %}

<ul>
{% for handout in site.data.handouts %}
    <li>
      Handout {{handout.handout_no}} ({{handout.handout_date}}): <a href="assets/handouts/{{ handout.basename }}">{{handout.title}}</a>
      </li>
{% endfor %}
</ul>
{% else %}

### Coming soon...

{% endif %}
