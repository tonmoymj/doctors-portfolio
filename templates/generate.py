import os
import json

templates = [
    {
        'filename': 'template-051.html',
        'specialty': 'General Physician',
        'layout': 3,
        'accent': '#2D6A4F',
        'doctor': 'Dr. Yuki Tanaka, MD, FACP',
        'city': 'San Francisco, CA',
        'services': ['Integrative Primary Care', 'Mind-Body Medicine', 'Functional Medicine', 'Sleep Medicine', 'Chronic Fatigue', 'Gut Health & Microbiome'],
        'education': ['UCSF School of Medicine (MD)', 'UCSF Medical Center (Residency – Internal Medicine)', 'Andrew Weil Center (Fellowship – Integrative Medicine)', 'Board Certified in Internal Medicine'],
        'stats': ['14+ years', '4,100+ patients', '99% satisfaction'],
        'phone': '+1 (415) 555-5163'
    },
    {
        'filename': 'template-052.html',
        'specialty': 'General Physician',
        'layout': 4,
        'accent': '#4A5C2A',
        'doctor': 'Dr. Amara Diallo, MD, MPH',
        'city': 'Washington, DC',
        'services': ['Women\'s Primary Care', 'Contraceptive Counseling', 'Pre-Conception Care', 'Sexual Health', 'Osteoporosis Prevention', 'Menopausal Management'],
        'education': ['Howard University College of Medicine (MD)', 'George Washington University (Residency)', 'Johns Hopkins Bloomberg (MPH – Women\'s Health)', 'Board Certified in Family Medicine'],
        'stats': ['12+ years', '4,800+ patients', '98% satisfaction'],
        'phone': '+1 (202) 555-5274'
    },
    {
        'filename': 'template-053.html',
        'specialty': 'General Physician',
        'layout': 5,
        'accent': '#1D5A3F',
        'doctor': 'Dr. Patrick Sullivan, MD, FACP, FAAFP',
        'city': 'Nashville, TN',
        'services': ['Rural Medicine', 'Urgent Care', 'Telemedicine', 'Occupational Health', 'DOT Physicals', 'Workers\' Compensation Medicine'],
        'education': ['Vanderbilt University School of Medicine (MD)', 'Saint Thomas Hospital (Residency – Family Medicine & Internal Medicine)', 'AAFP (Fellow)', 'Board Certified in Family Medicine'],
        'stats': ['24+ years', '9,200+ patients', '96% satisfaction'],
        'phone': '+1 (615) 555-5385'
    },
    {
        'filename': 'template-054.html',
        'specialty': 'General Physician',
        'layout': 6,
        'accent': '#3A4C1A',
        'doctor': 'Dr. Elena Marchetti, MD, PhD, FACP',
        'city': 'Philadelphia, PA',
        'services': ['Research-Based Primary Care', 'Clinical Trials Participation', 'Pharmacogenomics', 'Precision Medicine', 'Novel Therapeutics', 'Academic Consultations'],
        'education': ['University of Pennsylvania (MD, PhD)', 'Penn Medicine (Residency)', 'NIH (Fellowship – Translational Medicine)', 'Board Certified in Internal Medicine'],
        'stats': ['20+ years', '3,600+ patients', '98% satisfaction'],
        'phone': '+1 (215) 555-5496'
    },
    {
        'filename': 'template-055.html',
        'specialty': 'General Physician',
        'layout': 7,
        'accent': '#2D6A4F',
        'doctor': 'Dr. Kwame Asante, MD, FACP',
        'city': 'Chicago, IL',
        'services': ['Community Health', 'Preventive Screenings', 'Chronic Kidney Disease', 'Sickle Cell Disease Management', 'Hypertension in Diverse Populations', 'Health Equity Programs'],
        'education': ['Rush Medical College (MD)', 'Cook County Health (Residency – Internal Medicine)', 'University of Chicago (Fellowship – Community Health)', 'Board Certified in Internal Medicine'],
        'stats': ['16+ years', '7,300+ patients', '97% satisfaction'],
        'phone': '+1 (312) 555-5507'
    },
    {
        'filename': 'template-056.html',
        'specialty': 'General Physician',
        'layout': 8,
        'accent': '#4A5C2A',
        'doctor': 'Dr. Joanna Kowalski, MD, FACP',
        'city': 'Milwaukee, WI',
        'services': ['Geriatric Primary Care', 'Polypharmacy Review', 'Fall Prevention', 'Cognitive Assessment', 'Advance Care Planning', 'Palliative Medicine'],
        'education': ['Medical College of Wisconsin (MD)', 'Froedtert Hospital (Residency)', 'University of Wisconsin (Fellowship – Geriatric Medicine)', 'Board Certified in Geriatric Medicine'],
        'stats': ['18+ years', '5,900+ patients', '97% satisfaction'],
        'phone': '+1 (414) 555-5618'
    },
    {
        'filename': 'template-057.html',
        'specialty': 'Psychiatrist',
        'layout': 1,
        'accent': '#4A5568',
        'doctor': 'Dr. Rachel Goldstein, MD, FAPA',
        'city': 'New York, NY',
        'services': ['Adult Psychiatry', 'Depression & Anxiety', 'Bipolar Disorder', 'PTSD Treatment', 'Medication Management', 'Psychotherapy Integration'],
        'education': ['Columbia University Vagelos (MD)', 'NewYork-Presbyterian (Residency – Psychiatry)', 'NYU (Fellowship – Mood Disorders)', 'Board Certified in Psychiatry'],
        'stats': ['17+ years', '3,400+ patients', '98% satisfaction'],
        'phone': '+1 (212) 555-5729'
    },
    {
        'filename': 'template-058.html',
        'specialty': 'Psychiatrist',
        'layout': 2,
        'accent': '#6B7F6B',
        'doctor': 'Dr. Theodore Marsh, MD, FAPA',
        'city': 'Seattle, WA',
        'services': ['Child & Adolescent Psychiatry', 'ADHD Diagnosis & Treatment', 'Autism Spectrum Support', 'School Refusal', 'Childhood Anxiety', 'Trauma-Informed Care'],
        'education': ['University of Washington (MD)', 'Seattle Children\'s Hospital (Residency – Child Psychiatry)', 'UCSF (Fellowship – Child & Adolescent Psychiatry)', 'Board Certified in Child & Adolescent Psychiatry'],
        'stats': ['15+ years', '4,100+ patients', '98% satisfaction'],
        'phone': '+1 (206) 555-5834'
    },
    {
        'filename': 'template-059.html',
        'specialty': 'Psychiatrist',
        'layout': 3,
        'accent': '#4A5568',
        'doctor': 'Dr. Laila Al-Hussain, MD, FAPA, DFAACAP',
        'city': 'Houston, TX',
        'services': ['Geriatric Psychiatry', 'Dementia Behavioral Management', 'Late-Life Depression', 'Psychosis in Elderly', 'Caregiver Burnout', 'Memory Care Consultation'],
        'education': ['UT Health Houston (MD)', 'UTHealth Houston (Residency)', 'Baylor College of Medicine (Fellowship – Geriatric Psychiatry)', 'Board Certified in Geriatric Psychiatry'],
        'stats': ['19+ years', '2,900+ patients', '97% satisfaction'],
        'phone': '+1 (713) 555-5941'
    },
    {
        'filename': 'template-060.html',
        'specialty': 'Psychiatrist',
        'layout': 4,
        'accent': '#6B7F6B',
        'doctor': 'Dr. Eliot Fairbanks, MD, FAPA',
        'city': 'San Francisco, CA',
        'services': ['Addiction Psychiatry', 'Substance Use Disorders', 'Opioid Use Treatment', 'Dual Diagnosis', 'Harm Reduction', 'MAT Programs'],
        'education': ['Stanford University School of Medicine (MD)', 'UCSF Medical Center (Residency – Psychiatry)', 'San Francisco General Hospital (Fellowship – Addiction Psychiatry)', 'Board Certified in Addiction Psychiatry'],
        'stats': ['16+ years', '3,700+ patients', '97% satisfaction'],
        'phone': '+1 (415) 555-6052'
    }
]

