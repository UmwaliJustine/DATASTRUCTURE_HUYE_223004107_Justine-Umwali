class JobApplicationSystem:
    def __init__(jobb):
        jobb.job_openings = [
            {"JobID": 1101, "Position": "Software Engineer"},
            {"JobID": 1102, "Position": "Data Analyst"},
            {"JobID": 1103, "Position": "Project Manager"},
            {"JobID": 1104, "Position": "Data Scientist"},
            {"JobID": 1105, "Position": "Product Manager"},
            {"JobID": 1106, "Position": "Business Analyst"},
            {"JobID": 1107, "Position": "Programmerr"},
            {"JobID": 1108, "Position": "Marketing Specialist"},
            {"JobID": 1109, "Position": "Systems Engineer"},
            {"JobID": 1110, "Position": "DevOps Engineer"},
            {"JobID": 1111, "Position": "Security Analyst"},
            {"JobID": 1112, "Position": "Network Engineer"},
            {"JobID": 1113, "Position": "Mobile Developer"},
            {"JobID": 1114, "Position": "Machine Learning Engineer"},
            {"JobID": 1115, "Position": "Cloud Architect"},
            {"JobID": 1116, "Position": "Full Stack Developer"},
            {"JobID": 1117, "Position": "QA Tester"},
            {"JobID": 1118, "Position": "Database Administrator"},
            {"JobID": 1119, "Position": "Technical Writer"},
            {"JobID": 1120, "Position": "HR Specialist"}
        ]
        
        jobb.applicants_queue = [
            {"JobID": 1101, "ApplicantName": "Michael Adams", "Position": "Software Engineer", "Status": "Pending"},
            {"JobID": 1102, "ApplicantName": "Susan Brown", "Position": "Data Analyst", "Status": "Reviewed"},
            {"JobID": 1103, "ApplicantName": "Costasie Uwinema", "Position": "Project Manager", "Status": "Pending"},
            {"JobID": 1104, "ApplicantName": "Theogene Uzabakiriho", "Position": "Data Scientist", "Status": "Pending"},
            {"JobID": 1105, "ApplicantName": "Aminah Uwimana", "Position": "Product Manager", "Status": "Pending"},
            {"JobID": 1106, "ApplicantName": "Theogene Manishimwe", "Position": "Business Analyst", "Status": "Pending"},
            {"JobID": 1107, "ApplicantName": "Justine Umwali", "Position": "UI/UX Designer", "Status": "Pending"},
            {"JobID": 1108, "ApplicantName": "Eric Habumugisha", "Position": "Marketing Specialist", "Status": "Pending"},
            {"JobID": 1109, "ApplicantName": "Daniel Habimana", "Position": "Systems Engineer", "Status": "Pending"},
            {"JobID": 1110, "ApplicantName": "Enock Munezero", "Position": "DevOps Engineer", "Status": "Pending"},
            {"JobID": 1111, "ApplicantName": "Annet Uwera", "Position": "Security Analyst", "Status": "Pending"},
            {"JobID": 1112, "ApplicantName": "Jean Paul Munyemana", "Position": "Network Engineer", "Status": "Pending"},
            {"JobID": 1113, "ApplicantName": "Barbara Lewis", "Position": "Mobile Developer", "Status": "Pending"},
            {"JobID": 1114, "ApplicantName": "Rebecca Tuyikunde", "Position": "Machine Learning Engineer", "Status": "Pending"},
            {"JobID": 1115, "ApplicantName": "Placide Dufitukuri", "Position": "Cloud Architect", "Status": "Pending"},
            {"JobID": 1116, "ApplicantName": "Venuste Ntezimana", "Position": "Full Stack Developer", "Status": "Pending"},
            {"JobID": 1117, "ApplicantName": "Erin Ntampaka", "Position": "QA Tester", "Status": "Pending"},
            {"JobID": 1118, "ApplicantName": "Florence Kayitesi", "Position": "Database Administrator", "Status": "Pending"},
            {"JobID": 1119, "ApplicantName": "Diane Umuhoza", "Position": "Technical Writer", "Status": "Pending"},
            {"JobID": 1120, "ApplicantName": "Gentille Uwera", "Position": "HR Specialist", "Status": "Pending"}
        ]
        
        jobb.undo_stack = []

    def process_next_application(jobb):
        if len(jobb.applicants_queue) > 0:
            application = jobb.applicants_queue.pop(0)
            application["Status"] = "Reviewed"
            jobb.undo_stack.append(("review", application))
            print(f"Application for {application['ApplicantName']} ({application['Position']}) reviewed.")
        else:
            print("No job applications left to process.")

    def undo_last_action(jobb):
        if len(jobb.undo_stack) > 0:
            action, application = jobb.undo_stack.pop()
            if action == "review":
                application["Status"] = "Pending"
                jobb.applicants_queue.insert(0, application)
                print(f"Undo: Application for {application['ApplicantName']} ({application['Position']}) marked as Pending.")
        else:
            print("No actions to undo.")
    
    def display_job_openings(jobb):
        print("Available Job Openings:")
        for job in jobb.job_openings:
            print(f"JobID: {job['JobID']}, Position: {job['Position']}")
    
    def display_applicants(jobb):
        print("Applicants Queue:")
        for app in jobb.applicants_queue:
            print(f"JobID: {app['JobID']}, Applicant: {app['ApplicantName']}, Position: {app['Position']}, Status: {app['Status']}")
    
    def display_undo_stack(jobb):
        print("Undo Stack:")
        for action, app in jobb.undo_stack:
            print(f"Action: {action}, Applicant: {app['ApplicantName']}, Status: {app['Status']}")

system = JobApplicationSystem()

print("\nBefore push and pop Initial Job Applications:")
system.display_applicants()

system.process_next_application()

print("\nAfter pop Processing:")
system.display_applicants()

system.undo_last_action()

print("\nAfter Undoing:")
system.display_applicants()


print("\nAvailable Job Openings:")
system.display_job_openings()

print("\nUndo Stack:")
system.display_undo_stack()
