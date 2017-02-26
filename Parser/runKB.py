def Ask(pattern):
    list_of_binding_list=[]
    for fact in KB:
        bindings=facts_and_rules.pattern_match(pattern,fact)
        if bingdings!=False:
            list_of_binding_list.append(bindings)
        for b in list_of_binding_list:
            print "This is tule:\t",
            print fact_and_rules.statement(facts_and_rules.instantiate(pattern,b)).pretty()