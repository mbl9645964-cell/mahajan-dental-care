#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Mahajan Dental Care — from-scratch static site generator. Real content from mahajandentalcare.in."""
import os

BASE = os.path.dirname(os.path.abspath(__file__))
IMG = "assets/img/"

PHONE_DISPLAY = "+91 98731 40343"
PHONE_TEL = "tel:+919873140343"
WA_NUM = "919873140343"
def wa(msg):
    import urllib.parse
    return f"https://wa.me/{WA_NUM}?text={urllib.parse.quote(msg)}"
WA_BOOK = wa("Hello Mahajan Dental Care, I would like to book an appointment.")
WA_CHAT = wa("Hello Mahajan Dental Care, how can I help you?")
EMAIL = "mahajansiddhantdeb96845@gmail.com"
ADDRESS = "10-11-12, Chowk, MCF Market, Gopi Colony, Old Faridabad, Faridabad, Haryana 121002"
MAPS = "https://maps.app.goo.gl/8mZCr58FdoNz6xBy7"
HOURS = "Mon–Sat · 10:00 am – 8:00 pm"
FB = "https://www.facebook.com/mahajandentalcare"
IG = "https://www.instagram.com/mahajandentalcare"

NAV = [
    ("index.html", "Home"),
    ("about.html", "About"),
    ("services.html", "Services"),
    ("doctors.html", "Doctors"),
    ("clinic.html", "Clinic"),
    ("contact.html", "Contact"),
]

def ic(path, size=18):
    return f'<svg class="ic" viewBox="0 0 24 24" width="{size}" height="{size}" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{path}</svg>'

I_PHONE = ic('<path d="M6.5 3h3l1.5 5-2 1.5a12 12 0 0 0 5.5 5.5L16 18l5 1.5v3a1 1 0 0 1-1.1 1A18 18 0 0 1 3.5 6.1 1 1 0 0 1 4.5 5"/>')
I_WA = '<svg class="ic" viewBox="0 0 24 24" width="18" height="18" fill="currentColor" aria-hidden="true"><path d="M17.47 14.38c-.29-.14-1.7-.84-1.96-.94-.26-.1-.45-.14-.64.15-.19.29-.74.94-.91 1.13-.17.19-.34.21-.62.07-.29-.14-1.21-.45-2.3-1.42-.85-.76-1.42-1.7-1.59-1.98-.17-.29-.02-.44.13-.58.13-.13.29-.34.43-.51.14-.17.19-.29.29-.48.1-.19.05-.36-.02-.51-.07-.14-.64-1.55-.88-2.12-.23-.55-.47-.48-.64-.48h-.55c-.19 0-.5.07-.76.36-.26.29-1 .98-1 2.38 0 1.4 1.02 2.76 1.17 2.95.14.19 2.01 3.08 4.88 4.32.68.29 1.21.47 1.63.6.68.22 1.31.19 1.8.12.55-.08 1.7-.69 1.94-1.36.24-.67.24-1.24.17-1.36-.07-.12-.26-.19-.55-.33z"/><path d="M12 .9C5.87.9.9 5.87.9 12c0 1.95.51 3.86 1.48 5.55L.8 23.1l5.68-1.49A11.06 11.06 0 0 0 12 23.1c6.13 0 11.1-4.97 11.1-11.1S18.13.9 12 .9zm0 20.2c-1.72 0-3.4-.46-4.87-1.34l-.35-.21-3.37.89.9-3.29-.23-.35A9.06 9.06 0 0 1 2.9 12 9.1 9.1 0 1 1 12 21.1z"/></svg>'
I_CLOCK = ic('<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>')
I_PIN = ic('<path d="M12 21s7-5.5 7-11a7 7 0 1 0-14 0c0 5.5 7 11 7 11z"/><circle cx="12" cy="10" r="2.5"/>')
I_ARROW = ic('<path d="M5 12h14M13 6l6 6-6 6"/>')
I_IG = ic('<rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="1" fill="currentColor" stroke="none"/>', 15)
I_FB = '<svg class="ic" viewBox="0 0 24 24" width="15" height="15" fill="currentColor" aria-hidden="true"><path d="M14 8h2V5h-2c-1.7 0-3 1.3-3 3v2H9v3h2v6h3v-6h2l1-3h-3V8.5c0-.3.2-.5.5-.5z"/></svg>'
I_MENU = '<svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><path d="M3 6h18M3 12h18M3 18h18"/></svg>'
I_CLOSE = '<svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><path d="M6 6l12 12M18 6L6 18"/></svg>'
I_TOOTH = ic('<path d="M12 5.2c-1.6-1.3-3.1-1.9-4.5-1.5-1.9.5-3.2 2.2-3.2 4.5 0 1.7.4 2.9.9 4.5.3 1.3.4 2.6.6 4 .2 1.5.5 3.3 1.7 3.3s1.3-1.4 1.6-2.8c.3-1.3.6-2.6 1.5-2.6s1.2 1.3 1.5 2.6c.3 1.4.5 2.8 1.6 2.8 1.2 0 1.5-1.8 1.7-3.3.2-1.4.3-2.7.6-4 .5-1.6.9-2.8.9-4.5 0-2.3-1.3-4-3.2-4.5-1.4-.4-2.9.2-4.5 1.5z"/>', 20)
I_LEAF = ic('<path d="M5 19c0-8 6-13 14-13 0 8-5 14-13 14"/><path d="M5 19c3-4 6-6 10-8"/>', 34)

