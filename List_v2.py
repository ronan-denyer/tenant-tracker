#reads each line of the .txt file and places in a list
tenants = open("tenants.txt").readlines()
#print current list
print tenants
#define methods for adding/removing tenants from list
def remove_tenant(apt):
    for x in tenants:
        if x == apt:
            tenants.remove(apt);

def add_tenant(apt):
    tenants.append(apt);
#input for adding/removing tenants
response = raw_input("Would you like to add or remove tenants from this list?")
if response == "add":
    number = raw_input("What apartment number would you like to add?")
    str(number)
    add_tenant(number);
if response == "remove":
    number = raw_input("What apartment number would you like to remove?")
    str(number)
    remove_tenant(number);
#print updated list
print tenants;
#write new changes to .txt file
with open('tenants.txt', 'w') as out_file:
    out_file.write('\n'.join(tenants));
