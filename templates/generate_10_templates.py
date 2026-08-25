import os

templates = [
    {
        "id": "041", "layout": "classic", "accent": "#8B4566",
        "doctor": "Dr. Camille Fontaine, MD, FAAD", "city": "New York, NY", "spec": "Dermatologist",
        "services": ["Medical Dermatology", "Acne Treatment", "Rosacea Management", "Psoriasis & Eczema", "Skin Cancer Screening", "Mole Evaluation"],
        "education": ["Weill Cornell Medical College (MD)", "NewYork-Presbyterian (Residency)", "Sloan Kettering (Fellowship - Dermato-Oncology)"],
        "stats": ["16+ years", "4,200+ patients", "98% satisfaction"], "phone": "+1 (212) 555-4142"
    },
    {
        "id": "042", "layout": "sidebar", "accent": "#7B5080",
        "doctor": "Dr. Jonathan Abara, MD, FAAD", "city": "Miami, FL", "spec": "Dermatologist",
        "services": ["Cosmetic Dermatology", "Botox & Fillers", "Laser Resurfacing", "Chemical Peels", "Platelet-Rich Plasma", "Microneedling"],
        "education": ["University of Miami Miller School (MD)", "Jackson Memorial (Residency)", "Harvard Medical School (Fellowship - Cosmetic Dermatology)"],
        "stats": ["14+ years", "5,600+ patients", "97% satisfaction"], "phone": "+1 (305) 555-4253"
    },
    {
        "id": "043", "layout": "grid", "accent": "#8B4566",
        "doctor": "Dr. Ayesha Rahman, MD, FAAD", "city": "Houston, TX", "spec": "Dermatologist",
        "services": ["Skin of Color Dermatology", "Hyperpigmentation", "Keloid Management", "Hair Loss & Alopecia", "Vitiligo", "Cultural Sensitivity in Skin Care"],
        "education": ["Baylor College of Medicine (MD)", "Harris Health System (Residency)", "Howard University (Fellowship - Skin of Color)"],
        "stats": ["11+ years", "3,800+ patients", "99% satisfaction"], "phone": "+1 (713) 555-4364"
    },
    {
        "id": "044", "layout": "minimal", "accent": "#7B5080",
        "doctor": "Dr. Sebastian Krause, MD, FAAD", "city": "San Francisco, CA", "spec": "Dermatologist",
        "services": ["Surgical Dermatology", "Mohs Micrographic Surgery", "Skin Cancer Excision", "Reconstructive Flaps", "Nail Disorders", "Scalp Conditions"],
        "education": ["UCSF School of Medicine (MD)", "UCSF Medical Center (Residency)", "Memorial Sloan Kettering (Fellowship - Mohs Surgery)"],
        "stats": ["18+ years", "3,400+ surgeries", "98% satisfaction"], "phone": "+1 (415) 555-4475"
    },
    {
        "id": "045", "layout": "magazine", "accent": "#7A3555",
        "doctor": "Dr. Priya Menon, MD, FAAD", "city": "Chicago, IL", "spec": "Dermatologist",
        "services": ["Pediatric Dermatology", "Birthmarks & Vascular Lesions", "Infantile Eczema", "Ichthyosis", "Epidermolysis Bullosa", "Pediatric Psoriasis"],
        "education": ["University of Chicago Pritzker (MD)", "Children's Memorial Hospital (Residency)", "Cincinnati Children's (Fellowship - Pediatric Dermatology)"],
        "stats": ["13+ years", "6,200+ patients", "98% satisfaction"], "phone": "+1 (312) 555-4586"
    },
    {
        "id": "046", "layout": "timeline", "accent": "#7B5080",
        "doctor": "Dr. Laurent Dubois, MD, FAAD", "city": "Los Angeles, CA", "spec": "Dermatologist",
        "services": ["Anti-Aging Dermatology", "Skin Rejuvenation", "RF Microneedling", "IPL Photofacial", "Thread Lift", "Hormone-Related Skin Changes"],
        "education": ["Keck School of Medicine USC (MD)", "USC Medical Center (Residency)", "Stanford (Fellowship - Cosmetic Laser & Surgery)"],
        "stats": ["20+ years", "7,100+ patients", "97% satisfaction"], "phone": "+1 (323) 555-4697"
    },
    {
        "id": "047", "layout": "fullwidth", "accent": "#8B4566",
        "doctor": "Dr. Naomi Oduya, MD, FAAD", "city": "Atlanta, GA", "spec": "Dermatologist",
        "services": ["Autoimmune Skin Disease", "Pemphigus & Bullous Disorders", "Lupus Dermatology", "Dermatomyositis", "Biologics for Psoriasis", "Immunosuppressive Therapy"],
        "education": ["Emory University School of Medicine (MD)", "Emory University Hospital (Residency)", "Mayo Clinic (Fellowship - Autoimmune Dermatology)"],
        "stats": ["15+ years", "3,100+ patients", "98% satisfaction"], "phone": "+1 (404) 555-4752"
    },
    {
        "id": "048", "layout": "split", "accent": "#7B5080",
        "doctor": "Dr. Finn Andersen, MD, FAAD", "city": "Minneapolis, MN", "spec": "Dermatologist",
        "services": ["Contact Dermatitis", "Patch Testing", "Occupational Dermatology", "Drug Eruptions", "Photosensitivity Disorders", "Environmental Skin Disease"],
        "education": ["University of Minnesota Medical School (MD)", "Hennepin Healthcare (Residency)", "Duke University (Fellowship - Contact Dermatology)"],
        "stats": ["10+ years", "2,600+ patients", "98% satisfaction"], "phone": "+1 (612) 555-4863"
    },
    {
        "id": "049", "layout": "classic", "accent": "#2D6A4F",
        "doctor": "Dr. Helen Fitzgerald, MD, FACP", "city": "Portland, OR", "spec": "General Physician",
        "services": ["Primary Care", "Annual Physical Exams", "Chronic Disease Management", "Preventive Health Screenings", "Hypertension & Diabetes Care", "Lifestyle Medicine"],
        "education": ["Oregon Health & Science University (MD)", "OHSU Hospital (Residency - Internal Medicine)", "American Board of Internal Medicine (Board Certified)"],
        "stats": ["17+ years", "5,800+ patients", "97% satisfaction"], "phone": "+1 (503) 555-4971"
    },
    {
        "id": "050", "layout": "sidebar", "accent": "#4A5C2A",
        "doctor": "Dr. Marcus Baptiste, MD, FACP", "city": "New Orleans, LA", "spec": "General Physician",
        "services": ["Concierge Primary Care", "Executive Health Programs", "Travel Medicine", "Geriatric Care", "Preventive Oncology Screenings", "Men's Health"],
        "education": ["Tulane University School of Medicine (MD)", "Tulane Medical Center (Residency)", "American College of Physicians (Fellow)"],
        "stats": ["21+ years", "6,400+ patients", "98% satisfaction"], "phone": "+1 (504) 555-5082"
    }
]

