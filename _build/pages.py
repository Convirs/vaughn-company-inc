"""Page bodies. Copy carried over verbatim from the live Weblium site."""


def home(ICON, PHONES, ADDRESS):
    letter = [
        "I would like to take a moment to express our appreciation for all that Vaughn Company Inc. does for APAC &ndash; Central, Inc. We have been very satisfied with the services we have received over the many years of doing business together. With the many challenges that come from being a seasonal business in the construction industry, it is vital that we have a transport company like Vaughn Company Inc. that understands our business and aids us in meeting the needs of our projects.",
        "The drivers that are assigned for our projects are professional, punctual, and always friendly to deal with. Truck availability is always at the utmost importance to us at APAC &ndash; Central, Inc. and all year long Vaughn Company Inc. consistently comes through.",
        "Danny and Michael have been a major factor in our continued relationship with Vaughn Company Inc. Their experience and commitment to providing us with the best transport service available makes the decision to call Vaughn Company Inc. an easy one. They are always readily available on the phone and continuously meets our expectations.",
        "We look forward to many more years of successful and on time business with Vaughn Company Inc. and would not hesitate to recommend their services to any potential company.",
    ]
    letter_html = "\n              ".join(f"<p>{p}</p>" for p in letter)
    yt = "ZTzYgyLRYi8"
    return f"""
<section class="hero">
  <div class="bg-layer" aria-hidden="true"></div>
  <div class="bg-overlay" aria-hidden="true"></div>
  <div class="container">
    <h1 class="h-hero">Excavation, Material Hauling, Dirt Work, and Rock Sales</h1>
    <p class="lead">Earthwork done right the first time - hassle-free, no matter the size.</p>
    <a class="btn btn--lg" href="#contact">Call Us Today</a>
  </div>
</section>

<section class="section problems">
  <div class="bg-layer" aria-hidden="true"></div>
  <div class="bg-overlay" aria-hidden="true"></div>
  <div class="container split">
    <div>
      <h2 class="h-section">Lack of earthwork experience can lead to problems.</h2>
      <ul>
        <li>&#9679; Job isn't done right the first time</li>
        <li>&#9679; Inadequate man-power</li>
        <li>&#9679; Lack of industry connections</li>
        <li>&#9679; Equipment not built for the job</li>
      </ul>
    </div>
    <img src="/images/red-dump-truck.webp" alt="Red Vaughn Company dump truck parked on wet pavement" width="640" height="481" loading="lazy" decoding="async">
  </div>
</section>

<section class="video-band">
  <div class="yt-bg" aria-hidden="true">
    <iframe src="https://www.youtube-nocookie.com/embed/{yt}?autoplay=1&amp;mute=1&amp;loop=1&amp;playlist={yt}&amp;controls=0&amp;playsinline=1&amp;rel=0&amp;modestbranding=1" title="Background video" tabindex="-1" allow="autoplay; encrypted-media" loading="lazy"></iframe>
  </div>
  <div class="bg-overlay" aria-hidden="true"></div>
  <div class="container">
    <span class="eyebrow eyebrow--lg">Established in 1959</span>
    <h2 class="h-hero">You deserve experts to get your job done.</h2>
    <div><button class="play-btn" type="button" data-video-popup="{yt}" aria-label="Play video">{ICON['play']}</button></div>
    <a class="btn btn--lg btn--outline" href="#contact">Call Us Today</a>
  </div>
</section>

<section class="tiles" aria-label="Memberships">
  <div class="tile tile--1">
    <div class="bg-layer" aria-hidden="true"></div><div class="bg-overlay" aria-hidden="true"></div>
    <img src="/images/assoc-mdta.webp" alt="Missouri Dump Truckers Association logo" width="170" height="167" loading="lazy">
    <p>Missouri Dump Truckers Association</p>
  </div>
  <div class="tile tile--2">
    <div class="bg-layer" aria-hidden="true"></div><div class="bg-overlay" aria-hidden="true"></div>
    <img src="/images/assoc-tsaca.webp" alt="Tri-State Area Contractors Association logo" width="258" height="198" loading="lazy">
    <p>Tri-State Area Contractors Association</p>
  </div>
  <div class="tile tile--3">
    <div class="bg-layer" aria-hidden="true"></div><div class="bg-overlay" aria-hidden="true"></div>
    <img src="/images/assoc-agc.svg" alt="Associated General Contractors of America logo" width="390" height="148" loading="lazy">
    <p>Associated General Contractors of America</p>
  </div>
  <div class="tile tile--4">
    <div class="bg-layer" aria-hidden="true"></div><div class="bg-overlay" aria-hidden="true"></div>
    <img src="/images/assoc-monett.webp" alt="Monett Area Chamber of Commerce logo" width="1729" height="751" loading="lazy">
    <p>Monett Area Chamber of Commerce</p>
  </div>
</section>

<section class="testimonials" aria-label="Testimonials">
  <div class="container">
    <div class="carousel" data-carousel>
      <div class="carousel-viewport">
        <div class="carousel-track">
          <figure class="slide">
            <img class="contain" src="/images/testimonial-apac.webp" alt="APAC logo" width="120" height="120" loading="lazy">
            <figcaption><h3 class="h-card">Kayla Robertson</h3><p class="role">Transportation Manager | APAC</p></figcaption>
            <blockquote>With the many challenges that come from being a seasonal business in the construction industry, it is vital that we have a transport company like Vaughn Company Inc. that understands our business and aids us in meeting the needs of our projects.</blockquote>
            <details class="readmore acc" name="testimonial">
              <summary>Read more</summary>
              <div class="full">
              {letter_html}
              </div>
            </details>
          </figure>
          <figure class="slide">
            <img src="/images/testimonial-cowboy.webp" alt="Cowboy Asphalt Products logo" width="120" height="120" loading="lazy">
            <figcaption><h3 class="h-card">Cowboy Asphalt Products</h3><p class="role">&nbsp;</p></figcaption>
            <blockquote>Family owned and operated, extremely good people, really good friends of mine. They go out of their way to do things for you.</blockquote>
          </figure>
        </div>
      </div>
      <button class="carousel-arrow prev" type="button" aria-label="Previous testimonial">{ICON['chev-l']}</button>
      <button class="carousel-arrow next" type="button" aria-label="Next testimonial">{ICON['chev-r']}</button>
      <div class="carousel-dots"></div>
    </div>
  </div>
</section>

<section class="section complexity">
  <div class="bg-layer" aria-hidden="true"></div>
  <div class="bg-overlay" aria-hidden="true"></div>
  <div class="container">
    <span class="eyebrow">Project Complexity</span>
    <h2 class="h-sub">We've been in business since 1959 and realize that all jobs are unique and complex. Rest assured that we meticulously assess each job, ensuring the perfect match of skilled experts and equipment for a project's guaranteed success.</h2>
    <a class="btn btn--lg" href="#contact">Call Us Today</a>
  </div>
</section>

<section class="section steps">
  <div class="container">
    <h2 class="h-section">Get Started Today</h2>
    <div class="steps-grid">
      <div class="step"><div class="step-icon">{ICON['phone']}</div><h3 class="h-card">Call</h3><p>Call us to schedule a time to come by our office to talk about your project.</p></div>
      <div class="step"><div class="step-icon">{ICON['calc']}</div><h3 class="h-card">Estimate</h3><p>We will visit the project site to create the estimate for your project.</p></div>
      <div class="step"><div class="step-icon">{ICON['calendar']}</div><h3 class="h-card">Schedule</h3><p>Pay for your project and we will get it put on our schedule.</p></div>
    </div>
    <a class="btn" href="#contact">Call Us Today</a>
  </div>
</section>

<section class="ready" id="contact">
  <div class="ready-media">
    <img src="/images/dozer-dump-truck.webp" alt="Bulldozer and red dump truck working a cleared job site" width="1316" height="987" loading="lazy" decoding="async">
  </div>
  <div class="ready-content">
    <h2 class="h-section">Ready To Start Your Project?</h2>
    <p class="sub">Give us a call today to get your earthwork done right the first time.<br>Hassle-free, no matter the size.</p>
    <div class="info-row"><h3 class="h-card">Address</h3><span>22453 Highway H, Monett, MO</span></div>
    <div class="info-row"><h3 class="h-card">Hauling</h3><a href="tel:{PHONES['hauling'][1]}">{PHONES['hauling'][0]}</a></div>
    <div class="info-row"><h3 class="h-card">Excavation</h3><a href="tel:{PHONES['excavation'][1]}">{PHONES['excavation'][0]}</a></div>
  </div>
</section>

<div class="modal" role="dialog" aria-modal="true" aria-label="Video">
  <div class="modal-inner"><button class="modal-close" type="button" aria-label="Close video">&times;</button></div>
</div>
"""


