from DeltaEpsilon.proof import DeltaEpsilonProof

# test case 1 - straight proof
print("PROOF 1:")
pf = DeltaEpsilonProof("\\lim_{x \\to 2} (x + 3) = 5")
pf.insert("= |x - 2|")
pf.insert("< \\delta")
pf.choose_delta("\\epsilon")
pf.insert("= \\epsilon")
pf.print_all()

# test case 2 - delta with a multiple
print("\nPROOF 2:")
pf = DeltaEpsilonProof("\\lim_{x \\to 4} 2(x + 3) = 14")
pf.insert("= |2x + 6 - 14|")
pf.insert("= |2x - 8|")
pf.insert("= 2|x - 4|")  # says this is not valid ?!
pf.insert("< 2\\delta")
pf.choose_delta("\\frac{\\epsilon}{2}")
pf.insert("= 2\\frac{\\epsilon}{2}")
pf.insert("= \\epsilon")
pf.print_all()

# test case 3 - one sided limit
print("\nPROOF 3:")
pf = DeltaEpsilonProof("\\lim_{x \\to 4^-} 2(x + 3) = 14")
pf.insert("= -(2x + 6 - 14)")
pf.insert("= -(2x - 8)")
pf.insert("= -2x + 8)")
pf.insert("= 2(4 - x)")
pf.insert("< 2\\delta")
pf.choose_delta("\\frac{\\epsilon}{2}")
pf.insert("= 2\\frac{\\epsilon}{2}")
pf.insert("= \\epsilon")
pf.print_all()

# test case 4 - x approaches infinity limit
print("\nPROOF 4:")
pf = DeltaEpsilonProof("\\lim_{x \\to \\infty} \\frac{3}{x^2} = 0")
pf.insert("< |\\frac{3}{N^2}|")
pf.choose_delta("\\sqrt{\\frac{3}{\\epsilon}}")
pf.insert("= |\\frac{3}{(\\sqrt{\\frac{3}{\\epsilon}})^2}|")
pf.insert("= |\\epsilon|")
pf.insert("= \\epsilon")
pf.print_all()

# test case 5 - x approaches infinity limit
print("\nPROOF 5:")
pf = DeltaEpsilonProof("\\lim_{x \\to \\infty} \\frac{x + 1}{x} = 1")
pf.insert("= |\\frac{x + 1}{x} - \\frac{x}{x}|")  # automatic simplifcation?!
pf.insert("= |\\frac{x + 1 - x}{x}|")
pf.insert("= |\\frac{1}{x}|")
pf.insert("< |\\frac{1}{N}|") # problem
pf.choose_delta("\\frac{1}{\\epsilon}")
pf.insert("= |\\frac{1}{\\frac{1}{\\epsilon}}|")
pf.insert("= |\\epsilon|")
pf.insert("= \\epsilon")
pf.print_all()

# test case 6 - limit is infinity
print("\nPROOF 6:")
pf = DeltaEpsilonProof("\\lim_{x \\to 0^+} \\frac{1}{x} = \\infty")
pf.choose_delta("\\frac{1}{M}")
pf.insert("> \\frac{1}{\\delta}")
pf.insert("= \\frac{1}{\\frac{1}{M}}")
pf.insert("= M")
pf.print_all()

# test case 7 - limit is infinity, x approaches infinity
print("\nPROOF 7:")
pf = DeltaEpsilonProof("\\lim_{x \\to \\infty} 2(x + 2) = \\infty")
pf.insert("= 2x + 4")
pf.insert("> 2x")
pf.insert("> 2N")
pf.choose_delta("\\frac{M}{2}")
pf.insert("= 2\\frac{M}{2}")
pf.insert("= M")
pf.print_all()

# test case 8 - constant function
print("\nPROOF 8:")
pf = DeltaEpsilonProof("\\lim_{x \\to 3} 6 = 6")
pf.insert("= 0")
pf.insert("< \\epsilon")
pf.print_all()

# test case 9 - constant function with infinity
print("\nPROOF 9:")
pf = DeltaEpsilonProof("\\lim_{x \\to \\infty} 9 = 9")
pf.insert("= 0")
pf.insert("< \\epsilon")
pf.print_all()

# test case 10 - delta assumption
print("\nPROOF 10:")
pf = DeltaEpsilonProof("\\lim_{x \\to 2} x^2 = 4")
pf.insert("= |x + 2||x - 2|")
pf.init_bound_delta("1")
pf.insert_bound_equation("-1 \\leq x - 2 \\leq 1")
pf.insert_bound_equation("1 \\leq x \\leq 3")
pf.insert_bound_equation("3 \\leq x + 2 \\leq 5")
pf.bound_expression()
pf.insert("< 5|x - 2|")
pf.choose_delta("\\frac{\\epsilon}{5}")
pf.insert("< 5\\delta")
pf.insert("= 5\\frac{\\epsilon}{5}")
pf.insert("= \\epsilon")
pf.print_all()
