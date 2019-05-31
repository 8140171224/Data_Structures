# More on Conditions

    The conditions used in while and if statement can contain any operator, not just comparison.
    
    The comparison operators in and not in cheak whether a value occurs (does not occur) in a sequence.
    The operator is not compare whether two objects are really the same object; this only matters for 
    mutable objects like lists. All comparison operators have the same priority, which is lower then 
    that of all numerical.
    
    Comparisons can be chained. For exampled, [a < b == c] tests whether a is less then b and moreover 
    b equals c.
    
    Comparisons may be combined using the Boolean operation and & or, and the outcome of a comparison 
    (or of any other Boolean expression) may be negated with not. There have lower pariorities than
    comparison operation; between then, not has the highest priority and or the lowest, so the  A ans not B 
    or C is equivalent to (A and (not B)) or C. As alwayes, parentheses can be used to express the desires
    composition.
    
