# lib/sql_queries.py

# Selects all of the bears names and ages that are alive and orders them from youngest to oldest.
select_all_bears_names_and_ages_that_are_alive_and_order_youngest_to_oldest = """
    SELECT name, age
    FROM bears
    WHERE alive = 1
    ORDER BY age ASC;
"""

# Selects the oldest bear and returns their name and age.
select_oldest_bear_and_returns_name_and_age = """
    SELECT name, age
    FROM bears
    ORDER BY age DESC
    LIMIT 1;
"""

# Selects the youngest bear and returns their name and age.
select_youngest_bear_and_returns_name_and_age = """
    SELECT name, age
    FROM bears
    ORDER BY age ASC
    LIMIT 1;
"""

# Selects all of the female bears and returns their name and age.
select_all_female_bears_return_name_and_age = """
    SELECT name, age
    FROM bears
    WHERE sex = 'F';
"""

# ✅ FIXED: Only selects the name (no temperament)
select_all_bears_names_and_orders_in_alphabetical_order = """
    SELECT name
    FROM bears
    ORDER BY name ASC;
"""

# Selects all of the bears names and ages together.
select_all_bears_names_and_ages = """
    SELECT name, age
    FROM bears;
"""

# Selects the name and age of the bear with the temperament of 'calm'.
select_bear_name_and_age_that_is_calm = """
    SELECT name, age
    FROM bears
    WHERE temperament = 'calm'
    LIMIT 1;
"""

# Selects all bears ordered by age then by name alphabetically.
select_all_bears_ordered_by_age_then_name = """
    SELECT name, age
    FROM bears
    ORDER BY age ASC, name ASC;
"""
