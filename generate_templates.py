import os
import json

templates = [
    {
        "filename": "template-031.html",
        "specialty": "Orthopedic Surgeon",
        "layout": "Layout 7",
        "accent": "#2B5B8B",
        "doctor": "Dr. Ian Fitzgerald, MD, FAAOS",
        "city": "Baltimore, MD",
        "services": ["Trauma Surgery", "Complex Fracture Fixation", "Pelvic Acetabular Surgery", "External Fixation", "Bone Infection Treatment", "Reconstructive Surgery After Trauma"],
        "education": ["Johns Hopkins School of Medicine (MD)", "Johns Hopkins Hospital (Residency – Orthopedic Surgery)", "R Adams Cowley Shock Trauma Center (Fellowship – Orthopaedic Trauma)"],
        "stats": ["16+ years experience", "3,700+ procedures", "97% satisfaction"],
        "phone": "+1 (410) 555-3142"
    },
    {
        "filename": "template-032.html",
        "specialty": "Orthopedic Surgeon",
        "layout": "Layout 8",
        "accent": "#3D3D3D",
        "doctor": "Dr. Lydia Chambers, MD, FAAOS, MBA",
        "city": "Salt Lake City, UT",
        "services": ["Foot & Ankle Reconstruction", "Bunion Surgery", "Achilles Tendon Repair", "Ankle Replacement", "Flat Foot Correction", "Hammertoe Correction"],
        "education": ["University of Utah School of Medicine (MD)", "Intermountain Healthcare (Residency)", "OrthoCarolina (Fellowship – Foot & Ankle)"],
        "stats": ["13+ years experience", "3,100+ procedures", "98% satisfaction"],
        "phone": "+1 (801) 555-3254"
    },
    {
        "filename": "template-033.html",
        "specialty": "Neurologist",
        "layout": "Layout 1",
        "accent": "#4B2882",
        "doctor": "Dr. Amir Hassan, MD, PhD, FAAN",
        "city": "New York, NY",
        "services": ["Epilepsy & Seizure Management", "Multiple Sclerosis", "Parkinson's Disease", "Stroke Prevention", "Headache & Migraine Clinics", "Neuro-Immunology"],
        "education": ["Columbia University Vagelos College (MD, PhD)", "NewYork-Presbyterian (Residency – Neurology)", "Mayo Clinic (Fellowship – Epilepsy)"],
        "stats": ["19+ years experience", "4,800+ patients", "97% satisfaction"],
        "phone": "+1 (212) 555-3365"
    },
    {
        "filename": "template-034.html",
        "specialty": "Neurologist",
        "layout": "Layout 2",
        "accent": "#312ABF",
        "doctor": "Dr. Fatima Al-Rashid, MD, FAAN",
        "city": "Houston, TX",
        "services": ["Movement Disorders", "Deep Brain Stimulation", "Dystonia Management", "Tremor Treatment", "Huntington's Disease", "Cognitive Neurology"],
        "education": ["Baylor College of Medicine (MD)", "Houston Methodist (Residency)", "UCSF (Fellowship – Movement Disorders)"],
        "stats": ["15+ years experience", "3,600+ patients", "98% satisfaction"],
        "phone": "+1 (713) 555-3471"
    },
    {
        "filename": "template-035.html",
        "specialty": "Neurologist",
        "layout": "Layout 3",
        "accent": "#4B2882",
        "doctor": "Dr. Steven Park, MD, FAAN, FACP",
        "city": "Chicago, IL",
        "services": ["Neuromuscular Disease", "ALS Clinic", "Peripheral Neuropathy", "Myasthenia Gravis", "Muscular Dystrophy", "Nerve Conduction Studies"],
        "education": ["University of Chicago Pritzker (MD)", "Rush University Medical Center (Residency)", "Brigham & Women's Hospital (Fellowship – Neuromuscular Disease)"],
        "stats": ["22+ years experience", "5,400+ patients", "97% satisfaction"],
        "phone": "+1 (312) 555-3583"
    },
    {
        "filename": "template-036.html",
        "specialty": "Neurologist",
        "layout": "Layout 4",
        "accent": "#312ABF",
        "doctor": "Dr. Claire Beaumont, MD, MSc",
        "city": "San Francisco, CA",
        "services": ["Cognitive Neurology", "Dementia & Alzheimer's Care", "Memory Clinics", "Mild Cognitive Impairment", "Neuropsychological Testing", "Caregiver Support Programs"],
        "education": ["UCSF School of Medicine (MD)", "UCSF Memory & Aging Center (Residency & Fellowship – Behavioral Neurology)", "Stanford (MSc – Clinical Research)"],
        "stats": ["14+ years experience", "3,200+ patients", "99% satisfaction"],
        "phone": "+1 (415) 555-3694"
    },
    {
        "filename": "template-037.html",
        "specialty": "Neurologist",
        "layout": "Layout 5",
        "accent": "#3D1F6F",
        "doctor": "Dr. Nicholas Lombardi, MD, PhD",
        "city": "Boston, MA",
        "services": ["Neuro-Oncology", "Brain Tumor Management", "Glioma Treatment Protocols", "Meningioma", "CNS Lymphoma", "Immunotherapy for Brain Tumors"],
        "education": ["Harvard Medical School (MD, PhD)", "Mass General Hospital (Residency)", "Dana-Farber Cancer Institute (Fellowship – Neuro-Oncology)"],
        "stats": ["18+ years experience", "2,900+ patients", "97% satisfaction"],
        "phone": "+1 (617) 555-3705"
    },
    {
        "filename": "template-038.html",
        "specialty": "Neurologist",
        "layout": "Layout 6",
        "accent": "#312ABF",
        "doctor": "Dr. Ingrid Sorenson, MD, FAAN",
        "city": "Minneapolis, MN",
        "services": ["Headache Medicine", "Chronic Migraine Treatment", "Botox for Migraine", "CGRP Therapy", "Post-Traumatic Headache", "Occipital Nerve Blocks"],
        "education": ["University of Minnesota (MD)", "Hennepin Healthcare (Residency – Neurology)", "Mayo Clinic (Fellowship – Headache Medicine)"],
        "stats": ["12+ years experience", "4,100+ patients", "98% satisfaction"],
        "phone": "+1 (612) 555-3816"
    },
    {
        "filename": "template-039.html",
        "specialty": "Neurologist",
        "layout": "Layout 7",
        "accent": "#4B2882",
        "doctor": "Dr. Emmanuel Osei, MD, FAAN",
        "city": "Atlanta, GA",
        "services": ["Stroke Neurology", "Acute Stroke Care", "TIA Management", "Stroke Rehabilitation", "Vascular Neurology", "Carotid Artery Disease"],
        "education": ["Morehouse School of Medicine (MD)", "Emory University Hospital (Residency)", "Grady Memorial Hospital (Fellowship – Stroke & Vascular Neurology)"],
        "stats": ["17+ years experience", "5,200+ patients", "97% satisfaction"],
        "phone": "+1 (404) 555-3923"
    },
    {
        "filename": "template-040.html",
        "specialty": "Neurologist",
        "layout": "Layout 8",
        "accent": "#312ABF",
        "doctor": "Dr. Victoria Strand, MD, FAAN, FAES",
        "city": "Seattle, WA",
        "services": ["Pediatric Neurology", "Childhood Epilepsy", "Pediatric Stroke", "Developmental Delay", "Rett Syndrome", "Tuberous Sclerosis"],
        "education": ["University of Washington (MD)", "Seattle Children's Hospital (Residency & Fellowship – Pediatric Neurology)", "American Epilepsy Society (Fellow)"],
        "stats": ["16+ years experience", "4,700+ patients", "98% satisfaction"],
        "phone": "+1 (206) 555-4037"
    }
]

