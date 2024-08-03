from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Définissez les questions et les réponses ici
questions = [
    "Avez-vous des symptômes de fatigue ?",
    "Avez-vous des douleurs thoraciques ?",
    "Avez-vous des difficultés à respirer ?",
    # Ajoutez les questions supplémentaires ici
]

answers = ["Oui", "Non"]


# Définissez le traitement des données ici
def diagnose_tuberculose(patient_data):
    if patient_data:
        fatigue = patient_data["Avez-vous des symptômes de fatigue ?"]
        douleurs_thoraciques = patient_data["Avez-vous des douleurs thoraciques ?"]
        difficultes_respirer = patient_data["Avez-vous des difficultés à respirer ?"]
        if (
            fatigue == "OUI"
            and douleurs_thoraciques == "OUI"
            and difficultes_respirer == "OUI"
        ):
            return "Oui, le patient est atteint de la tuberculose."
        elif (
            fatigue == "OUI"
            or douleurs_thoraciques == "OUI"
            or difficultes_respirer == "OUI"
        ):
            if fatigue == "OUI" and douleurs_thoraciques == "NON" and difficultes_respirer == "NON":
                return "Non, le patient n'est pas atteint de la tuberculose. \n Et si la fatigue continue, veuillez consulter le medecin !!"
            elif douleurs_thoraciques == "OUI" and fatigue == "NON" and difficultes_respirer == "NON":
                return "Non, le patient n'est pas atteint de la tuberculose. \n Et si la douleur thoracique continue, veuillez consulter le medecin !!"
            elif difficultes_respirer == "OUI" and douleurs_thoraciques == "NON" and fatigue == "NON" :
                return "Non, le patient n'est pas atteint de la tuberculose. \n Et si la difficulté respiratoire continue, veuillez consulter le medecin !!"
            elif difficultes_respirer == "OUI" and douleurs_thoraciques == "OUI":
                return "Le patient developpe peut-etre la tuberculose. \n Et si la difficulté respiratoire et la douleur thoracique continuent, veuillez consulter le medecin !!"
            elif difficultes_respirer == "OUI" and fatigue == "OUI":
                return "Le patient developpe peut-etre la tuberculose. \n Et si la difficulté respiratoire et la fatigue continuent, veuillez consulter le medecin !!"
            elif fatigue == "OUI" and douleurs_thoraciques == "OUI":
                return "Le patient developpe peut-etre la tuberculose. \n Et si la la douleur thoracique et la fatigue continuent, veuillez consulter le medecin !!"
    else:

        return "Non, le patient n'est pas atteint de la tuberculose."


@app.route("/")
def index():
    return render_template("index.html", questions=questions, answers=answers)


@app.route("/submit", methods=["POST"])
def submit():
    data = request.json
    patient_data = {question: data.get(question) for question in questions}
    diagnosis = diagnose_tuberculose(patient_data)
    return jsonify({"diagnosis": diagnosis})


if __name__ == "__main__":
    app.run(debug=True)
