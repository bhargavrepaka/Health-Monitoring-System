class Patient:
    def __init__(self, name, age, patient_id):
        self.name = name
        self.age = age
        self.patient_id = patient_id
        self.reports = []

    def add_report(self, date, diagnosis, treatment):
        for report in self.reports:
            if report['diagnosis'] == diagnosis:
                print(f"Similar diagnosis '{diagnosis}' found on {report['date']}. Avoiding duplicate diagnostic.")
                return
        report = {
            'date': date,
            'diagnosis': diagnosis,
            'treatment': treatment
        }
        self.reports.append(report)
        print(f"Report added for {self.name} on {date}.")

    def get_reports(self):
        if not self.reports:
            print(f"No reports available for {self.name}.")
            return
        print(f"Reports for {self.name}:")
        for report in self.reports:
            print(f"Date: {report['date']}, Diagnosis: {report['diagnosis']}, Treatment: {report['treatment']}")

    def update_info(self, name=None, age=None):
        if name:
            self.name = name
        if age:
            self.age = age
        print(f"Patient information updated: Name: {self.name}, Age: {self.age}")

    def delete_report(self, date, diagnosis):
        for report in self.reports:
            if report['date'] == date and report['diagnosis'] == diagnosis:
                self.reports.remove(report)
                print(f"Report on {date} for diagnosis '{diagnosis}' deleted.")
                return
        print("Report not found.")

    def get_treatment(self, diagnosis):
        for report in self.reports:
            if report['diagnosis'].lower() == diagnosis.lower():
                return report['treatment']
        return None


class HealthMonitoringSystem:
    def __init__(self):
        self.patients = {}
        self.next_id = 1

    def add_patient(self, name, age):
        patient_id = f"P{self.next_id:04d}"
        self.patients[patient_id] = Patient(name, age, patient_id)
        print(f"Patient {name} added with ID {patient_id}.")
        self.next_id += 1

    def get_patient(self, patient_id):
        patient = self.patients.get(patient_id)
        if not patient:
            print(f"Patient with ID {patient_id} not found.")
            return None
        return patient

    def update_patient(self, patient_id, name=None, age=None):
        patient = self.get_patient(patient_id)
        if patient:
            patient.update_info(name, age)

    def delete_patient(self, patient_id):
        if patient_id in self.patients:
            del self.patients[patient_id]
            print(f"Patient with ID {patient_id} deleted.")
        else:
            print(f"Patient with ID {patient_id} not found.")

    def delete_patient_by_name(self, name):
        patient_id_to_delete = None
        for patient_id, patient in self.patients.items():
            if patient.name.lower() == name.lower():
                patient_id_to_delete = patient_id
                break
        if patient_id_to_delete:
            self.delete_patient(patient_id_to_delete)
        else:
            print("No patient found with that name.")

    def add_report_to_patient(self, patient_id, date, diagnosis, treatment):
        patient = self.get_patient(patient_id)
        if patient:
            patient.add_report(date, diagnosis, treatment)

    def get_patient_reports(self, patient_id):
        patient = self.get_patient(patient_id)
        if patient:
            patient.get_reports()

    def delete_report_from_patient(self, patient_id, date, diagnosis):
        patient = self.get_patient(patient_id)
        if patient:
            patient.delete_report(date, diagnosis)

    def list_patients(self):
        if not self.patients:
            print("No patients in the system.")
            return
        print("List of patients:")
        for patient_id, patient in self.patients.items():
            print(f"ID: {patient_id}, Name: {patient.name}, Age: {patient.age}")

    def search_patient_by_name(self, name):
        found = False
        for patient in self.patients.values():
            if patient.name.lower() == name.lower():
                print(f"Patient found: ID: {patient.patient_id}, Name: {patient.name}, Age: {patient.age}")
                found = True
        if not found:
            print("No patient found with that name.")

    def get_treatment_by_id_and_diagnosis(self, patient_id, diagnosis):
        patient = self.get_patient(patient_id)
        if patient:
            treatment = patient.get_treatment(diagnosis)
            if treatment:
                print(f"Treatment for diagnosis '{diagnosis}' is: {treatment}")
            else:
                print(f"No treatment found for diagnosis '{diagnosis}'.")
        else:
            print(f"Patient with ID {patient_id} not found.")


import sys


def main():
    system = HealthMonitoringSystem()

    while True:
        print("\n--- Health Monitoring System ---")
        print("1. Add Patient")
        print("2. Update Patient Information")
        print("3. Delete Patient")
        print("4. Delete Patient by Name")
        print("5. Add Report to Patient")
        print("6. View Patient Reports")
        print("7. Delete Report from Patient")
        print("8. List All Patients")
        print("9. Search Patient by Name")
        print("10. Get Treatment by ID and Diagnosis")
        print("11. Exit")
        choice = input("Enter your choice (1-11): ")

        if choice == '1':
            name = input("Enter patient's name: ")
            age = int(input("Enter patient's age: "))
            system.add_patient(name, age)

        elif choice == '2':
            patient_id = input("Enter patient ID to update: ")
            name = input("Enter new name (or press Enter to skip): ")
            age = input("Enter new age (or press Enter to skip): ")
            age = int(age) if age else None
            system.update_patient(patient_id, name if name else None, age)

        elif choice == '3':
            patient_id = input("Enter patient ID to delete: ")
            system.delete_patient(patient_id)

        elif choice == '4':
            name = input("Enter patient's name to delete: ")
            system.delete_patient_by_name(name)

        elif choice == '5':
            patient_id = input("Enter patient ID: ")
            date = input("Enter report date (YYYY-MM-DD): ")
            diagnosis = input("Enter diagnosis: ")
            treatment = input("Enter treatment: ")
            system.add_report_to_patient(patient_id, date, diagnosis, treatment)

        elif choice == '6':
            patient_id = input("Enter patient ID: ")
            system.get_patient_reports(patient_id)

        elif choice == '7':
            patient_id = input("Enter patient ID: ")
            date = input("Enter report date (YYYY-MM-DD): ")
            diagnosis = input("Enter diagnosis: ")
            system.delete_report_from_patient(patient_id, date, diagnosis)

        elif choice == '8':
            system.list_patients()

        elif choice == '9':
            name = input("Enter patient's name to search: ")
            system.search_patient_by_name(name)

        elif choice == '10':
            patient_id = input("Enter patient ID: ")
            diagnosis = input("Enter diagnosis: ")
            system.get_treatment_by_id_and_diagnosis(patient_id, diagnosis)

        elif choice == '11':
            print("Exiting the system.")
            sys.exit()

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