def page(title, description, body, active="", extra_head=""):
    def _nav_item(href, label):
        cur = ' aria-current="page"' if href == active else ""
        return f'<li><a href="{href}"{cur}>{label}</a></li>'
    nav_links = "".join(_nav_item(href, label) for href, label in NAV)
    mobile_links = "".join(f'<li><a href="{href}">{label}</a></li>' for href, label in NAV)
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} — Mahajan Dental Care</title>
<meta name="description" content="{description}">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;1,400;1,500&family=Jost:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/site.css">
<link rel="icon" href="{IMG}favicon.png">
{extra_head}
</head>
<body>
<a class="skip-link" href="#main">Skip to content</a>

<div class="topbar"><div class="wrap topbar__row">
<div class="topbar__info">
<a href="{PHONE_TEL}">{I_PHONE}<span>{PHONE_DISPLAY}</span></a>
<a href="{WA_CHAT}" target="_blank" rel="noopener">{I_WA}<span>WhatsApp</span></a>
<span>{I_CLOCK}<span>{HOURS}</span></span>
</div>
<div class="topbar__soc">
<a href="{IG}" target="_blank" rel="noopener" aria-label="Instagram">{I_IG}</a>
<a href="{FB}" target="_blank" rel="noopener" aria-label="Facebook">{I_FB}</a>
<a href="{MAPS}" target="_blank" rel="noopener" aria-label="Directions">{I_PIN}</a>
</div>
</div></div>

<header class="site-header" data-header>
<div class="wrap nav">
<a class="brand" href="index.html">
<span class="brand__mark">{I_TOOTH}</span>
<span class="brand__word"><span class="brand__name">Mahajan Dental Care</span><span class="brand__tag">Since 1986 &middot; Old Faridabad</span></span>
</a>
<ul class="nav__menu">{nav_links}</ul>
<a class="btn nav__cta" href="{WA_BOOK}" target="_blank" rel="noopener">Book an Appointment</a>
<button class="nav__toggle" data-nav-toggle aria-label="Open menu" aria-expanded="false">{I_MENU}</button>
</div>
</header>

<div class="nav-scrim" data-nav-scrim></div>
<nav class="mobile-nav" data-mobile-nav aria-label="Mobile">
<button class="mobile-nav__close" data-nav-close aria-label="Close menu">{I_CLOSE}</button>
<ul>{mobile_links}</ul>
<a class="btn" style="width:100%;justify-content:center" href="{WA_BOOK}" target="_blank" rel="noopener">Book an Appointment</a>
</nav>

<main id="main">
{body}
</main>

<footer class="site-footer">
<div class="wrap footer-grid">
<div>
<p class="footer-brand__name">Mahajan Dental Care</p>
<p class="footer-brand__stmt">A trusted dental clinic in Old Faridabad since 1986 — nearly four decades of honest, patient-centred care.</p>
<div class="footer-soc">
<a href="{IG}" target="_blank" rel="noopener" aria-label="Instagram">{I_IG}</a>
<a href="{FB}" target="_blank" rel="noopener" aria-label="Facebook">{I_FB}</a>
<a href="{MAPS}" target="_blank" rel="noopener" aria-label="Directions">{I_PIN}</a>
</div>
</div>
<div class="footer-col"><h5>Explore</h5><ul>
<li><a href="about.html">About</a></li><li><a href="services.html">Services</a></li>
<li><a href="doctors.html">Doctors</a></li><li><a href="clinic.html">Clinic</a></li></ul></div>
<div class="footer-col"><h5>Services</h5><ul>
<li><a href="services.html#root-canal">Root Canal Treatment</a></li><li><a href="services.html#implants">Dental Implants</a></li>
<li><a href="services.html#braces">Braces &amp; Orthodontics</a></li><li><a href="services.html#cosmetic">Cosmetic Dentistry</a></li></ul></div>
<div class="footer-col"><h5>Visit</h5><ul>
<li>{ADDRESS}</li><li><a href="{PHONE_TEL}">{PHONE_DISPLAY}</a></li>
<li><a href="mailto:{EMAIL}">{EMAIL}</a></li><li>{HOURS}</li></ul></div>
</div>
<div class="wrap footer-bottom">
<span>&copy; 2026 Mahajan Dental Care. All rights reserved.</span>
<span><a href="privacy.html">Privacy Policy</a><a href="disclaimer.html">Medical Disclaimer</a></span>
</div>
</footer>

