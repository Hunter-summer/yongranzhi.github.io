---
permalink: /
title: "Academic CV & Research"
description: "Academic CV of Yongran Zhi, Ph.D. researcher in Control Science and Engineering at Huazhong University of Science and Technology."
keywords: "Yongran Zhi, Carlton Zhi, HUST, control science, formation control, multi-agent systems, flight control"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

I am **Yongran Zhi** (Carlton Zhi), a Ph.D. researcher in Control Science and Engineering at Huazhong University of Science and Technology (HUST) in Wuhan, China.

My research focuses on reliable and intelligent control for multi-agent systems and unmanned aerial vehicles.

## Research interests

- Formation control and resilient multi-agent systems
- Adaptive, prescribed-time, and event-triggered control
- Flight control and fault-tolerant control of unmanned aerial vehicles

## Education

- **Ph.D. in Control Science and Engineering**, Huazhong University of Science and Technology, School of Artificial Intelligence and Automation, 2020–present
- **Bachelor's study**, Zhengzhou University, School of Electrical and Information Engineering, 2016–2020

## Selected Publications

{% assign publications = site.publications | sort: "date" | reverse %}
{% for publication in publications limit: 5 %}
1. [{{ publication.title }}]({{ publication.paperurl }})
   *{{ publication.venue }}*, {{ publication.date | date: "%Y" }}.
{% endfor %}

[View all publications]({{ '/publications/' | relative_url }})

## Academic Profiles

[Google Scholar](https://scholar.google.com.hk/citations?hl=zh-CN&pli=1&user=lUVD2egAAAAJ) · [ORCID](https://orcid.org/0000-0003-4521-7900) · [IEEE Author Profile](https://ieeexplore.ieee.org/author/37089999148) · [Scopus](https://www.scopus.com/authid/detail.uri?authorId=57667409500) · [GitHub](https://github.com/Hunter-summer)

[View the full CV]({{ '/cv/' | relative_url }})
