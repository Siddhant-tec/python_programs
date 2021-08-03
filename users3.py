class user:
    def __init__(self, first_name, last_name, qualification):
        self.first_name = first_name
        self.last_name = last_name
        self.qualification = qualification

    def describe_user(self):
        print("\nFirst Name:", self.first_name)
        print("Last Name:", self.last_name)
        print("Qualification:", self.qualification)

    def greet_user(self):
        print("\nHello ", self.first_name, self.last_name + "!", "How may i assist you!",
              "\nHere is a suggestion: Would you like to proceed to the", self.qualification.title(), "section?")


class Admin(user):
    def __init__(self, first_name, last_name, qualification):
        super().__init__(first_name, last_name, qualification)
        self.privilages = ["can add post", "can delete post", "can ban user"]

    def show_privilages(self):
        if self.qualification == "Admin":
            print("The following privilages are available to", self.first_name, self.privilages)
        else:
            print("None of the privilages are available to", self.first_name)


u1 = user("Siddhant", "Tiwari", "Student")
p1 = Admin("Siddhant", "Tiwari", "Admin")
u2 = user("Ashish", "Tiwari", "Advocate")
u3 = user("Manisha", "Tiwari", "Cyber Lawyer")
p3 = Admin("Manisha", "Tiwari", "User")
print("Hello Welcome to Company Help Service Portal! I am your Virtual Assistant.")
name = input("Please enter your first name to proceed: ")
if name == u1.first_name:
    u1.describe_user()
    u1.greet_user()
    p1.show_privilages()
if name == u3.first_name:
    u3.describe_user()
    u3.greet_user()
    p3.show_privilages()
if name == u2.first_name:
    u2.describe_user()
    u2.greet_user()

