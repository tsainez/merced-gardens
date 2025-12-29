---
title: Project Status
layout: page
description: Progress updates for Merced Gardens
bodyClass: page-status
---

<div class="mb-5">
  <h2>Are we active? Yes.</h2>
  <p class="lead">We post dated updates so you can see our momentum and hold us accountable as we build Merced Gardens.</p>
  <p>These milestones cover incorporation, land conversations, planning, and fundraising. If you want more detail or to help with a next step, <a href="/contact/">reach out</a>—we love collaborating with neighbors, partners, and supporters.</p>
</div>

<section class="mb-5">
  <h3 class="mb-3">Latest milestone</h3>
  {% assign latest = site.data.status_updates | sort: 'date' | last %}
  <div class="highlight mb-4">
    <div class="text-muted">{{ latest.date | date: "%B %-d, %Y" }}</div>
    <h4 class="mb-2">{{ latest.title }}</h4>
    <p class="mb-2">{{ latest.summary }}</p>
    <p class="mb-0"><strong>Next step:</strong> {{ latest.next_step }}</p>
  </div>
</section>

<section>
  <h3 class="mb-3">All updates</h3>
  <div class="status-grid">
    {% assign updates = site.data.status_updates | sort: 'date' | reverse %}
    {% for update in updates %}
    <article class="status-card mb-4">
      <div class="text-muted">{{ update.date | date: "%B %-d, %Y" }}</div>
      <h4 class="mt-1 mb-2">{{ update.title }}</h4>
      <p class="mb-2">{{ update.summary }}</p>
      <p class="mb-0"><strong>Next step:</strong> {{ update.next_step }}</p>
    </article>
    {% endfor %}
  </div>
</section>

<div class="mt-5">
  <h3 class="mb-2">What we track</h3>
  <ul>
    <li>Formal steps like incorporation, board formation, and filings.</li>
    <li>Site and land conversations with the City and County.</li>
    <li>Planning milestones that shape the garden experience.</li>
    <li>Fundraising activity and sponsorship progress.</li>
  </ul>
</div>
