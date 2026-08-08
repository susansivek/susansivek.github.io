---
layout: default
title: Home
---

# Susan Currie Sivek, Ph.D.

Writing and editing portfolio — a collection of published articles, case studies, and reports.

<ul class="post-list">
{% for post in paginator.posts %}
  <li class="post-item">
    <span class="post-date">{{ post.date | date: "%b %Y" }}</span>
    <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
  </li>
{% endfor %}
</ul>

{% if paginator.next_page %}
<a href="{{ paginator.next_page_path | relative_url }}">Older posts &raquo;</a>
{% endif %}
{% if paginator.previous_page %}
<a href="{{ paginator.previous_page_path | relative_url }}">&laquo; Newer posts</a>
{% endif %}
