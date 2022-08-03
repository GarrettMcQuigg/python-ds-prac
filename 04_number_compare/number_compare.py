def number_compare(a, b):
    """Report on whether a>b, b>a, or b==a
    
        >>> number_compare(1, 1)
        'Numbers are equal'
        
        >>> number_compare(-1, 1)
        'Second is greater'
        
        >>> number_compare(1, -2)
        'First is greater'
    """
    if a > b:
        return F"{a} is greater than {b}"
    elif b > a:
        return F"{b} is greater than {a}"
    elif a == b:
        return F"{a} is equal to {b}"