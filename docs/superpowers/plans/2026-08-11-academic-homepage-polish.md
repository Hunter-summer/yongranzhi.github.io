# Academic Homepage Polish Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Improve the existing English Academic Pages site without redesigning it, then publish a correct, searchable GitHub Pages build.

**Architecture:** Keep the current Jekyll theme and collections. Limit changes to site identity in `_config.yml`, homepage copy in `_pages/about.md`, navigation in `_data/navigation.yml`, and clearly malformed academic records. Add a focused Ruby validation script so configuration, links, navigation, YAML front matter, and template-remnant rules remain testable.

**Tech Stack:** Jekyll, Liquid, Markdown, YAML, Ruby standard library, GitHub Pages

## Global Constraints

- English-only site.
- Preserve the existing portrait, layout, and theme.
- Do not fabricate publications, awards, biography details, email addresses, or CV content.
- Use `url: https://hunter-summer.github.io` and `baseurl: /yongranzhi.github.io`.
- Preserve substantive academic records unless an item is clearly malformed or a template remnant.

---

### Task 1: Add regression validation for visible site identity

**Files:**
- Create: `test/validate_academic_site.rb`
- Test: `test/validate_academic_site.rb`

**Interfaces:**
- Consumes: `_config.yml`, `_pages/about.md`, `_data/navigation.yml`, collection Markdown files.
- Produces: a zero exit status only when required identity, URL, navigation, and front-matter invariants hold.

- [ ] **Step 1: Write the failing validation script**

Create assertions that require the canonical URL/base URL, `Hunter-summer` as the GitHub username, a professional site description, no `Guide` navigation entry, no malformed nested Markdown links on the homepage, unique teaching permalinks, valid YAML front matter, and absence of mojibake sequences such as `鈥` in publication titles.

- [ ] **Step 2: Run it to verify failure**

Run: `ruby test/validate_academic_site.rb`

Expected: non-zero status listing the current URL, GitHub username, description, Guide link, homepage-link, duplicate-permalink, and mojibake failures.

- [ ] **Step 3: Commit the failing test**

Run:

```bash
git add test/validate_academic_site.rb
git commit -m "test: validate academic site metadata"
```

### Task 2: Correct site identity, URLs, navigation, and homepage copy

**Files:**
- Modify: `_config.yml`
- Modify: `_pages/about.md`
- Modify: `_data/navigation.yml`
- Test: `test/validate_academic_site.rb`

**Interfaces:**
- Consumes: current verified academic profile links already present in `_config.yml`.
- Produces: consistent Jekyll canonical URLs, professional English identity text, and research-focused navigation.

- [ ] **Step 1: Apply minimal configuration changes**

Set the title to `Yongran Zhi | Academic Homepage`; describe the site as research in formation control, adaptive control, and flight control systems; use `https://hunter-summer.github.io` plus `/yongranzhi.github.io`; set the GitHub username to `Hunter-summer`; set `social.type` to `Person`, `social.name` to `Yongran Zhi`, and list the existing Google Scholar, ORCID, GitHub, and IEEE profile URLs.

- [ ] **Step 2: Replace the homepage copy**

Use two short paragraphs: current Ph.D. status and institution, followed by research interests. Add plain, valid Markdown links for Google Scholar, ORCID, IEEE, GitHub, and Publications. Do not add an email address because none is verified.

- [ ] **Step 3: Simplify navigation**

Keep Publications, Talks, and Education. Enable CV only if `_pages/cv.md` no longer contains template data; otherwise omit CV. Remove Guide.

- [ ] **Step 4: Run the focused validation**

Run: `ruby test/validate_academic_site.rb`

Expected: remaining failures are limited to malformed collection records handled in Task 3.

- [ ] **Step 5: Commit site identity changes**

Run:

```bash
git add _config.yml _pages/about.md _data/navigation.yml
git commit -m "fix: polish academic site identity and navigation"
```

### Task 3: Repair malformed publication, talk, and education metadata

**Files:**
- Modify: `_publications/2009-10-01-paper-title-number-1.md`
- Modify: `_publications/2010-10-01-paper-title-number-2.md`
- Modify: `_talks/2014-03-01-talk-3.md`
- Modify: `_teaching/2015-spring-teaching-2.md`
- Test: `test/validate_academic_site.rb`

**Interfaces:**
- Consumes: existing record titles, venues, dates, and URLs.
- Produces: parseable YAML front matter, readable punctuation, unique permalinks, and accurate degree labels.

- [ ] **Step 1: Repair encoding and YAML errors**

Replace mojibake dashes with ordinary hyphens in the first two publication titles. Repair the unmatched quote and stray `collection: publications` text inside the second talk title.

- [ ] **Step 2: Repair education metadata**

Give the doctoral entry the unique permalink `/teaching/2015-spring-teaching-2` and type `Ph.D.`. Change only grammatical wording such as `Stage of doctoral candidate` to `Ph.D. in Control Science and Engineering`; do not invent dates.

- [ ] **Step 3: Run the focused validation**

Run: `ruby test/validate_academic_site.rb`

Expected: PASS with a summary naming all checked files.

- [ ] **Step 4: Commit collection repairs**

Run:

```bash
git add _publications _talks _teaching test/validate_academic_site.rb
git commit -m "fix: repair academic record metadata"
```

### Task 4: Build, inspect generated SEO output, and publish

**Files:**
- Modify only if validation finds a defect: `_config.yml`, `_pages/about.md`, `_data/navigation.yml`
- Verify: `_site/index.html`, `_site/sitemap.xml`, `_site/robots.txt` when generated

**Interfaces:**
- Consumes: the corrected Jekyll source tree.
- Produces: a successful GitHub Pages-compatible build and a publishable branch.

- [ ] **Step 1: Install project dependencies if missing**

Run: `bundle install`

Expected: dependencies resolve using `Gemfile` without changing application code.

- [ ] **Step 2: Build the site**

Run: `bundle exec jekyll build --trace`

Expected: exit status 0 and generated `_site/index.html` plus `_site/sitemap.xml`.

- [ ] **Step 3: Inspect generated metadata and internal links**

Confirm the canonical URL uses `https://hunter-summer.github.io/yongranzhi.github.io/`, the meta description names Yongran Zhi's research areas, the sitemap uses the same base URL, and primary navigation links resolve under the project path.

- [ ] **Step 4: Run all validation again**

Run:

```bash
ruby test/validate_academic_site.rb
bundle exec jekyll build --trace
git diff --check master...HEAD
```

Expected: all commands exit 0.

- [ ] **Step 5: Publish the branch and open a pull request**

Push `codex/academic-homepage-polish`, open a pull request into `master`, verify GitHub Pages checks, then merge after checks pass. Confirm the deployed site and `/sitemap.xml` respond publicly. Search-engine indexing may take days or weeks after publication.

