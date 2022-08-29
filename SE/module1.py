class client:
    name_list = []
    num_of_clients = 0

    raise_amt = 1.04

    def __init__(self, first, last, gender,savings):
        self.first = first
        self.last = last
        self.gender = gender
        self.savings = savings
        self.regno = client.num_of_clients
        client.num_of_clients += 1
        client.name_list.append(self)

    def fullname(self):
        return "{} {}".format(self.first.title(), self.last.title())

    def email(self):
        return self.first +"."+ self.last + str(1000 + self.regno)+ "@company.com"

    def apply_interest(self):
        self.savings = int(self.savings * self.raise_amt)




class info():
    def __init__(self) -> None:
        pass
    def display(self):
        print("Name of client : ","{} {}".format(self.first.title(), self.last.title()))
        print(self.first +"."+ self.last + str(1000 + self.regno)+ "@company.com")
        print("Savings : ",self.savings)
 


class employee(client,info):
    name_list = []
    num_of_employees = 0
    def __init__(self, first, last, gender , clients = None):
        self.first = first
        self.last = last
        self.gender = gender
        self.regno = employee.num_of_employees
        employee.num_of_employees += 1
        if clients is None:
            self.clients = []
        else:
            self.clients = clients
        employee.name_list.append(self)
        
    def add_client(self,i):
        if i not in self.clients:
            self.clients.append(i)
    def remove_client(self,i):
        if i  in self.clients:
            self.clients.remove(i)
    def print_client(self):
        print("Clients under",self.fullname(),"with their emails")
        for i in self.clients:
            i.display()

        return ""

class manager(employee):
    pass
    name_list = []
    num_of_employees = 0

    def __init__(self, first, last, gender, employees = None):
        super().__init__(first, last, gender)
        if employees is None:
            self.num_of_employees = []
        else:
            self.employees = employees

    def add_emp(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)
    def remove_emp(self,emp):
        if emp  in self.employees:
            self.employees.remove(emp)
    def print_emp(self):
        for emp in self.employees:
            emp.display()



