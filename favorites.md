---
layout: default
title: Favorites
permalink: /favorites/
---

<div class="page-intro">
  <h1>Favorites</h1>
  <p>A short curated selection across beats and years.</p>
</div>

{% assign posts = site.posts | where: "featured", true %}
{% if posts.size == 0 %}
<p class="empty-state">No favorites selected yet.</p>
{% else %}
{% include post-list.html %}
{% endif %}
