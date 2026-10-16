---
layout: about
title: Home
permalink: /
subtitle: Machine Learning Research • Multimodal Learning • Computer Vision
description: Shun-Hsiang Hsu is a UIUC Ph.D. student working on multimodal learning, computer vision, synthetic data, and LLM evaluation, with experience at Google and Reconstruct.

profile:
  align: left
  image: prof_pic.jpg
  image_circular: false # crops the image to make it circular
  more_info: >
    <p>Ph.D. Student · UIUC</p>
    <p>Expected graduation: 2027</p>
    <p>Champaign, Illinois</p>

selected_papers: true # includes a list of papers marked as "selected={true}"
social: true # includes social icons at the bottom of the page

announcements:
  enabled: false # includes a list of news items
  scrollable: true # adds a vertical scroll bar if there are more than 3 news items
  limit: 5 # leave blank to include all the news in the `_news` folder

latest_posts:
  enabled: false
  scrollable: true # adds a vertical scroll bar if there are more than 3 new posts items
  limit: 3 # leave blank to include all the blog posts
---

<style>
.about-panels {
  margin-top: 2rem;
  display: flex;
  flex-direction: column;
  gap: 2rem;
  --about-hero-border: #f4e3d7;
  --about-hero-bg: linear-gradient(135deg, #ffffff 0%, #fff6ea 60%, #ffe9d5 100%);
  --about-hero-text: #1c1f2a;
  --about-eyebrow: #6f7688;
  --about-card-border: #f0ebe5;
  --about-card-bg: #fffcf6;
  --about-card-heading: #1f2933;
  --about-card-text: #3a3f4b;
  --about-title: #0f172a;
  --about-strong: #101828;
}

.about-panels__intro {
  padding: 2rem;
  border-radius: 16px;
  border: 1px solid var(--about-hero-border);
  background: var(--about-hero-bg);
  box-shadow: 0 25px 45px rgba(15,23,42,0.08);
  color: var(--about-hero-text);
}

.about-panels__eyebrow {
  font-size: 0.8rem;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: var(--about-eyebrow);
  margin-bottom: 0.6rem;
}

.about-panels__title {
  font-size: clamp(1.5rem, 2.4vw, 2.1rem);
  margin: 0 0 1rem;
  color: var(--about-title);
}

.about-panels__grid {
  display: grid;
  grid-template-columns: minmax(0, 1fr);
  gap: 1.25rem;
}

.about-panels__card {
  padding: 1.5rem;
  border-radius: 14px;
  border: 1px solid var(--about-card-border);
  background: var(--about-card-bg);
  box-shadow: 0 16px 30px rgba(15,23,42,0.07);
}

.about-panels__card h3 {
  margin-top: 0;
  font-size: 1.1rem;
  color: var(--about-card-heading);
}

.about-panels__card p,
.about-panels__card li {
  color: var(--about-card-text);
  margin-bottom: 0.75rem;
}

.about-panels__list {
  padding-left: 1rem;
  margin: 0;
}

.about-panels__list strong {
  display: block;
  font-weight: 600;
  color: var(--about-strong);
}

@media (max-width: 991px) {
  .about-panels {
    clear: both;
    margin-top: 1.5rem;
  }
}

@media (max-width: 767px) {
  .post .profile.float-left,
  .post .profile.float-right {
    float: none !important;
    width: 100%;
    margin: 0 auto 1.5rem auto;
  }

  .post .profile img {
    display: block;
    margin-left: auto;
    margin-right: auto;
  }
}

[data-theme="dark"] .about-panels {
  --about-hero-border: rgba(255,255,255,0.1);
  --about-hero-bg: linear-gradient(135deg, rgba(40,32,25,0.95), rgba(29,28,39,0.98));
  --about-hero-text: #fdf8ef;
  --about-eyebrow: #f0e1d2;
  --about-card-border: rgba(255,255,255,0.1);
  --about-card-bg: rgba(46,38,33,0.92);
  --about-card-heading: #fef5e7;
  --about-card-text: #f0e1d2;
  --about-title: #fef5e7;
  --about-strong: #fff2d5;
}
</style>

<div class="about-panels">
  <div class="about-panels__intro">
    <h2 class="about-panels__title">Machine learning for visual understanding and reasoning</h2>
    <p>I am a Ph.D. student in <strong>Construction Engineering and Management</strong> at the University of Illinois Urbana-Champaign, working in the <a href="https://raamac.cee.illinois.edu/">RAAMAC Lab</a>. My research spans <strong>multimodal learning, computer vision, and geometry-grounded synthetic data</strong>, with applications in construction and infrastructure inspection.</p>
    <p>My work connects model and method development with controlled experiments, benchmarking, and data and training iteration. I also work on <strong>LLM evaluation and agent workflows</strong>, turning research ideas into usable systems.</p>
    <p class="mb-0"><a href="{{ '/assets/pdf/Shun_Hsiang_Hsu_Resume.pdf' | relative_url }}">Resume (PDF)</a> · <a href="{{ '/publications/' | relative_url }}">Publications &amp; research</a> · <a href="mailto:hsus2@illinois.edu">Email</a></p>
  </div>

  <div class="about-panels__grid">
    <section class="about-panels__card">
      <h3>Experience highlights</h3>
      <ul class="about-panels__list">
        <li>
          <strong>Google · Software Engineering Intern (PhD)</strong>
          Summer 2026 · LLM evaluation and skill-based agent systems.
        </li>
        <li>
          <strong><a href="https://reconstructinc.com/">Reconstruct Inc.</a> · Computer Vision Engineer Intern</strong>
          Jan. 2024–May 2026 · Vision and 3D reconstruction benchmarks, model adaptation, and active-learning iteration.
        </li>
        <li>
          <strong>TryTech Co., Ltd. · Founder / Technical Lead</strong>
          Jan. 2021–present · LLM applications and human-AI workflows.
        </li>
      </ul>
    </section>

    <section class="about-panels__card">
      <h3>Education</h3>
      <ul class="about-panels__list">
        <li>
          <strong>Ph.D., Construction Engineering and Management</strong>
          University of Illinois Urbana-Champaign · 2022–present (expected 2027)
        </li>
        <li>
          <strong>Master of Computer Science</strong>
          University of Illinois Urbana-Champaign · 2023–2024
        </li>
      </ul>
    </section>

  </div>
</div>
