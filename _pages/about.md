---
layout: about
title: Home
permalink: /
description: Shun-Hsiang Hsu — machine learning research and engineering in multimodal AI, computer vision, synthetic data, and LLM evaluation. UIUC Ph.D. student, expected 2027.
---

<section class="hero" aria-labelledby="hero-title">
  <div class="hero-copy">
    <p class="eyebrow">Shun-Hsiang Hsu <span class="eyebrow-divider" aria-hidden="true">/</span> UIUC</p>
    <h1 id="hero-title">Machine learning <br>research <span>&amp; engineering.</span></h1>
    <p class="hero-focus">Multimodal AI · Computer vision · LLM evaluation</p>
    <p class="hero-description">I develop and evaluate multimodal models, geometry-grounded synthetic data, and LLM agent workflows.</p>
    <div class="hero-actions">
      <a class="button button-primary" href="{{ '/assets/pdf/Shun_Hsiang_Hsu_Resume.pdf' | relative_url }}">{% include icon.liquid name='paper' %} Resume (PDF)</a>
      <a class="button button-secondary" href="#selected-work">Selected Work <span aria-hidden="true">↓</span></a>
    </div>
    <div class="profile-links" id="profiles" aria-label="Contact and profiles">
      <a href="mailto:hsus2@illinois.edu">{% include icon.liquid name='email' %}<span>Email</span></a>
      <a href="https://www.linkedin.com/in/shunhsianghsu/">{% include icon.liquid name='linkedin' %}<span>LinkedIn</span></a>
      <a href="https://scholar.google.com/citations?user=ZuBSYdwAAAAJ">{% include icon.liquid name='scholar' %}<span>Scholar</span></a>
      <a href="https://github.com/huhuman">{% include icon.liquid name='github' %}<span>GitHub</span></a>
    </div>
  </div>
  <aside class="hero-profile" aria-label="Education and affiliation">
    <img class="portrait" src="{{ '/assets/img/prof_pic.jpg' | relative_url }}" width="200" height="200" alt="Portrait of Shun-Hsiang Hsu" fetchpriority="high">
    <div class="profile-caption">
      <p class="profile-university">University of Illinois Urbana-Champaign</p>
      <p><strong>Ph.D. student</strong><span class="profile-field">Construction Engineering and Management</span><span class="muted">Expected 2027</span></p>
      <p><strong>Master of Computer Science</strong><span class="muted">2024</span></p>
      <a class="lab-link" href="https://raamac.cee.illinois.edu/">RAAMAC Lab {% include icon.liquid name='external' %}</a>
    </div>
  </aside>
</section>

<section class="section work-section" id="selected-work" aria-labelledby="work-title">
  <div class="section-heading"><h2 id="work-title">Selected Work</h2></div>
  <div class="work-list">
    {% for project in site.data.selected_work %}
      {% include work-row.liquid project=project %}
    {% endfor %}
  </div>
</section>

<section class="section experience-section" id="experience" aria-labelledby="experience-title">
  <div class="section-heading"><h2 id="experience-title">Experience</h2></div>
  <ol class="experience-timeline">
    {% for work in site.data.resume.work %}
      <li class="timeline-entry" id="{{ work.anchor | escape }}">
        <p class="timeline-date">{{ work.period | escape }}</p>
        <article class="timeline-content">
          <h3 class="company-heading">{{ work.name | escape }}{% if work.division %}<span class="company-unit">{{ work.division | escape }}{% if work.team %} · {{ work.team | escape }}{% endif %}</span>{% endif %}</h3>
          <p class="timeline-role">{{ work.position | escape }}</p>
          <ul class="timeline-highlights">
            {% for highlight in work.brief %}<li>{{ highlight | escape }}</li>{% endfor %}
          </ul>
          {% include skill-tags.liquid skills=work.skills %}
        </article>
      </li>
    {% endfor %}
  </ol>
</section>

<section class="section" aria-labelledby="research-title">
  <div class="section-heading">
    <h2 id="research-title">Selected Publications</h2>
    <a class="text-link" href="{{ '/publications/' | relative_url }}">All publications <span aria-hidden="true">↗</span></a>
  </div>
  {% include selected_papers.liquid %}
</section>