PROJECTS = [
    ("project-menards.webp", "Menards", "Joplin, MO.", "Aerial view of earthwork at the Menards site in Joplin", 680, 382),
    ("project-coops-coffee.webp", "Coop's Coffee", "Monett, MO.", "Coming soon sign and excavator at the Coop's Coffee site in Monett", 987, 1316),
    ("project-performing-arts.webp", "Performing Arts Center", "Cassville, MO.", "Excavator grading the Performing Arts Center site in Cassville", 1639, 793),
    ("project-cowork-collective.webp", "Cowork Collective", "Monett, MO.", "Excavator demolishing a building for Cowork Collective in Monett", 1316, 987),
    ("project-ozark-high.webp", "Ozark High School Storm Shelter", "Ozark, MO.", "Aerial view of the Ozark High School storm shelter dig", 1348, 963),
    ("project-ozark-middle.webp", "Ozark Middle School Storm Shelter", "Ozark, MO.", "Aerial view of the Ozark Middle School storm shelter site", 1348, 963),
    ("project-tiger-paw.webp", "Tiger Paw Early Childhood Center Storm Shelter", "Ozark, MO.", "Aerial view of the Tiger Paw Early Childhood Center storm shelter excavation", 1348, 963),
]


def about(ICON):
    cards = "\n      ".join(
        f'<figure class="project"><img src="/images/{f}" alt="{alt}" width="{w}" height="{h}" loading="lazy" decoding="async">'
        f'<figcaption><h3>{t}</h3><p>{loc}</p></figcaption></figure>'
        for f, t, loc, alt, w, h in PROJECTS)
    vid = "dnon5u-oxNI"
    return f"""
<section class="section about-hero">
  <div class="bg-layer" aria-hidden="true"></div>
  <div class="bg-overlay" aria-hidden="true"></div>
  <div class="container split">
    <div>
      <span class="eyebrow eyebrow--ink">ABOUT US</span>
      <h1>Vaughn Company, Inc.</h1>
      <p class="lead">established 1959</p>
      <p class="body">Vaughn Company was founded in 1959 by the late Leon Vaughn. He started out with one truck and a backhoe and grew the company to what it is today. Danny Vaughn took sole ownership in 2021 and works alongside his children.</p>
    </div>
    <img src="/images/about-team.webp" alt="The Vaughn family and team at a Monett Area Chamber of Commerce event" width="1076" height="1207" fetchpriority="high">
  </div>
</section>

<section class="section about-video">
  <div class="container">
    <span class="eyebrow eyebrow--red">Vaughn Company, Inc.</span>
    <h2 class="h-sub">A Day in the Life of Hauling Asphalt and Moving Dirt!</h2>
    <div class="video-embed" data-video="{vid}" data-title="A Day in the Life of Hauling Asphalt and Moving Dirt" style="background-image:url('https://i.ytimg.com/vi/{vid}/hqdefault.jpg')">
      <button class="play-btn" type="button" aria-label="Play video: A Day in the Life of Hauling Asphalt and Moving Dirt">{ICON['play']}</button>
    </div>
  </div>
</section>

<section class="section projects">
  <div class="container">
    <h2 class="h-section">Past Projects</h2>
    <p class="sub">Check Out Some Of Our Earth-Moving Marvels!</p>
    <div class="project-grid">
      {cards}
    </div>
  </div>
</section>

<section class="cta-band">
  <div class="bg-layer" aria-hidden="true"></div>
  <div class="bg-overlay" aria-hidden="true"></div>
  <div class="container" style="position:relative;z-index:2">
    <h2 class="h-sub">Contact Us Today To Get Your Project Started!</h2>
    <a class="btn btn--dark" href="/#contact">Call Us Today</a>
  </div>
</section>
"""