def hex_to_rgb(hex_code):
    hex_code = hex_code.lstrip('#')
    return ','.join(tuple(str(int(hex_code[i:i+2], 16)) for i in (0, 2, 4)))

hero_svg = """
<div style="width:100%;height:100%;display:flex;align-items:center;justify-content:center;background:var(--bg-alt);border-radius:var(--radius-lg);position:relative;overflow:hidden;min-height:400px;">
  <svg width="160" height="220" viewBox="0 0 160 220" fill="none" style="opacity:0.18;">
    <circle cx="80" cy="60" r="48" fill="currentColor" style="color:var(--accent)"/>
    <ellipse cx="80" cy="180" rx="70" ry="44" fill="currentColor" style="color:var(--accent)"/>
    <rect x="60" y="108" width="40" height="16" rx="8" fill="white" opacity="0.8"/>
  </svg>
  <div style="position:absolute;bottom:16px;left:16px;right:16px;background:white;border-radius:8px;padding:12px 16px;border:1px solid var(--border);box-shadow:var(--shadow-sm);">
    <div style="font-size:0.7rem;color:var(--accent);font-weight:700;text-transform:uppercase;letter-spacing:0.08em;font-family:Inter,sans-serif;">Available for Consultation</div>
    <div style="font-size:0.82rem;color:var(--text-secondary);margin-top:3px;font-family:Inter,sans-serif;">Mon–Fri: 9:00 AM – 5:00 PM</div>
  </div>
</div>
"""

js = """
function toggleMenu() { document.getElementById('mobileMenu').classList.toggle('open'); }
document.querySelectorAll('#mobileMenu a').forEach(l => l.addEventListener('click', () => document.getElementById('mobileMenu').classList.remove('open')));
const observer = new IntersectionObserver((entries) => { entries.forEach(e => { if(e.isIntersecting){e.target.classList.add('visible');observer.unobserve(e.target);} }); }, {threshold:0.1, rootMargin:'0px 0px -40px 0px'});
document.querySelectorAll('.fade-in').forEach(el => observer.observe(el));
function handleSubmit(e) { e.preventDefault(); const btn=e.target.querySelector('[type="submit"]'); const orig=btn.textContent; btn.textContent='Request Sent ✓'; btn.style.background='var(--accent)'; btn.disabled=true; setTimeout(()=>{btn.textContent=orig;btn.style.background='';btn.disabled=false;e.target.reset();},4000); return false; }
"""

