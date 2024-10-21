def convert_kg(value):
	pounds = value * 2.20462
	ounces = value * 35.274
	print(f"{value} kg converted is {pounds} pounds and {ounces} ounces")

def convert_pounds(value):
	kilograms = value * .453592
	ounces = value * 16
	print(f"{value} pounds converted is {kilograms} pounds and {ounces} ounces")

def convert_ounces(value):
	kilograms = value * .0283495
	pounds = value * .0625
	print(f"{value} ounces converted is {kilograms} pounds and {pounds} pounds")
	
if __name__ == "__main__":
	convert_kg(20)
	convert_pounds(10)
	convert_ounces(5)

# Make It Your Own
def convert_liters(value):
    fluid_ounces = value * 33.814
    pints = value * 2.11338
    quarts = value * 1.05669
    print(f"{value} liters converted is {fluid_ounces} fluid ounces, {pints} pints, and {quarts} quarts.")	

def convert_fluid_ounces(value):
    liters = value / 33.814
    pints = value / 16
    quarts = value / 32
    print(f"{value} fluid ounces converted is {liters} liters, {pints} pints, and {quarts} quarts.")

if __name__ == "__main__":
	convert_liters(4)
	convert_fluid_ounces(35)