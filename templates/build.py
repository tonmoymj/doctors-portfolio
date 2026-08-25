import os

data = [
    {
        "filename": "template-071.html",
        "specialty": "Gynecologist",
        "layout": 7,
        "accent": "#9B6B7B",
        "doctor": "Dr. Miranda Walsh, MD, FACOG",
        "city": "Chicago, IL",
        "services": ["General Gynecology", "Laparoscopic Surgery", "Fibroids Treatment", "Ovarian Cysts", "Annual Well-Woman Exams", "Colposcopy & LEEP"],
        "edu": ["Loyola University Stritch School (MD)", "Loyola University Medical Center (Residency – OB/GYN)", "American Board of Obstetrics & Gynecology (Board Certified)"],
        "stats": ["13+", "5,800+", "98%"],
        "phone": "+1 (312) 555-7142",
        "bio": "Dr. Miranda Walsh is a board-certified gynecologist dedicated to providing comprehensive and compassionate care for women at all stages of life. With over a decade of experience, she specializes in minimally invasive procedures and preventive health."
    },
    {
        "filename": "template-072.html",
        "specialty": "Gynecologist",
        "layout": 8,
        "accent": "#6B3B6B",
        "doctor": "Dr. Rania Khoury, MD, FACOG",
        "city": "Dallas, TX",
        "services": ["Maternal-Fetal Medicine", "Fetal Anomaly Scanning", "Genetic Counseling", "Preeclampsia Management", "Multiple Gestation", "Fetal Intervention"],
        "edu": ["UT Southwestern (MD)", "Parkland Memorial Hospital (Residency)", "Texas Children's Fetal Center (Fellowship – Maternal-Fetal Medicine)"],
        "stats": ["15+", "3,200+", "97%"],
        "phone": "+1 (214) 555-7254",
        "bio": "Dr. Rania Khoury specializes in high-risk pregnancies and maternal-fetal medicine, offering expert care and advanced diagnostics to ensure the best outcomes for both mother and child."
    },
    {
        "filename": "template-073.html",
        "specialty": "ENT Specialist",
        "layout": 1,
        "accent": "#7B1D1D",
        "doctor": "Dr. Andrew Pearce, MD, FACS",
        "city": "New York, NY",
        "services": ["Otolaryngology", "Sinus Surgery (FESS)", "Nasal Septoplasty", "Tonsillectomy & Adenoidectomy", "Hearing Loss Evaluation", "Thyroid & Parathyroid Surgery"],
        "edu": ["NYU Grossman School of Medicine (MD)", "NYU Langone (Residency – Otolaryngology)", "New York Eye & Ear Infirmary (Fellowship – Rhinology)"],
        "stats": ["18+", "4,100+", "97%"],
        "phone": "+1 (212) 555-7365",
        "bio": "Dr. Andrew Pearce is a premier ENT specialist in New York, focusing on advanced rhinology and comprehensive otolaryngology services to restore function and improve quality of life."
    },
    {
        "filename": "template-074.html",
        "specialty": "ENT Specialist",
        "layout": 2,
        "accent": "#8B5A2B",
        "doctor": "Dr. Diana Cho, MD, FACS",
        "city": "Los Angeles, CA",
        "services": ["Pediatric ENT", "Ear Tubes", "Childhood Tonsils", "Pediatric Hearing Loss", "Cochlear Implant Evaluation", "Voice Disorders in Children"],
        "edu": ["Keck School of Medicine USC (MD)", "Children's Hospital Los Angeles (Residency – Pediatric ENT)", "Johns Hopkins (Fellowship – Pediatric Otolaryngology)"],
        "stats": ["16+", "6,400+", "99%"],
        "phone": "+1 (310) 555-7471",
        "bio": "Dr. Diana Cho is a compassionate pediatric ENT surgeon dedicated to treating complex ear, nose, and throat conditions in children of all ages, ensuring comfortable and effective care."
    },
    {
        "filename": "template-075.html",
        "specialty": "ENT Specialist",
        "layout": 3,
        "accent": "#7B1D1D",
        "doctor": "Dr. Gerhard Mueller, MD, FACS",
        "city": "Chicago, IL",
        "services": ["Head & Neck Surgery", "Thyroid Cancer", "Salivary Gland Tumors", "Parotidectomy", "Neck Dissection", "Reconstructive Head & Neck Surgery"],
        "edu": ["Rush Medical College (MD)", "Rush University Medical Center (Residency – Head & Neck Surgery)", "MD Anderson Cancer Center (Fellowship)"],
        "stats": ["22+", "3,700+", "97%"],
        "phone": "+1 (312) 555-7582",
        "bio": "Dr. Gerhard Mueller is an esteemed head and neck surgeon specializing in the surgical management of benign and malignant tumors of the head and neck region, utilizing the latest reconstructive techniques."
    },
    {
        "filename": "template-076.html",
        "specialty": "ENT Specialist",
        "layout": 4,
        "accent": "#8B5A2B",
        "doctor": "Dr. Sarah Okonkwo, MD, FACS",
        "city": "Atlanta, GA",
        "services": ["Neurotology", "Cochlear Implants", "Acoustic Neuroma", "Dizziness & Balance Disorders", "Meniere's Disease", "Skull Base Surgery"],
        "edu": ["Morehouse School of Medicine (MD)", "Emory University Hospital (Residency – Otolaryngology)", "Emory Neurotology Group (Fellowship – Neurotology)"],
        "stats": ["14+", "2,900+", "98%"],
        "phone": "+1 (404) 555-7693",
        "bio": "Dr. Sarah Okonkwo is a neurotologist expert in the diagnosis and surgical treatment of complex ear diseases and lateral skull base disorders, dedicated to restoring hearing and balance."
    },
    {
        "filename": "template-077.html",
        "specialty": "ENT Specialist",
        "layout": 5,
        "accent": "#6B0D0D",
        "doctor": "Dr. Thomas Whitfield, MD, FACS",
        "city": "Boston, MA",
        "services": ["Voice & Swallowing Disorders", "Laryngology", "Vocal Cord Surgery", "Dysphonia", "Laryngopharyngeal Reflux", "Swallowing Rehabilitation"],
        "edu": ["Harvard Medical School (MD)", "Mass Eye and Ear (Residency – Otolaryngology)", "Brigham & Women's (Fellowship – Laryngology)"],
        "stats": ["20+", "4,500+", "98%"],
        "phone": "+1 (617) 555-7704",
        "bio": "Dr. Thomas Whitfield is a renowned laryngologist offering cutting-edge care for patients with voice, airway, and swallowing disorders. He employs advanced therapeutic and surgical interventions."
    },
    {
        "filename": "template-078.html",
        "specialty": "ENT Specialist",
        "layout": 6,
        "accent": "#7B4A1B",
        "doctor": "Dr. Keiko Matsumoto, MD, FACS",
        "city": "Seattle, WA",
        "services": ["Rhinology & Sinus Disease", "Chronic Sinusitis", "Smell & Taste Disorders", "Epistaxis Management", "Nasal Polyps", "Skull Base Approaches"],
        "edu": ["University of Washington (MD)", "UW Medical Center (Residency – Otolaryngology)", "Oregon Health & Science (Fellowship – Advanced Rhinology)"],
        "stats": ["15+", "3,800+", "98%"],
        "phone": "+1 (206) 555-7815",
        "bio": "Dr. Keiko Matsumoto is a fellowship-trained rhinologist delivering advanced endoscopic interventions for complex sinus and nasal conditions, improving patient breathing and overall health."
    },
    {
        "filename": "template-079.html",
        "specialty": "ENT Specialist",
        "layout": 7,
        "accent": "#7B1D1D",
        "doctor": "Dr. Henri Beaumont, MD, FACS",
        "city": "Houston, TX",
        "services": ["Facial Plastic & Reconstructive Surgery", "Rhinoplasty", "Facelift", "Blepharoplasty", "Otoplasty", "Facial Trauma Reconstruction"],
        "edu": ["Baylor College of Medicine (MD)", "Ben Taub Hospital (Residency – Otolaryngology-Head & Neck)", "UCSF (Fellowship – Facial Plastic & Reconstructive Surgery)"],
        "stats": ["17+", "5,300+", "99%"],
        "phone": "+1 (713) 555-7926",
        "bio": "Dr. Henri Beaumont is a leading facial plastic and reconstructive surgeon, combining artistic vision with surgical precision to achieve natural and beautiful results."
    },
    {
        "filename": "template-080.html",
        "specialty": "ENT Specialist",
        "layout": 8,
        "accent": "#8B5A2B",
        "doctor": "Dr. Miriam Stenberg, MD, FACS",
        "city": "Minneapolis, MN",
        "services": ["Allergy & Immunology ENT", "Allergic Rhinitis", "Immunotherapy (Allergy Shots)", "Food Allergy Testing", "Sinusitis & Allergies", "Biological Therapies"],
        "edu": ["University of Minnesota (MD)", "Hennepin Healthcare (Residency – Otolaryngology)", "American Academy of Otolaryngic Allergy (Certification)"],
        "stats": ["12+", "3,600+", "98%"],
        "phone": "+1 (612) 555-8037",
        "bio": "Dr. Miriam Stenberg provides specialized care in otolaryngic allergy, helping patients find lasting relief from chronic allergic conditions through targeted therapies and management strategies."
    }
]

