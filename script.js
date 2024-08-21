const subjects = {
    sem1: ["Communicative English", "Engineering Chemistry", "Matrices and Calculus", "Engineering Physics", "Problem Solving and Python Programming", "Heritage of Tamil", "Physics and Chemistry Laboratory", "Problem Solving and Python Programming Laboratory", "Communicative English Laboratory"],
    sem2: ["Technical English", "Statistics and Numerical Methods", "Physics for Computer Science Engineers", "Engineering Graphics", "Programming in C", "தமிழரும் தொழில்நுட்பமும் Tamils and Technology", "Environmental Science and Sustainability", "NCC Credit Course Level 1#", "Technical English Laboratory", "Engineering Practices Laboratory", "Programming in C Laboratory"],
    sem3: ["Discrete Mathematics", "Digital Principles and Computer Organization", "Object Oriented Programming using C++ and Java", "Data Structures and Algorithms", "Foundations of Data Science", "Data Structures and Algorithms Laboratory", "Object Oriented Programming using C++ and Java Laboratory", "Data Science Laboratory", "Quantitative Aptitude & Verbal Reasoning"],
    sem4: ["Probability and Statistics","Theory of Computation","Engineering Secure Software Systems","Database Management Systems and Security","Operating Systems and Security","Networks Essentials","NCC Credit Course Level 2#","Database Management System security Laboratory","Operating Systems and Security Laboratory","Quantitative Aptitude & Behavioural Skills"],
    sem5: ["Distributed System","Cyber Law","Cyber Forensics","Mandatory Course-I#","Open Elective I","Cryptography and cyber security","Professional Elective I","Security Laboratory","Quantitative Aptitude & Communication Skills"],
    sem6: ["Internet of Things","Open Elective-II","Mandatory Course-II","NCC Credit Course Level 3#","Artificial Intelligence and Machine Learning","Professional Elective II","Professional Elective III","Professional Elective IV","Mini Project","Quantitative Aptitude & Soft Skills"],
    sem7: ["Human Values and Ethics","# Elective - Management","Open Elective - III","Professional Elective V","Professional Elective VI","Internship"],
    sem8: ["Project Work"]
};

const credits = {
    sem1: [3, 3, 4, 3, 3, 1, 2, 2, 1],
    sem2: [3, 4, 3, 4, 3, 1, 2, 2, 1, 2, 2],
    sem3: [4, 4, 3, 3, 3, 2, 2, 2, 1],
    sem4: [4, 3, 3, 3, 3, 4, 3, 2, 2, 1],
    sem5: [3, 3, 3, 0, 3, 4, 3, 2, 1],
    sem6: [3, 3, 0, 3, 4, 3, 3, 3, 2, 1],
    sem7: [2, 3, 3, 3, 3, 1],
    sem8: [10]
};

document.getElementById("semesters").addEventListener("change", function() {
    const semCount = this.value;
    const container = document.getElementById("semesters-container");
    container.innerHTML = "";

    for (let i = 1; i <= semCount; i++) {
        const semSubjects = subjects[`sem${i}`];
        const semCredits = credits[`sem${i}`];

        const semDiv = document.createElement("div");
        semDiv.classList.add("semester-container");
        semDiv.innerHTML = `<h3>Semester ${i}</h3>`;

        semSubjects.forEach((subject, idx) => {
            const gradeSelect = document.createElement("select");
            gradeSelect.id = `sem${i}-subject${idx}`;
            gradeSelect.innerHTML = `
                <option value="select">Select grade</option>
                <option value="10">O</option>
                <option value="9">A+</option>
                <option value="8">A</option>
                <option value="7">B+</option>
                <option value="6">B</option>
                <option value="5">C</option>
                <option value="0">F</option>
            `;
            semDiv.innerHTML += `<label>${subject} (Credits: ${semCredits[idx]}): </label>`;
            semDiv.appendChild(gradeSelect);
            semDiv.innerHTML += "<br>";
        });
        container.appendChild(semDiv);
    }
});

function goToResultPage() {
    calculateGPAandCGPA();
    document.getElementById('mainPage').style.display = 'none';
    document.getElementById('resultPage').style.display = 'block';
}

function goBack() {
    document.getElementById('mainPage').style.display = 'block';
    document.getElementById('resultPage').style.display = 'none';
}

function calculateGPAandCGPA() {
    let totalPoints = 0;
    let totalCredits = 0;
    let semesterGPAs = [];

    const semCount = document.getElementById("semesters").value;

    for (let i = 1; i <= semCount; i++) {
        let semPoints = 0;
        let semCredits = 0;
        const semSubjects = subjects[`sem${i}`];
        const semCreditsArr = credits[`sem${i}`];

        semSubjects.forEach((subject, idx) => {
            const gradeSelect = document.getElementById(`sem${i}-subject${idx}`);
            const grade = Number(gradeSelect.value);

            if (grade !== 0 && grade !== "select") { // Exclude F grade and "select" option
                semPoints += grade * semCreditsArr[idx];
                semCredits += semCreditsArr[idx];
            }
        });

        // Calculate GPA for the semester
        const semGPA = semCredits === 0 ? 0 : (semPoints / semCredits).toFixed(2);
        semesterGPAs.push(`GPA for Semester ${i}: ${semGPA}`);
        
        totalPoints += semPoints;
        totalCredits += semCredits;
    }

    // Calculate CGPA
    const cgpa = totalCredits === 0 ? 0 : (totalPoints / totalCredits).toFixed(2);

    // Display CGPA and GPA for each semester
    document.getElementById("result").innerHTML = `<p>CGPA: ${cgpa}</p>` + semesterGPAs.map(gpa => `<p>${gpa}</p>`).join('');
}