def generate_html(template):
    accent_rgb = tuple(int(template['accent'].lstrip('#')[i:i+2], 16) for i in (0, 2, 4))
    accent_rgba = f"{accent_rgb[0]}, {accent_rgb[1]}, {accent_rgb[2]}"
    
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{template['doctor']} - {template['specialty']} | {template['city']}</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Playfair+Display:ital,wght@0,400;0,600;0,700;1,400&display=swap" rel="stylesheet">
    <style>
        :root {{
            --accent: {template['accent']};
            --accent-hover: #1a1a2e;
            --accent-light: rgba({accent_rgba}, 0.08);
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
        body {{ font-family: 'Inter', sans-serif; color: var(--text-primary); line-height: 1.6; background: var(--bg); overflow-x: hidden; }}
        h1, h2, h3, h4, h5, h6 {{ font-family: 'Playfair Display', serif; color: var(--text-primary); }}
        a {{ text-decoration: none; color: inherit; transition: var(--transition); }}
        ul {{ list-style: none; }}
        .container {{ max-width: 1120px; margin: 0 auto; padding: 0 24px; }}
        
        .navbar {{ position: sticky; top: 0; z-index: 100; background: rgba(255,255,255,0.95); backdrop-filter: blur(10px); border-bottom: 1px solid var(--border); padding: 16px 0; }}
        .nav-inner {{ display: flex; justify-content: space-between; align-items: center; }}
        .logo {{ font-family: 'Playfair Display', serif; font-size: 1.5rem; font-weight: 700; color: var(--accent); }}
        .nav-links {{ display: flex; gap: 32px; align-items: center; }}
        .nav-links a {{ font-weight: 500; font-size: 0.95rem; color: var(--text-secondary); }}
        .nav-links a:hover {{ color: var(--accent); }}
        .btn {{ display: inline-block; padding: 12px 24px; background: var(--accent); color: white; border-radius: var(--radius); font-weight: 600; text-align: center; cursor: pointer; border: none; transition: var(--transition); }}
        .btn:hover {{ background: var(--accent-hover); color: white; }}
        .btn-outline {{ background: transparent; color: var(--accent); border: 2px solid var(--accent); }}
        .btn-outline:hover {{ background: var(--accent); color: white; }}
        
        .hamburger {{ display: none; cursor: pointer; font-size: 1.5rem; }}
        .mobile-menu {{ display: none; position: absolute; top: 100%; left: 0; width: 100%; background: white; padding: 24px; border-bottom: 1px solid var(--border); box-shadow: var(--shadow-md); }}
        .mobile-menu.open {{ display: flex; flex-direction: column; gap: 16px; }}
        
        section {{ padding: 80px 0; }}
        .section-title {{ font-size: 2.5rem; margin-bottom: 16px; text-align: center; }}
        .section-desc {{ text-align: center; color: var(--text-secondary); max-width: 600px; margin: 0 auto 48px auto; }}
        .bg-alt {{ background: var(--bg-alt); }}
        
        .fade-in {{ opacity: 0; transform: translateY(20px); transition: opacity 0.8s ease, transform 0.8s ease; }}
        .fade-in.visible {{ opacity: 1; transform: translateY(0); }}
'''

    if template['layout'] == 'Layout 1':
        html += '''
        .hero { display: grid; grid-template-columns: 1fr 1fr; gap: 64px; align-items: center; padding: 120px 0; }
        .hero-content h1 { font-size: 3.5rem; line-height: 1.2; margin: 16px 0; }
        .hero-label { display: inline-block; padding: 8px 16px; background: var(--accent-light); color: var(--accent); font-weight: 600; border-radius: 20px; font-size: 0.85rem; text-transform: uppercase; letter-spacing: 1px; }
        .hero-stats { display: flex; gap: 24px; margin-top: 32px; padding-top: 32px; border-top: 1px solid var(--border); }
        .stat-item h4 { font-size: 1.5rem; color: var(--accent); font-family: 'Inter', sans-serif; font-weight: 700; }
        .stat-item p { font-size: 0.85rem; color: var(--text-secondary); }
        .hero-actions { margin-top: 32px; display: flex; gap: 16px; }
        '''
    elif template['layout'] == 'Layout 2':
        html += '''
        .page-wrapper { display: grid; grid-template-columns: 280px 1fr; gap: 48px; max-width: 1200px; margin: 0 auto; padding: 48px 24px; }
        .sidebar { position: sticky; top: 100px; height: calc(100vh - 100px); overflow-y: auto; padding-right: 24px; border-right: 1px solid var(--border); }
        .sidebar-profile { text-align: center; margin-bottom: 32px; }
        .sidebar-profile h2 { font-size: 1.8rem; margin: 16px 0 8px; }
        .sidebar-label { color: var(--accent); font-weight: 600; font-size: 0.9rem; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 24px; display: block; }
        .sidebar-stats { display: flex; flex-direction: column; gap: 16px; margin-top: 24px; border-top: 1px solid var(--border); padding-top: 24px; }
        .stat-item { display: flex; justify-content: space-between; align-items: center; }
        .stat-item h4 { font-size: 1.1rem; color: var(--accent); font-family: 'Inter', sans-serif; font-weight: 700; }
        .stat-item p { font-size: 0.85rem; color: var(--text-secondary); }
        .sidebar .btn { width: 100%; margin-top: 24px; }
        .hero { padding: 0 0 64px 0; }
        .hero h1 { font-size: 3.5rem; line-height: 1.2; margin-bottom: 24px; }
        .main-content section { padding: 64px 0; }
        .main-content .section-title { text-align: left; }
        .main-content .section-desc { text-align: left; margin-left: 0; }
        @media(max-width: 992px) { .page-wrapper { grid-template-columns: 1fr; } .sidebar { position: static; height: auto; border-right: none; border-bottom: 1px solid var(--border); padding-bottom: 32px; } }
        '''
    elif template['layout'] == 'Layout 3':
        html += '''
        .hero { display: grid; grid-template-columns: 7fr 5fr; gap: 48px; align-items: center; padding: 120px 0; }
        .hero-content h1 { font-size: 3.8rem; line-height: 1.1; margin: 16px 0; }
        .hero-label { display: inline-block; padding: 8px 16px; background: var(--accent-light); color: var(--accent); font-weight: 600; border-radius: 4px; font-size: 0.85rem; text-transform: uppercase; letter-spacing: 1px; }
        .hero-stats { display: grid; grid-template-columns: repeat(3, 1fr); gap: 16px; margin-top: 32px; }
        .stat-item { background: var(--bg-alt); padding: 16px; border-radius: var(--radius); text-align: center; }
        .stat-item h4 { font-size: 1.5rem; color: var(--accent); font-family: 'Inter', sans-serif; font-weight: 700; }
        .stat-item p { font-size: 0.85rem; color: var(--text-secondary); margin-top: 4px; }
        .hero-actions { margin-top: 32px; display: flex; gap: 16px; }
        .about-grid { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 32px; }
        '''
    elif template['layout'] == 'Layout 4':
        html += '''
        section { padding: 100px 0; }
        .bg-alt { background: transparent; }
        .hero { text-align: center; max-width: 800px; margin: 0 auto; padding: 140px 24px 80px; }
        .hero-label { display: inline-block; color: var(--accent); font-weight: 600; font-size: 0.9rem; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 24px; position: relative; }
        .hero-label::after { content: ''; display: block; width: 40px; height: 1px; background: var(--accent); margin: 8px auto 0; }
        .hero h1 { font-size: 4rem; line-height: 1.1; margin-bottom: 24px; font-weight: 400; }
        .hero-image-container { max-width: 800px; margin: 0 auto 64px auto; height: 400px; }
        .hero-stats { display: flex; justify-content: center; gap: 48px; margin-bottom: 48px; }
        .stat-item h4 { font-size: 1.5rem; color: var(--text-primary); font-family: 'Inter', sans-serif; font-weight: 300; }
        .stat-item p { font-size: 0.85rem; color: var(--text-secondary); text-transform: uppercase; letter-spacing: 1px; }
        .hero-actions { display: flex; justify-content: center; gap: 16px; }
        .card { border: none !important; box-shadow: none !important; border-bottom: 1px solid var(--border) !important; border-radius: 0 !important; padding: 32px 0 !important; }
        .card-icon { background: transparent !important; color: var(--accent); width: auto !important; height: auto !important; margin-bottom: 16px; }
        '''
    elif template['layout'] == 'Layout 5':
        html += '''
        .hero { position: relative; padding: 140px 0; overflow: hidden; }
        .hero-bg-text { position: absolute; top: 10%; left: -5%; font-size: 12vw; font-family: 'Playfair Display', serif; color: var(--accent-light); opacity: 0.5; white-space: nowrap; z-index: -1; pointer-events: none; font-weight: 700; }
        .hero-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 48px; align-items: center; }
        .hero h1 { font-size: 4.5rem; line-height: 1; margin: 16px 0 24px; }
        .hero-label { font-family: 'Inter', sans-serif; text-transform: uppercase; letter-spacing: 2px; font-size: 0.85rem; font-weight: 600; color: var(--accent); border-left: 2px solid var(--accent); padding-left: 12px; }
        .hero-stats { display: flex; gap: 32px; margin-top: 48px; }
        .stat-item { border-left: 1px solid var(--border); padding-left: 16px; }
        .stat-item h4 { font-size: 1.2rem; color: var(--text-primary); font-family: 'Inter', sans-serif; }
        .stat-item p { font-size: 0.85rem; color: var(--text-secondary); }
        .about-editorial { display: grid; grid-template-columns: 1fr 1fr; gap: 48px; }
        .about-editorial p:first-child::first-letter { font-family: 'Playfair Display', serif; font-size: 4rem; float: left; line-height: 0.8; padding-right: 8px; color: var(--accent); }
        .section-number { font-family: 'Playfair Display', serif; font-size: 2rem; color: var(--accent); opacity: 0.5; display: block; margin-bottom: 8px; }
        .services-list { border-top: 2px solid var(--text-primary); }
        .service-row { display: grid; grid-template-columns: 1fr 2fr auto; padding: 24px 0; border-bottom: 1px solid var(--border); align-items: center; }
        .service-row h3 { font-family: 'Inter', sans-serif; font-size: 1.2rem; margin: 0; }
        .testimonial-card { background: transparent !important; box-shadow: none !important; border: 1px solid var(--border); border-radius: 0 !important; }
        .pull-quote { font-family: 'Playfair Display', serif; font-size: 1.5rem; font-style: italic; color: var(--accent); margin-bottom: 16px; line-height: 1.4; }
        '''
    elif template['layout'] == 'Layout 6':
        html += '''
        .hero { display: grid; grid-template-columns: 1fr 1fr; gap: 64px; align-items: center; padding: 120px 0; }
        .hero-content h1 { font-size: 3.5rem; line-height: 1.2; margin: 16px 0; }
        .hero-label { display: inline-block; padding: 8px 16px; background: var(--accent-light); color: var(--accent); font-weight: 600; border-radius: 20px; font-size: 0.85rem; text-transform: uppercase; letter-spacing: 1px; }
        .hero-mini-timeline { display: flex; margin-top: 32px; border-top: 1px solid var(--border); padding-top: 32px; gap: 24px; }
        .stat-item { position: relative; padding-left: 16px; border-left: 2px solid var(--accent); }
        .stat-item h4 { font-size: 1.5rem; color: var(--text-primary); font-family: 'Inter', sans-serif; font-weight: 700; }
        .stat-item p { font-size: 0.85rem; color: var(--text-secondary); }
        .timeline-section { background: var(--bg-alt); padding: 120px 0; }
        .detailed-timeline { position: relative; max-width: 800px; margin: 0 auto; }
        .detailed-timeline::before { content: ''; position: absolute; top: 0; bottom: 0; left: 24px; width: 2px; background: var(--accent-light); }
        .dt-item { position: relative; padding-left: 64px; margin-bottom: 48px; }
        .dt-year { position: absolute; left: 0; top: 0; width: 48px; height: 48px; background: var(--accent); color: white; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: 700; font-size: 0.9rem; z-index: 2; }
        .dt-content { background: white; padding: 32px; border-radius: var(--radius-lg); box-shadow: var(--shadow-sm); }
        .dt-content h3 { font-size: 1.5rem; margin-bottom: 8px; }
        .dt-badge { display: inline-block; padding: 4px 12px; background: var(--accent-light); color: var(--accent); font-size: 0.8rem; font-weight: 600; border-radius: 12px; margin-bottom: 16px; }
        .services-simple-list { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; max-width: 800px; margin: 0 auto; }
        .services-simple-list li { display: flex; align-items: center; gap: 12px; padding: 16px; background: var(--bg-alt); border-radius: var(--radius); font-weight: 500; }
        .services-simple-list svg { color: var(--accent); }
        '''
    elif template['layout'] == 'Layout 7':
        html += '''
        .hero { position: relative; height: 90vh; min-height: 600px; display: flex; align-items: center; padding: 0; }
        .hero-bg { position: absolute; top: 0; right: 0; width: 50vw; height: 100%; background: var(--bg-alt); z-index: -1; }
        .hero-content { max-width: 600px; padding: 48px 0; }
        .hero-label { display: inline-block; padding: 8px 16px; background: var(--accent-light); color: var(--accent); font-weight: 600; border-radius: 20px; font-size: 0.85rem; text-transform: uppercase; letter-spacing: 1px; }
        .hero h1 { font-size: 4rem; line-height: 1.1; margin: 24px 0; }
        .hero-stats { display: flex; gap: 32px; margin-top: 48px; }
        .stat-item h4 { font-size: 1.8rem; color: var(--accent); font-family: 'Inter', sans-serif; font-weight: 700; }
        .stat-item p { font-size: 0.9rem; color: var(--text-secondary); text-transform: uppercase; letter-spacing: 1px; font-weight: 500; }
        .hero-actions { margin-top: 40px; display: flex; gap: 16px; }
        .hero-image-panel { position: absolute; top: 0; right: 0; width: 50vw; height: 100%; padding: 48px; display: flex; align-items: center; justify-content: center; }
        @media(max-width: 992px) { .hero { height: auto; display: block; padding-top: 80px; } .hero-bg, .hero-image-panel { position: static; width: 100%; height: 400px; } .hero-image-panel { padding: 24px; } }
        '''
    elif template['layout'] == 'Layout 8':
        html += '''
        .hero { display: flex; min-height: 100vh; padding: 0; }
        .hero-left { flex: 1; background: var(--accent); color: white; display: flex; align-items: center; justify-content: center; padding: 48px; }
        .hero-right { flex: 1; background: #f5f5f5; display: flex; align-items: center; justify-content: center; position: relative; }
        .hero-content-inner { max-width: 500px; }
        .hero h1 { color: white; font-size: 4rem; line-height: 1.1; margin: 16px 0 24px; }
        .hero-label { color: rgba(255,255,255,0.8); font-weight: 600; font-size: 0.9rem; text-transform: uppercase; letter-spacing: 2px; }
        .hero-desc { color: rgba(255,255,255,0.9); font-size: 1.1rem; margin-bottom: 40px; }
        .hero-stats { display: flex; gap: 32px; border-top: 1px solid rgba(255,255,255,0.2); padding-top: 32px; margin-bottom: 40px; }
        .stat-item h4 { font-size: 1.8rem; color: white; font-family: 'Inter', sans-serif; font-weight: 700; }
        .stat-item p { font-size: 0.85rem; color: rgba(255,255,255,0.8); }
        .btn-hero { background: white; color: var(--accent); padding: 16px 32px; display: inline-block; border-radius: var(--radius); font-weight: 600; transition: var(--transition); }
        .btn-hero:hover { background: rgba(255,255,255,0.9); transform: translateY(-2px); }
        .btn-outline-hero { background: transparent; color: white; border: 2px solid white; padding: 14px 32px; display: inline-block; border-radius: var(--radius); font-weight: 600; transition: var(--transition); }
        .btn-outline-hero:hover { background: white; color: var(--accent); }
        @media(max-width: 992px) { .hero { flex-direction: column; } .hero-left, .hero-right { min-height: 50vh; } }
        '''

    html += '''
        .grid-2 { display: grid; grid-template-columns: 1fr 1fr; gap: 32px; }
        .grid-3 { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 32px; }
        
        .card { background: white; padding: 32px; border-radius: var(--radius-lg); box-shadow: var(--shadow-sm); border: 1px solid var(--border); transition: var(--transition); height: 100%; }
        .card:hover { box-shadow: var(--shadow-md); transform: translateY(-5px); }
        .card-icon { width: 48px; height: 48px; border-radius: var(--radius); background: var(--accent-light); color: var(--accent); display: flex; align-items: center; justify-content: center; margin-bottom: 24px; }
        .card h3 { font-size: 1.25rem; margin-bottom: 12px; }
        .card p { color: var(--text-secondary); font-size: 0.95rem; }
        
        .timeline { position: relative; max-width: 800px; margin: 0 auto; padding-left: 32px; }
        .timeline::before { content: ''; position: absolute; left: 0; top: 0; bottom: 0; width: 2px; background: var(--border); }
        .timeline-item { position: relative; margin-bottom: 40px; }
        .timeline-item::before { content: ''; position: absolute; left: -37px; top: 4px; width: 12px; height: 12px; border-radius: 50%; background: var(--accent); border: 4px solid white; box-shadow: 0 0 0 1px var(--border); }
        .timeline-date { font-weight: 600; color: var(--accent); font-size: 0.9rem; margin-bottom: 8px; }
        .timeline-title { font-size: 1.2rem; margin-bottom: 4px; }
        .timeline-desc { color: var(--text-secondary); font-size: 0.95rem; }
        
        .testimonial-card { background: white; padding: 32px; border-radius: var(--radius-lg); box-shadow: var(--shadow-sm); border: 1px solid var(--border); }
        .stars { color: #f59e0b; margin-bottom: 16px; display: flex; gap: 4px; }
        .quote { font-style: italic; color: var(--text-secondary); margin-bottom: 24px; font-size: 1.05rem; }
        .patient { display: flex; align-items: center; gap: 16px; }
        .patient-avatar { width: 40px; height: 40px; border-radius: 50%; background: var(--accent-light); color: var(--accent); display: flex; align-items: center; justify-content: center; font-weight: 600; font-size: 0.9rem; }
        .patient-info h4 { font-size: 1rem; margin: 0; }
        
        .contact-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 48px; background: white; border-radius: var(--radius-lg); box-shadow: var(--shadow-md); overflow: hidden; }
        .contact-info { background: var(--accent); color: white; padding: 48px; }
        .contact-info h3 { color: white; font-size: 1.8rem; margin-bottom: 24px; }
        .info-item { display: flex; gap: 16px; margin-bottom: 24px; align-items: flex-start; }
        .info-item svg { width: 24px; height: 24px; opacity: 0.8; flex-shrink: 0; }
        .contact-form { padding: 48px; }
        .form-group { margin-bottom: 20px; }
        .form-label { display: block; font-weight: 500; margin-bottom: 8px; font-size: 0.9rem; }
        .form-control { width: 100%; padding: 12px 16px; border: 1px solid var(--border); border-radius: var(--radius); font-family: inherit; font-size: 1rem; transition: var(--transition); }
        .form-control:focus { outline: none; border-color: var(--accent); box-shadow: 0 0 0 3px var(--accent-light); }
        textarea.form-control { resize: vertical; min-height: 120px; }
        
        footer { background: #1a1a2e; color: white; padding: 64px 0 24px; text-align: center; }
        .footer-logo { font-family: 'Playfair Display', serif; font-size: 1.5rem; font-weight: 700; margin-bottom: 24px; color: white; }
        .footer-links { display: flex; justify-content: center; gap: 24px; margin-bottom: 32px; flex-wrap: wrap; }
        .footer-links a { color: #8a8a9b; }
        .footer-links a:hover { color: white; }
        .copyright { color: #5a5a6b; font-size: 0.9rem; border-top: 1px solid rgba(255,255,255,0.1); padding-top: 24px; }

        @media(max-width: 768px) {
            .nav-links, .navbar .btn { display: none; }
            .hamburger { display: block; }
            .grid-2, .grid-3, .contact-grid, .about-grid, .about-editorial { grid-template-columns: 1fr; }
            .hero { padding: 64px 0; }
            .hero-stats { flex-wrap: wrap; }
            section { padding: 60px 0; }
            .hero-content h1 { font-size: 2.5rem; }
        }
    </style>
</head>
<body>

    <!-- Navbar -->
    <nav class="navbar">
        <div class="container nav-inner">
            <a href="#" class="logo">{template['doctor'].split(',')[0]}</a>
            <div class="nav-links">
                <a href="#about">About</a>
                <a href="#services">Specialties</a>
                <a href="#experience">Experience</a>
                <a href="#reviews">Reviews</a>
                <a href="#contact">Contact</a>
            </div>
            <a href="#contact" class="btn">Book Appointment</a>
            <div class="hamburger" onclick="toggleMenu()">☰</div>
        </div>
        <div class="mobile-menu" id="mobileMenu">
            <a href="#about">About</a>
            <a href="#services">Specialties</a>
            <a href="#experience">Experience</a>
            <a href="#reviews">Reviews</a>
            <a href="#contact">Contact</a>
            <a href="#contact" class="btn">Book Appointment</a>
        </div>
    </nav>

'''
    
    # SVG Placeholder string
    svg_placeholder = f'''
        <div style="width:100%;height:100%;display:flex;align-items:center;justify-content:center;background:var(--bg-alt);border-radius:var(--radius-lg);position:relative;overflow:hidden;">
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
'''

    if template['layout'] == 'Layout 2':
        html += f'''
    <div class="page-wrapper">
        <aside class="sidebar">
            <div class="sidebar-profile">
                <div style="width:200px;height:240px;margin:0 auto;">
                    {svg_placeholder}
                </div>
                <h2>{template['doctor'].split(',')[0]}</h2>
                <p>{template['doctor'].split(',')[1] if len(template['doctor'].split(','))>1 else ''}</p>
            </div>
            <span class="sidebar-label">{template['specialty']}</span>
            <p>Board-certified specialist providing advanced care in {template['city']}.</p>
            <div class="sidebar-stats">
                <div class="stat-item"><h4>{template['stats'][0].split()[0]}</h4><p>Experience</p></div>
                <div class="stat-item"><h4>{template['stats'][1].split()[0]}</h4><p>Cases</p></div>
                <div class="stat-item"><h4>{template['stats'][2]}</h4><p>Satisfaction</p></div>
            </div>
            <a href="#contact" class="btn">Book Now</a>
        </aside>
        <main class="main-content">
            <section id="about" class="hero fade-in">
                <h1>Advanced {template['specialty']} Care in {template['city']}</h1>
                <p class="hero-desc">Dedicated to providing state-of-the-art treatment and compassionate care. I specialize in complex cases and innovative therapeutic approaches.</p>
                <div class="hero-actions">
                    <a href="#contact" class="btn">Schedule Consultation</a>
                    <a href="#services" class="btn btn-outline">View Services</a>
                </div>
            </section>
'''
    elif template['layout'] == 'Layout 8':
        html += f'''
    <header class="hero fade-in">
        <div class="hero-left">
            <div class="hero-content-inner">
                <span class="hero-label">{template['specialty']}</span>
                <h1>{template['doctor'].split(',')[0]}</h1>
                <p class="hero-desc">Providing expert care in {template['city']} with a focus on advanced treatments and patient-centered recovery plans.</p>
                <div class="hero-stats">
                    <div class="stat-item"><h4>{template['stats'][0].split()[0]}</h4><p>Years</p></div>
                    <div class="stat-item"><h4>{template['stats'][1].split()[0]}</h4><p>Patients</p></div>
                    <div class="stat-item"><h4>{template['stats'][2]}</h4><p>Rating</p></div>
                </div>
                <div>
                    <a href="#contact" class="btn-hero">Book Appointment</a>
                    <a href="#about" class="btn-outline-hero" style="margin-left:16px;">Learn More</a>
                </div>
            </div>
        </div>
        <div class="hero-right">
            <div style="width:70%; height:70%; max-width:400px; max-height:500px;">
                {svg_placeholder}
            </div>
        </div>
    </header>
'''
    elif template['layout'] == 'Layout 7':
        html += f'''
    <header class="hero fade-in">
        <div class="hero-bg"></div>
        <div class="container" style="position:relative; width:100%;">
            <div class="hero-content">
                <span class="hero-label">{template['specialty']}</span>
                <h1>{template['doctor']}</h1>
                <p style="font-size: 1.1rem; color: var(--text-secondary); margin-bottom: 24px;">Specialized care in {template['city']} focused on restoring function and improving quality of life through advanced medical techniques.</p>
                <div class="hero-stats">
                    <div class="stat-item"><h4>{template['stats'][0].split()[0]}</h4><p>Experience</p></div>
                    <div class="stat-item"><h4>{template['stats'][1].split()[0]}</h4><p>Procedures</p></div>
                </div>
                <div class="hero-actions">
                    <a href="#contact" class="btn">Consultation</a>
                    <a href="#services" class="btn btn-outline">Our Services</a>
                </div>
            </div>
            <div class="hero-image-panel">
                <div style="width:100%; height:100%; max-width:400px; max-height:500px;">
                    {svg_placeholder}
                </div>
            </div>
        </div>
    </header>
'''
    else:
        hero_class = "hero container fade-in"
        if template['layout'] == 'Layout 5':
            hero_class = "hero container fade-in"
            
        html += f'''
    <header class="{hero_class}">
'''
        if template['layout'] == 'Layout 5':
            html += f'''<div class="hero-bg-text">{template['specialty'].split()[0].upper()}</div>'''
        
        if template['layout'] in ['Layout 4', 'Layout 5']:
            if template['layout'] == 'Layout 4':
                html += f'''
        <span class="hero-label">{template['specialty']}</span>
        <h1>{template['doctor']}</h1>
        <p style="font-size:1.1rem; color:var(--text-secondary); margin-bottom:32px;">Expert {template['specialty'].lower()} care in {template['city']}.</p>
        <div class="hero-stats">
            <div class="stat-item"><h4>{template['stats'][0].split()[0]}</h4><p>Years</p></div>
            <div class="stat-item"><h4>{template['stats'][1].split()[0]}</h4><p>Patients</p></div>
        </div>
        <div class="hero-actions" style="margin-bottom:64px;">
            <a href="#contact" class="btn">Book Appointment</a>
        </div>
        <div class="hero-image-container">{svg_placeholder}</div>
'''
            else: # Layout 5
                html += f'''
        <div class="hero-grid">
            <div class="hero-content">
                <span class="hero-label">{template['specialty']}</span>
                <h1>{template['doctor']}</h1>
                <p>Leading specialist in {template['city']}, dedicated to comprehensive diagnosis and state-of-the-art treatment plans.</p>
                <div class="hero-stats">
                    <div class="stat-item"><h4>{template['stats'][0].split()[0]}</h4><p>Years Experience</p></div>
                    <div class="stat-item"><h4>{template['stats'][1].split()[0]}</h4><p>Patients Treated</p></div>
                </div>
                <div class="hero-actions" style="margin-top:32px;">
                    <a href="#contact" class="btn">Book Appointment</a>
                </div>
            </div>
            <div style="height: 500px;">{svg_placeholder}</div>
        </div>
'''
        else:
            html += f'''
        <div class="hero-content">
            <span class="hero-label">{template['specialty']}</span>
            <h1>{template['doctor'].split(',')[0]}</h1>
            <p style="font-size: 1.1rem; color: var(--text-secondary);">{template['doctor']} is a board-certified {template['specialty'].lower()} in {template['city']}, committed to providing the highest standard of personalized medical care.</p>
'''
            if template['layout'] == 'Layout 6':
                html += f'''
            <div class="hero-mini-timeline">
                <div class="stat-item"><h4>{template['stats'][0].split()[0]}</h4><p>Experience</p></div>
                <div class="stat-item"><h4>{template['stats'][1].split()[0]}</h4><p>Patients</p></div>
                <div class="stat-item"><h4>{template['stats'][2]}</h4><p>Rating</p></div>
            </div>
'''
            else:
                html += f'''
            <div class="hero-stats">
                <div class="stat-item"><h4>{template['stats'][0].split()[0]}</h4><p>Experience</p></div>
                <div class="stat-item"><h4>{template['stats'][1].split()[0]}</h4><p>Patients</p></div>
                <div class="stat-item"><h4>{template['stats'][2]}</h4><p>Rating</p></div>
            </div>
'''
            html += f'''
            <div class="hero-actions">
                <a href="#contact" class="btn">Schedule Visit</a>
                <a href="#services" class="btn btn-outline">Services</a>
            </div>
        </div>
        <div style="height: 100%; min-height: 400px; border-radius: var(--radius-lg); overflow: hidden;">
            {svg_placeholder}
        </div>
'''
        html += '''
    </header>
'''

    if template['layout'] != 'Layout 2':
        html += '''<main>'''

    # About Section
    if template['layout'] == 'Layout 2':
        html += f'''
            <section id="about" class="fade-in">
                <h2 class="section-title">Credentials & Education</h2>
                <div class="grid-2">
'''
    elif template['layout'] == 'Layout 3':
        html += f'''
        <section id="about" class="container fade-in">
            <h2 class="section-title">About the Doctor</h2>
            <div class="about-grid">
                <div>{svg_placeholder}</div>
                <div>
                    <h3>Biography</h3>
                    <p>{template['doctor'].split(',')[0]} is a dedicated {template['specialty'].lower()} serving the {template['city']} community. With years of rigorous training and clinical practice, they emphasize evidence-based treatments tailored to each patient's unique needs.</p>
                </div>
                <div>
                    <h3>Credentials</h3>
                    <ul style="margin-top:16px; display:flex; flex-direction:column; gap:16px;">
'''
    elif template['layout'] == 'Layout 5':
        html += f'''
        <section id="about" class="container fade-in">
            <div class="about-editorial">
                <div>
                    <span class="section-number">01</span>
                    <h2 class="section-title" style="text-align:left; margin-bottom:24px;">Philosophy of Care</h2>
                    <p>{template['doctor'].split(',')[0]} believes in a holistic approach to {template['specialty'].lower()}. Every patient deserves a comprehensive evaluation and a customized treatment plan that addresses not just symptoms, but root causes.</p>
                </div>
                <div>
                    <h3 style="margin-bottom:16px; font-family:'Inter',sans-serif;">Education & Training</h3>
'''
    else:
        html += f'''
        <section id="about" class="container fade-in">
            <h2 class="section-title">About {template['doctor'].split(',')[0]}</h2>
            <p class="section-desc">Committed to excellence in {template['specialty'].lower()} through advanced clinical practice and compassionate patient care.</p>
            <div class="grid-3">
'''
    
    icons = ['<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 10v6M2 10l10-5 10 5-10 5z"/><path d="M6 12v5c3 3 9 3 12 0v-5"/></svg>',
             '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></svg>',
             '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="8" r="7"/><polyline points="8.21 13.89 7 23 12 20 17 23 15.79 13.88"/></svg>']
    
    if template['layout'] in ['Layout 2', 'Layout 1', 'Layout 4', 'Layout 6', 'Layout 7', 'Layout 8']:
        for i, edu in enumerate(template['education']):
            html += f'''
                <div class="card">
                    <div class="card-icon">{icons[i%3]}</div>
                    <h3>{edu.split(' (')[0]}</h3>
                    <p>{'(' + edu.split(' (')[1] if ' (' in edu else edu}</p>
                </div>
'''
        html += '''
            </div>
        </section>
'''
    elif template['layout'] == 'Layout 3':
        for i, edu in enumerate(template['education']):
            html += f'''
                        <li style="display:flex; gap:12px; align-items:flex-start;">
                            <div style="width:24px; color:var(--accent);">{icons[i%3]}</div>
                            <div><strong>{edu.split(' (')[0]}</strong><br><span style="color:var(--text-secondary);font-size:0.9rem;">{'(' + edu.split(' (')[1] if ' (' in edu else edu}</span></div>
                        </li>
'''
        html += '''
                    </ul>
                </div>
            </div>
        </section>
'''
    elif template['layout'] == 'Layout 5':
        for i, edu in enumerate(template['education']):
            html += f'''
                    <div style="margin-bottom:24px; padding-bottom:24px; border-bottom:1px solid var(--border);">
                        <h4 style="font-size:1.1rem; margin-bottom:4px;">{edu.split(' (')[0]}</h4>
                        <p style="color:var(--text-secondary);">{'(' + edu.split(' (')[1] if ' (' in edu else edu}</p>
                    </div>
'''
        html += '''
                </div>
            </div>
        </section>
'''

    # Services Section
    bg_class = "bg-alt" if template['layout'] not in ['Layout 4', 'Layout 5'] else ""
    html += f'''
        <section id="services" class="{bg_class} fade-in">
            <div class="container">
'''
    if template['layout'] == 'Layout 5':
        html += f'''
                <span class="section-number">02</span>
                <h2 class="section-title" style="text-align:left;">Clinical Specialties</h2>
                <div class="services-list" style="margin-top:48px;">
'''
        for srv in template['services']:
            html += f'''
                    <div class="service-row">
                        <div style="color:var(--accent); width:32px;">{icons[0]}</div>
                        <h3>{srv}</h3>
                        <a href="#contact" style="color:var(--text-secondary); text-transform:uppercase; font-size:0.8rem; font-weight:600; letter-spacing:1px;">Inquire &rarr;</a>
                    </div>
'''
        html += '''
                </div>
'''
    elif template['layout'] == 'Layout 6':
        html += f'''
                <h2 class="section-title">Areas of Expertise</h2>
                <p class="section-desc">Comprehensive {template['specialty'].lower()} services utilizing the latest advancements in medical technology.</p>
                <ul class="services-simple-list">
'''
        for srv in template['services']:
            html += f'''
                    <li>
                        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline></svg>
                        {srv}
                    </li>
'''
        html += '''
                </ul>
'''
    else:
        html += f'''
                <h2 class="section-title">Specialized Services</h2>
                <p class="section-desc">Comprehensive {template['specialty'].lower()} care providing tailored solutions for optimal patient outcomes.</p>
                <div class="grid-3">
'''
        for srv in template['services']:
            html += f'''
                    <div class="card">
                        <div class="card-icon">
                            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 12h-4l-3 9L9 3l-3 9H2"/></svg>
                        </div>
                        <h3>{srv}</h3>
                        <p>Advanced diagnostic and therapeutic options to ensure the highest standard of care and recovery.</p>
                    </div>
'''
        html += '''
                </div>
'''
    html += '''
            </div>
        </section>
'''

    # Timeline Section
    if template['layout'] == 'Layout 6':
        html += f'''
        <section id="experience" class="timeline-section fade-in">
            <div class="container">
                <h2 class="section-title" style="margin-bottom:64px;">Professional Journey</h2>
                <div class="detailed-timeline">
                    <div class="dt-item">
                        <div class="dt-year">2023</div>
                        <div class="dt-content">
                            <span class="dt-badge">Current Role</span>
                            <h3>Lead {template['specialty']}</h3>
                            <p>Directing clinical care, overseeing complex cases, and introducing innovative protocols for patient management at top medical centers in {template['city']}.</p>
                        </div>
                    </div>
                    <div class="dt-item">
                        <div class="dt-year">2018</div>
                        <div class="dt-content">
                            <span class="dt-badge">Attending Staff</span>
                            <h3>Senior Specialist</h3>
                            <p>Managed a high-volume outpatient clinic and performed advanced procedures, mentoring residents and contributing to departmental research.</p>
                        </div>
                    </div>
                    <div class="dt-item">
                        <div class="dt-year">2014</div>
                        <div class="dt-content">
                            <span class="dt-badge">Specialization</span>
                            <h3>Fellowship Training</h3>
                            <p>Completed intensive subspecialty training focusing on advanced diagnostic modalities and cutting-edge therapeutic interventions.</p>
                        </div>
                    </div>
                    <div class="dt-item">
                        <div class="dt-year">2010</div>
                        <div class="dt-content">
                            <span class="dt-badge">Residency</span>
                            <h3>Chief Resident</h3>
                            <p>Led the residency program, organizing educational schedules, and providing direct supervision in both inpatient and outpatient settings.</p>
                        </div>
                    </div>
                </div>
            </div>
        </section>
'''
    else:
        bg_timeline = "" if template['layout'] in ['Layout 4', 'Layout 5'] else ("bg-alt" if template['layout'] in ['Layout 2', 'Layout 8', 'Layout 7'] else "")
        if template['layout'] in ['Layout 1', 'Layout 2', 'Layout 3', 'Layout 7', 'Layout 8']:
            bg_timeline = ""
            
        html += f'''
        <section id="experience" class="container {bg_timeline} fade-in">
'''
        if template['layout'] == 'Layout 5':
            html += '''<span class="section-number">03</span><h2 class="section-title" style="text-align:left;">Career Milestones</h2>'''
        else:
            html += '''<h2 class="section-title">Career Milestones</h2><p class="section-desc">A track record of clinical excellence and leadership.</p>'''

        html += f'''
            <div class="timeline" style="margin-top:48px;">
                <div class="timeline-item">
                    <div class="timeline-date">Present</div>
                    <h3 class="timeline-title">Lead {template['specialty']}</h3>
                    <p class="timeline-desc">Providing expert consultations and leading advanced treatment protocols in {template['city']}.</p>
                </div>
                <div class="timeline-item">
                    <div class="timeline-date">2015 – 2021</div>
                    <h3 class="timeline-title">Attending Physician</h3>
                    <p class="timeline-desc">Specialized in complex cases, utilizing state-of-the-art diagnostic and therapeutic techniques.</p>
                </div>
                <div class="timeline-item">
                    <div class="timeline-date">2012 – 2015</div>
                    <h3 class="timeline-title">Fellowship & Advanced Training</h3>
                    <p class="timeline-desc">Completed rigorous subspecialty fellowship focusing on advanced clinical methodologies.</p>
                </div>
                <div class="timeline-item">
                    <div class="timeline-date">2008 – 2012</div>
                    <h3 class="timeline-title">Residency Program</h3>
                    <p class="timeline-desc">Extensive clinical training and patient management across various hospital departments.</p>
                </div>
            </div>
        </section>
'''

    # Testimonials
    bg_test = "bg-alt" if template['layout'] not in ['Layout 4', 'Layout 5', 'Layout 6'] else ""
    if template['layout'] in ['Layout 1', 'Layout 2', 'Layout 3', 'Layout 7', 'Layout 8']:
        bg_test = "bg-alt"
        
    html += f'''
        <section id="reviews" class="{bg_test} fade-in">
            <div class="container">
'''
    if template['layout'] == 'Layout 5':
        html += '''<span class="section-number">04</span><h2 class="section-title" style="text-align:left;">Patient Stories</h2>'''
    else:
        html += '''<h2 class="section-title">Patient Reviews</h2><p class="section-desc">Read what patients have to say about their experience and quality of care.</p>'''

    html += f'''
                <div class="grid-3" style="margin-top:48px;">
                    <div class="testimonial-card">
                        <div class="stars">{'<svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor" stroke="none"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>' * 5}</div>
'''
    if template['layout'] == 'Layout 5':
         html += '''<p class="pull-quote">"Exceptional care and attention to detail. The treatment plan was thoroughly explained."</p>'''
    else:
         html += '''<p class="quote">"Exceptional care and attention to detail. The treatment plan was thoroughly explained, and the results have been life-changing. Highly recommend to anyone seeking expert care."</p>'''
    html += '''
                        <div class="patient">
                            <div class="patient-avatar">MJ</div>
                            <div class="patient-info"><h4>M. Johnson</h4><p style="font-size:0.85rem;color:var(--text-secondary);">Verified Patient</p></div>
                        </div>
                    </div>
                    <div class="testimonial-card">
                        <div class="stars">{'<svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor" stroke="none"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>' * 5}</div>
'''
    if template['layout'] == 'Layout 5':
         html += '''<p class="pull-quote">"A truly compassionate professional who takes the time to listen and provide the best solutions."</p>'''
    else:
         html += '''<p class="quote">"A truly compassionate professional who takes the time to listen and provide the best solutions. The entire clinic staff is welcoming and efficient."</p>'''
    html += '''
                        <div class="patient">
                            <div class="patient-avatar">SR</div>
                            <div class="patient-info"><h4>S. Roberts</h4><p style="font-size:0.85rem;color:var(--text-secondary);">Verified Patient</p></div>
                        </div>
                    </div>
                    <div class="testimonial-card">
                        <div class="stars">{'<svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor" stroke="none"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>' * 5}</div>
'''
    if template['layout'] == 'Layout 5':
         html += '''<p class="pull-quote">"Outstanding expertise. I felt completely confident in the diagnosis and surgical outcome."</p>'''
    else:
         html += '''<p class="quote">"Outstanding expertise. I felt completely confident in the diagnosis and surgical outcome. Recovery was smooth thanks to their excellent post-op care."</p>'''
    html += '''
                        <div class="patient">
                            <div class="patient-avatar">DL</div>
                            <div class="patient-info"><h4>D. Lee</h4><p style="font-size:0.85rem;color:var(--text-secondary);">Verified Patient</p></div>
                        </div>
                    </div>
                </div>
            </div>
        </section>
'''

    # Contact Section
    html += f'''
        <section id="contact" class="container fade-in">
'''
    if template['layout'] == 'Layout 5':
         html += '''<span class="section-number">05</span><h2 class="section-title" style="text-align:left; margin-bottom:48px;">Request a Consultation</h2>'''
    else:
         html += '''<h2 class="section-title">Request a Consultation</h2><p class="section-desc">Take the first step towards better health. Contact our office to schedule an appointment.</p>'''
    
    html += f'''
            <div class="contact-grid">
                <div class="contact-info">
                    <h3>Contact Information</h3>
                    <div class="info-item">
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path><circle cx="12" cy="10" r="3"></circle></svg>
                        <div>
                            <strong style="display:block; margin-bottom:4px;">Clinic Location</strong>
                            <p style="color:rgba(255,255,255,0.8);">{template['city']} Medical Center<br>Suite 400</p>
                        </div>
                    </div>
                    <div class="info-item">
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path></svg>
                        <div>
                            <strong style="display:block; margin-bottom:4px;">Phone</strong>
                            <p style="color:rgba(255,255,255,0.8);">{template['phone']}</p>
                        </div>
                    </div>
                    <div class="info-item">
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>
                        <div>
                            <strong style="display:block; margin-bottom:4px;">Office Hours</strong>
                            <p style="color:rgba(255,255,255,0.8);">Monday - Friday: 9:00 AM - 5:00 PM<br>Saturday - Sunday: Closed</p>
                        </div>
                    </div>
                </div>
                <div class="contact-form">
                    <form onsubmit="return handleSubmit(event)">
                        <div class="grid-2" style="gap:16px;">
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
                                <option value="">Select a reason...</option>
                                <option value="consultation">New Patient Consultation</option>
                                <option value="followup">Follow-up Appointment</option>
                                <option value="second_opinion">Second Opinion</option>
                                <option value="other">Other</option>
                            </select>
                        </div>
                        <div class="form-group">
                            <label class="form-label">Additional Notes</label>
                            <textarea class="form-control"></textarea>
                        </div>
                        <button type="submit" class="btn" style="width:100%;">Send Request</button>
                    </form>
                </div>
            </div>
        </section>
'''

    if template['layout'] != 'Layout 2':
        html += '''</main>'''
    else:
        html += '''
        </main>
    </div>
'''

    # Footer
    html += f'''
    <footer>
        <div class="container">
            <div class="footer-logo">{template['doctor'].split(',')[0]}</div>
            <div class="footer-links">
                <a href="#about">About</a>
                <a href="#services">Specialties</a>
                <a href="#experience">Experience</a>
                <a href="#reviews">Reviews</a>
                <a href="#contact">Contact</a>
            </div>
            <div class="copyright">
                &copy; 2024 {template['doctor'].split(',')[0]}. All rights reserved. | {template['specialty']} in {template['city']}.
            </div>
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
</html>
'''

    with open(f"d:/website/doctors portfolio/templates/{template['filename']}", "w", encoding="utf-8") as f:
        f.write(html)

print("Starting generation...")
os.makedirs("d:/website/doctors portfolio/templates", exist_ok=True)
for t in templates:
    print(f"Generating {t['filename']}...")
    generate_html(t)
print("All templates generated successfully!")
