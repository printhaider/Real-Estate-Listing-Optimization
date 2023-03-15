"""
Purpose: Return a list of the most recent listing IDs for each unique address in the input list of listings.

This algorithm uses sorting to group the listings by address and date, and then only looks at the most recent listing for each address.
This approach is more efficient than a simple O(n) algorithm that scans the entire list for each unique address.
The time complexity of this algorithm is O(n log n) due to the sorting step, which is more efficient than an O(n^2) algorithm.
This makes the algorithm better suited for larger datasets, as the time it takes to execute will increase slower than a simple O(n) algorithm as the dataset grows.

Args:
    listings (list): A list of tuples representing the listings, where each tuple has the format (ID, address, date).

Returns:
    list: A list of the most recent listing IDs for each unique address in the input list of listings.
"""

listings = [
    ('L4', '123 kings road', '2022'),
    ('L1', '123 kings road', '2020'),
    ('L2', '20 queen road', '1990'),
    ('L3', '20 queen road', '1992')
]

def most_recent_listings(listings):
    # sort the listings by address and date in descending order
    sorted_listings = sorted(listings, key=lambda x: (x[1], -int(x[2])))
    
    most_recent = []
    current_address = None
    
    # iterate through the sorted listings and add the most recent listing for each address to the most_recent list
    for listing in sorted_listings:
        address = listing[1]
        if address != current_address:
            most_recent.append(listing[0])
            current_address = address
    
    return most_recent

most_recent = most_recent_listings(listings)
print(tuple(most_recent))  # Output: ('L4', 'L3')
