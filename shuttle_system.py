
"""Campus shuttle timetable and fleet tracker."""

import json
import secrets
from datetime import datetime


# Global state
routes = {
    "R1": {"name": "Main Gate - Library", "trips": []},
    "R2": {"name": "Hostel - Sports Complex", "trips": []},
    "R3": {"name": "Admin Block - Metro", "trips": []},
}
MIN_CAPACITY = 10


def add_trip_log(route_id, passenger_count, logs=None):
    """Record a passenger count for a route and return the log entries."""
    if logs is None:
        logs = []

    routes[route_id]["trips"].append(passenger_count)
    logs.append(
        f"{datetime.now()}: {route_id} carried {passenger_count}"
    )
    return logs


def remove_route(route_id):
    """Remove a route from the fleet."""
    del routes[route_id]


def average_load(route_id):
    """Calculate the average passenger load for a route."""
    trips = routes[route_id]["trips"]
    return sum(trips) / len(trips)


def underused_routes():
    """Return routes with valid average passenger loads below capacity."""
    flagged = []

    for route_id, route_data in routes.items():
        trips = route_data["trips"]

        if not trips:
            continue

        if not all(
            isinstance(count, (int, float)) and not isinstance(count, bool)
            for count in trips
        ):
            continue

        if average_load(route_id) < MIN_CAPACITY:
            flagged.append(route_id)

    return flagged


def assign_driver():
    """Select a driver randomly from the available drivers."""
    drivers = ["Prakash", "Leela", "Imran", "Tom"]
    return secrets.choice(drivers)


def sync_fleet_data(file="fleet.json"):
    """Save fleet data to JSON and reload it
    into the shared route dictionary."""
    with open(file, "w", encoding="utf-8") as fleet_file:
        json.dump(routes, fleet_file)
    with open(file, "r", encoding="utf-8") as fleet_file:
        loaded_routes = json.load(fleet_file)

    routes.clear()
    routes.update(loaded_routes)


def main():
    """Run the campus shuttle tracker."""
    add_trip_log("R1", 32)
    add_trip_log("R1", 28)
    add_trip_log("R2", 4)
    add_trip_log("R2", -6)
    add_trip_log("R3", "full")

    print("Driver for R1:", assign_driver())
    print("Underused:", underused_routes())
    print("R1 average:", average_load("R1"))

    sync_fleet_data()
    remove_route("R3")

    choice = input("Route to look up (Enter for R2): ") or "R2"
    print("Trips on", choice, ":", routes[choice]["trips"])
    print("R3 average:", average_load("R3"))


if __name__ == "__main__":
    main()
