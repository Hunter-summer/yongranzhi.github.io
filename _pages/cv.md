---
layout: archive
title: "Curriculum Vitae"
permalink: /cv/
description: "Curriculum vitae of Yongran Zhi, including education, research interests, publications, and conference presentations."
keywords: "Yongran Zhi CV, Carlton Zhi CV, control science, HUST, publications"
author_profile: true
redirect_from:
  - /resume
---

{% include base_path %}

## Profile

Yongran Zhi (Carlton Zhi) is a postdoctoral research fellow in Control Science and Engineering at Huazhong University of Science and Technology. His research interests include formation control, resilient multi-agent systems, adaptive and event-triggered control, and flight control systems.

## Education

- **Ph.D. in Control Science and Engineering**, Huazhong University of Science and Technology, School of Artificial Intelligence and Automation, 2020.9–2026.6
- **Bachelor's study**, Zhengzhou University, School of Electrical and Information Engineering, 2016.9–2020.6

## Research interests

- Formation control of heterogeneous multi-agent systems
- Resilient control under deception, spoofing, and false-data-injection attacks
- Adaptive, prescribed-time, event-triggered, and fault-tolerant control
- Flight control of fixed-wing and flying-wing unmanned aerial vehicles

## Publications

{% assign publications = site.publications | sort: "date" | reverse %}
<ol>
{% for publication in publications %}
  <li><a href="{{ publication.paperurl }}">{{ publication.title }}</a>. <em>{{ publication.venue }}</em>, {{ publication.date | date: "%Y" }}.</li>
{% endfor %}
</ol>

## Conference presentations

{% assign talks = site.talks | sort: "date" | reverse %}
<ul>
{% for talk in talks %}
  <li>{{ talk.title }}. <em>{{ talk.venue }}</em>, {{ talk.location }}, {{ talk.date | date: "%Y" }}.</li>
{% endfor %}
</ul>

## Academic profiles

[Google Scholar](https://scholar.google.com.hk/citations?hl=zh-CN&pli=1&user=lUVD2egAAAAJ) · [ORCID](https://orcid.org/0000-0003-4521-7900) · [IEEE Author Profile](https://ieeexplore.ieee.org/author/37089999148) · [Scopus](https://www.scopus.com/authid/detail.uri?authorId=57667409500) · [Semantic Scholar](https://www.semanticscholar.org/author/Yongran-Zhi/2164571270)
