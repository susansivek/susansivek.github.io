---
layout: default
title: Data Science and Tech
permalink: /categories/data-science/
---

<div class="page-intro">
  <h1>Data Science and Tech</h1>
  <p>Analytics, AI, ML, and applied data storytelling.</p>
</div>

{% assign posts = site.categories["data-science"] %}
{% if posts and posts.size > 0 %}
{% include post-list.html %}
{% else %}
<p class="empty-state">No posts in this category yet.</p>
{% endif %}