<a class="wa-fab" href="{WA_CHAT}" target="_blank" rel="noopener" aria-label="Chat on WhatsApp">{I_WA}</a>
<nav class="mobar" aria-label="Quick contact"><div class="mobar__row">
<a href="{PHONE_TEL}">{I_PHONE}<span>Call</span></a>
<a href="{WA_CHAT}" target="_blank" rel="noopener">{I_WA}<span>Chat</span></a>
<a class="is-primary" href="{WA_BOOK}" target="_blank" rel="noopener">{I_ARROW}<span>Book</span></a>
</div></nav>

<script src="assets/js/site.js"></script>
</body>
</html>'''

def section_head(kicker, title, intro="", center=False, light=False):
    c = " is-center" if center else ""
    ec = "eyebrow--center" if center else ""
    el = "eyebrow--light" if light else ""
    out = f'<div class="section-head{c}" data-reveal><span class="eyebrow {ec} {el}">{kicker}</span><h2 class="display-2">{title}</h2>'
    if intro:
        out += f'<p class="lead" style="margin-top:1rem">{intro}</p>'
    return out + "</div>"

# ============================================================== INDEX =====
def build_index():
    hero = f'''<section class="hero" data-hero-slideshow>
<div class="hero__slides">
<div class="hero__slide is-active"><img src="{IMG}treatment-room-1.jpg" alt="Treatment room at Mahajan Dental Care"></div>
<div class="hero__slide"><img src="{IMG}reception-bench.jpg" alt="Reception at Mahajan Dental Care"></div>
<div class="hero__slide"><img src="{IMG}treatment-room-2.jpg" alt="Treatment room at Mahajan Dental Care"></div>
<div class="hero__slide"><img src="{IMG}entrance-signage.jpg" alt="Mahajan Dental Care clinic entrance"></div>
</div>
<div class="hero__scrim"></div>
<div class="wrap hero__inner">
<div data-reveal>
<span class="hero__eyebrow">Old Faridabad &middot; Since 1986</span>
<h1 class="hero__title">Nearly <em>four decades</em> of trusted dental care.</h1>
<p class="hero__lead">One of Old Faridabad&rsquo;s oldest dental clinics — honest, ethical, patient-first treatment for generations of families.</p>
<div class="hero__actions">
<a class="btn" href="{WA_BOOK}" target="_blank" rel="noopener">Book an Appointment</a>
<a class="text-link text-link--light" href="{WA_CHAT}" target="_blank" rel="noopener">{I_WA}<span>WhatsApp us</span></a>
<a class="text-link text-link--light" href="{PHONE_TEL}">{I_PHONE}<span>{PHONE_DISPLAY}</span></a>
</div>
<dl class="hero__ticket">
<div><dt>Address</dt><dd>Gopi Colony, Old Faridabad</dd></div>
<div><dt>Hours</dt><dd>{HOURS}</dd></div>
<div><dt>Since</dt><dd>1986 &middot; ISO 9001:2008 Certified</dd></div>
</dl>
</div>
</div>
<div class="hero__dots" data-hero-dots></div>
</section>'''

    factstrip = f'''<section class="factstrip"><div class="wrap factstrip__row" data-reveal>
<div class="fact"><span class="fact__no">01</span><h3>Nearly 40 years</h3><p>Serving Old Faridabad families since 1986, across generations.</p></div>
<div class="fact"><span class="fact__no">02</span><h3>ISO certified</h3><p>ISO 9001:2008 certified clinic with modern equipment.</p></div>
<div class="fact"><span class="fact__no">03</span><h3>Specialist-led</h3><p>Endodontics, implants and orthodontics handled by specialists.</p></div>
<div class="fact"><span class="fact__no">04</span><h3>Honest planning</h3><p>Ethical, patient-centric treatment — no unnecessary procedures.</p></div>
</div></section>'''

    intro = f'''<section class="section bg-card"><div class="wrap split">