def generate_layout_styles(layout):
    css = ''
    if layout == 1:
        css = """
        .hero { display: grid; grid-template-columns: 1fr 1fr; gap: 40px; align-items: center; }
        .container { max-width: 1120px; margin: 0 auto; padding: 60px 20px; }
        section:nth-child(even) { background-color: var(--bg-alt); }
        .services-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 30px; }
        """
    elif layout == 2:
        css = """
        .layout-wrapper { display: grid; grid-template-columns: 280px 1fr; gap: 40px; max-width: 1200px; margin: 0 auto; padding: 40px 20px; align-items: start;}
        .sidebar { position: sticky; top: 100px; padding: 30px; background: var(--bg-alt); border-radius: var(--radius-lg); border: 1px solid var(--border);}
        .main-content { display: flex; flex-direction: column; gap: 60px; }
        .contact-section { grid-column: 1 / -1; max-width: 800px; margin: 0 auto; padding: 60px 20px; }
        .services-grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 20px; }
        .hero { display: none; }
        @media(max-width: 768px) { .layout-wrapper { grid-template-columns: 1fr; } .sidebar { position: static; } .services-grid { grid-template-columns: 1fr; } }
        """
    elif layout == 3:
        css = """
        .hero { display: grid; grid-template-columns: 7fr 5fr; gap: 60px; align-items: center; padding: 80px 20px; max-width: 1200px; margin: 0 auto; }
        .about-grid { display: grid; grid-template-columns: 1fr 1.5fr 1fr; gap: 40px; align-items: start; max-width: 1200px; margin: 0 auto; padding: 60px 20px; }
        .services-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 30px; max-width: 1200px; margin: 0 auto; padding: 60px 20px; }
        .service-card { min-height: 200px; padding: 30px; background: var(--bg); border: 1px solid var(--border); border-radius: var(--radius); }
        .container { padding: 60px 20px; max-width: 1200px; margin: 0 auto; }
        @media(max-width: 900px) { .about-grid, .services-grid, .hero { grid-template-columns: 1fr; } }
        """
    elif layout == 4:
        css = """
        section { padding: 100px 20px; max-width: 900px; margin: 0 auto; background: var(--bg) !important; }
        .hero { text-align: center; }
        .hero-img { margin-top: 60px; }
        .service-card { border: none; box-shadow: var(--shadow-sm); padding: 40px; text-align: center; }
        .services-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 40px; }
        .timeline-item { border-left: 2px solid var(--border); padding-left: 30px; margin-bottom: 40px; position: relative; }
        .timeline-item::before { content: ''; position: absolute; left: -6px; top: 0; width: 10px; height: 10px; border-radius: 50%; background: var(--accent); }
        .decorative-line { height: 1px; background: var(--border); margin: 20px 0; }
        @media(max-width: 768px) { .services-grid { grid-template-columns: 1fr; } }
        """
    elif layout == 5:
        css = """
        .hero { padding: 100px 20px; max-width: 1100px; margin: 0 auto; position: relative; }
        .hero-bg-text { position: absolute; top: 0; left: 0; font-size: 10vw; font-weight: 800; color: var(--bg-alt); z-index: -1; line-height: 1; opacity: 0.5;}
        .about-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 60px; max-width: 1100px; margin: 0 auto; padding: 60px 20px; }
        .services-list { list-style: none; padding: 0; max-width: 1100px; margin: 0 auto; padding: 60px 20px; }
        .services-list li { border-bottom: 1px solid var(--border); padding: 30px 0; display: flex; align-items: center; gap: 20px; }
        .section-num { font-family: 'Playfair Display', serif; font-size: 2rem; color: var(--accent); opacity: 0.5; }
        .pull-quote { font-size: 1.5rem; font-style: italic; border-left: 4px solid var(--accent); padding-left: 30px; margin: 40px 0; font-family: 'Playfair Display', serif; }
        .container { max-width: 1100px; margin: 0 auto; padding: 60px 20px;}
        @media(max-width: 768px) { .about-grid { grid-template-columns: 1fr; } }
        """
    elif layout == 6:
        css = """
        .hero { display: grid; grid-template-columns: 1fr 1fr; gap: 40px; align-items: center; max-width: 1000px; margin: 0 auto; padding: 80px 20px; }
        .milestone-counter { display: flex; gap: 20px; margin-top: 30px; }
        .timeline-section { padding: 80px 20px; max-width: 800px; margin: 0 auto; }
        .timeline-entry { padding: 40px; background: var(--bg-alt); border-radius: var(--radius-lg); margin-bottom: 30px; position: relative; }
        .timeline-entry::before { content: ''; position: absolute; left: -20px; top: 50%; width: 40px; height: 2px; background: var(--accent); }
        .timeline-year { font-weight: bold; color: var(--accent); margin-bottom: 10px; font-size: 1.2rem; }
        .services-simple { padding: 60px 20px; max-width: 800px; margin: 0 auto; display: flex; flex-wrap: wrap; gap: 15px; }
        .service-tag { padding: 10px 20px; background: var(--accent-light); color: var(--accent); border-radius: 30px; font-weight: 500; }
        .container { max-width: 1000px; margin: 0 auto; padding: 60px 20px; }
        @media(max-width: 768px) { .hero { grid-template-columns: 1fr; } .timeline-entry::before { display: none; } }
        """
    elif layout == 7:
        css = """
        .hero { display: flex; flex-direction: column; justify-content: center; align-items: center; text-align: center; min-height: 85vh; max-width: 800px; margin: 0 auto; padding: 40px 20px; position: relative;}
        .hero-title { font-size: 4rem; line-height: 1.1; margin-bottom: 20px; }
        .hero-img-panel { display: none; } 
        /* We'll override the hero for layout 7 specific HTML */
        .layout7-hero { display: flex; height: 90vh; }
        .layout7-hero-content { flex: 1; display: flex; flex-direction: column; justify-content: center; padding: 10%; }
        .layout7-hero-img { flex: 1; background: var(--bg-alt); display: flex; align-items: center; justify-content: center; }
        .container { max-width: 1120px; margin: 0 auto; padding: 80px 20px; }
        .services-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 30px; }
        @media(max-width: 900px) { .layout7-hero { flex-direction: column; } .layout7-hero-img { display: none; } }
        """
    elif layout == 8:
        css = """
        .split-hero { display: flex; height: 100vh; }
        .split-left { flex: 1; background: var(--accent); color: white; display: flex; flex-direction: column; justify-content: center; padding: 10%; }
        .split-left h1, .split-left h2, .split-left p { color: white; }
        .split-right { flex: 1; background: #e0e0e0; display: flex; align-items: center; justify-content: center; }
        .container { max-width: 1120px; margin: 0 auto; padding: 80px 20px; }
        .services-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 30px; }
        @media(max-width: 900px) { .split-hero { flex-direction: column; } .split-right { display: none; } }
        """
    return css