svg_placeholder = """
<div style="width:100%;height:100%;display:flex;align-items:center;justify-content:center;background:var(--bg-alt);border-radius:var(--radius-lg);position:relative;overflow:hidden;min-height:400px;">
  <svg width="160" height="220" viewBox="0 0 160 220" fill="none" style="opacity:0.18;">
    <circle cx="80" cy="60" r="48" fill="currentColor" style="color:var(--accent)"/>
    <ellipse cx="80" cy="180" rx="70" ry="44" fill="currentColor" style="color:var(--accent)"/>
    <rect x="60" y="108" width="40" height="16" rx="8" fill="white" opacity="0.8"/>
  </svg>
  <div style="position:absolute;bottom:16px;left:16px;right:16px;background:white;border-radius:8px;padding:12px 16px;border:1px solid var(--border);">
    <div style="font-size:0.7rem;color:var(--accent);font-weight:700;text-transform:uppercase;letter-spacing:0.08em;">Available for Consultation</div>
    <div style="font-size:0.82rem;color:var(--text-secondary);margin-top:3px;">Mon–Fri: 9:00 AM – 5:00 PM</div>
  </div>
</div>
"""

js_block = """
<script>
function toggleMenu() { document.getElementById('mobileMenu').classList.toggle('open'); }
document.querySelectorAll('#mobileMenu a').forEach(l => l.addEventListener('click', () => document.getElementById('mobileMenu').classList.remove('open')));
const observer = new IntersectionObserver((entries) => { entries.forEach(e => { if(e.isIntersecting){e.target.classList.add('visible');observer.unobserve(e.target);} }); }, {threshold:0.1, rootMargin:'0px 0px -40px 0px'});
document.querySelectorAll('.fade-in').forEach(el => observer.observe(el));
function handleSubmit(e) { e.preventDefault(); const btn=e.target.querySelector('[type="submit"]'); const orig=btn.textContent; btn.textContent='Request Sent ✓'; btn.style.background='#2D6A4F'; btn.disabled=true; setTimeout(()=>{btn.textContent=orig;btn.style.background='';btn.disabled=false;e.target.reset();},4000); return false; }
window.addEventListener('scroll', () => { const nav=document.querySelector('.navbar'); if(nav) nav.style.boxShadow = window.scrollY>10 ? '0 2px 16px rgba(0,0,0,0.08)' : ''; });
</script>
"""