<div data-reveal>
<span class="eyebrow">Our story</span>
<h2 class="display-2">A legacy built on trust, continued with precision.</h2>
<p class="lead" style="margin-top:1.3rem">Mahajan Dental Care has treated generations of families in Old Faridabad since 1986. What began as one dentist&rsquo;s practice is now a specialist-led clinic — combining decades of clinical experience with modern dental technique.</p>
<p class="muted" style="margin-top:1rem">Patient satisfaction, hygiene standards and long-term oral health remain the clinic&rsquo;s highest priorities, as they have been for nearly four decades.</p>
<a class="text-link" style="margin-top:1.6rem" href="about.html">More about our story{I_ARROW}</a>
</div>
<div class="split__media" data-reveal>
<figure class="frame frame--tall"><img src="{IMG}treatment-room-3.jpg" alt="Treatment room at Mahajan Dental Care"></figure>
</div>
</div></section>'''

    services_teaser = f'''<section class="section bg-band"><div class="wrap">
{section_head("What we treat", "A full range of dental care, under one roof.", "From routine check-ups to specialist implant and root canal care — handled by the doctor it actually needs.")}
<ul class="tlist" data-reveal>
<li><a href="services.html#root-canal"><span class="tlist__thumb">{I_TOOTH}</span><span class="tlist__body"><h3>Root Canal Treatment</h3><p>Designed to save a tooth damaged by deep decay or infection — including single-sitting RCT.</p></span><span class="tlist__arrow">{I_ARROW}</span></a></li>
<li><a href="services.html#implants"><span class="tlist__thumb">{I_TOOTH}</span><span class="tlist__body"><h3>Dental Implants</h3><p>Long-lasting replacements for missing teeth, planned by a certified implantologist.</p></span><span class="tlist__arrow">{I_ARROW}</span></a></li>
<li><a href="services.html#braces"><span class="tlist__thumb">{I_TOOTH}</span><span class="tlist__body"><h3>Braces &amp; Orthodontics</h3><p>Correcting misaligned teeth, gaps and bite problems for a healthier smile.</p></span><span class="tlist__arrow">{I_ARROW}</span></a></li>
<li><a href="services.html#gum-care"><span class="tlist__thumb">{I_TOOTH}</span><span class="tlist__body"><h3>Gum Disease &amp; Bleeding Gums</h3><p>Early treatment for gum problems before they become serious periodontal issues.</p></span><span class="tlist__arrow">{I_ARROW}</span></a></li>
</ul>
<p style="margin-top:2.2rem" data-reveal><a class="text-link" href="services.html">View every service{I_ARROW}</a></p>
</div></section>'''

    doctors_teaser = f'''<section class="section bg-ink"><div class="wrap">
<div style="display:flex;align-items:flex-end;justify-content:space-between;gap:2rem;flex-wrap:wrap;margin-bottom:clamp(2rem,4vw,3rem)" data-reveal>
<div><span class="eyebrow eyebrow--light">The doctors</span><h2 class="display-2" style="color:var(--cream)">Two generations of dental expertise.</h2></div>
<a class="text-link text-link--light" href="doctors.html">Meet the doctors{I_ARROW}</a>
</div>
<div class="team-grid stagger on-dark" data-reveal>
<article class="person"><span class="person__photo"><span class="person__ph">{I_LEAF}<span>Add doctor photo</span></span></span><div class="person__body"><h3 class="person__name">Dr. Tarun Mahajan</h3><p class="person__role">Founder &middot; Endodontist, Oral Surgeon &amp; Implantologist</p><p class="person__qual" style="color:var(--cream-70)">B.D.S. (Pb.), D.Endo, MISOI &middot; Fellow, International College of Dentists (USA)</p></div></article>
<article class="person"><span class="person__photo"><span class="person__ph">{I_LEAF}<span>Add doctor photo</span></span></span><div class="person__body"><h3 class="person__name">Dr. Siddhant Mahajan</h3><p class="person__role">Micro-Endodontics &amp; Smile Makeover Specialist</p><p class="person__qual" style="color:var(--cream-70)">BDS, MDS &middot; Single-Sitting RCT specialist</p></div></article>
</div>
</div></section>'''

    reviews = f'''<section class="section bg-band"><div class="wrap split split--rev">
