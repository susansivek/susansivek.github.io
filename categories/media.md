---
layout: default
title: Media Industry
permalink: /categories/media/
---

<div class="page-intro">
  <h1>Media Industry</h1>
  <p>Magazines, journalism, and the business of publishing.</p>
</div>

{% assign posts = site.categories["media"] %}
{% if posts and posts.size > 0 %}
{% include post-list.html %}
{% else %}
<p class="empty-state">No posts in this category yet.</p>
{% endif %}
