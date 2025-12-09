# Welcome
print("Welcome to my projectile simulator!")
print("Enter \"exit\" at any time to terminate the program.\n")

# Initial velocity loop
while True:
    try:
        raw_velocity = input("Enter the initial speed (m/s): ")

        if raw_velocity.lower().strip() == 'exit':
            print("Goodbye!\n")
            quit()

        initial_velocity = float(raw_velocity)

        if initial_velocity <= 0:
            print("The speed must be a positive value. Try again or exit.\n")
            continue

    except ValueError:
        print("The speed must be a numerical data type. Try again or exit.\n")
        continue
    else:
        print(f"Initial velocity of {initial_velocity:.2f} m/s registered.\n")
        break


# Launch angle loop
while True:
    try:
        raw_angle = input("Enter the launch angle (between 0 and 90 degrees, exclusive): ")

        if raw_angle.lower().strip() == 'exit':
            print("Goodbye!\n")
            quit()

        launch_angle = float(raw_angle)

        if launch_angle <= 0 or launch_angle >= 90:
            print("The launch must be between 0 and 90 degrees, exclusive. Try again or exit.\n")
            continue

    except ValueError:
        print("The launch angle must be a numerical data type. Try again or exit.\n")
        continue
    else:
        print(f"Launch angle of {launch_angle:.2f} degrees registered.\n")
        break
