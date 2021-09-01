---
title: Assignments
layout: page
---

{% if site.data.assignments %}

<ul>
{% for assignment in site.data.assignments %}
    <li>
        <a href="assets/assignments/{{ assignment.basename }}"> Assignment {{assignment.assignment_no}}</a> Due: {{assignment.assignment_date}}
    </li>
{% endfor %}
</ul>
{% else %}

### Coming soon...

{% endif %}
