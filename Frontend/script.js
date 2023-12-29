document.addEventListener('DOMContentLoaded', function () {
    const selectedSymptoms = [];
    const symptomDropdown = document.getElementById('symptomDropdown');
    const symptomSearch = document.getElementById('symptomSearch');
    const selectedSymptomsContainer = document.getElementById('selectedSymptoms');

    window.filterSymptoms = function () {
        const searchTerm = symptomSearch.value.toLowerCase();
        const symptoms = document.querySelectorAll('#symptomDropdown option');

        symptoms.forEach(symptom => {
            const symptomText = symptom.text.toLowerCase();
            const isSelected = selectedSymptoms.includes(symptomText);

            if (symptomText.includes(searchTerm) && !isSelected) {
                symptom.style.display = 'block';
            } else {
                symptom.style.display = 'none';
            }
        });

        submitButton.style.display = selectedSymptoms.length > 0 ? 'block' : 'none';
    }

    let allSymptoms = [
        "abdominal_pain", "abnormal_menstruation", "acidity", "acute_liver_failure", "altered_sensorium", "anxiety", "back_pain", "belly_pain", "blackheads", "bladder_discomfort", "blister", "blood_in_sputum", "bloody_stool", "blurred_and_distorted_vision", "breathlessness", "brittle_nails", "bruising", "burning_micturition", "chest_pain", "chills", "cold_hands_and_feets", "coma", "congestion", "constipation", "continuous_feel_of_urine", "continuous_sneezing", "cough", "cramps", "dark_urine", "dehydration", "depression", "diarrhoea", "dischromic_patches", "distention_of_abdomen", "dizziness", "drying_and_tingling_lips", "enlarged_thyroid", "excessive_hunger", "extra_marital_contacts", "family_history", "fast_heart_rate", "fatigue", "fluid_overload", "foul_smell_of_urine", "headache", "high_fever", "hip_joint_pain", "history_of_alcohol_consumption", "increased_appetite", "indigestion", "inflammatory_nails", "internal_itching", "irregular_sugar_level", "irritability", "irritation_in_anus", "joint_pain", "knee_pain", "lack_of_concentration", "lethargy", "loss_of_appetite", "loss_of_balance", "loss_of_smell", "malaise", "mild_fever", "mood_swings", "movement_stiffness", "mucoid_sputum", "muscle_pain", "muscle_wasting", "muscle_weakness", "nausea", "neck_pain", "nodal_skin_eruptions", "obesity", "pain_behind_the_eyes", "pain_during_bowel_movements", "pain_in_anal_region", "painful_walking", "palpitations", "passage_of_gases", "patches_in_throat", "phlegm", "polyuria", "prominent_veins_on_calf", "puffy_face_and_eyes", "pus_filled_pimples", "receiving_blood_transfusion", "receiving_unsterile_injections", "red_sore_around_nose", "red_spots_over_body", "redness_of_eyes", "restlessness", "runny_nose", "rusty_sputum", "scurring", "shivering", "silver_like_dusting", "sinus_pressure", "skin_peeling", "skin_rash", "slurred_speech", "small_dents_in_nails", "spinning_movements", "spotting_urination", "stiff_neck", "stomach_bleeding", "stomach_pain", "sunken_eyes", "sweating", "swelled_lymph_nodes", "swelling_joints", "swelling_of_stomach", "swollen_blood_vessels", "swollen_extremities", "swollen_legs", "throat_irritation", "toxic_look_(typhos)", "ulcers_on_tongue", "unsteadiness", "visual_disturbances", "vomiting", "watering_from_eyes", "weakness_in_limbs", "weakness_of_one_body_side", "weight_gain", "weight_loss", "yellow_crust_ooze", "yellow_urine", "yellowing_of_eyes", "yellowish_skin", "itching"
    ];

    allSymptoms.forEach(symptom => {
        const option = document.createElement('option');
        option.text = symptom;
        option.classList.add('symptom-option');
        symptomDropdown.add(option);
    });

    symptomDropdown.addEventListener('mouseover', function (event) {
        if (event.target.classList.contains('symptom-option')) {
            event.target.style.fontWeight = 'bold';
            event.target.style.cursor = 'pointer';
        }
    });

    symptomDropdown.addEventListener('mouseout', function (event) {
        if (event.target.classList.contains('symptom-option')) {
            event.target.style.fontWeight = 'normal';
        }
    });

    symptomDropdown.addEventListener('click', function (event) {
        if (event.target.classList.contains('symptom-option')) {
            const selectedSymptom = event.target.text;
            allSymptoms.splice(allSymptoms.indexOf(selectedSymptom), 1);
            if (!selectedSymptoms.includes(selectedSymptom)) {
                selectedSymptoms.push(selectedSymptom);
                updateSelectedSymptoms();
                event.target.style.display = 'none';
                filterSymptoms(); // Update the displayed symptoms after selecting one
            }
        }
    });

    function updateSelectedSymptoms() {
        selectedSymptomsContainer.innerHTML = '';
        selectedSymptoms.forEach(symptom => {
            const button = document.createElement('button');
            button.innerText = symptom;
            button.classList.add('selected-symptom-button');
            button.addEventListener('click', function () {
                removeSelectedSymptom(symptom);
            });
            selectedSymptomsContainer.appendChild(button);
        });
    }

    function removeSelectedSymptom(symptom) {
        const index = selectedSymptoms.indexOf(symptom);
        if (index !== -1) {
            selectedSymptoms.splice(index, 1);
            updateSelectedSymptoms();
            filterSymptoms(); // Update the displayed symptoms after removing one
        }
    }
    const submitButton = document.getElementById('submitSymptomsButton');
    submitButton.addEventListener('click', function () {
        submitSymptoms();
    });

    function submitSymptoms() {
        fetch('http://localhost:5000/api', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ symptoms: selectedSymptoms }),
        })
        .then(response => response.json())
        .then(data => {
            const resultDiv = document.getElementById('diseaseResult');
            resultDiv.style.visibility = 'visible';
            const DTresult = document.getElementById('decisionTreeResult');
            const NBresult = document.getElementById('naiveBayesResult');
            const KNNresult = document.getElementById('knnResult');
            DTresult.innerText = data.DT;
            NBresult.innerText = data.NB;
            KNNresult.innerText = data.KNN;
        })
        .catch(error => {
            console.error('Error:', error);
        });
    }
});