<div class="split__media" data-reveal><figure class="frame frame--tall"><img src="{IMG}waiting-area.jpg" alt="Waiting area at Mahajan Dental Care"></figure></div>
<div data-reveal>
<span class="eyebrow">Patient trust</span>
<h2 class="display-2">Read as patients describe us.</h2>
<div style="margin-top:2rem">
<div class="quote"><blockquote>Excellent team of doctors providing the best treatment in the area — I&rsquo;m not scared of dental treatment anymore.</blockquote><cite>Patient review</cite></div>
<div class="quote"><blockquote>Been coming here for years. Honest advice, clean clinic, and they genuinely care about their patients.</blockquote><cite>Patient review</cite></div>
</div>
<a class="text-link" style="margin-top:1.8rem" href="{MAPS}" target="_blank" rel="noopener">Read reviews on Google{I_ARROW}</a>
</div>
</div></section>'''

    cta = f'''<section class="ctaband"><div class="wrap ctaband__row" data-reveal>
<div><span class="eyebrow eyebrow--light">Book your visit</span><h2>Ready when you are.</h2><p>Message us on WhatsApp or call the clinic — new patients are always welcome.</p></div>
<div class="ctaband__btns"><a class="btn btn--cream" href="{WA_BOOK}" target="_blank" rel="noopener">Book an Appointment</a><a class="text-link text-link--light" href="{WA_CHAT}" target="_blank" rel="noopener">Chat with us{I_ARROW}</a></div>
</div></section>'''

    body = hero + factstrip + intro + services_teaser + doctors_teaser + reviews + cta
    return page(
        "Trusted Dental Clinic in Old Faridabad Since 1986",
        "Mahajan Dental Care — one of Old Faridabad's oldest and most trusted dental clinics, serving families since 1986.",
        body, active="index.html"
    )

open(os.path.join(BASE, "index.html"), "w", encoding="utf-8").write(build_index())
print("index.html written")

# ============================================================== ABOUT =====
def build_about():
    hero = f'''<section class="section" style="padding-top:clamp(3rem,6vw,4.5rem)"><div class="wrap">
<nav aria-label="Breadcrumb" class="muted" style="font-size:.85rem;margin-bottom:1.6rem"><a href="index.html">Home</a> / About</nav>
<span class="eyebrow">About the clinic</span>
<h1 class="display-1" style="max-width:18ch">One of Old Faridabad&rsquo;s oldest dental clinics.</h1>
<p class="lead" style="margin-top:1.4rem;max-width:60ch">Established in 1986, Mahajan Dental Care has spent nearly four decades serving the Old Faridabad community with honest, ethical, patient-centric dental treatment.</p>
</div></section>'''

    story = f'''<section class="section bg-card"><div class="wrap split split--rev">
<div class="split__media" data-reveal><figure class="frame frame--tall"><img src="{IMG}entrance-signage.jpg" alt="Mahajan Dental Care entrance"></figure></div>
<div data-reveal>
<span class="eyebrow">Our legacy</span>
<h2 class="display-2">Generations of families, one trusted clinic.</h2>
<p class="lead" style="margin-top:1.3rem">Since founding the clinic in 1986, Dr. Tarun Mahajan has combined time-tested expertise with modern dental innovations. What began as a single dentist&rsquo;s practice has grown into a specialist-led clinic, now with a second generation — Dr. Siddhant Mahajan — continuing the family&rsquo;s commitment to patient care.</p>
<p class="muted" style="margin-top:1rem">The clinic operates as an ISO 9001:2008 certified facility, specialising in dental implants and orthodontics, equipped with modern diagnostic and treatment technology.</p>
</div>
</div></section>'''

    values = f'''<section class="section bg-ink"><div class="wrap">
{section_head("What guides us", "The same principles, for nearly 40 years.", "", light=True)}
<div class="feat-grid stagger" data-reveal>
<div class="feat"><span class="feat__no">i.</span><h3>Honest, ethical care</h3><p>Patient-centric treatment — no unnecessary procedures, ever.</p></div>
<div class="feat"><span class="feat__no">ii.</span><h3>Specialist-led</h3><p>Endodontics, implants and orthodontics handled by trained specialists.</p></div>
<div class="feat"><span class="feat__no">iii.</span><h3>Modern technique</h3><p>Time-tested expertise combined with current dental technology.</p></div>
<div class="feat"><span class="feat__no">iv.</span><h3>Hygiene standards</h3><p>ISO 9001:2008 certified facility, maintained to strict standards.</p></div>
</div>
</div></section>'''

    cta = f'''<section class="ctaband"><div class="wrap ctaband__row" data-reveal>
