---
title: 'Blog'
description: 'Random blogs'
lang: en
---
## Blogs
<ul>
{% for post in site.posts %}
    <li>
      <a href="{{ post.url }}">{{ post.title }}</a>
    </li>
{% endfor %}
</ul>

## Athka (National Olympiad for Programming)
Checkout [Teqaniaat blog](https://teqaniaat.github.io/Teqaniaat/athka/)