def generate_html(t):
    accent_rgb = hex_to_rgb(t['accent'])
    layout = t['layout']
    
    # Common CSS
    css = f"""
    :root {{
      --accent: {t['accent']};
      --accent-hover: {t['accent']}dd;
      --accent-light: rgba({accent_rgb}, 0.08);
      --text-primary: #1a1a2e;
      --text-secondary: #5a5a6b;
      --text-light: #8a8a9b;
      --bg: #ffffff;
      --bg-alt: #f9f9fc;
      --border: #e4e4ee;
      --shadow-sm: 0 1px 3px rgba(0,0,0,0.06);
      --shadow-md: 0 4px 12px rgba(0,0,0,0.08);
      --radius: 8px;
      --radius-lg: 12px;
      --transition: 0.3s ease;
    }}
    * {{ margin: 0; padding: 0; box-sizing: border-box; }}
    body {{ font-family: 'Inter', sans-serif; color: var(--text-primary); background: var(--bg); line-height: 1.6; }}
    h1, h2, h3, h4, h5, h6 {{ font-family: 'Playfair Display', serif; color: var(--text-primary); }}
    a {{ text-decoration: none; color: inherit; transition: var(--transition); }}
    .btn {{ display: inline-block; padding: 12px 24px; border-radius: var(--radius); font-weight: 500; cursor: pointer; transition: var(--transition); text-align: center; border: none; font-family: 'Inter', sans-serif; }}
    .btn-primary {{ background: var(--accent); color: white; }}
    .btn-primary:hover {{ background: var(--accent-hover); }}
    .btn-outline {{ border: 1px solid var(--border); background: transparent; color: var(--text-primary); }}
    .btn-outline:hover {{ border-color: var(--accent); color: var(--accent); }}
    .fade-in {{ opacity: 0; transform: translateY(20px); transition: opacity 0.6s ease, transform 0.6s ease; }}
    .fade-in.visible {{ opacity: 1; transform: translateY(0); }}
    
    /* Navbar */
    .navbar {{ position: sticky; top: 0; background: rgba(255,255,255,0.95); backdrop-filter: blur(10px); border-bottom: 1px solid var(--border); z-index: 1000; }}
    .nav-container {{ max-width: 1200px; margin: 0 auto; padding: 15px 20px; display: flex; justify-content: space-between; align-items: center; }}
    .nav-logo {{ font-family: 'Playfair Display', serif; font-size: 1.5rem; font-weight: 700; color: var(--accent); }}
    .nav-links {{ display: flex; gap: 30px; align-items: center; }}
    .nav-links a {{ font-size: 0.95rem; font-weight: 500; }}
    .nav-links a:hover {{ color: var(--accent); }}
    .hamburger {{ display: none; cursor: pointer; background: none; border: none; font-size: 1.5rem; color: var(--text-primary); }}
    .mobile-menu {{ display: none; position: absolute; top: 100%; left: 0; right: 0; background: var(--bg); border-bottom: 1px solid var(--border); padding: 20px; flex-direction: column; gap: 15px; box-shadow: var(--shadow-md); }}
    .mobile-menu.open {{ display: flex; }}
    @media (max-width: 768px) {{ .nav-links {{ display: none; }} .hamburger {{ display: block; }} }}
    
    /* Global Styles for sections */
    section {{ padding: 80px 20px; }}
    .section-title {{ font-size: 2.5rem; margin-bottom: 20px; text-align: center; }}
    .section-subtitle {{ text-align: center; color: var(--text-secondary); max-width: 600px; margin: 0 auto 50px; font-size: 1.1rem; }}
    
    .card {{ background: var(--bg); border: 1px solid var(--border); border-radius: var(--radius); padding: 30px; transition: var(--transition); }}
    .card:hover {{ box-shadow: var(--shadow-md); transform: translateY(-5px); }}
    .card-icon {{ width: 50px; height: 50px; background: var(--accent-light); color: var(--accent); border-radius: 50%; display: flex; align-items: center; justify-content: center; margin-bottom: 20px; }}
    .card-title {{ font-size: 1.2rem; margin-bottom: 10px; font-weight: 600; font-family: 'Inter', sans-serif; }}
    .card-text {{ color: var(--text-secondary); font-size: 0.95rem; }}
    
    /* Contact Form */
    .contact-form {{ display: grid; gap: 20px; }}
    .form-row {{ display: grid; grid-template-columns: 1fr 1fr; gap: 20px; }}
    .form-group {{ display: flex; flex-direction: column; gap: 8px; }}
    .form-label {{ font-weight: 500; font-size: 0.9rem; }}
    .form-control {{ padding: 12px 15px; border: 1px solid var(--border); border-radius: var(--radius); font-family: 'Inter', sans-serif; transition: var(--transition); }}
    .form-control:focus {{ outline: none; border-color: var(--accent); box-shadow: 0 0 0 3px var(--accent-light); }}
    textarea.form-control {{ min-height: 120px; resize: vertical; }}
    @media (max-width: 600px) {{ .form-row {{ grid-template-columns: 1fr; }} }}
    
    /* Footer */
    .footer {{ background: var(--text-primary); color: white; padding: 60px 20px 20px; text-align: center; }}
    .footer-links {{ display: flex; justify-content: center; gap: 20px; margin: 30px 0; flex-wrap: wrap; }}
    .footer-links a {{ color: #ccc; }}
    .footer-links a:hover {{ color: white; }}
    .footer-copy {{ color: #888; font-size: 0.9rem; margin-top: 30px; border-top: 1px solid #333; padding-top: 20px; }}
    
    {generate_layout_styles(layout)}
    """

    hero_html = ''
    if layout == 7:
        hero_html = f"""
        <div class="layout7-hero">
            <div class="layout7-hero-content fade-in">
                <span style="color:var(--accent);font-weight:600;text-transform:uppercase;letter-spacing:1px;margin-bottom:15px;display:block;">{t['specialty']}</span>
                <h1 style="font-size:4rem;line-height:1.1;margin-bottom:20px;font-family:'Playfair Display', serif;">{t['doctor']}</h1>
                <p style="font-size:1.2rem;color:var(--text-secondary);margin-bottom:30px;max-width:500px;">Providing compassionate, comprehensive care in {t['city']}. Dedicated to your long-term health and well-being.</p>
                <div style="display:flex;gap:15px;">
                    <a href="#contact" class="btn btn-primary">Book Appointment</a>
                    <a href="#services" class="btn btn-outline">Our Services</a>
                </div>
            </div>
            <div class="layout7-hero-img">
                {hero_svg}
            </div>
        </div>
        """
    elif layout == 8:
        hero_html = f"""
        <div class="split-hero">
            <div class="split-left fade-in">
                <span style="font-weight:600;text-transform:uppercase;letter-spacing:1px;margin-bottom:15px;display:block;opacity:0.8;">{t['specialty']}</span>
                <h1 style="font-size:3.5rem;line-height:1.2;margin-bottom:20px;font-family:'Playfair Display', serif;">{t['doctor']}</h1>
                <p style="font-size:1.1rem;margin-bottom:30px;opacity:0.9;max-width:400px;">Dedicated {t['specialty']} in {t['city']}, delivering personalized, evidence-based care.</p>
                <div style="display:flex;gap:15px;">
                    <a href="#contact" class="btn" style="background:white;color:var(--accent);">Book Appointment</a>
                </div>
            </div>
            <div class="split-right">
                <div style="width:70%;max-width:400px;">{hero_svg}</div>
            </div>
        </div>
        """
    elif layout == 5:
        hero_html = f"""
        <section class="hero fade-in">
            <div class="hero-bg-text">{t['specialty'].split()[0]}</div>
            <div style="max-width:600px;">
                <h1 style="font-size:3.5rem;margin-bottom:20px;">{t['doctor']}</h1>
                <p style="font-size:1.2rem;color:var(--text-secondary);margin-bottom:30px;">Specialized {t['specialty']} services located in the heart of {t['city']}. Emphasizing holistic and evidence-based patient care.</p>
                <div style="display:flex;gap:15px;margin-bottom:40px;">
                    <a href="#contact" class="btn btn-primary">Book Appointment</a>
                </div>
                <div style="display:flex;gap:30px;margin-top:20px;border-top:1px solid var(--border);padding-top:20px;">
                    <div><div style="font-size:1.5rem;font-weight:700;color:var(--accent);">{t['stats'][0]}</div><div style="font-size:0.9rem;color:var(--text-secondary);">Experience</div></div>
                    <div><div style="font-size:1.5rem;font-weight:700;color:var(--accent);">{t['stats'][1]}</div><div style="font-size:0.9rem;color:var(--text-secondary);">Patients</div></div>
                    <div><div style="font-size:1.5rem;font-weight:700;color:var(--accent);">{t['stats'][2]}</div><div style="font-size:0.9rem;color:var(--text-secondary);">Satisfaction</div></div>
                </div>
            </div>
        </section>
        """
    elif layout != 2:
        hero_html = f"""
        <section class="hero fade-in container">
            <div class="hero-content">
                <span style="color:var(--accent);font-weight:600;text-transform:uppercase;letter-spacing:1px;margin-bottom:15px;display:block;">{t['specialty']}</span>
                <h1 style="font-size:3rem;line-height:1.2;margin-bottom:20px;">{t['doctor']}</h1>
                <p style="font-size:1.1rem;color:var(--text-secondary);margin-bottom:30px;">Experienced {t['specialty']} serving the {t['city']} community. Focused on preventative care, accurate diagnosis, and personalized treatment plans.</p>
                <div style="display:flex;gap:15px;margin-bottom:40px;flex-wrap:wrap;">
                    <a href="#contact" class="btn btn-primary">Book Appointment</a>
                    <a href="#services" class="btn btn-outline">Our Services</a>
                </div>
                <div style="display:flex;gap:30px;">
                    <div><div style="font-size:1.5rem;font-weight:700;color:var(--accent);">{t['stats'][0]}</div><div style="font-size:0.9rem;color:var(--text-secondary);">Experience</div></div>
                    <div><div style="font-size:1.5rem;font-weight:700;color:var(--accent);">{t['stats'][1]}</div><div style="font-size:0.9rem;color:var(--text-secondary);">Patients</div></div>
                    <div><div style="font-size:1.5rem;font-weight:700;color:var(--accent);">{t['stats'][2]}</div><div style="font-size:0.9rem;color:var(--text-secondary);">Satisfaction</div></div>
                </div>
            </div>
            <div class="hero-img">
                {hero_svg}
            </div>
        </section>
        """

    about_html = ''
    if layout == 3:
        about_html = f"""
        <section id="about" class="container fade-in">
            <h2 class="section-title">About & Credentials</h2>
            <div class="about-grid">
                <div>{hero_svg}</div>
                <div>
                    <h3 style="margin-bottom:15px;font-size:1.5rem;">{t['doctor']}</h3>
                    <p style="color:var(--text-secondary);margin-bottom:15px;">I am a dedicated {t['specialty']} with over {t['stats'][0].split('+')[0]} years of clinical experience. My practice focuses on delivering evidence-based, patient-centered care. I believe in a collaborative approach, working closely with my patients to achieve optimal health outcomes and improve their overall quality of life.</p>
                </div>
                <div style="display:flex;flex-direction:column;gap:15px;">
                    {''.join([f'<div style="background:var(--bg-alt);padding:15px;border-radius:var(--radius);border:1px solid var(--border);"><div style="font-weight:600;font-size:0.95rem;">{ed}</div></div>' for ed in t['education']])}
                </div>
            </div>
        </section>
        """
    elif layout == 5:
        about_html = f"""
        <section id="about" class="fade-in" style="background:var(--bg-alt);">
            <div class="container">
                <h2 class="section-title" style="text-align:left;">About the Doctor</h2>
                <div class="about-grid" style="padding:0;">
                    <div>
                        <p style="font-size:1.1rem;color:var(--text-secondary);margin-bottom:20px;line-height:1.8;">{t['doctor']} is a distinguished {t['specialty']} practicing in {t['city']}. With {t['stats'][0]} of experience, the focus remains on delivering precise, empathetic care tailored to individual patient needs.</p>
                        <p style="font-size:1.1rem;color:var(--text-secondary);line-height:1.8;">A strong advocate for medical education and continuous learning, ensuring all treatments are rooted in the latest scientific advancements.</p>
                    </div>
                    <div>
                        <h4 style="margin-bottom:20px;font-size:1.2rem;border-bottom:1px solid var(--border);padding-bottom:10px;">Credentials</h4>
                        <ul style="list-style:none;padding:0;display:flex;flex-direction:column;gap:15px;">
                            {''.join([f'<li style="display:flex;align-items:start;gap:10px;"><span style="color:var(--accent);">✓</span> <span>{ed}</span></li>' for ed in t['education']])}
                        </ul>
                    </div>
                </div>
            </div>
        </section>
        """
    else:
        about_html = f"""
        <section id="about" class="container fade-in">
            <h2 class="section-title">About the Doctor</h2>
            <div class="section-subtitle">Dedicated to excellence in healthcare and patient well-being.</div>
            <div style="max-width:800px;margin:0 auto;text-align:center;margin-bottom:50px;">
                <p style="color:var(--text-secondary);font-size:1.1rem;">{t['doctor']} is a highly trained {t['specialty']} with extensive experience in diagnosing and treating complex medical conditions. Committed to compassionate care, the practice in {t['city']} emphasizes thorough communication and personalized treatment strategies.</p>
            </div>
            <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:20px;">
                {''.join([f'<div class="card" style="text-align:center;padding:20px;"><div style="color:var(--accent);font-size:24px;margin-bottom:10px;">🎓</div><div style="font-weight:500;font-size:0.95rem;">{ed}</div></div>' for ed in t['education']])}
            </div>
        </section>
        """

    services_html = ''
    if layout == 5:
        services_html = f"""
        <section id="services" class="container fade-in">
            <h2 class="section-title" style="text-align:left;">Clinical Services</h2>
            <ul class="services-list">
                {''.join([f'<li><div class="section-num">0{i+1}</div><div><h3 style="font-size:1.2rem;margin-bottom:5px;">{s}</h3><p style="color:var(--text-secondary);font-size:0.95rem;">Comprehensive evaluation and management.</p></div></li>' for i, s in enumerate(t['services'])])}
            </ul>
        </section>
        """
    elif layout == 6:
        services_html = f"""
        <section id="services" class="container fade-in">
            <h2 class="section-title">Areas of Expertise</h2>
            <div class="services-simple">
                {''.join([f'<div class="service-tag">{s}</div>' for s in t['services']])}
            </div>
        </section>
        """
    else:
        services_html = f"""
        <section id="services" class="fade-in" style="background:var(--bg-alt);">
            <div class="container">
                <h2 class="section-title">Clinical Services</h2>
                <div class="section-subtitle">Comprehensive {t['specialty']} care tailored to your specific needs.</div>
                <div class="services-grid">
                    {''.join([f'<div class="service-card card"><div class="card-icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 12h-4l-3 9L9 3l-3 9H2"></path></svg></div><h3 class="card-title">{s}</h3><p class="card-text">Evidence-based diagnosis, management, and ongoing support for optimal outcomes.</p></div>' for s in t['services']])}
                </div>
            </div>
        </section>
        """

    timeline_html = ''
    if layout == 6:
        timeline_html = f"""
        <section id="experience" class="fade-in" style="background:var(--bg-alt);">
            <div class="container">
                <h2 class="section-title">Career Milestones</h2>
                <div class="timeline-section">
                    <div class="timeline-entry fade-in">
                        <div class="timeline-year">Present</div>
                        <h3 style="margin-bottom:10px;">Private Practice, {t['city']}</h3>
                        <p style="color:var(--text-secondary);">Leading an independent clinic focused on delivering personalized {t['specialty']} services with top-tier patient satisfaction.</p>
                    </div>
                    <div class="timeline-entry fade-in">
                        <div class="timeline-year">2018 - 2022</div>
                        <h3 style="margin-bottom:10px;">Attending Physician</h3>
                        <p style="color:var(--text-secondary);">Served as a senior attending, supervising residents and managing complex cases in a high-volume hospital setting.</p>
                    </div>
                    <div class="timeline-entry fade-in">
                        <div class="timeline-year">2014 - 2018</div>
                        <h3 style="margin-bottom:10px;">Clinical Fellowship</h3>
                        <p style="color:var(--text-secondary);">Completed advanced subspecialty training, focusing on progressive therapies and clinical research.</p>
                    </div>
                    <div class="timeline-entry fade-in">
                        <div class="timeline-year">2011 - 2014</div>
                        <h3 style="margin-bottom:10px;">Residency Program</h3>
                        <p style="color:var(--text-secondary);">Comprehensive medical training with rotations across multiple clinical departments.</p>
                    </div>
                </div>
            </div>
        </section>
        """
    else:
        timeline_html = f"""
        <section id="experience" class="container fade-in">
            <h2 class="section-title">Experience</h2>
            <div style="max-width:800px;margin:0 auto;padding-left:20px;border-left:2px solid var(--border);">
                <div style="position:relative;margin-bottom:30px;padding-left:20px;">
                    <div style="position:absolute;left:-25px;top:5px;width:12px;height:12px;border-radius:50%;background:var(--accent);"></div>
                    <div style="font-weight:bold;color:var(--accent);font-size:0.9rem;margin-bottom:5px;">Present</div>
                    <h3 style="font-size:1.1rem;margin-bottom:5px;">Private Practice</h3>
                    <p style="color:var(--text-secondary);font-size:0.95rem;">Providing expert {t['specialty']} care in {t['city']}.</p>
                </div>
                <div style="position:relative;margin-bottom:30px;padding-left:20px;">
                    <div style="position:absolute;left:-25px;top:5px;width:12px;height:12px;border-radius:50%;background:var(--border);"></div>
                    <div style="font-weight:bold;color:var(--text-light);font-size:0.9rem;margin-bottom:5px;">Previous Role</div>
                    <h3 style="font-size:1.1rem;margin-bottom:5px;">Attending Physician</h3>
                    <p style="color:var(--text-secondary);font-size:0.95rem;">Managed complex clinical cases and supervised medical residents.</p>
                </div>
                <div style="position:relative;margin-bottom:30px;padding-left:20px;">
                    <div style="position:absolute;left:-25px;top:5px;width:12px;height:12px;border-radius:50%;background:var(--border);"></div>
                    <div style="font-weight:bold;color:var(--text-light);font-size:0.9rem;margin-bottom:5px;">Training</div>
                    <h3 style="font-size:1.1rem;margin-bottom:5px;">Fellowship & Residency</h3>
                    <p style="color:var(--text-secondary);font-size:0.95rem;">Completed rigorous medical training at premier institutions.</p>
                </div>
            </div>
        </section>
        """

    testimonials_html = f"""
    <section id="reviews" class="fade-in" style="background:{'var(--bg)' if layout==4 else 'var(--bg-alt)'};">
        <div class="container">
            <h2 class="section-title">Patient Testimonials</h2>
            <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:30px;">
                <div class="card">
                    <div style="color:#F59E0B;font-size:1.2rem;margin-bottom:15px;">★★★★★</div>
                    <p style="color:var(--text-secondary);font-style:italic;margin-bottom:20px;">"Exceptional care. The doctor listened to all my concerns and explained the treatment plan clearly. Highly recommend."</p>
                    <div style="font-weight:600;font-size:0.9rem;">— M. R.</div>
                </div>
                <div class="card">
                    <div style="color:#F59E0B;font-size:1.2rem;margin-bottom:15px;">★★★★★</div>
                    <p style="color:var(--text-secondary);font-style:italic;margin-bottom:20px;">"Very professional and knowledgeable. The office staff is friendly and I rarely have to wait long for my appointment."</p>
                    <div style="font-weight:600;font-size:0.9rem;">— J. S.</div>
                </div>
                <div class="card">
                    <div style="color:#F59E0B;font-size:1.2rem;margin-bottom:15px;">★★★★★</div>
                    <p style="color:var(--text-secondary);font-style:italic;margin-bottom:20px;">"I feel genuinely cared for here. It's rare to find a physician who takes this much time to ensure you understand everything."</p>
                    <div style="font-weight:600;font-size:0.9rem;">— A. T.</div>
                </div>
            </div>
        </div>
    </section>
    """

    contact_html = f"""
    <section id="contact" class="contact-section container fade-in">
        <h2 class="section-title">Contact & Booking</h2>
        <div class="section-subtitle">Reach out to schedule an appointment or ask any questions.</div>
        <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:50px;">
            <div>
                <h3 style="margin-bottom:20px;font-size:1.5rem;">Get in Touch</h3>
                <div style="display:flex;flex-direction:column;gap:20px;">
                    <div style="display:flex;gap:15px;align-items:start;">
                        <div style="color:var(--accent);margin-top:2px;"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path></svg></div>
                        <div><div style="font-weight:600;margin-bottom:5px;">Phone</div><div style="color:var(--text-secondary);">{t['phone']}</div></div>
                    </div>
                    <div style="display:flex;gap:15px;align-items:start;">
                        <div style="color:var(--accent);margin-top:2px;"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path><polyline points="22,6 12,13 2,6"></polyline></svg></div>
                        <div><div style="font-weight:600;margin-bottom:5px;">Email</div><div style="color:var(--text-secondary);">contact@dr{t['doctor'].split(',')[0].split()[-1].lower()}.com</div></div>
                    </div>
                    <div style="display:flex;gap:15px;align-items:start;">
                        <div style="color:var(--accent);margin-top:2px;"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path><circle cx="12" cy="10" r="3"></circle></svg></div>
                        <div><div style="font-weight:600;margin-bottom:5px;">Location</div><div style="color:var(--text-secondary);">Medical Arts Building<br>{t['city']}</div></div>
                    </div>
                    <div style="display:flex;gap:15px;align-items:start;">
                        <div style="color:var(--accent);margin-top:2px;"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg></div>
                        <div><div style="font-weight:600;margin-bottom:5px;">Hours</div><div style="color:var(--text-secondary);">Mon-Fri: 9:00 AM - 5:00 PM<br>Sat-Sun: Closed</div></div>
                    </div>
                </div>
            </div>
            <div style="background:var(--bg);padding:30px;border-radius:var(--radius);border:1px solid var(--border);box-shadow:var(--shadow-sm);">
                <form class="contact-form" onsubmit="return handleSubmit(event)">
                    <div class="form-row">
                        <div class="form-group"><label class="form-label">First Name</label><input type="text" class="form-control" required></div>
                        <div class="form-group"><label class="form-label">Last Name</label><input type="text" class="form-control" required></div>
                    </div>
                    <div class="form-group"><label class="form-label">Email Address</label><input type="email" class="form-control" required></div>
                    <div class="form-group"><label class="form-label">Phone Number</label><input type="tel" class="form-control" required></div>
                    <div class="form-group">
                        <label class="form-label">Reason for Visit</label>
                        <select class="form-control" required>
                            <option value="">Select a reason...</option>
                            <option value="new">New Patient Consultation</option>
                            <option value="followup">Follow-up Appointment</option>
                            <option value="telehealth">Telehealth Visit</option>
                            <option value="other">Other</option>
                        </select>
                    </div>
                    <div class="form-group"><label class="form-label">Additional Notes</label><textarea class="form-control" placeholder="Briefly describe your medical concern..."></textarea></div>
                    <button type="submit" class="btn btn-primary" style="width:100%;margin-top:10px;">Request Appointment</button>
                </form>
            </div>
        </div>
    </section>
    """

    footer_html = f"""
    <footer class="footer">
        <div style="font-family:'Playfair Display', serif;font-size:1.8rem;margin-bottom:10px;">{t['doctor']}</div>
        <div style="color:#aaa;margin-bottom:20px;">{t['specialty']} in {t['city']}</div>
        <div class="footer-links">
            <a href="#about">About</a>
            <a href="#services">Services</a>
            <a href="#experience">Experience</a>
            <a href="#reviews">Reviews</a>
            <a href="#contact">Contact</a>
        </div>
        <div class="footer-copy">
            &copy; 2025 {t['doctor']}. All Rights Reserved. Designed for professional medical practice.
        </div>
    </footer>
    """

    main_content = ''
    if layout == 2:
        main_content = f"""
        <div class="layout-wrapper">
            <aside class="sidebar fade-in">
                {hero_svg}
                <div style="margin-top:20px;text-align:center;">
                    <h2 style="font-size:1.5rem;margin-bottom:5px;">{t['doctor']}</h2>
                    <div style="color:var(--text-secondary);margin-bottom:20px;font-size:0.95rem;">{t['specialty']}</div>
                    <a href="#contact" class="btn btn-primary" style="width:100%;margin-bottom:20px;">Book Now</a>
                    <div style="display:flex;flex-direction:column;gap:10px;text-align:left;font-size:0.9rem;">
                        <div><strong>Experience:</strong> {t['stats'][0]}</div>
                        <div><strong>Patients:</strong> {t['stats'][1]}</div>
                        <div><strong>Phone:</strong> {t['phone']}</div>
                    </div>
                </div>
            </aside>
            <main class="main-content">
                {about_html}
                {services_html}
                {timeline_html}
                {testimonials_html}
            </main>
            {contact_html}
        </div>
        """
    else:
        main_content = f"""
        {hero_html}
        {about_html}
        {services_html}
        {timeline_html}
        {testimonials_html}
        {contact_html}
        """

    full_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{t['doctor']} | {t['specialty']}</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Playfair+Display:ital,wght@0,400;0,600;0,700;1,400&display=swap" rel="stylesheet">
    <style>
        {css}
    </style>
</head>
<body>

    <nav class="navbar">
        <div class="nav-container">
            <div class="nav-logo">{t['doctor'].split(',')[0]}</div>
            <button class="hamburger" onclick="toggleMenu()">☰</button>
            <div class="nav-links">
                <a href="#about">About</a>
                <a href="#services">Services</a>
                <a href="#experience">Experience</a>
                <a href="#reviews">Reviews</a>
                <a href="#contact">Contact</a>
                <a href="#contact" class="btn btn-primary" style="padding:8px 16px;">Book Appointment</a>
            </div>
        </div>
        <div class="mobile-menu" id="mobileMenu">
            <a href="#about">About</a>
            <a href="#services">Services</a>
            <a href="#experience">Experience</a>
            <a href="#reviews">Reviews</a>
            <a href="#contact">Contact</a>
        </div>
    </nav>

    {main_content}

    {footer_html}

    <script>
        {js}
    </script>
</body>
</html>
"""
    return full_html

out_dir = r"d:\website\doctors portfolio\templates"
os.makedirs(out_dir, exist_ok=True)

for t in templates:
    html = generate_html(t)
    with open(os.path.join(out_dir, t['filename']), 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Generated {{t['filename']}}")

