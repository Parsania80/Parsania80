<p>
<picture>
  <source media="(max-width: 640px) and (prefers-color-scheme: light)" srcset="assets/hero-mobile-light.svg">
  <source media="(max-width: 640px)" srcset="assets/hero-mobile-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="assets/hero-light.svg">
  <img src="assets/hero-dark.svg" alt="Mohammadreza Parsania — Backend Developer at EEPACO. C++, PostgreSQL, real-time systems, and software delivery." width="100%">
</picture>
</p>

<p align="center">
  <a href="https://www.linkedin.com/in/parsania80/"><img src="assets/linkedin.svg" alt="Connect on LinkedIn" height="36"></a>
  <a href="mailto:parsania80@gmail.com"><img src="assets/email.svg" alt="Email parsania80@gmail.com" height="36"></a>
  <a href="tel:+989396003945"><img src="assets/phone.svg" alt="Call +98 939 600 3945" height="36"></a>
  <a href="https://github.com/Parsania80?tab=repositories"><img src="assets/opensource.svg" alt="Explore my open source" height="36"></a>
</p>

<p align="center">
  <a href="#selected-work">Selected work</a> &nbsp; / &nbsp;
  <a href="#engineering-at-forg">Engineering at FORG</a> &nbsp; / &nbsp;
  <a href="#research">Research</a> &nbsp; / &nbsp;
  <a href="#stack">Stack</a> &nbsp; / &nbsp;
  <a href="#activity">Activity</a> &nbsp; / &nbsp;
  <a href="#lets-connect">Contact</a>
</p>

I’m **Mohammadreza Parsania**, a backend developer at **EEPACO**, working on **FORG**, a mobile device management platform. My work spans C++ services, PostgreSQL, real-time communication, testing, and the tooling that gets software onto servers.

Outside my company work, I build products of my own: **Daily Planner** with Flutter, **FluxGet** with Go, and **parsBackUp** with Rust. I also publish my master’s research on hybrid group key exchange and adaptive TreeKEM.


## Engineering at FORG

