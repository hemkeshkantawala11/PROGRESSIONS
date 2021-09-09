def arithematic_progression_nth_term(): 
    while True:
        number1=float(input("Enter The First Number:- "))
        number2=float(input("Enter The Second Number:- "))
        global a,d,n
        a=number1
        d=number2-number1
            
        number3=float(input("Enter The Third Number:- "))
        if number3==0:
            n=3
            break

        number4=float(input("Enter The Fourth Number:- "))

        if number4==0:
            n=4
            break
        
        if d!=number3-number2 or d!=number4-number3:
            print("ERROR:- ")
            print("PLEASE WRITE IN THE CORRECT FORMAT OF ARITHEMATIC PROGRESSION!!!")
            
        elif d!=number3-number2 or d!=number4-number3:
            arithematic_progression_nth_term()
    
        if d==number3-number2 and d==number4-number3:
            n=int(input("Enter The Number Of Term Which You Want To Know:- "))
            break

def printing_the_answers():
    global a,d,n
    print ("The First Term Of The Sequence Is:- ",a)
            
    print ("The Number Of Term Which You Want To Find Is:- ",n)
            
    print ("The Common Difference Of Your Sequence Is:- ",d)
            
    print("The" ,n,"th term Is:- ",(a + (n - 1) * d))
    
    
    
    
def to_find_a_for_AP():
    global no_of_terms,nth_term,common_difference
    
    nth_term = int(input('enter the number of which you know:- '))
    no_of_terms = int(input('enter the number of terms:- '))
    common_difference = int(input('enter the common difference of the AP:- '))
    
def printing_answers_to_find_a():
    global no_of_terms,common_difference,nth_term
    print ("The number of terms of the AP is:- ",no_of_terms)
    print ("nth term of the AP is:- ",nth_term)
    print ("the common difference of the AP is:- ",common_difference)
    print("The first term of the Ap is:- ",(nth_term)-((no_of_terms-1)*common_difference))
    
    
def to_find_d_for_AP():
    global no_of_terms,nth_term,first_term
    
    nth_term = int(input('enter the number of which you know:- '))
    no_of_terms = int(input('enter the number of terms:- '))
    first_term = int(input('enter the first term of the AP:- '))
    
    
def printing_answers_to_find_d_of_AP():
    global no_of_terms,nth_term,first_term
    print ("\n The number of terms of the AP is:- ",no_of_terms)
    print ("\n nth term of the AP is:- ",nth_term)
    print ("\n the first term of the AP is:- ",first_term)
    print("\n The common difference of the AP is:- ",(nth_term-first_term)/(no_of_terms-1))
    
def to_find_no_of_terms_of_AP():
    global common_difference,nth_term,first_term
    
    nth_term = int(input('enter the number of which you know:- '))
    common_difference = int(input('enter the common difference of the AP:- '))
    first_term = int(input('enter the first term of the AP:- '))

def printing_answer_to_find_no_of_terms_of_AP():
    global common_difference,nth_term,first_term
    
    print ("\n The common difference of the AP is:- ",common_difference)
    print ("\n nth term of the AP is:- ",nth_term)
    print ("\n the first term of the AP is:- ",first_term)
    print("\n The Number of terms of the AP is:- ",((nth_term-first_term)/(common_difference))+1)


def sum_of_terms_of_ap():

    number1=float(input("Enter The First Number:- "))
    number2=float(input("Enter The Second Number:- "))
    global a,d,n2
    a=number1
    d=number2-number1
    number3=float(input("Enter The Third Number:- "))
            
    number4=float(input("Enter The Fourth Number:- "))
            
    if d != number3-number2 or d != number4-number3 :
        print("ERROR:- ")
        print("PLEASE WRITE IN THE CORRECT FORMAT OF ARITHEMATIC PROGRESSION!!!")
        #continue
       
    if d == number3-number2 and d == number4-number3:           
        n2=int(input("Enter The Number till which you want to find the sum of AP:- "))
    
    else:
         sum_of_terms_of_ap()
            
def printing_the_answers_of_sum():
    global a,d,n2
    print ("The First Term Of The Sequence Is:- ",a)
            
    print ("The Number till which you want the sum:- ",n2)
            
    print ("\nThe Common Differnce Of Your Sequence Is:- ",d)
            
    print("\nThe sum of first",n2,"terms of an AP is:- ",(n2/2)*(2*a + (n2 - 1) * d))
    