<div><span class="eyebrow eyebrow--light">Meet the doctors</span><h2>Two generations of expertise.</h2><p>Get to know the doctors who will treat you.</p></div>
<div class="ctaband__btns"><a class="btn btn--cream" href="doctors.html">Meet the Doctors</a></div>
</div></section>'''

    body = hero + story + values + cta
    return page("About", "The story and legacy of Mahajan Dental Care, Old Faridabad, since 1986.", body, active="about.html")

open(os.path.join(BASE, "about.html"), "w", encoding="utf-8").write(build_about())
print("about.html written")

# ============================================================ SERVICES ====
def build_services():
    hero = f'''<section class="section" style="padding-top:clamp(3rem,6vw,4.5rem)"><div class="wrap">
<nav aria-label="Breadcrumb" class="muted" style="font-size:.85rem;margin-bottom:1.6rem"><a href="index.html">Home</a> / Services</nav>
<span class="eyebrow">Services</span>
<h1 class="display-1" style="max-width:18ch">Every treatment, handled by the right specialist.</h1>
<p class="lead" style="margin-top:1.4rem;max-width:60ch">Nearly four decades of dental care under one roof — from routine check-ups to specialist implant and root canal treatment.</p>
</div></section>'''

    items = [
        ("root-canal", "Root Canal Treatment", "Designed to save a tooth damaged by deep decay or infection. Single-sitting RCT available, so you leave pain-free faster."),
        ("implants", "Dental Implants", "Long-lasting replacements for missing teeth, planned and placed by a certified implantologist."),
        ("braces", "Braces &amp; Orthodontics", "Correcting misaligned teeth, gaps and bite problems for a healthier, more confident smile."),
        ("gum-care", "Gum Disease &amp; Bleeding Gums", "Early diagnosis and treatment for gum problems, before they progress to serious periodontal disease."),
        ("dentures", "Dentures", "An effective, affordable solution for replacing missing teeth and restoring oral function."),
        ("cosmetic", "Cosmetic Dentistry &amp; Smile Makeovers", "Smile transformations planned around your natural proportions — refined, not overdone."),
        ("tooth-replacement", "Tooth Replacement &amp; Impaction", "Treatment for impacted teeth and comprehensive options for replacing missing ones."),
        ("microendo", "Micro-Endodontics", "Precise, microscope-level root canal treatment for complex cases."),
    ]
    lis = []
    for anchor, title, desc in items:
        lis.append(f'<li id="{anchor}"><a href="{WA_BOOK}" target="_blank" rel="noopener"><span class="tlist__thumb">{I_TOOTH}</span><span class="tlist__body"><h3>{title}</h3><p>{desc}</p></span><span class="tlist__arrow">{I_ARROW}</span></a></li>')
    listing = f'<section class="section bg-card"><div class="wrap"><ul class="tlist" data-reveal>{"".join(lis)}</ul></div></section>'

    cta = f'''<section class="ctaband"><div class="wrap ctaband__row" data-reveal>
<div><span class="eyebrow eyebrow--light">Not sure what you need?</span><h2>Tell us the problem — we&rsquo;ll recommend the treatment.</h2></div>
<div class="ctaband__btns"><a class="btn btn--cream" href="{WA_BOOK}" target="_blank" rel="noopener">WhatsApp Us</a></div>
</div></section>'''

    body = hero + listing + cta
    return page("Services", "The full range of dental treatments at Mahajan Dental Care, Old Faridabad.", body, active="services.html")

open(os.path.join(BASE, "services.html"), "w", encoding="utf-8").write(build_services())
print("services.html written")

# ============================================================= DOCTORS ====
def build_doctors():
    hero = f'''<section class="section" style="padding-top:clamp(3rem,6vw,4.5rem)"><div class="wrap">
