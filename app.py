from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Evidence-Based Medical Textbook Records Dictionary Database Array
MEDICAL_DATABASE = {
    "fever": {
        "info": "Clinical guidelines define acute pyrexia (fever) as an immune-mediated rise in body temperature (>38.0C). Fluid tracking is highly recommended.",
        "cause": "Commonly triggered by viral upper respiratory infections or acute seasonal bacterial pathogens.",
        "precautions": "Maintain strict hand hygiene, sanitize high-touch objects, and ensure optimal room ventilation."
    },
    "sore throat": {
        "info": "Medical literature shows that acute pharyngitis (sore throat) is predominantly viral. Centor scoring mechanisms guide diagnostic workflows.",
        "cause": "Most frequently driven by airborne respiratory viruses or highly contagious bacterial strains spread via droplets.",
        "precautions": "Avoid sharing cups or utensils, replace oral hygiene instruments post-recovery, and practice warm saline gargles."
    },
    "cough": {
        "info": "Standard respiratory guidelines classify acute coughs as protective biological mechanisms to clear secretions from the airway.",
        "cause": "Typically driven by post-nasal drip from viral rhinosinusitis or transient bronchial hyperresponsiveness.",
        "precautions": "Cover mouth when coughing using a flexed elbow and eliminate exposure to environmental smoke or dust."
    },
    "tongue changes": {
        "info": "Oral medicine manuals note that a temporary dark tongue coating combined with an altered sense of taste represents a benign elongation of filiform papillae.",
        "cause": "Frequently induced by acute dehydration during febrile states or chemical reactions from over-the-counter bismuth stomach medications.",
        "precautions": "Incorporate gentle tongue scraping twice daily and significantly escalate plain water consumption to counter dehydration."
    },
    "stomach issues": {
        "info": "Gastrointestinal diagnostic protocols note that acute vomiting is a coordinated autonomic reflex. The absolute priority is correcting fluid deficits.",
        "cause": "Most commonly driven by norovirus or rotavirus strains, or ingestion of pre-formed bacterial enterotoxins in food.",
        "precautions": "Enforce strict temporary bowel rest following an episode and transition gradually to small, frequent sips of rehydration solutions (ORS)."
    }
}

@app.route('/run-triage', methods=['POST'])
def execute_triage_calculations():
    data = request.json
    name = data.get('name', '')
    age = data.get('age', '')
    gender = data.get('gender', '')
    tier = data.get('tier', '')
    checklist_symptoms = data.get('symptoms', '').lower()
    typed_details = data.get('extraDetails', '').lower()
    has_image = data.get('hasImage', False)

    combined_symptoms = f"{checklist_symptoms} {typed_details}"
    matched_sections = []
    
    image_status = "⚠️ NO VISUAL TELEMETRY ATTACHED" if not has_image else "✅ HIGH-RESOLUTION VISUAL EVIDENCE VAULTED IN PROTOTYPE BUFFER"
    
    if "throat" in combined_symptoms or "swallow" in combined_symptoms:
        matched_sections.append(("ACUTE PHARYNGITIS CORE", MEDICAL_DATABASE["sore throat"]))
    if "fever" in combined_symptoms or "temperature" in combined_symptoms or "hot" in combined_symptoms:
        matched_sections.append(("SYSTEMIC PYREXIA SCANNER", MEDICAL_DATABASE["fever"]))
    if "cough" in combined_symptoms or "cold" in combined_symptoms or "breath" in combined_symptoms:
        matched_sections.append(("RESPIRATORY SEGMENT ARCHIVE", MEDICAL_DATABASE["cough"]))
    if "tongue" in combined_symptoms or "taste" in combined_symptoms:
        matched_sections.append(("ORAL & GUSTATORY TELEMETRY", MEDICAL_DATABASE["tongue changes"]))
    if "vomit" in combined_symptoms or "stomach" in combined_symptoms or "nausea" in combined_symptoms:
        matched_sections.append(("GASTROINTESTINAL ANALYSIS", MEDICAL_DATABASE["stomach issues"]))

    base_cost = 45.00 if tier == "Standard Virtual Triage Simulation" else 95.00
    imaging_fee = 25.00 if has_image else 0.00
    subtotal = base_cost + imaging_fee
    tax_factor = 0.08
    calculated_tax = subtotal * tax_factor
    final_accounting_total = subtotal + calculated_tax

    if not matched_sections:
        unmapped_log = f"[NEXUS ENGINE - V7.5 PROTOTYPE CLOUD]\n-----------------------------------------------------\nPatient ID: {name.upper()} | Age: {str(age)}\nSYSTEM STATUS: Telemetry unmapped. Consult a licensed physician."
        return jsonify({"output": unmapped_log})

    compiled_output = f"[NEXUS ENGINE - CORE PROTOCOL RUNTIME V7.5 CLOUD PROTOTYPE]\nNOTICE: NON-CLINICAL SIMULATION RUNTIME | MOCK DATA ONLY\n-----------------------------------------------------\nPatient Profile Reference: {name.upper()}\nAge Telemetry Group: {str(age)} Years Old\nGender Code Classification: {gender.upper()}\nVisual Vault Record: {image_status}\n"
    
    for title, segment in matched_sections:
        compiled_output += f"\n📋 CLASSIFICATION CORE: [{title}]\n🤖 EDUCATIONAL SUMMARY: {segment['info']}\n🔍 IDENTIFIED ROOT CAUSE: {segment['cause']}\n🛡️ POST-RECOVERY PRECAUTIONS: {segment['precautions']}\n"
        
    compiled_output += f"\n=====================================================\n🧾 SIMULATED PROTOTYPE ACCOUNTING INVOICE TRANSACTION RECEIPT\n=====================================================\nFinal Prototype Value: ${final_accounting_total:.2f}\nSTATUS: DEMO CLOUD TRANSACTION COMPLETE\nVALIDATION STAMP KEY: PROTO-V7.5-CLOUD-DEMO\n=====================================================\n\nDISCLAIMER: Educational Simulation sandbox. Not real medical advice. Consult a doctor."
    
    return jsonify({"output": compiled_output})

if __name__ == '__main__':
    # Force Flask to dynamic environment porting for free cloud clusters
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