base_html = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{doctor} - {specialty}</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Playfair+Display:wght@400;600;700&display=swap" rel="stylesheet">
  <style>
    :root {{
      --accent: {accent};
      --accent-hover: color-mix(in srgb, var(--accent) 80%, black);
      --accent-light: color-mix(in srgb, var(--accent) 8%, white);
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
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{ font-family: 'Inter', sans-serif; color: var(--text-primary); line-height: 1.6; background: var(--bg); overflow-x: hidden; }}
    h1, h2, h3, h4, h5, h6 {{ font-family: 'Playfair Display', serif; margin-bottom: 1rem; color: inherit; }}
    a {{ text-decoration: none; color: inherit; transition: var(--transition); }}
    ul {{ list-style: none; }}
    .container {{ max-width: 1120px; margin: 0 auto; padding: 0 24px; }}
    section {{ padding: 80px 0; }}
    section:nth-child(even) {{ background: var(--bg-alt); }}
    .btn {{ display: inline-block; padding: 12px 24px; background: var(--accent); color: white; border-radius: var(--radius); font-weight: 500; border: none; cursor: pointer; transition: var(--transition); text-align: center; }}
    .btn:hover {{ background: var(--accent-hover); }}
    .btn-outline {{ background: transparent; border: 1px solid var(--accent); color: var(--accent); }}
    .btn-outline:hover {{ background: var(--accent-light); }}
    .fade-in {{ opacity: 0; transform: translateY(20px); transition: opacity 0.8s ease, transform 0.8s ease; }}
    .fade-in.visible {{ opacity: 1; transform: translateY(0); }}
    
    /* Navbar */
    header {{ position: sticky; top: 0; z-index: 100; background: rgba(255,255,255,0.95); backdrop-filter: blur(10px); border-bottom: 1px solid var(--border); }}
    .nav-container {{ display: flex; justify-content: space-between; align-items: center; height: 80px; }}
    .logo {{ font-family: 'Playfair Display', serif; font-size: 1.5rem; font-weight: 700; color: var(--accent); }}
    .nav-links {{ display: flex; gap: 32px; align-items: center; }}
    .nav-links a {{ font-weight: 500; font-size: 0.95rem; }}
    .nav-links a:hover {{ color: var(--accent); }}
    .hamburger {{ display: none; background: none; border: none; font-size: 1.5rem; cursor: pointer; color: var(--text-primary); }}
    
    /* Layout Specific CSS */
    {layout_css}

    /* Common Elements */
    .grid-cards {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 24px; }}
    .card {{ background: white; padding: 32px; border-radius: var(--radius); border: 1px solid var(--border); box-shadow: var(--shadow-sm); }}
    .card-icon {{ color: var(--accent); margin-bottom: 16px; width: 40px; height: 40px; }}
    .form-group {{ margin-bottom: 20px; }}
    .form-group label {{ display: block; margin-bottom: 8px; font-weight: 500; font-size: 0.9rem; }}
    .form-control {{ width: 100%; padding: 12px; border: 1px solid var(--border); border-radius: var(--radius); font-family: inherit; }}
    footer {{ background: var(--text-primary); color: white; padding: 40px 0; text-align: center; }}
    
    @media (max-width: 768px) {{
      .nav-links {{ display: none; position: absolute; top: 80px; left: 0; width: 100%; background: white; flex-direction: column; padding: 24px; border-bottom: 1px solid var(--border); }}
      .nav-links.open {{ display: flex; }}
      .hamburger {{ display: block; }}
      .hero-grid, .layout-grid, .split-screen, .mag-grid {{ grid-template-columns: 1fr !important; }}
      .split-screen {{ flex-direction: column; height: auto; }}
      .split-screen .hero-left, .split-screen .hero-right {{ width: 100%; height: auto; padding: 48px 24px; }}
      .hero-bg {{ width: 100% !important; }}
    }}
  </style>