<nav aria-label="Breadcrumb" class="muted" style="font-size:.85rem;margin-bottom:1.6rem"><a href="index.html">Home</a> / Doctors</nav>
<span class="eyebrow">The doctors</span>
<h1 class="display-1" style="max-width:18ch">Two generations of dental expertise.</h1>
<p class="lead" style="margin-top:1.4rem;max-width:60ch">A family practice — the person planning your treatment is the one who sees it through.</p>
</div></section>'''

    docs = [
        ("Dr. Tarun Mahajan", "Founder &middot; Endodontist, Oral Surgeon &amp; Implantologist",
         "B.D.S. (Pb.), D.Endo, MISOI",
         "With nearly four decades of clinical excellence, Dr. Tarun Mahajan is a highly experienced dental surgeon dedicated to advanced endodontic and implant care. Since founding Mahajan Dental Centre in 1986, he has combined time-tested expertise with modern dental innovations to ensure the highest standards of patient health and comfort.",
         ["Fellow of the International College of Dentists (USA)",
          "Formerly House Surgeon at Government Dental College &amp; Hospital, Amritsar",
          "Regd. No. PDC 929/A",
          "Leads an ISO 9001:2008 certified clinic specialising in implants and orthodontics"]),
        ("Dr. Siddhant Mahajan", "Micro-Endodontics &amp; Smile Makeover Specialist",
         "BDS, MDS",
         "Dr. Siddhant Mahajan combines 5 years of clinical experience with a gentle touch to redefine the dental experience. As a specialist in micro-endodontics and smile makeovers, he believes every tooth deserves the highest level of care — and specialises in single-sitting RCTs, so patients get back to their lives faster and pain-free.",
         ["Specialist in Micro-Endodontics",
          "Smile Makeover specialist",
          "Single-Sitting Root Canal Treatment (RCT)",
          "Precise, microscopic-level treatment in a relaxed environment"]),
    ]
    cards = []
    for name, role, qual, bio, creds in docs:
        cred_html = "".join(f"<li>{c}</li>" for c in creds)
        cards.append(f'''<article class="person" data-reveal>
<span class="person__photo"><span class="person__ph">{I_LEAF}<span>Add doctor photo</span></span></span>
<div class="person__body"><h3 class="person__name">{name}</h3><p class="person__role">{role}</p><p class="person__qual">{qual}</p><p class="person__bio">{bio}</p><ul class="person__cred">{cred_html}</ul></div>
</article>''')
    grid = f'<section class="section bg-card"><div class="wrap"><div class="team-grid">{"".join(cards)}</div></div></section>'

    cta = f'''<section class="ctaband"><div class="wrap ctaband__row" data-reveal>
<div><span class="eyebrow eyebrow--light">Book a consultation</span><h2>Meet the doctors in person.</h2></div>
<div class="ctaband__btns"><a class="btn btn--cream" href="{WA_BOOK}" target="_blank" rel="noopener">Book an Appointment</a></div>
</div></section>'''

    body = hero + grid + cta
    return page("Doctors", "Meet Dr. Tarun Mahajan and Dr. Siddhant Mahajan at Mahajan Dental Care.", body, active="doctors.html")

open(os.path.join(BASE, "doctors.html"), "w", encoding="utf-8").write(build_doctors())
print("doctors.html written")

# ============================================================== CLINIC ====
def build_clinic():
    hero = f'''<section class="section" style="padding-top:clamp(3rem,6vw,4.5rem)"><div class="wrap">
<nav aria-label="Breadcrumb" class="muted" style="font-size:.85rem;margin-bottom:1.6rem"><a href="index.html">Home</a> / Clinic</nav>
<span class="eyebrow">The clinic</span>
<h1 class="display-1" style="max-width:16ch">Nearly 40 years in the same community.</h1>
<p class="lead" style="margin-top:1.4rem;max-width:60ch">In Gopi Colony, Old Faridabad — an ISO 9001:2008 certified facility equipped with modern dental technology.</p>
</div></section>'''

    gallery = f'''<section class="section bg-card"><div class="wrap">
<div class="gallery" data-reveal>
<figure class="frame g1"><img src="{IMG}entrance-signage.jpg" alt="Clinic entrance"><span class="frame__tag">Entrance</span></figure>
<figure class="frame g2"><img src="{IMG}treatment-room-1.jpg" alt="Treatment room"><span class="frame__tag">Treatment room</span></figure>
<figure class="frame g4"><img src="{IMG}reception-bench.jpg" alt="Reception"><span class="frame__tag">Reception</span></figure>
<figure class="frame g4"><img src="{IMG}treatment-room-2.jpg" alt="Treatment room"><span class="frame__tag">Treatment room</span></figure>
<figure class="frame g5"><img src="{IMG}treatment-room-3.jpg" alt="Treatment room"><span class="frame__tag">Treatment room</span></figure>
</div>
</div></section>'''

    access = f'''<section class="section bg-ink"><div class="wrap split">
<div data-reveal><span class="eyebrow eyebrow--light">Getting here</span><h2 class="display-2" style="color:var(--cream)">Easy to find, easy to reach.</h2><p class="mut" style="margin-top:1.2rem">{ADDRESS}</p><a class="text-link text-link--light" style="margin-top:1.4rem" href="{MAPS}" target="_blank" rel="noopener">Open in Google Maps{I_ARROW}</a></div>
<div class="split__media" data-reveal><figure class="frame frame--wide"><img src="{IMG}exterior-signage.jpg" alt="Mahajan Dental Care building"></figure></div>
</div></section>'''

    body = hero + gallery + access
    return page("Clinic", "Inside Mahajan Dental Care, Old Faridabad.", body, active="clinic.html")

open(os.path.join(BASE, "clinic.html"), "w", encoding="utf-8").write(build_clinic())
print("clinic.html written")

# ============================================================= CONTACT ====
def build_contact():
    hero = f'''<section class="section" style="padding-top:clamp(3rem,6vw,4.5rem)"><div class="wrap">