def hiring(ICON, DRIVER_APP, EMPLOY_APP):
    vid = "dnon5u-oxNI"
    benefits = [("home", "Home Every Night"), ("pay", "Paid Weekly"), ("shield", "Health/Dental/Vision Insurance"),
                ("piggy", "401K"), ("sun", "Vacation Pay")]
    items = "\n        ".join(f'<li><span class="benefit-icon">{ICON[i]}</span>{t}</li>' for i, t in benefits)
    return f"""
<section class="hiring-hero">
  <div class="yt-bg" aria-hidden="true">
    <iframe src="https://www.youtube-nocookie.com/embed/{vid}?autoplay=1&amp;mute=1&amp;loop=1&amp;playlist={vid}&amp;controls=0&amp;playsinline=1&amp;rel=0&amp;modestbranding=1" title="Background video" tabindex="-1" allow="autoplay; encrypted-media"></iframe>
  </div>
  <div class="bg-overlay" aria-hidden="true"></div>
  <div class="container">
    <h1>Work For Vaughn Company Today</h1>
    <p>Home Every Night | Paid Weekly | Health/Dental/Vision Insurance | 401K | Vacation Pay</p>
    <div class="btn-row">
      <a class="btn" href="{DRIVER_APP}" target="_blank" rel="noopener">Driver Employment Application</a>
      <a class="btn" href="{EMPLOY_APP}" target="_blank" rel="noopener">Application For Employment</a>
    </div>
  </div>
</section>

<section class="section benefits">
  <div class="container split">
    <img src="/images/hiring-truck.webp" alt="Black Vaughn Company dump truck at a truck show" width="640" height="555" loading="lazy" decoding="async">
    <div>
      <h2 class="sr-only">Benefits</h2>
      <ul class="benefit-list">
        {items}
      </ul>
    </div>
  </div>
</section>

<section class="cta-band cta-band--strong">
  <div class="bg-layer" aria-hidden="true"></div>
  <div class="bg-overlay" aria-hidden="true"></div>
  <div class="container" style="position:relative;z-index:2">
    <h2 class="h-section">Apply Today Online!</h2>
    <div class="btn-row">
      <a class="btn btn--white" href="{DRIVER_APP}" target="_blank" rel="noopener">Driver Employment Application</a>
      <a class="btn btn--white" href="{EMPLOY_APP}" target="_blank" rel="noopener">Application For Employment</a>
    </div>
  </div>
</section>
"""


