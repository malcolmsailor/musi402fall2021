---
title: Example work
layout: page
---

{% if site.data.sketches %}

<ul>
{% for sketch in site.data.sketches %}
    <li>
        <a href="assets/sketches/{{ sketch.basename }}">{{sketch.date}}</a> (for assignment {{sketch.assignment_no}})
    </li>
{% endfor %}
</ul>
{% else %}

### Coming soon...

{% endif %}