</head>
<body>
  <header>
    <div class="container nav-container">
      <div class="logo">{doctor_short}</div>
      <button class="hamburger" onclick="toggleMenu()">☰</button>
      <nav class="nav-links" id="mobileMenu">
        <a href="#about">About</a>
        <a href="#services">Services</a>
        <a href="#experience">Experience</a>
        <a href="#reviews">Reviews</a>
        <a href="#contact">Contact</a>
        <a href="#contact" class="btn">Book Appointment</a>
      </nav>
    </div>
  </header>
  
  {layout_html}

  <section id="contact">
    <div class="container fade-in">
      <h2>Contact & Appointments</h2>
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 48px; margin-top: 40px;">
        <div>
          <h3>Get in Touch</h3>
          <p style="color: var(--text-secondary); margin-bottom: 24px;">Schedule a consultation or ask a question.</p>
          <ul style="display: flex; flex-direction: column; gap: 16px;">
            <li><strong>Phone:</strong> {phone}</li>
            <li><strong>Email:</strong> contact@{domain}</li>
            <li><strong>Address:</strong> 123 Medical Plaza, {city}</li>
            <li><strong>Hours:</strong> Mon-Fri 9AM - 5PM</li>
          </ul>
        </div>
        <form onsubmit="return handleSubmit(event)">
          <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px;">
            <div class="form-group">
              <label>First Name</label>
              <input type="text" class="form-control" required>
            </div>
            <div class="form-group">
              <label>Last Name</label>
              <input type="text" class="form-control" required>
            </div>
          </div>
          <div class="form-group">
            <label>Email</label>
            <input type="email" class="form-control" required>
          </div>
          <div class="form-group">
            <label>Phone</label>
            <input type="tel" class="form-control" required>
          </div>
          <div class="form-group">
            <label>Reason for Visit</label>
            <select class="form-control" required>
              <option value="">Select a reason...</option>
              <option>Consultation</option>
              <option>Follow-up</option>
              <option>Procedure</option>
            </select>
          </div>
          <div class="form-group">
            <label>Notes</label>
            <textarea class="form-control" rows="4"></textarea>
          </div>
          <button type="submit" class="btn" style="width: 100%;">Submit Request</button>
        </form>
      </div>
    </div>
  </section>

  <footer>
    <div class="container">
      <h3>{doctor}</h3>
      <p style="margin: 16px 0; color: var(--text-light);">{specialty} &bull; {city}</p>
      <div style="margin-bottom: 24px; display: flex; justify-content: center; gap: 24px;">
         <a href="#about" style="color:var(--text-light)">About</a>
         <a href="#services" style="color:var(--text-light)">Services</a>
         <a href="#experience" style="color:var(--text-light)">Experience</a>
         <a href="#reviews" style="color:var(--text-light)">Reviews</a>
         <a href="#contact" style="color:var(--text-light)">Contact</a>
      </div>
      <p style="color: var(--text-secondary); font-size: 0.9rem;">&copy; 2026 {doctor_short}. All rights reserved.</p>
    </div>
  </footer>

  <script>
    function toggleMenu() {{ document.getElementById('mobileMenu').classList.toggle('open'); }}
    document.querySelectorAll('#mobileMenu a').forEach(l => l.addEventListener('click', () => document.getElementById('mobileMenu').classList.remove('open')));
    const observer = new IntersectionObserver((entries) => {{ entries.forEach(e => {{ if(e.isIntersecting){{e.target.classList.add('visible');observer.unobserve(e.target);}} }}); }}, {{threshold:0.1, rootMargin:'0px 0px -40px 0px'}});
    document.querySelectorAll('.fade-in').forEach(el => observer.observe(el));
    function handleSubmit(e) {{ e.preventDefault(); const btn=e.target.querySelector('[type="submit"]'); const orig=btn.textContent; btn.textContent='Request Sent ✓'; btn.style.background='#2D6A4F'; btn.disabled=true; setTimeout(()=>{{btn.textContent=orig;btn.style.background='';btn.disabled=false;e.target.reset();}},4000); return false; }}
  </script>