# this finds a for the AP
def to_find_a_for_sum_of_terms_of_AP():
    global no_of_terms,sums,common_difference
    
    sums = int(input('enter the sum of the AP:- '))
    no_of_terms = int(input('enter the number of terms:- '))
    common_difference = int(input('enter the common difference of the AP:- '))

#this finds d of the AP
def to_find_d_for_sum_of_AP():
    global no_of_terms,first_term_of_AP,sums
    sums = int(input('enter the sum of the AP:- '))
    no_of_terms = int(input('enter the number of terms:- '))
    first_term_of_AP = int(input('enter the first term of the AP:- '))

# this finds the answers to find d
def printing_answers_to_find_d():
    global no_of_terms,common_difference,sums
    print ("The number of terms of the AP is:- ",no_of_terms)
    print ("\nThe sum of the", no_of_terms, "of AP Is:- :- ",sums)            
    print("\nThe common difference of the AP is:- ",((2*sums/no_of_terms) - (2*first_term_of_AP))/(no_of_terms - 1))
    
# this finds the answers to find a
def printing_the_answers_to_find_a():
    global no_of_terms,first_term_of_AP,sums
    print ("The number of terms of the AP is:- ",no_of_terms)
    print ("\nThe sum of the", no_of_terms, "of AP Is:- :- ",sums)
            
    print ("\nThe Common Differnce Of Your Sequence Is:- ",common_difference)
            
    print("\nThe first term of the AP is:- ",(((2*sums)/no_of_terms)-(no_of_terms*common_difference-(common_difference)))/2)

#this finds no of terms of the AP
def to_find_no_of_terms_for_sum_of_AP():
    global last_term_of_AP,first_term_of_AP,sums
    sums = int(input('enter the sum of the AP:- '))
    last_term_of_AP = int(input('enter the last term of the AP:- '))
    first_term_of_AP = int(input('enter the first term of the AP:- '))
    
def printing_the_answers_to_find_no_of_terms():
    global last_term_of_AP,first_term_of_AP,sums
    
    print ("the first term of the AP is:- ",first_term_of_AP)
    print ("\nThe sum of the required no of terms of AP Is:- ",sums)
            
    print ("\nThe Last term of the AP is:- ",last_term_of_AP)
            
    print("\nThe number of terms of AP is:- ",(sums*2)/(first_term_of_AP + last_term_of_AP))

def to_find_nth_term_of_gp():
    global first_term, difference, no_of_terms
    first_term = float(input('Enter the first term of the GP:- '))
    difference = float(input('Enter the difference of the GP:- '))
    no_of_terms = float(input('enter the no of the term which you want to find:- '))
    
def to_find_answer_of_nth_term_GP():
    global first_term, difference, no_of_terms
    print ("The first term of the GP is:- ",first_term)
    print ("\nThe difference between the terms is:- ",difference)        
    print ("\nThe number of term which you know is:- ",no_of_terms)
    print('\nThe',no_of_terms,'th term is:- ',(first_term)*(difference**(no_of_terms-1)))

def to_find_nth_term_of_gp_type2():
    global first_term, difference, no_of_terms, second_term
    first_term = float(input('Enter the first term of the GP:- '))
    second_term = float(input('Enter the second term of the GP:- '))
    no_of_terms = float(input('enter the no of the term which you want to find:- '))
    difference = second_term/first_term
def to_find_answer_of_nth_term_GP_type2():
    global first_term, difference, no_of_terms, second_term
    print ("The first term of the GP is:- ",first_term)
    print ("The second term of the GP is:- ",second_term)
    print ("\nThe difference between the terms is:- ",difference)        
    print ("\nThe number of term which you know is:- ",no_of_terms)
    print('\nThe',no_of_terms,'th term is:- ',(first_term)*(difference**(no_of_terms-1)))
    
def to_find_first_term_of_gp():
    global difference, no_of_terms, nth_term
    nth_term = float(input('Enter the term of the GP which you know:- '))
    difference = float(input('Enter the difference of the GP:- '))
    no_of_terms = float(input('enter the no of the term which you want to find:- '))
    
def to_find_answers_of_first_term_of_GP():
    global difference, no_of_terms, nth_term
    print ("The term which you know is- ",nth_term)
    print ("\nThe no of terms in Gp is:- ",no_of_terms)        
    print ("\nThe difference of the GP is:- ",difference)
    print('\nThe first term of the GP is',nth_term/(difference**(no_of_terms-1)))
    
    
