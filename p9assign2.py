import json

resume={
    "informations": [
        {
            "FirstName":"Leon Adriel Franco",
            "MiddleName":"Mercurio",
            "LastName":"Agcaoili",

            "Address":"Quezon City",
            "ContactNumber":"09563168673",

            "SchoolsAttended1":"Pre-school: Ste Anne de beaupre School",
            "SchoolsAttended2":"Elementary: Project 6 Elementary School",
            "SchoolsAttended3":"High School: Erenesto Rondon High School: Information Techonology",
            "SchoolsAttended4":"Senior High School: Don Alejandro Roces Senior Science-Technology High School: Drafting",
            "SchoolsAttended5":"College: Polytechnic University of the Philippines: Computer Engineering",

            "Experiences":"Varsity Player in Elementary to Senior High School",

            "Achievements1":"With Honors",
            "Achievements2":"Most Valuable Player",
            "Achievements3":"Champion in 3-Point Shootout",

            "Summary":"Most Valuable Player in year 2019 in basketball. Placed on Mythical 5 on specific league. Confident in skills, like dribbling, shooting, passing, and guarding.",
            "Objective":"I am confident in my skills. I can do whatever position that you will give to me and do whatever it takes just to the best on it."
        }  
    ]
}

json_string = json.dumps(resume, indent=2)
with open('infos.json', 'w') as f:
    f.write(json_string)