</body>
</html>"""

svg_placeholder = """
<div style="width:100%;height:100%;display:flex;align-items:center;justify-content:center;background:var(--bg-alt);border-radius:var(--radius-lg);position:relative;overflow:hidden;min-height:300px;">
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

def generate_sections(item):
    s_html = f'<section id="services"><div class="container fade-in"><h2>Areas of Expertise</h2><div class="grid-cards">'
    for s in item['services']:
        s_html += f'<div class="card"><svg class="card-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 12h-4l-3 9L9 3l-3 9H2"/></svg><h4>{s}</h4><p style="color:var(--text-secondary);font-size:0.9rem;margin-top:8px;">Comprehensive evaluation and treatment plan customized for optimal patient care.</p></div>'
    s_html += '</div></div></section>'

    e_html = f'<section id="experience"><div class="container fade-in"><h2>Experience & Milestones</h2><div style="margin-top:32px;border-left:2px solid var(--accent-light);padding-left:24px;">'
    years = [2022, 2018, 2012, 2008, 2004]
    milestones = ["Current Position & Medical Director", "Senior Attending Physician", "Fellowship & Advanced Training", "Residency Program Completion", "Medical School Graduation"]
    for y, m in zip(years, milestones):
        e_html += f'<div style="position:relative;margin-bottom:32px;"><div style="position:absolute;left:-31px;top:0;width:12px;height:12px;border-radius:50%;background:var(--accent);"></div><h4 style="color:var(--accent);">{y}</h4><h3 style="margin-bottom:8px;">{m}</h3><p style="color:var(--text-secondary);">Dedicated commitment to medical excellence, continuous learning, and outstanding patient care.</p></div>'
    e_html += '</div></div></section>'

    r_html = f'<section id="reviews"><div class="container fade-in"><h2>Patient Testimonials</h2><div class="grid-cards">'
    for i in range(3):
        r_html += f'<div class="card"><div style="color:#FFB800;margin-bottom:12px;font-size:1.2rem;">★★★★★</div><p style="font-style:italic;margin-bottom:16px;color:var(--text-secondary);">"The care I received was absolutely exceptional. Dr. takes time to listen and explains everything clearly. Highly recommended for anyone needing expert attention."</p><div style="font-weight:600;font-size:0.9rem;">- Patient {chr(65+i)}.{chr(75+i)}.</div></div>'
    r_html += '</div></div></section>'

    a_html = f'''<section id="about"><div class="container fade-in"><h2>About {item['doctor'].split(',')[0]}</h2>
    <div style="display:grid;grid-template-columns:repeat(auto-fit, minmax(300px, 1fr));gap:48px;margin-top:32px;">
    <div><p style="font-size:1.1rem;color:var(--text-secondary);line-height:1.8;">{item['bio']}</p>
    <div style="display:flex;gap:16px;margin-top:24px;"><div style="background:var(--bg-alt);padding:16px;border-radius:var(--radius);text-align:center;flex:1;"><h3 style="color:var(--accent)">{item['stats'][0]}</h3><div style="font-size:0.8rem;color:var(--text-secondary);text-transform:uppercase;">Years Exp.</div></div>
    <div style="background:var(--bg-alt);padding:16px;border-radius:var(--radius);text-align:center;flex:1;"><h3 style="color:var(--accent)">{item['stats'][1]}</h3><div style="font-size:0.8rem;color:var(--text-secondary);text-transform:uppercase;">Patients</div></div>
    <div style="background:var(--bg-alt);padding:16px;border-radius:var(--radius);text-align:center;flex:1;"><h3 style="color:var(--accent)">{item['stats'][2]}</h3><div style="font-size:0.8rem;color:var(--text-secondary);text-transform:uppercase;">Rating</div></div></div>
    </div><div><div class="card" style="padding:24px;"><h3 style="margin-bottom:16px;">Credentials</h3><ul style="display:flex;flex-direction:column;gap:16px;">'''
    for ed in item['edu']:
        a_html += f'<li style="display:flex;align-items:flex-start;gap:12px;"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="var(--accent)" stroke-width="2" style="flex-shrink:0;margin-top:2px;"><path d="M22 10v6M2 10l10-5 10 5-10 5z"/><path d="M6 12v5c3 3 9 3 12 0v-5"/></svg><span style="color:var(--text-secondary);font-size:0.95rem;">{ed}</span></li>'
    a_html += '</ul></div></div></div></div></section>'

    return a_html + s_html + e_html + r_html