def generate_html(tmpl):
    layout_css = ""
    hero_html = ""
    about_html = ""
    services_html = ""
    timeline_html = ""
    
    if tmpl["layout"] == "sidebar":
        layout_css = """
        .main-wrapper { display: grid; grid-template-columns: 280px 1fr; gap: 40px; max-width: 1200px; margin: 0 auto; padding: 120px 20px 40px; }
        .sidebar { position: sticky; top: 100px; height: fit-content; background: var(--bg-alt); padding: 24px; border-radius: var(--radius-lg); }
        @media (max-width: 900px) { .main-wrapper { grid-template-columns: 1fr; } .sidebar { position: static; } }
        """
        hero_html = f"""<div class="hero fade-in">
            <span class="specialty">{tmpl['spec']}</span>
            <h1>{tmpl['doctor']}</h1>
            <p>Dedicated to providing exceptional care for patients in {tmpl['city']}.</p>
            <div class="stats-grid" style="margin-top:20px;">
                <div class="stat-box"><strong>{tmpl['stats'][0]}</strong><br>Experience</div>
                <div class="stat-box"><strong>{tmpl['stats'][1]}</strong><br>Patients</div>
                <div class="stat-box"><strong>{tmpl['stats'][2]}</strong><br>Satisfaction</div>
            </div>
        </div>"""
    elif tmpl["layout"] == "split":
        layout_css = """
        .split-hero { display: flex; width: 100%; height: 100vh; }
        .split-left { width: 50vw; background: var(--accent); color: white; display: flex; flex-direction: column; justify-content: center; padding: 80px; }
        .split-left p, .split-left span { color: rgba(255,255,255,0.8); }
        .split-right { width: 50vw; background: var(--bg-alt); display: flex; align-items: center; justify-content: center; }
        @media (max-width: 768px) { .split-hero { flex-direction: column; height: auto; } .split-left, .split-right { width: 100%; padding: 40px 20px; } }
        """
        hero_html = f"""
        <section class="split-hero" id="home">
            <div class="split-left fade-in">
                <span style="text-transform:uppercase;letter-spacing:1px;font-size:0.9rem;">{tmpl['spec']}</span>
                <h1 style="color:white; font-size:3rem; margin:10px 0;">{tmpl['doctor']}</h1>
                <p style="font-size:1.1rem; line-height:1.6; margin-bottom:30px;">Delivering specialized care in {tmpl['city']}.</p>
                <div style="display:flex; gap:20px;">
                    <a href="#contact" class="btn" style="background:white; color:var(--accent);">Book Appointment</a>
                    <a href="#services" class="btn btn-outline" style="border-color:white; color:white;">Our Services</a>
                </div>
            </div>
            <div class="split-right fade-in">
                {svg_placeholder}
            </div>
        </section>"""
    elif tmpl["layout"] == "grid":
        layout_css = """
        .hero-grid { display: grid; grid-template-columns: 7fr 5fr; gap: 40px; align-items: center; min-height: 80vh; padding-top:80px; }
        .about-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 30px; }
        .service-card { min-height: 200px; }
        @media (max-width: 768px) { .hero-grid, .about-grid { grid-template-columns: 1fr; } }
        """
        hero_html = f"""
        <section class="container hero-grid fade-in" id="home">
            <div>
                <span class="specialty">{tmpl['spec']}</span>
                <h1>{tmpl['doctor']}</h1>
                <p>Expert medical care utilizing the latest advancements in {tmpl['spec'].lower()} for patients in {tmpl['city']}.</p>
                <div class="stats-grid">
                    <div class="stat-box"><strong>{tmpl['stats'][0]}</strong><br>Experience</div>
                    <div class="stat-box"><strong>{tmpl['stats'][1]}</strong><br>Patients</div>
                    <div class="stat-box"><strong>{tmpl['stats'][2]}</strong><br>Satisfaction</div>
                </div>
                <div class="btn-group" style="margin-top:30px;">
                    <a href="#contact" class="btn">Book Appointment</a>
                    <a href="#about" class="btn btn-outline">Learn More</a>
                </div>
            </div>
            <div>{svg_placeholder}</div>
        </section>"""
    elif tmpl["layout"] == "minimal":
        layout_css = """
        section { padding: 100px 0; background: #ffffff !important; }
        .hero-minimal { text-align: center; padding-top: 150px; max-width: 800px; margin: 0 auto; }
        .hero-minimal h1 { font-size: 3.5rem; margin-bottom: 20px; }
        hr { border: none; border-top: 1px solid var(--border); margin: 40px 0; }
        .minimal-image { max-width: 600px; margin: 40px auto; }
        """
        hero_html = f"""
        <section class="container hero-minimal fade-in" id="home">
            <span class="specialty">{tmpl['spec']}</span>
            <h1>{tmpl['doctor']}</h1>
            <p>Minimalist approach to maximal care in {tmpl['city']}.</p>
            <div class="minimal-image">{svg_placeholder}</div>
            <div class="stats-grid" style="justify-content:center; gap:40px;">
                <div class="stat-box" style="border:none;"><strong>{tmpl['stats'][0]}</strong><br>Experience</div>
                <div class="stat-box" style="border:none;"><strong>{tmpl['stats'][1]}</strong><br>Patients</div>
                <div class="stat-box" style="border:none;"><strong>{tmpl['stats'][2]}</strong><br>Satisfaction</div>
            </div>
        </section>"""
    elif tmpl["layout"] == "fullwidth":
        layout_css = """
        .hero-full { display: flex; height: 85vh; padding-top: 80px; align-items: center; }
        .hero-full h1 { font-size: 4rem; line-height: 1.1; margin-bottom: 20px; }
        .hero-content { flex: 1; padding-right: 40px; }
        .hero-image { flex: 1; height: 100%; padding: 40px; }
        @media (max-width: 768px) { .hero-full { flex-direction: column; height: auto; } .hero-image { width:100%; height:400px; } }
        """
        hero_html = f"""
        <section class="container hero-full fade-in" id="home">
            <div class="hero-content">
                <span class="specialty">{tmpl['spec']}</span>
                <h1>{tmpl['doctor']}</h1>
                <p style="font-size:1.2rem; margin-bottom:30px;">Premier medical care located in the heart of {tmpl['city']}.</p>
                <div class="stats-grid">
                    <div class="stat-box"><strong>{tmpl['stats'][0]}</strong><br>Experience</div>
                    <div class="stat-box"><strong>{tmpl['stats'][1]}</strong><br>Patients</div>
                    <div class="stat-box"><strong>{tmpl['stats'][2]}</strong><br>Satisfaction</div>
                </div>
                <div class="btn-group" style="margin-top:30px;">
                    <a href="#contact" class="btn" style="font-size:1.1rem; padding: 14px 28px;">Book Appointment</a>
                </div>
            </div>
            <div class="hero-image">{svg_placeholder}</div>
        </section>"""
    elif tmpl["layout"] == "magazine":
        layout_css = """
        .hero-mag { position: relative; padding: 120px 0 80px; overflow: hidden; }
        .bg-text { position: absolute; font-size: 15vw; font-weight: 900; color: rgba(0,0,0,0.02); top: 50%; left: 50%; transform: translate(-50%, -50%); z-index: 0; white-space: nowrap; font-family: 'Playfair Display', serif; }
        .hero-mag .content { position: relative; z-index: 1; display: grid; grid-template-columns: 1fr 1fr; gap: 40px; align-items: center; }
        .section-num { font-size: 3rem; color: var(--accent-light); font-weight: 700; margin-bottom: -20px; display: block; font-family: 'Playfair Display', serif; }
        .service-list { display: flex; flex-direction: column; gap: 20px; }
        .service-item { display: flex; justify-content: space-between; border-bottom: 1px solid var(--border); padding-bottom: 20px; align-items: center; }
        @media (max-width: 768px) { .hero-mag .content { grid-template-columns: 1fr; } }
        """
        hero_html = f"""
        <section class="hero-mag fade-in" id="home">
            <div class="bg-text">{tmpl['spec'].upper()}</div>
            <div class="container content">
                <div>
                    <span class="specialty">{tmpl['spec']}</span>
                    <h1 style="font-size:3.5rem;">{tmpl['doctor']}</h1>
                    <p style="font-size:1.1rem; line-height:1.6; margin: 20px 0;">Providing advanced medical treatments in {tmpl['city']}.</p>
                    <div class="stats-grid">
                        <div class="stat-box"><strong>{tmpl['stats'][0]}</strong><br>Experience</div>
                        <div class="stat-box"><strong>{tmpl['stats'][1]}</strong><br>Patients</div>
                        <div class="stat-box"><strong>{tmpl['stats'][2]}</strong><br>Satisfaction</div>
                    </div>
                    <div class="btn-group" style="margin-top:30px;">
                        <a href="#contact" class="btn">Book Consultation</a>
                    </div>
                </div>
                <div>{svg_placeholder}</div>
            </div>
        </section>"""
    elif tmpl["layout"] == "timeline":
        layout_css = """
        .hero-timeline { text-align: center; padding: 120px 0 60px; }
        .timeline-large { max-width: 800px; margin: 0 auto; position: relative; padding-left: 40px; }
        .timeline-large::before { content: ''; position: absolute; left: 10px; top: 0; bottom: 0; width: 2px; background: var(--border); }
        .timeline-item-large { position: relative; margin-bottom: 40px; }
        .timeline-item-large::before { content: ''; position: absolute; left: -36px; top: 5px; width: 14px; height: 14px; border-radius: 50%; background: var(--accent); border: 4px solid white; box-shadow: 0 0 0 2px var(--border); }
        """
        hero_html = f"""
        <section class="container hero-timeline fade-in" id="home">
            <span class="specialty">{tmpl['spec']}</span>
            <h1 style="font-size:3.5rem; margin:20px 0;">{tmpl['doctor']}</h1>
            <p style="max-width:600px; margin:0 auto 40px; font-size:1.1rem;">A legacy of excellence in patient care in {tmpl['city']}.</p>
            <div class="stats-grid" style="justify-content:center; gap:30px; margin-bottom:40px;">
                <div class="stat-box"><strong>{tmpl['stats'][0]}</strong><br>Experience</div>
                <div class="stat-box"><strong>{tmpl['stats'][1]}</strong><br>Patients</div>
                <div class="stat-box"><strong>{tmpl['stats'][2]}</strong><br>Satisfaction</div>
            </div>
            <div style="max-width:800px; margin:0 auto;">{svg_placeholder}</div>
        </section>"""
    else:
        # Classic
        layout_css = """
        .hero { display: grid; grid-template-columns: 1fr 1fr; gap: 40px; align-items: center; padding: 120px 0 80px; }
        @media (max-width: 768px) { .hero { grid-template-columns: 1fr; padding-top: 100px; } }
        """
        hero_html = f"""
        <section class="container hero fade-in" id="home">
            <div>
                <span class="specialty">{tmpl['spec']}</span>
                <h1>{tmpl['doctor']}</h1>
                <p>Compassionate and comprehensive medical care based in {tmpl['city']}. Dedicated to improving patient health and wellbeing.</p>
                <div class="stats-grid" style="margin: 30px 0;">
                    <div class="stat-box"><strong>{tmpl['stats'][0]}</strong><br>Experience</div>
                    <div class="stat-box"><strong>{tmpl['stats'][1]}</strong><br>Patients</div>
                    <div class="stat-box"><strong>{tmpl['stats'][2]}</strong><br>Satisfaction</div>
                </div>
                <div class="btn-group">
                    <a href="#contact" class="btn">Book Appointment</a>
                    <a href="#services" class="btn btn-outline">Our Services</a>
                </div>
            </div>
            <div>{svg_placeholder}</div>
        </section>"""

    # Generate Services
    services_list = ""
    if tmpl["layout"] == "magazine" or tmpl["layout"] == "timeline":
        services_list = "<div class='service-list'>" + "".join([f"<div class='service-item fade-in'><h3>{s}</h3><p>Comprehensive evaluation and treatment for {s.lower()}.</p></div>" for s in tmpl["services"]]) + "</div>"
    else:
        services_list = "<div class='grid-3'>" + "".join([f"<div class='card service-card fade-in'><div class='icon'>⚕️</div><h3>{s}</h3><p>Professional diagnosis and advanced treatment options customized for your needs regarding {s.lower()}.</p></div>" for s in tmpl["services"]]) + "</div>"

    # Generate Full HTML
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{tmpl['doctor']} - {tmpl['spec']}</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Playfair+Display:wght@600;700&display=swap" rel="stylesheet">
    <style>
        :root {{
            --accent: {tmpl['accent']};
            --accent-hover: {tmpl['accent']}dd;
            --accent-light: {tmpl['accent']}15;
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
        body {{ font-family: 'Inter', sans-serif; color: var(--text-secondary); line-height: 1.6; background: var(--bg); }}
        h1, h2, h3, h4 {{ font-family: 'Playfair Display', serif; color: var(--text-primary); }}
        h1 {{ font-size: 3rem; line-height: 1.2; margin-bottom: 1rem; }}
        h2 {{ font-size: 2.2rem; margin-bottom: 2rem; }}
        a {{ text-decoration: none; color: inherit; transition: var(--transition); }}
        ul {{ list-style: none; }}
        
        .container {{ max-width: 1120px; margin: 0 auto; padding: 0 20px; }}
        section {{ padding: 80px 0; }}
        .bg-alt {{ background: var(--bg-alt); }}
        
        /* Navbar */
        .navbar {{ position: fixed; top: 0; width: 100%; background: rgba(255,255,255,0.95); backdrop-filter: blur(10px); z-index: 1000; transition: var(--transition); border-bottom: 1px solid var(--border); }}
        .nav-container {{ display: flex; justify-content: space-between; align-items: center; height: 80px; max-width: 1120px; margin: 0 auto; padding: 0 20px; }}
        .logo {{ font-family: 'Playfair Display', serif; font-size: 1.4rem; font-weight: 700; color: var(--text-primary); }}
        .nav-links {{ display: flex; gap: 30px; align-items: center; }}
        .nav-links a {{ font-weight: 500; font-size: 0.95rem; color: var(--text-primary); }}
        .nav-links a:hover {{ color: var(--accent); }}
        
        /* Buttons */
        .btn {{ display: inline-block; background: var(--accent); color: white; padding: 12px 24px; border-radius: var(--radius); font-weight: 500; text-align: center; transition: var(--transition); border: 2px solid var(--accent); cursor: pointer; font-family: inherit; font-size: 1rem; }}
        .btn:hover {{ background: var(--accent-hover); border-color: var(--accent-hover); color: white; }}
        .btn-outline {{ background: transparent; color: var(--accent); }}
        .btn-outline:hover {{ background: var(--accent); color: white; }}
        .btn-group {{ display: flex; gap: 15px; flex-wrap: wrap; }}
        
        /* Elements */
        .specialty {{ display: inline-block; padding: 6px 12px; background: var(--accent-light); color: var(--accent); border-radius: 20px; font-size: 0.85rem; font-weight: 600; margin-bottom: 15px; letter-spacing: 0.5px; text-transform: uppercase; }}
        .stats-grid {{ display: flex; gap: 20px; flex-wrap: wrap; }}
        .stat-box {{ background: white; border: 1px solid var(--border); padding: 15px 20px; border-radius: var(--radius); text-align: center; flex: 1; min-width: 120px; }}
        .stat-box strong {{ display: block; font-size: 1.5rem; color: var(--accent); font-family: 'Playfair Display', serif; margin-bottom: 5px; }}
        
        .grid-2 {{ display: grid; grid-template-columns: 1fr 1fr; gap: 40px; }}
        .grid-3 {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 30px; }}
        
        .card {{ background: white; padding: 30px; border-radius: var(--radius-lg); border: 1px solid var(--border); box-shadow: var(--shadow-sm); transition: var(--transition); }}
        .card:hover {{ box-shadow: var(--shadow-md); transform: translateY(-3px); }}
        .icon {{ width: 50px; height: 50px; background: var(--accent-light); color: var(--accent); border-radius: var(--radius); display: flex; align-items: center; justify-content: center; font-size: 1.5rem; margin-bottom: 20px; }}
        
        /* Timeline */
        .timeline {{ border-left: 2px solid var(--accent-light); padding-left: 30px; margin-left: 15px; }}
        .timeline-item {{ position: relative; margin-bottom: 30px; }}
        .timeline-item::before {{ content: ''; position: absolute; left: -37px; top: 5px; width: 12px; height: 12px; background: var(--accent); border-radius: 50%; box-shadow: 0 0 0 4px white; }}
        
        /* Forms */
        .form-group {{ margin-bottom: 20px; }}
        .form-label {{ display: block; margin-bottom: 8px; font-weight: 500; color: var(--text-primary); }}
        .form-control {{ width: 100%; padding: 12px 15px; border: 1px solid var(--border); border-radius: var(--radius); font-family: inherit; font-size: 1rem; background: var(--bg-alt); transition: var(--transition); }}
        .form-control:focus {{ outline: none; border-color: var(--accent); background: white; box-shadow: 0 0 0 3px var(--accent-light); }}
        
        /* Animations */
        .fade-in {{ opacity: 0; transform: translateY(20px); transition: opacity 0.8s ease, transform 0.8s ease; }}
        .fade-in.visible {{ opacity: 1; transform: translateY(0); }}
        
        /* Mobile Menu */
        .hamburger {{ display: none; background: none; border: none; font-size: 1.5rem; cursor: pointer; color: var(--text-primary); }}
        .mobile-menu {{ display: none; position: fixed; top: 80px; left: 0; width: 100%; background: white; padding: 20px; border-bottom: 1px solid var(--border); box-shadow: var(--shadow-md); z-index: 999; flex-direction: column; gap: 15px; }}
        .mobile-menu.open {{ display: flex; }}
        
        @media (max-width: 768px) {{
            .nav-links {{ display: none; }}
            .hamburger {{ display: block; }}
            .grid-2 {{ grid-template-columns: 1fr; }}
        }}
        
        {layout_css}
    </style>
</head>
<body>

<nav class="navbar">
    <div class="nav-container">
        <a href="#" class="logo">{tmpl['doctor'].split(',')[0]}</a>
        <div class="nav-links">
            <a href="#about">About</a>
            <a href="#services">Services</a>
            <a href="#experience">Experience</a>
            <a href="#reviews">Reviews</a>
            <a href="#contact" class="btn">Book Appointment</a>
        </div>
        <button class="hamburger" onclick="toggleMenu()">☰</button>
    </div>
</nav>

<div class="mobile-menu" id="mobileMenu">
    <a href="#about">About</a>
    <a href="#services">Services</a>
    <a href="#experience">Experience</a>
    <a href="#reviews">Reviews</a>
    <a href="#contact" class="btn" style="text-align:center;">Book Appointment</a>
</div>

"""
    
    if tmpl["layout"] == "sidebar":
        html += f"""
<div class="main-wrapper">
    <aside class="sidebar fade-in">
        <div style="margin-bottom:20px; border-radius:var(--radius-lg); overflow:hidden;">
            <svg width="100%" height="200" viewBox="0 0 160 220" fill="none" style="background:#fff;opacity:0.8;">
                <circle cx="80" cy="60" r="48" fill="currentColor" style="color:var(--accent-light)"/>
                <ellipse cx="80" cy="180" rx="70" ry="44" fill="currentColor" style="color:var(--accent-light)"/>
            </svg>
        </div>
        <h3 style="font-size:1.2rem;margin-bottom:10px;">{tmpl['doctor']}</h3>
        <p style="font-size:0.9rem;margin-bottom:20px;">{tmpl['city']}</p>
        <div style="font-size:0.9rem; margin-bottom:20px;">
            <strong>Phone:</strong> {tmpl['phone']}<br>
            <strong>Hours:</strong> Mon-Fri, 9am-5pm
        </div>
        <a href="#contact" class="btn" style="width:100%; text-align:center;">Book Now</a>
    </aside>
    <main>
        {hero_html}
        """
    elif tmpl["layout"] not in ["sidebar", "split"]:
        html += hero_html
    else:
        # split handled differently but we can just append
        html += hero_html

    html += f"""
<!-- About Section -->
<section id="about" class="bg-alt">
    <div class="container">
        <div class="fade-in">
            <h2>About & Credentials</h2>
            <p style="font-size: 1.1rem; max-width: 800px; margin-bottom: 40px;">
                {tmpl['doctor']} is a board-certified {tmpl['spec'].lower()} dedicated to providing exceptional, evidence-based care. With years of extensive training and clinical practice, the focus remains on delivering personalized treatments that prioritize patient well-being and long-term health outcomes.
            </p>
        </div>
        <div class="grid-2">
            <div class="card fade-in">
                <div class="icon">🎓</div>
                <h3 style="font-size:1.2rem;margin-bottom:10px;">Medical Education</h3>
                <p>{tmpl['education'][0]}</p>
            </div>
            <div class="card fade-in">
                <div class="icon">🏥</div>
                <h3 style="font-size:1.2rem;margin-bottom:10px;">Residency</h3>
                <p>{tmpl['education'][1]}</p>
            </div>
            <div class="card fade-in">
                <div class="icon">🔬</div>
                <h3 style="font-size:1.2rem;margin-bottom:10px;">Fellowship</h3>
                <p>{tmpl['education'][2]}</p>
            </div>
            <div class="card fade-in">
                <div class="icon">📜</div>
                <h3 style="font-size:1.2rem;margin-bottom:10px;">Certification</h3>
                <p>Board Certified - American Board of Medical Specialties</p>
            </div>
        </div>
    </div>
</section>

<!-- Services Section -->
<section id="services">
    <div class="container">
        <div class="fade-in" style="margin-bottom: 40px;">
            <h2>Areas of Expertise</h2>
            <p>Comprehensive {tmpl['spec'].lower()} services tailored to your individual health needs.</p>
        </div>
        {services_list}
    </div>
</section>

<!-- Experience Section -->
<section id="experience" class="bg-alt">
    <div class="container">
        <h2 class="fade-in">Career Journey</h2>
        <div class="timeline fade-in" style="max-width:800px;">
            <div class="timeline-item">
                <h3 style="font-size:1.2rem;">Attending {tmpl['spec']}</h3>
                <span style="color:var(--accent); font-weight:600; font-size:0.9rem;">Present</span>
                <p style="margin-top:10px;">Leading clinical care and establishing advanced treatment protocols for a diverse patient demographic.</p>
            </div>
            <div class="timeline-item">
                <h3 style="font-size:1.2rem;">Fellowship Training</h3>
                <span style="color:var(--accent); font-weight:600; font-size:0.9rem;">{tmpl['education'][2]}</span>
                <p style="margin-top:10px;">Specialized advanced training focusing on complex cases and modern methodologies.</p>
            </div>
            <div class="timeline-item">
                <h3 style="font-size:1.2rem;">Residency Program</h3>
                <span style="color:var(--accent); font-weight:600; font-size:0.9rem;">{tmpl['education'][1]}</span>
                <p style="margin-top:10px;">Intensive clinical training, managing high-volume patient loads across various clinical settings.</p>
            </div>
            <div class="timeline-item">
                <h3 style="font-size:1.2rem;">Medical Degree</h3>
                <span style="color:var(--accent); font-weight:600; font-size:0.9rem;">{tmpl['education'][0]}</span>
                <p style="margin-top:10px;">Graduated with honors, laying the foundation for a career dedicated to medical excellence.</p>
            </div>
        </div>
    </div>
</section>

<!-- Testimonials Section -->
<section id="reviews">
    <div class="container">
        <h2 class="fade-in" style="text-align:center;">Patient Testimonials</h2>
        <div class="grid-3" style="margin-top:40px;">
            <div class="card fade-in">
                <div style="color:#f59e0b; font-size:1.2rem; margin-bottom:15px;">★★★★★</div>
                <p style="font-style:italic;">"{tmpl['doctor'].split(',')[0]} is incredibly thorough and compassionate. I always feel heard and well cared for."</p>
                <div style="margin-top:20px; font-weight:600; color:var(--text-primary);">— A.R.</div>
            </div>
            <div class="card fade-in">
                <div style="color:#f59e0b; font-size:1.2rem; margin-bottom:15px;">★★★★★</div>
                <p style="font-style:italic;">"The staff is friendly, and the doctor took the time to explain every detail of my treatment plan."</p>
                <div style="margin-top:20px; font-weight:600; color:var(--text-primary);">— M.S.</div>
            </div>
            <div class="card fade-in">
                <div style="color:#f59e0b; font-size:1.2rem; margin-bottom:15px;">★★★★★</div>
                <p style="font-style:italic;">"Outstanding experience from start to finish. Highly recommend this practice for anyone needing specialized care."</p>
                <div style="margin-top:20px; font-weight:600; color:var(--text-primary);">— J.L.</div>
            </div>
        </div>
    </div>
</section>

<!-- Contact Section -->
<section id="contact" class="bg-alt">
    <div class="container">
        <div class="grid-2">
            <div class="fade-in">
                <h2>Get In Touch</h2>
                <p style="margin-bottom:30px;">Ready to schedule a consultation? Fill out the form, and our office will contact you shortly.</p>
                
                <div style="margin-bottom:40px;">
                    <div style="display:flex; gap:15px; margin-bottom:20px; align-items:center;">
                        <div class="icon" style="margin:0; width:40px; height:40px; font-size:1.2rem;">📍</div>
                        <div>
                            <strong>Location</strong><br>
                            Medical Arts Building, {tmpl['city']}
                        </div>
                    </div>
                    <div style="display:flex; gap:15px; margin-bottom:20px; align-items:center;">
                        <div class="icon" style="margin:0; width:40px; height:40px; font-size:1.2rem;">📞</div>
                        <div>
                            <strong>Phone</strong><br>
                            {tmpl['phone']}
                        </div>
                    </div>
                    <div style="display:flex; gap:15px; align-items:center;">
                        <div class="icon" style="margin:0; width:40px; height:40px; font-size:1.2rem;">🕒</div>
                        <div>
                            <strong>Office Hours</strong><br>
                            Mon-Fri: 9:00 AM - 5:00 PM
                        </div>
                    </div>
                </div>
            </div>
            
            <div class="card fade-in">
                <form onsubmit="return handleSubmit(event)">
                    <div class="grid-2" style="gap:20px;">
                        <div class="form-group">
                            <label class="form-label">First Name</label>
                            <input type="text" class="form-control" required>
                        </div>
                        <div class="form-group">
                            <label class="form-label">Last Name</label>
                            <input type="text" class="form-control" required>
                        </div>
                    </div>
                    <div class="form-group">
                        <label class="form-label">Email Address</label>
                        <input type="email" class="form-control" required>
                    </div>
                    <div class="form-group">
                        <label class="form-label">Phone Number</label>
                        <input type="tel" class="form-control" required>
                    </div>
                    <div class="form-group">
                        <label class="form-label">Reason for Visit</label>
                        <select class="form-control" required>
                            <option value="">Select an option...</option>
                            <option value="new">New Patient Consultation</option>
                            <option value="followup">Follow-up Appointment</option>
                            <option value="procedure">Specific Procedure</option>
                            <option value="other">Other</option>
                        </select>
                    </div>
                    <div class="form-group">
                        <label class="form-label">Additional Notes</label>
                        <textarea class="form-control" rows="4"></textarea>
                    </div>
                    <button type="submit" class="btn" style="width:100%;">Submit Request</button>
                </form>
            </div>
        </div>
    </div>
</section>
"""

    if tmpl["layout"] == "sidebar":
        html += """
    </main>
</div>
"""

    html += f"""
<footer style="background:var(--text-primary); color:white; padding:60px 0 30px; text-align:center;">
    <div class="container fade-in">
        <h3 style="color:white; margin-bottom:20px;">{tmpl['doctor']}</h3>
        <div style="display:flex; justify-content:center; gap:20px; margin-bottom:30px; flex-wrap:wrap;">
            <a href="#about" style="color:#aaa;">About</a>
            <a href="#services" style="color:#aaa;">Services</a>
            <a href="#experience" style="color:#aaa;">Experience</a>
            <a href="#contact" style="color:#aaa;">Contact</a>
        </div>
        <div style="color:#777; font-size:0.9rem; border-top:1px solid rgba(255,255,255,0.1); padding-top:30px;">
            &copy; {tmpl['doctor'].split(',')[0]} Portfolio. All rights reserved.
        </div>
    </div>
</footer>

{js_block}
</body>
</html>
"""
    return html

os.makedirs(r"d:\website\doctors portfolio\templates", exist_ok=True)
for tmpl in templates:
    content = generate_html(tmpl)
    with open(rf"d:\website\doctors portfolio\templates\template-{tmpl['id']}.html", "w", encoding="utf-8") as f:
        f.write(content)

print("Generated all 10 templates.")
