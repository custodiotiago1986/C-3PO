def format_person_data(person):
    return (f"**Name**: {person['name']}\n"
            f"**Height**: {person['height']} cm\n"
            f"**Mass**: {person['mass']} kg\n"
            f"**Hair Color**: {person['hair_color']}\n"
            f"**Skin Color**: {person['skin_color']}\n"
            f"**Birth Year**: {person['birth_year']}\n"
            f"**Gender**: {person['gender']}")

def format_planet_data(planet):
    return (f"**Name**: {planet['name']}\n"
            f"**Climate**: {planet['climate']}\n"
            f"**Terrain**: {planet['terrain']}\n"
            f"**Population**: {planet['population']}\n"
            f"**Orbital Period**: {planet['orbital_period']} days\n"
            f"**Rotation Period**: {planet['rotation_period']} hours")

def format_starship_data(starship):
    return (f"**Name**: {starship['name']}\n"
            f"**Model**: {starship['model']}\n"
            f"**Manufacturer**: {starship['manufacturer']}\n"
            f"**Cost in Credits**: {starship['cost_in_credits']}\n"
            f"**Length**: {starship['length']} meters\n"
            f"**Crew**: {starship['crew']}\n"
            f"**Passengers**: {starship['passengers']}")