<nav aria-label="Breadcrumb" class="muted" style="font-size:.85rem;margin-bottom:1.6rem"><a href="index.html">Home</a> / Contact</nav>
<span class="eyebrow">Get in touch</span>
<h1 class="display-1" style="max-width:16ch">Let&rsquo;s find you a time.</h1>
<p class="lead" style="margin-top:1.4rem;max-width:60ch">Message us on WhatsApp, call the clinic, or send a note below — we usually reply the same day.</p>
</div></section>'''

    grid = f'''<section class="section bg-card"><div class="wrap contact-grid">
<div data-reveal>
<div class="contact-card"><h3>{I_PIN}Visit</h3><p>{ADDRESS}</p><a class="text-link" href="{MAPS}" target="_blank" rel="noopener">Get directions{I_ARROW}</a></div>
<div class="contact-card"><h3>{I_CLOCK}Hours</h3><p>{HOURS}</p></div>
<div class="contact-card"><h3>{I_PHONE}Contact</h3><p><a href="{PHONE_TEL}">{PHONE_DISPLAY}</a><br><a href="mailto:{EMAIL}">{EMAIL}</a></p><a class="text-link" href="{WA_BOOK}" target="_blank" rel="noopener">WhatsApp us{I_ARROW}</a></div>
</div>
<div data-reveal>
<form data-wa-form>
<div class="formfield"><label for="cf-name">Your name</label><input id="cf-name" name="name" type="text" required></div>
<div class="formfield"><label for="cf-phone">Phone number</label><input id="cf-phone" name="phone" type="tel"></div>
<div class="formfield"><label for="cf-msg">How can we help?</label><textarea id="cf-msg" name="message" required></textarea></div>
<button class="btn" type="submit" style="width:100%;justify-content:center">Send via WhatsApp</button>
<p class="form__msg"></p>
</form>
</div>
</div></section>'''

    body = hero + grid
    return page("Contact", "Contact Mahajan Dental Care, Old Faridabad.", body, active="contact.html")

open(os.path.join(BASE, "contact.html"), "w", encoding="utf-8").write(build_contact())
print("contact.html written")

# ====================================================== PRIVACY/DISCLAIMER
def build_legal(title, active, paras):
    hero = f'''<section class="section" style="padding-top:clamp(3rem,6vw,4.5rem)"><div class="wrap">
<nav aria-label="Breadcrumb" class="muted" style="font-size:.85rem;margin-bottom:1.6rem"><a href="index.html">Home</a> / {title}</nav>
<span class="eyebrow">Legal</span>
<h1 class="display-1" style="max-width:18ch">{title}</h1>
</div></section>'''
    body_paras = "".join(f'<p class="muted" style="margin-bottom:1.2rem">{p}</p>' for p in paras)
    content = f'<section class="section bg-card"><div class="wrap" style="max-width:70ch">{body_paras}</div></section>'
    body = hero + content
    return page(title, f"{title} — Mahajan Dental Care.", body, active=active)

open(os.path.join(BASE, "privacy.html"), "w", encoding="utf-8").write(build_legal(
    "Privacy Policy", "privacy.html",
    [
        "Mahajan Dental Care respects your privacy. Information you share with us — by phone, WhatsApp, email or the contact form on this site — is used only to respond to your enquiry and to manage your care.",
        "We do not sell or share your personal information with third parties for marketing purposes. Clinical records are kept confidential and handled in line with standard medical record-keeping practice.",
        "If you have questions about how your information is handled, please contact us directly at " + EMAIL + ".",
    ]
))
print("privacy.html written")

open(os.path.join(BASE, "disclaimer.html"), "w", encoding="utf-8").write(build_legal(
    "Medical Disclaimer", "disclaimer.html",
    [
        "The content on this website is provided for general informational purposes only and is not a substitute for professional dental advice, diagnosis or treatment.",
        "Always consult a qualified dentist regarding any dental concern before making treatment decisions. Individual results vary from patient to patient depending on clinical circumstances.",
        "In a dental emergency, please call the clinic directly at " + PHONE_DISPLAY + ".",
    ]
))
print("disclaimer.html written")
