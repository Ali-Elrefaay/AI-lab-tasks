
#first_question
import aima.utils
import aima.logic
def main():
    clauses = []
    
    clauses.append(aima.utils.expr("color(carrots,orange)")) 
    
    clauses.append(aima.utils.expr ("vegetarian(person) ==> like(person,carrots) "))
    
    clauses.append(aima.utils.expr(" study hard(student) ==> pass(student) "))
    
    clauses.append(aima.utils.expr("?pass(who)"))
    
    clauses.append(aima.utils.expr("teaches(professor,course) "))
    
    clauses.append(aima.utils.expr("enemies(x,y) ==> hate(x,y) & fight(x,y) "))
    
    

#second_question
import aima.utils
import aima.logic
def main():
    clauses = []
    clauses.append(aima.utils.expr("read(maria,book) & book(logic programming,peter lucas)")) 
    clauses.append(aima.utils.expr("(likes shoping(x) ==>girl(x) "))
    clauses.append(aima.utils.expr("(?like shopping(who) "))
    clauses.append(aima.utils.expr("(city(x) & big(x) & crowdy(x) ==>hate(kirk,x) "))
    
    
#fourth_question
import aima.utils as au
import aima.logic
def main():
    clauses=[]
    clauses.append(au.expr("(woman(x))"))
    clauses.append(au.expr("(man(x))"))
    clauses.append(au.expr("(woman(x) ==>one(x))"))
    clauses.append(au.expr("(man(x) ==> one(x))"))
    clauses.append(au.expr("(healthy(x))"))
    clauses.append(au.expr("(wealthy(x))"))
    clauses.append(au.expr("(one(x) & healthy(x) & wealthy(x) ==> traveller(x))"))
    clauses.append(au.expr("(one(x) & traveller(x) ==> cantravel(x))"))
    KB=aima.logic.FolKB(clauses)
    KB.tell(au.expr("woman(jia)")) 
    KB.tell(au.expr("man(john)"))
    KB.tell(au.expr("healthy(john)"))
    KB.tell(au.expr("healthy(jia)")) 
    KB.tell(au.expr("wealthy(john)"))
    can_travel= KB.ask(au.expr('cantravel(x)'))
    H_W= KB.ask(au.expr('traveller(x)'))
    print('\n Can travel?')
    print(can_travel)
    print('\n Healthy and Wealthy?')
    print(H_W)
      