import os
out_dir = r"d:\\website\\doctors portfolio\\templates"
os.makedirs(out_dir, exist_ok=True)

for item in data:
    l = item['layout']
    css = ""
    html = ""
    sections = generate_sections(item)
    doc_short = item['doctor'].split(',')[0]
    domain = item['specialty'].lower().replace(' ', '') + ".com"

    if l == 1:
        css = ".hero-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 48px; align-items: center; padding: 80px 0; }"
        html = f'<main><div class="container hero-grid fade-in"><div><span style="color:var(--accent);font-weight:700;letter-spacing:1px;text-transform:uppercase;font-size:0.9rem;">{item["specialty"]}</span><h1 style="font-size:3rem;margin:16px 0;">{item["doctor"]}</h1><p style="font-size:1.2rem;color:var(--text-secondary);margin-bottom:32px;">{item["bio"]}</p><div style="display:flex;gap:16px;"><a href="#contact" class="btn">Book Appointment</a><a href="#about" class="btn btn-outline">Learn More</a></div></div><div>{svg_placeholder}</div></div>{sections}</main>'
    
    elif l == 2:
        css = ".layout-grid { display: grid; grid-template-columns: 280px 1fr; gap: 48px; padding: 40px 0; } .sidebar { position: sticky; top: 100px; height: fit-content; }"
        html = f'<main class="container layout-grid fade-in"><aside class="sidebar">{svg_placeholder}<div style="margin-top:24px;background:var(--bg-alt);padding:24px;border-radius:var(--radius);"><h3 style="margin-bottom:16px;font-size:1.2rem;">Quick Stats</h3><p style="margin-bottom:8px;"><strong>{item["stats"][0]} Years Exp.</strong></p><p style="margin-bottom:8px;"><strong>{item["stats"][1]} Patients</strong></p><a href="#contact" class="btn" style="width:100%;margin-top:16px;">Book Now</a></div></aside><div class="content"><div style="margin-bottom:48px;padding-top:40px;"><span style="color:var(--accent);font-weight:700;letter-spacing:1px;text-transform:uppercase;font-size:0.9rem;">{item["specialty"]}</span><h1 style="font-size:3rem;margin:16px 0;">{item["doctor"]}</h1><p style="font-size:1.2rem;color:var(--text-secondary);">{item["bio"]}</p></div>{sections.replace("container ", "")}</div></main>'
        
    elif l == 3:
        css = ".hero-grid { display: grid; grid-template-columns: 7fr 5fr; gap: 48px; align-items: center; padding: 80px 0; } .grid-cards { grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); } .card { min-height: 200px; }"
        html = f'<main><div class="container hero-grid fade-in"><div><span style="color:var(--accent);font-weight:700;letter-spacing:1px;text-transform:uppercase;font-size:0.9rem;">{item["specialty"]}</span><h1 style="font-size:3.5rem;margin:16px 0;line-height:1.1;">{item["doctor"]}</h1><p style="font-size:1.1rem;color:var(--text-secondary);margin-bottom:32px;">{item["bio"]}</p><div style="display:flex;gap:16px;"><a href="#contact" class="btn">Book Appointment</a><a href="#services" class="btn btn-outline">Our Services</a></div></div><div>{svg_placeholder}</div></div>{sections}</main>'

    elif l == 4:
        css = "section { padding: 100px 0; background: white !important; } .hero { text-align: center; max-width: 800px; margin: 0 auto; padding: 120px 24px 60px; } .card { box-shadow: none; border: none; border-top: 2px solid var(--border); border-radius: 0; padding: 24px 0; }"
        html = f'<main><div class="hero fade-in"><span style="color:var(--accent);font-weight:700;letter-spacing:2px;text-transform:uppercase;font-size:0.85rem;">{item["specialty"]}</span><h1 style="font-size:3.5rem;margin:24px 0;">{item["doctor"]}</h1><p style="font-size:1.2rem;color:var(--text-secondary);margin-bottom:40px;">{item["bio"]}</p><div style="display:flex;gap:16px;justify-content:center;margin-bottom:64px;"><a href="#contact" class="btn" style="border-radius:30px;padding:14px 32px;">Book Appointment</a></div><div style="max-width:600px;margin:0 auto;">{svg_placeholder}</div></div>{sections}</main>'

    elif l == 5:
        css = ".hero { position: relative; padding: 120px 0 60px; overflow: hidden; } .bg-text { position: absolute; top: 0; left: -2%; font-size: 12vw; font-family:'Playfair Display', serif; font-weight: 700; color: var(--bg-alt); z-index: -1; white-space: nowrap; line-height: 1; } .mag-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 64px; align-items:center; } .pull-quote { font-size:1.5rem; font-family:'Playfair Display', serif; color:var(--accent); border-left:4px solid var(--accent); padding-left:24px; margin:32px 0; }"
        s_list = '<div style="margin-top:40px;">'
        for idx, s in enumerate(item['services']):
            s_list += f'<div style="padding:24px 0;border-top:1px solid var(--border);display:flex;align-items:center;"><span style="color:var(--accent);font-weight:700;margin-right:24px;font-size:1.5rem;font-family:\\'Playfair Display\\', serif;">0{idx+1}</span><h4 style="margin:0;font-size:1.2rem;">{s}</h4></div>'
        s_list += '<div style="border-top:1px solid var(--border);"></div></div>'
        custom_sections = sections.split('<section id="services">')[0] + f'<section id="services" style="background:white;"><div class="container fade-in"><h2>Clinical Expertise</h2>{s_list}</div></section>' + sections.split('</section>', 2)[2]
        html = f'<main><div class="hero fade-in"><div class="bg-text">{item["specialty"].upper()}</div><div class="container mag-grid"><div><h1 style="font-size:4rem;line-height:1.1;margin-bottom:24px;">{item["doctor"]}</h1><div class="pull-quote">Committed to excellence in patient care and advanced medical treatments.</div><p style="font-size:1.1rem;color:var(--text-secondary);">{item["bio"]}</p><a href="#contact" class="btn" style="margin-top:32px;">Book Appointment</a></div><div>{svg_placeholder}</div></div></div>{custom_sections}</main>'

    elif l == 6:
        css = ".timeline-item { display: grid; grid-template-columns: 150px 1fr; gap: 32px; margin-bottom: 48px; position:relative; } .timeline-item::before { content:''; position:absolute; left:170px; top:12px; width:12px; height:12px; border-radius:50%; background:var(--accent); } .timeline-item::after { content:''; position:absolute; left:175px; top:24px; bottom:-48px; width:2px; background:var(--border); } .timeline-item:last-child::after { display:none; } .timeline-year { font-size: 2rem; font-family: 'Playfair Display', serif; color: var(--text-primary); font-weight: 700; text-align: right; } .hero-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 48px; align-items: center; padding: 80px 0; }"
        t_list = '<div style="margin-top:64px;">'
        years = [2022, 2018, 2012, 2008, 2004]
        milestones = ["Current Position & Medical Director", "Senior Attending Physician", "Fellowship & Advanced Training", "Residency Program Completion", "Medical School Graduation"]
        for y, m in zip(years, milestones):
            t_list += f'<div class="timeline-item"><div class="timeline-year">{y}</div><div style="padding-left:32px;"><h3 style="margin-bottom:8px;font-size:1.5rem;">{m}</h3><p style="color:var(--text-secondary);font-size:1.1rem;margin-bottom:16px;">Demonstrated leadership and excellence in clinical practice, adopting the latest surgical techniques and patient care protocols.</p><span style="display:inline-block;padding:6px 16px;background:var(--accent-light);color:var(--accent);border-radius:20px;font-size:0.85rem;font-weight:600;">Milestone Achieved</span></div></div>'
        t_list += '</div>'
        custom_sections = sections.split('<section id="experience">')[0] + f'<section id="experience" style="background:var(--bg-alt);"><div class="container fade-in"><div style="text-align:center;margin-bottom:40px;"><h2>Career Milestones</h2><p style="color:var(--text-secondary);max-width:600px;margin:16px auto 0;">A detailed look at my professional journey and commitment to medical advancement.</p></div>{t_list}</div></section>' + sections.split('</section>', 3)[3]
        s_list = '<ul style="display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-top:32px;">'
        for s in item['services']: s_list += f'<li style="display:flex;align-items:center;gap:12px;"><div style="width:8px;height:8px;background:var(--accent);border-radius:50%;"></div>{s}</li>'
        s_list += '</ul>'
        custom_sections = custom_sections.split('<section id="services">')[0] + f'<section id="services"><div class="container fade-in"><h2>Clinical Services</h2>{s_list}</div></section>' + custom_sections.split('</section>', 2)[2]
        
        html = f'<main><div class="container hero-grid fade-in"><div><span style="color:var(--accent);font-weight:700;letter-spacing:1px;text-transform:uppercase;font-size:0.9rem;">{item["specialty"]}</span><h1 style="font-size:3.5rem;margin:16px 0;">{item["doctor"]}</h1><p style="font-size:1.1rem;color:var(--text-secondary);">{item["bio"]}</p><div style="display:flex;gap:32px;margin:32px 0;"><div style="text-align:center"><h3 style="color:var(--accent);font-size:2rem;">{item["stats"][0]}</h3><span style="color:var(--text-secondary);font-size:0.9rem;text-transform:uppercase;letter-spacing:1px;">Years</span></div><div style="text-align:center"><h3 style="color:var(--accent);font-size:2rem;">{item["stats"][1]}</h3><span style="color:var(--text-secondary);font-size:0.9rem;text-transform:uppercase;letter-spacing:1px;">Patients</span></div></div><div style="display:flex;gap:16px;"><a href="#experience" class="btn">View Timeline</a></div></div><div>{svg_placeholder}</div></div>{custom_sections}</main>'

    elif l == 7:
        css = ".hero { height: 90vh; display: flex; align-items: center; text-align: left; position: relative; } .hero-bg { position: absolute; right: 0; top: 0; width: 50vw; height: 100%; z-index: -1; } .hero-content { max-width: 600px; z-index: 1; padding: 48px 0; }"
        html = f'<main><div class="hero fade-in"><div class="hero-bg">{svg_placeholder}</div><div class="container" style="width:100%;"><div class="hero-content"><span style="color:var(--accent);font-weight:700;letter-spacing:1px;text-transform:uppercase;font-size:1rem;">{item["specialty"]}</span><h1 style="font-size:4rem;margin:24px 0;line-height:1.1;">{item["doctor"]}</h1><p style="font-size:1.2rem;color:var(--text-secondary);margin-bottom:40px;">{item["bio"]}</p><div style="display:flex;gap:16px;"><a href="#contact" class="btn" style="font-size:1.1rem;padding:16px 32px;">Book Appointment</a></div></div></div></div>{sections}</main>'

    elif l == 8:
        css = ".split-screen { display: flex; height: 100vh; } .hero-left { width: 50vw; background: var(--accent); color: white; display: flex; align-items: center; justify-content: center; padding: 48px 10%; } .hero-right { width: 50vw; background: var(--bg-alt); } .hero-left h1, .hero-left h2, .hero-left h3, .hero-left p { color: white; } .hero-left .text-secondary { color: rgba(255,255,255,0.8) !important; }"
        html = f'<main><div class="split-screen fade-in"><div class="hero-left"><div><span style="font-weight:700;letter-spacing:1.5px;text-transform:uppercase;font-size:0.9rem;opacity:0.9;">{item["specialty"]}</span><h1 style="font-size:4rem;margin:24px 0;line-height:1.1;">{item["doctor"]}</h1><p class="text-secondary" style="font-size:1.2rem;margin-bottom:40px;line-height:1.7;">{item["bio"]}</p><a href="#contact" class="btn" style="background:white;color:var(--accent);font-size:1.1rem;padding:16px 32px;">Book Appointment</a></div></div><div class="hero-right">{svg_placeholder}</div></div>{sections}</main>'

    final_html = base_html.format(
        doctor=item["doctor"],
        doctor_short=doc_short,
        specialty=item["specialty"],
        accent=item["accent"],
        city=item["city"],
        phone=item["phone"],
        domain=domain,
        layout_css=css,
        layout_html=html
    )
    
    filepath = os.path.join(out_dir, item['filename'])
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(final_html)

print("All 10 templates generated successfully.")
