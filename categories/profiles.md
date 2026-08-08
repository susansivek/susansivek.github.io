---
layout: default
title: Profiles
permalink: /categories/profiles/
---

<div class="page-intro">
  <h1>Profiles</h1>
  <p>Interviews, guest features, and people-focused stories.</p>
</div>

{% assign posts = site.categories["profiles"] %}
{% if posts and posts.size > 0 %}
{% include post-list.html %}
{% else %}
<p class="empty-state">No posts in this category yet.</p>
{% endif %}
