import math


def main():
    # Input the radius
    radius = float(input("Enter the radius in cm: "))
    # Calculations for both circumference and radius
    circumference = math.pi * 2 * radius
    area = math.pi * radius**2
    # displaying both the radius and the circumference
    print(f"circumference = {circumference:.2f}")
    print(f"area = : {area:.2f}")


# end
if __name__ == "__main__":
    main()