def to_find_difference_of_gp():
    global first_term, no_of_terms, nth_term
    first_term = float(input('Enter the first term of the GP:- '))
    no_of_terms = float(input('Enter the number of terms of the GP'))
    nth_term = float(input('Enter the term which you know:- '))

def nthrootofm(a,n):
    return pow(a,(1/n))

def to_find_answers_to_find_differnce_of_GP():
    global first_term, no_of_terms, nth_term
    print ("The term which you know is- ",nth_term)
    print ("\nThe no of terms in Gp is:- ",no_of_terms)        
    print ("\nThe first term of the GP is:- ",first_term)
    print('\nThe difference of the GP is',nthrootofm((nth_term/first_term),(no_of_terms-1)))

def to_find_n_of_GP():
    global first_term, difference, nth_term
    first_term = float(input('Enter the first term of the GP:- '))
    difference = float(input('Enter the difference of the GP'))
    nth_term = float(input('Enter the term which you know:- '))

def finding_the_answer_of_n():
    print ("The term which you know is- ",nth_term)
    print ("\nThe difference in Gp is:- ",difference)        
    print ("\nThe first term of the GP is:- ",first_term)
    a=nthrootofm((nth_term/first_term),difference)
    print('\n', nth_term,'is',int(a+1),'term of GP')
    
def to_find_sum_of_GP_type1():
    global first_term, difference, no_of_terms
    first_term = float(input('Enter the first term of the GP:- '))
    difference = float(input('Enter the difference of the GP:- '))
    no_of_terms = float(input('enter the no of the term which you want to find:- '))
    
def to_find_answer_of_sum_of_GP_type1():
    global first_term, difference, no_of_terms
    print ("The first term of the GP is:- ",first_term)
    print ("\nThe difference between the terms is:- ",difference)        
    print ("\nThe number of terms:- ",no_of_terms)
    if difference > 1: 
        print('\nThe sum of the GP is:- ',(first_term)*((difference**no_of_terms)-1)/(difference-1))
    else:
        print('\nThe sum of the GP is:- ',(first_term)*(1-(difference**no_of_terms))/(1-difference))
        
        
def to_find_sum_of_GP_type2():
    global first_term, no_of_terms,second_term,difference
    first_term = float(input('Enter the first term of the GP:- '))
    second_term = float(input('Enter the second term of the GP:- '))
    difference = second_term/first_term
    no_of_terms = float(input('enter the no of the terms:- '))
    
def to_find_answer_of_sum_of_GP_type2():
    global first_term, difference, no_of_terms
    print ("The first term of the GP is:- ",first_term)
    print ("The second term of the GP is:- ",second_term)
    print ("\nThe difference between the terms is:- ",difference)        
    print ("\nThe number of terms:- ",no_of_terms)
    if difference > 1: 
        print('\nThe sum of the GP is:- ',(first_term)*((difference**no_of_terms)-1)/(difference-1))
    else:
        print('\nThe sum of the GP is:- ',(first_term)*(1-(difference**no_of_terms))/(1-difference))
        

def to_find_first_term_from_sum():
    global no_of_terms,sums,difference
    sums = float(input('Enter the sum of the GP:- '))
    difference = float(input('Enter the difference of the GP:- '))
    no_of_terms = float(input('enter the no of the terms:- '))
    
def to_find_answer_of_first_term_of_sum_of_gp():
    global no_of_terms,sums,difference
    print ("The sum of the GP is:- ",sums)
    print ("The difference of the GP is:- ",difference)  
    print ("\nThe number of terms:- ",no_of_terms)
    if difference > 1: 
        print('\nThe first term of the GP is:- ', (sums)*(difference-1)/((difference**no_of_terms)-1))
    else:
        print('\nThe first term of the GP is:- ',(sums)*(1-difference)/(1-(difference**no_of_terms)))
        
def to_find_n_of_sum_GP():
    global first_term,sums,difference
    sums = float(input('Enter the sum of the GP:- '))
    difference = float(input('Enter the difference of the GP:- '))
    first_term = float(input('enter the first term of the GP:- '))

def to_find_answer_of_n_of_sum_of_GP():
    global first_term,sums,difference
    print ("The sum of the GP is:- ",sums)
    print ("The difference of the GP is:- ",difference)  
    print ("\nThe first term of the GP is:- ",first_term)
    a = nthrootofm((((sums)*(difference-1))/first_term)+1,difference)
    print('\nThe number of terms in this GP is:- ', a)