def contact():
    def person(name, phone, email):
        digits = "+" + "".join(c for c in phone if c.isdigit())
        return (f'<div class="person"><strong>{name}</strong><a href="tel:{digits}">{phone}</a>'
                f'<a href="mailto:{email}">{email}</a></div>')
    return f"""
<section class="section contact-page">
  <div class="container">
    <span class="eyebrow eyebrow--red">Contact Information</span>
    <h1 class="h-section">Ready To Start Your Project?</h1>
    <p class="lead">Give us a call today to get your earthwork done right the first time - hassle-free, no matter the size.</p>
    <div class="directory">
      <div>
        <h2>Excavation</h2>
        {person("Jacob Vaughn", "+1 417-737-1427", "jvaughn@vaughndirtworks.com")}
        {person("Clayton Murphy", "+1 417-235-9912", "cmurphy@vaughndirtworks.com")}
      </div>
      <div>
        <h2>Hauling</h2>
        {person("Michael Flummerfelt", "+1 417-236-2269", "michael@vaughncompany.net")}
      </div>
      <div>
        <h2>Office</h2>
        {person("Office", "+1 417-235-7700", "jdvco@vaughncompany.net")}
      </div>
    </div>
  </div>
</section>
"""


def privacy():
    return """
<section class="legal">
  <div class="container">
    <h1 class="sr-only">Privacy Policy</h1>
    <div id="policy" data-policy-key="WXpGVVdFSTVZa2d5UzFOQlRXYzlQUT09" data-extra="h-align=left&amp;table-style=accordion">Please wait while the policy is loaded. If it does not load, please <a rel="nofollow" href="https://app.termageddon.com/api/policy/WXpGVVdFSTVZa2d5UzFOQlRXYzlQUT09?h-align=left&amp;table-style=accordion" target="_blank">click here</a>.</div>
  </div>
</section>
"""


def notfound():
    return """
<section class="notfound">
  <div class="container">
    <h1 class="h-section">Page Not Found</h1>
    <p>The page you are looking for does not exist or has moved.</p>
    <a class="btn btn--lg" href="/">Back to Home</a>
  </div>
</section>
"""
