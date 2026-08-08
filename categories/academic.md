---
layout: default
title: Academic Life
permalink: /categories/academic/
---

<div class="page-intro">
  <h1>Academic Life</h1>
  <p>Research, teaching, and scholarship.</p>
</div>

{% assign posts = site.categories["academic"] %}
{% if posts and posts.size > 0 %}
{% include post-list.html %}
{% else %}
<p class="empty-state">No posts in this category yet.</p>
{% endif %}