**Backend developer at EEPACO** · [FORG](https://forgco.ir/) · Private company project

I build and improve the backend, device server, and the workflows that test and ship FORG. My contributions span six areas:

<!-- FORG:START -->
<p>
<picture><source media="(max-width: 640px) and (prefers-color-scheme: light)" srcset="assets/forg/backend-mobile-light.svg"><source media="(max-width: 640px)" srcset="assets/forg/backend-mobile-dark.svg"><source media="(prefers-color-scheme: light)" srcset="assets/forg/backend-light.svg"><img src="assets/forg/backend-dark.svg" alt="Backend &amp; real-time features. Architecture: Controller, service and middleware layers in C++, Qt and Drogon. Backend features: Syslog, admin access, a backup service and API-based AI review. Database performance: Batched SQL queries and PostgreSQL notification listeners. Live dashboards: Real-time dashboard updates over WebSocket connections. WebSocket: Live dashboard updates C++ services built with Qt and Drogon." width="100%"></picture>
</p>

<p>
<picture><source media="(max-width: 640px) and (prefers-color-scheme: light)" srcset="assets/forg/server-mobile-light.svg"><source media="(max-width: 640px)" srcset="assets/forg/server-mobile-dark.svg"><source media="(prefers-color-scheme: light)" srcset="assets/forg/server-light.svg"><img src="assets/forg/server-dark.svg" alt="Device server &amp; connection handling. Device communication: WebSocket connections for mobile devices. Database efficiency: Batch-query optimization and PostgreSQL LISTEN/NOTIFY updates. Memory ownership: Smart pointers for object lifetimes and resource management. 100,000: Concurrent device connections Designed for this workload; validated with our device connection tester." width="100%"></picture>
</p>

<p>
<picture><source media="(max-width: 640px) and (prefers-color-scheme: light)" srcset="assets/forg/delivery-mobile-light.svg"><source media="(max-width: 640px)" srcset="assets/forg/delivery-mobile-dark.svg"><source media="(prefers-color-scheme: light)" srcset="assets/forg/delivery-light.svg"><img src="assets/forg/delivery-dark.svg" alt="CI/CD, migrations &amp; packaging. Database delivery: Versioned SQL migrations and nightly maintenance with pg_cron. Build &amp; release: Custom Jenkins parameters, package publishing and GitLab releases. Infrastructure scripts: Automated updates for the GitLab Docker deployment. Debian packages: Dependency metadata and post-installation configuration. .deb: Backend &amp; frontend Database &amp; device server Packaging all four components with dependency rules and post-installation scripts." width="100%"></picture>
</p>

<p>
<picture><source media="(max-width: 640px) and (prefers-color-scheme: light)" srcset="assets/forg/testing-mobile-light.svg"><source media="(max-width: 640px)" srcset="assets/forg/testing-mobile-dark.svg"><source media="(prefers-color-scheme: light)" srcset="assets/forg/testing-light.svg"><img src="assets/forg/testing-dark.svg" alt="API, UI &amp; stress testing. API &amp; UI coverage: API tests and Playwright UI tests for product behavior. Reusable access tests: Flow-based administrator-access test implementation. Load scenarios: Stress-test scenarios and simulated device connection testing. 14 days: To implement admin-access tests Reduced from 3 months by using reusable test flows." width="100%"></picture>
</p>

<p>
<picture><source media="(max-width: 640px) and (prefers-color-scheme: light)" srcset="assets/forg/deployment-mobile-light.svg"><source media="(max-width: 640px)" srcset="assets/forg/deployment-mobile-dark.svg"><source media="(prefers-color-scheme: light)" srcset="assets/forg/deployment-light.svg"><img src="assets/forg/deployment-dark.svg" alt="Automated deployment. Build-to-install automation: A complete build and deployment system for local test servers. Repeatable environments: Connected build, package, installation and deployment steps. Testing workflow: Faster iteration through automated local-server deployment. Build → deploy: Repeatable server setup Build, package and install through an automated workflow." width="100%"></picture>
</p>

<p>
<picture><source media="(max-width: 640px) and (prefers-color-scheme: light)" srcset="assets/forg/licensing-mobile-light.svg"><source media="(max-width: 640px)" srcset="assets/forg/licensing-mobile-dark.svg"><source media="(prefers-color-scheme: light)" srcset="assets/forg/licensing-light.svg"><img src="assets/forg/licensing-dark.svg" alt="Licensing &amp; cryptography. License handling: In-memory processing of license information. Cryptographic integration: PKCS #11 integration for cryptographic operations. License signatures: RSA-2048 signing of license information. RSA-2048: PKCS #11 integration In-memory license handling and cryptographic signing." width="100%"></picture>
</p>
<!-- FORG:END -->

## Selected work

<p>
  <a href="https://forgco.ir/"><picture><source media="(max-width: 640px) and (prefers-color-scheme: light)" srcset="assets/forg-mobile-light.svg"><source media="(max-width: 640px)" srcset="assets/forg-mobile-dark.svg"><source media="(prefers-color-scheme: light)" srcset="assets/forg-light.svg"><img src="assets/forg-dark.svg" alt="FORG — Private company project. Backend developer at EEPACO. C++, Qt, Drogon, PostgreSQL." width="48%"></picture></a> &nbsp;
  <a href="https://myket.ir/app/com.parsania.roozchin"><picture><source media="(max-width: 640px) and (prefers-color-scheme: light)" srcset="assets/planner-mobile-light.svg"><source media="(max-width: 640px)" srcset="assets/planner-mobile-dark.svg"><source media="(prefers-color-scheme: light)" srcset="assets/planner-light.svg"><img src="assets/planner-dark.svg" alt="Daily Planner — Private personal product. Flutter and Dart, clean architecture, BLoC/Cubit, and Drift/SQLite. Available on Myket and Cafe Bazaar." width="48%"></picture></a>
</p>
<p>
  <a href="https://github.com/Parsania80/FluxGet"><picture><source media="(max-width: 640px) and (prefers-color-scheme: light)" srcset="assets/fluxget-mobile-light.svg"><source media="(max-width: 640px)" srcset="assets/fluxget-mobile-dark.svg"><source media="(prefers-color-scheme: light)" srcset="assets/fluxget-light.svg"><img src="assets/fluxget-dark.svg" alt="FluxGet — Open-source download manager for Linux and Windows, written in Go." width="48%"></picture></a> &nbsp;
  <a href="https://github.com/Parsania80/parsBackUp"><picture><source media="(max-width: 640px) and (prefers-color-scheme: light)" srcset="assets/backup-mobile-light.svg"><source media="(max-width: 640px)" srcset="assets/backup-mobile-dark.svg"><source media="(prefers-color-scheme: light)" srcset="assets/backup-light.svg"><img src="assets/backup-dark.svg" alt="parsBackUp — Open-source PostgreSQL backup and restore project in Rust. Development and testing across PostgreSQL 16, 17, and 18." width="48%"></picture></a>
</p>

Also explore my [open-source master’s research in hybrid MLS and TreeKEM](#research).

### FORG · Backend developer at EEPACO

**Private company project** · [Open FORG](https://forgco.ir/)

I develop the backend and device communication server, with responsibilities across access control, database performance, live dashboards, delivery automation, and testing. See the engineering panels above for the implementation work and validation results.

### Daily Planner · Owner & developer

**Private personal product** · [Myket](https://myket.ir/app/com.parsania.roozchin) · [Cafe Bazaar](https://cafebazaar.ir/app/com.parsania.roozchin)

An **offline-first Flutter/Dart planner** for tasks, recurring routines, projects, and notes, available as **Roozchin** on Myket and Cafe Bazaar.

- **Architecture & state:** clean architecture with presentation, domain, and data layers; repository abstractions; BLoC/Cubit state management; GetIt dependency injection.
- **Persistence:** Drift over SQLite for local storage, relational task hierarchies, and database migrations.
- **Planning logic:** recurring task expansion, nested projects and folders, date-based planning, search, and bulk operations.
- **Native Android integration:** scheduled reminders, notification actions, and reminder reconciliation across app lifecycle changes.
- **Localization & UX:** Persian/English localization, RTL layouts, Jalali/Gregorian calendars, and persistent theme and time-format preferences.
- **Product engineering:** backup/restore workflows, separate store billing adapters, and Android release variants for Myket and Cafe Bazaar.
- **Testing:** unit, BLoC, widget, integration, architecture-boundary, and golden-image tests.

### FluxGet · Open source

**Go · Linux & Windows** · [Source](https://github.com/Parsania80/FluxGet) · [Releases](https://github.com/Parsania80/FluxGet/releases)

A desktop download manager for managing multiple downloads, pausing and resuming transfers, and controlling download speeds. I work on the download engine, desktop experience, browser integration, and native packaging.

### parsBackUp · Open source

**Rust · PostgreSQL 16 / 17 / 18** · [Source](https://github.com/Parsania80/parsBackUp)

A PostgreSQL backup and restore platform I’m developing in Rust, with work on backup verification, selective restore, encrypted artifacts, and recovery workflows. The current development CLI is tested against synthetic databases across PostgreSQL 16, 17, and 18; the production service is still in progress.

## Research

<p>
<a href="https://github.com/Parsania80/Master-Hybrid-MLS"><picture><source media="(max-width: 640px) and (prefers-color-scheme: light)" srcset="assets/research-mobile-light.svg"><source media="(max-width: 640px)" srcset="assets/research-mobile-dark.svg"><source media="(prefers-color-scheme: light)" srcset="assets/research-light.svg"><img src="assets/research-dark.svg" alt="Master-Hybrid-MLS — Open-source master’s research in cybersecurity at the University of Isfahan. Hybrid group key exchange based on TreeKEM, with a Rust research prototype." width="100%"></picture></a>
</p>

### Master-Hybrid-MLS · Master’s thesis

**Open-source research · Rust · MLS / TreeKEM** · [Repository](https://github.com/Parsania80/Master-Hybrid-MLS) · [Thesis PDF](https://github.com/Parsania80/Master-Hybrid-MLS/blob/main/%D9%BE%D8%A7%DB%8C%D8%A7%D9%86%20%D9%86%D8%A7%D9%85%D9%87/Thesis.pdf) · [Current implementation](https://github.com/Parsania80/Master-Hybrid-MLS/tree/main/implementation/new)

My master’s research in cybersecurity at the **University of Isfahan**, titled **Hybrid Group Key Exchange based on TreeKEM**, explores hybrid classical/post-quantum key delivery and adaptive tree structures for secure group messaging.

- **Protocol research:** hybrid path-secret delivery combining classical HPKE with an educational multi-recipient mKyber implementation.
- **Adaptive TreeKEM:** policy-controlled binary-to-quaternary transitions, authenticated group-state changes, and temporary TreeCover delivery during migration.
- **Rust implementation:** a standard OpenMLS baseline and an isolated experimental fork, with group-state convergence checks, transition/retirement workflows, and regression/property tests.
- **Experiment tooling:** controlled group workloads, serialized Commit-byte measurements, CSV/JSON reports, and SVG plots. Reports distinguish observed protocol measurements from analytical or educational models.

The implementation is a **research prototype**, with documented security and interoperability limits.

## How I work

<p>
<picture><source media="(max-width: 640px) and (prefers-color-scheme: light)" srcset="assets/principles-mobile-light.svg"><source media="(max-width: 640px)" srcset="assets/principles-mobile-dark.svg"><source media="(prefers-color-scheme: light)" srcset="assets/principles-light.svg"><img src="assets/principles-dark.svg" alt="Separate responsibilities with clean architecture. Measure behavior with API, UI, and load tests. Make delivery repeatable with migrations, packages, and automation." width="100%"></picture>
</p>

## Stack

<!-- STACK:START -->
**BACKEND & SYSTEMS**

<p>
<a href="https://isocpp.org/"><picture><source media="(prefers-color-scheme: light)" srcset="assets/stack/cplusplus-light.svg"><img src="assets/stack/cplusplus-dark.svg" alt="C++" height="44"></picture></a>
<a href="https://www.qt.io/"><picture><source media="(prefers-color-scheme: light)" srcset="assets/stack/qt-light.svg"><img src="assets/stack/qt-dark.svg" alt="Qt" height="44"></picture></a>
<a href="https://github.com/drogonframework/drogon"><picture><source media="(prefers-color-scheme: light)" srcset="assets/stack/drogon-light.svg"><img src="assets/stack/drogon-dark.svg" alt="Drogon" height="44"></picture></a>
<a href="https://go.dev/"><picture><source media="(prefers-color-scheme: light)" srcset="assets/stack/go-light.svg"><img src="assets/stack/go-dark.svg" alt="Go" height="44"></picture></a>
<a href="https://www.rust-lang.org/"><picture><source media="(prefers-color-scheme: light)" srcset="assets/stack/rust-light.svg"><img src="assets/stack/rust-dark.svg" alt="Rust" height="44"></picture></a>
</p>

**DATA & REAL-TIME**

<p>
<a href="https://www.postgresql.org/"><picture><source media="(prefers-color-scheme: light)" srcset="assets/stack/postgresql-light.svg"><img src="assets/stack/postgresql-dark.svg" alt="PostgreSQL" height="44"></picture></a>
<a href="https://www.sqlite.org/"><picture><source media="(prefers-color-scheme: light)" srcset="assets/stack/sqlite-light.svg"><img src="assets/stack/sqlite-dark.svg" alt="SQLite" height="44"></picture></a>
<a href="https://drift.simonbinder.eu/"><picture><source media="(prefers-color-scheme: light)" srcset="assets/stack/drift-light.svg"><img src="assets/stack/drift-dark.svg" alt="Drift" height="44"></picture></a>
<a href="https://www.rfc-editor.org/rfc/rfc6455"><picture><source media="(prefers-color-scheme: light)" srcset="assets/stack/websocket-light.svg"><img src="assets/stack/websocket-dark.svg" alt="WebSockets" height="44"></picture></a>
<a href="https://github.com/citusdata/pg_cron"><picture><source media="(prefers-color-scheme: light)" srcset="assets/stack/pgcron-light.svg"><img src="assets/stack/pgcron-dark.svg" alt="pg_cron" height="44"></picture></a>
</p>

**MOBILE & ARCHITECTURE**

<p>
<a href="https://flutter.dev/"><picture><source media="(prefers-color-scheme: light)" srcset="assets/stack/flutter-light.svg"><img src="assets/stack/flutter-dark.svg" alt="Flutter" height="44"></picture></a>
<a href="https://dart.dev/"><picture><source media="(prefers-color-scheme: light)" srcset="assets/stack/dart-light.svg"><img src="assets/stack/dart-dark.svg" alt="Dart" height="44"></picture></a>
<a href="https://bloclibrary.dev/"><picture><source media="(prefers-color-scheme: light)" srcset="assets/stack/bloc-light.svg"><img src="assets/stack/bloc-dark.svg" alt="BLoC / Cubit" height="44"></picture></a>
<a href="https://pub.dev/packages/get_it"><picture><source media="(prefers-color-scheme: light)" srcset="assets/stack/getit-light.svg"><img src="assets/stack/getit-dark.svg" alt="GetIt" height="44"></picture></a>
</p>

**DELIVERY & INFRASTRUCTURE**

<p>
<a href="https://www.kernel.org/"><picture><source media="(prefers-color-scheme: light)" srcset="assets/stack/linux-light.svg"><img src="assets/stack/linux-dark.svg" alt="Linux" height="44"></picture></a>
<a href="https://www.jenkins.io/"><picture><source media="(prefers-color-scheme: light)" srcset="assets/stack/jenkins-light.svg"><img src="assets/stack/jenkins-dark.svg" alt="Jenkins" height="44"></picture></a>
<a href="https://docs.gitlab.com/user/packages/package_registry/"><picture><source media="(prefers-color-scheme: light)" srcset="assets/stack/gitlab-light.svg"><img src="assets/stack/gitlab-dark.svg" alt="GitLab Registry" height="44"></picture></a>
<a href="https://www.docker.com/"><picture><source media="(prefers-color-scheme: light)" srcset="assets/stack/docker-light.svg"><img src="assets/stack/docker-dark.svg" alt="Docker" height="44"></picture></a>
<a href="https://www.debian.org/doc/manuals/maint-guide/"><picture><source media="(prefers-color-scheme: light)" srcset="assets/stack/debian-light.svg"><img src="assets/stack/debian-dark.svg" alt="Debian packages" height="44"></picture></a>
<a href="https://git-scm.com/"><picture><source media="(prefers-color-scheme: light)" srcset="assets/stack/git-light.svg"><img src="assets/stack/git-dark.svg" alt="Git" height="44"></picture></a>
</p>

**QUALITY & SECURITY**

<p>
<a href="https://playwright.dev/"><picture><source media="(prefers-color-scheme: light)" srcset="assets/stack/playwright-light.svg"><img src="assets/stack/playwright-dark.svg" alt="Playwright" height="44"></picture></a>
<a href="https://docs.flutter.dev/testing"><picture><source media="(prefers-color-scheme: light)" srcset="assets/stack/fluttertest-light.svg"><img src="assets/stack/fluttertest-dark.svg" alt="Flutter Test" height="44"></picture></a>
<a href="https://www.oasis-open.org/committees/pkcs11/"><picture><source media="(prefers-color-scheme: light)" srcset="assets/stack/pkcs11-light.svg"><img src="assets/stack/pkcs11-dark.svg" alt="PKCS #11" height="44"></picture></a>
<a href="https://www.rfc-editor.org/rfc/rfc8017"><picture><source media="(prefers-color-scheme: light)" srcset="assets/stack/rsa-light.svg"><img src="assets/stack/rsa-dark.svg" alt="RSA-2048" height="44"></picture></a>
</p>

<!-- STACK:END -->

## Activity

<p>
<a href="https://github.com/Parsania80?tab=overview"><picture><source media="(max-width: 640px) and (prefers-color-scheme: light)" srcset="assets/activity-mobile-light.svg"><source media="(max-width: 640px)" srcset="assets/activity-mobile-dark.svg"><source media="(prefers-color-scheme: light)" srcset="assets/activity-light.svg"><img src="assets/activity-dark.svg" alt="GitHub activity: contribution total, active days, public repositories, and public language distribution. Based on fetched GitHub data." width="100%"></picture></a>
</p>

<p>
<a href="https://github.com/Parsania80?tab=overview"><picture><source media="(prefers-color-scheme: light)" srcset="assets/contributions-3d-light.svg"><img src="assets/contributions-3d-dark.svg" alt="An isometric contribution calendar. Each column represents a day in my GitHub-visible contribution history." width="100%"></picture></a>
</p>

The calendar shows GitHub-visible activity. Language shares cover **public, non-fork GitHub repositories**; my private C++ company work and Flutter app are outside that language breakdown. Company GitLab activity is not counted.

## Let’s connect

Find me on [LinkedIn](https://www.linkedin.com/in/parsania80/), email me at [parsania80@gmail.com](mailto:parsania80@gmail.com), call [+98 939 600 3945](tel:+989396003945), or explore my [public projects](https://github.com/Parsania80?tab=repositories).

<picture>
  <source media="(prefers-color-scheme: light)" srcset="assets/footer-light.svg">
  <img src="assets/footer-dark.svg" alt="Mohammadreza Parsania · Backend, products, and the tools that ship them." width="100%">
</picture>
