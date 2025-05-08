# Airline Scheduling and Cargo Expert System

def get_flight_schedule(flight_type, destination, cargo_weight, preferred_time):
    schedules = {
        "Morning": ["06:00", "07:30", "09:00"],
        "Afternoon": ["12:00", "14:00", "15:30"],
        "Evening": ["18:00", "19:30", "21:00"]
    }

    cargo_limits = {
        "Passenger": 200,   # in kg
        "Cargo": 1000       # in kg
    }

    # Rule 1: Validate Cargo Weight
    if cargo_weight > cargo_limits[flight_type]:
        return {
            "status": "Rejected",
            "reason": f"Cargo exceeds limit for {flight_type} flight ({cargo_limits[flight_type]} kg)",
            "suggestion": "Switch to Cargo flight or reduce cargo weight."
        }

    # Rule 2: Match Preferred Time
    time_slots = schedules.get(preferred_time, [])

    if not time_slots:
        return {
            "status": "Failed",
            "reason": "Invalid preferred time slot.",
            "suggestion": "Choose Morning, Afternoon, or Evening."
        }

    # Rule 3: Assign First Available Slot
    assigned_slot = time_slots[0]

    return {
        "status": "Success",
        "flight_type": flight_type,
        "assigned_time": assigned_slot,
        "destination": destination,
        "cargo_weight": cargo_weight,
        "note": "Flight scheduled successfully!"
    }

# ---- MAIN PROGRAM ----
def main():
    print("\n✈️  Airline Scheduling and Cargo Expert System")
    print("--------------------------------------------------")

    flight_type = input("Enter flight type (Passenger/Cargo): ").strip().title()
    destination = input("Enter destination: ").strip().title()
    cargo_weight = float(input("Enter cargo weight (in kg): "))
    preferred_time = input("Preferred time (Morning/Afternoon/Evening): ").strip().title()

    result = get_flight_schedule(flight_type, destination, cargo_weight, preferred_time)

    print("\n📋 Scheduling Result")
    print("--------------------------------------------------")
    if result["status"] == "Success":
        print(f"✅ Status          : {result['status']}")
        print(f"✈️  Flight Type     : {result['flight_type']}")
        print(f"📍 Destination      : {result['destination']}")
        print(f"🕒 Assigned Time    : {result['assigned_time']}")
        print(f"📦 Cargo Weight     : {result['cargo_weight']} kg")
        print(f"📝 Note             : {result['note']}")
    else:
        print(f"❌ Status          : {result['status']}")
        print(f"⚠️  Reason          : {result['reason']}")
        print(f"💡 Suggestion       : {result['suggestion']}")

if __name__ == "__main__":
    main()
