from Progressions_functions import *


def re_run():
    to_continue = str(input('\n \n Do you want to do it again? (for yes type(c) and for no type(q) [ANYTHING ELSE WOULD NOT BE ALLOWED!])'))
    if to_continue == 'c':
        run_main_program()
    if to_continue == 'q':
        exit()
    else:
        re_run()
def run_main_program():
    asking = str(input("\nDo you want sum of the terms of AP or want the nth term of the AP  or want to go to GP program.(for sum-(sum) and for nth term-(nth term) and for GP-(GP))"))
    if asking == 'GP':
        type_2 = input("\nEnter the type of function you want to do for sum type(sum) and for nth term type(nth term):- ")
        if type_2 == 'nth term':
            while True:
                to_find_2 = input('\nEnter what you wan to find [for first term type(a), for difference type(r), number of terms type(n), nth term type(nth)]')
                if to_find_2 == 'a':
                    to_find_first_term_of_gp()
                    to_find_answers_of_first_term_of_GP()
                    break
                if to_find_2 == 'r':
                    to_find_difference_of_gp()
                    to_find_answers_to_find_differnce_of_GP()
                    break
                if to_find_2 == 'n':
                    to_find_n_of_GP()
                    finding_the_answer_of_n()
                    break
                if to_find_2 == 'nth':
                    nth_1 = input('\n\nHow you want to find the nth term. 1)by entering a, r, no_of_terms(for this type(1)) 2)by entering first 2 terms and no of terms(for this type(2)):- ')
                    if nth_1 == '1':
                        to_find_nth_term_of_gp()
                        to_find_answer_of_nth_term_GP()
                        break
                    elif nth_1 == '2':
                        to_find_nth_term_of_gp_type2()
                        to_find_answer_of_nth_term_GP_type2()
                        break
                    else:
                        print('write in correct format')
                        run_main_program()
            re_run()
        elif type_2 == 'sum':
            while True:
                to_find_2 = input('Enter what you wan to find [for sum type(s), first term type(a), for difference type(r), number of terms type(n)]')
                if to_find_2 == 's':
                    sum_1 = input('\n\nHow you want to find the sum. 1)by entering a, r, no_of_terms(for this type(1)) 2)by entering first 2 terms and no of terms(for this type(2)):- ')
                    if sum_1 == '1':
                        to_find_sum_of_GP_type1()
                        to_find_answer_of_sum_of_GP_type1()
                        break
                    elif sum_1 == '2':
                        to_find_sum_of_GP_type2()
                        to_find_answer_of_sum_of_GP_type2()
                        break
                    else:
                        print('write in correct format')
                        run_main_program()
                if to_find_2 == 'a':
                    to_find_first_term_from_sum()
                    to_find_answer_of_first_term_of_sum_of_gp()
                    break
                if to_find_2 == 'r':
                    print('To find this a higher knowledge of python is required.\n SO really very sorry but will will not able to find this answer, check the further code of this program \n which is very interesting and useful\nUNDER DEVELOPMENT KEEP CHECKING......')
                if to_find_2 == 'n':
                    to_find_r_of_sum_GP()
                    to_find_answer_of_r_of_sum_of_GP()
                    break
            re_run()
                
    if asking == 'nth term':
                
        while True:
            
            if asking == 'nth term':
                to_find_1 = str(input("Enter what you want to find [for first term type(a) for common difference type(d) for nth term type(nt) and for number of terms type(n):- ]"))
                if to_find_1 == 'a':
                    to_find_a_for_AP()
                    printing_answers_to_find_a()
                    break
                if to_find_1 == 'd':
                    to_find_d_for_AP()
                    printing_answers_to_find_d_of_AP()
                    break
                if to_find_1 == 'n':
                    to_find_no_of_terms_of_AP()
                    printing_answer_to_find_no_of_terms_of_AP()
                    break
                if to_find_1 == 'nt':
                    arithematic_progression_nth_term()
                    printing_the_answers()
                    break
                elif to_find_1 != 'nt' or to_find_1 != 'n' or to_find_1 != 'd' or to_find_1 != 'd' or to_find_1 != 'a':
                    print("ERROR TRY AGAIN \n WRITE IN CORRECT FORMAT ")
                    continue
                
        re_run()
    if asking == 'sum':
        while True:
            if asking == 'sum':
                to_find = str(input("Enter what you want to find [for first term type(a) for common difference type(d) for sum type(s) and for number of term type(n):- ]"))
                if to_find == 'a':
                    to_find_a_for_sum_of_terms_of_AP()
                    printing_the_answers_to_find_a()
                    break
                if to_find == 'd':
                    to_find_d_for_sum_of_AP()
                    printing_answers_to_find_d()
                    break
                if to_find == 'n':
                    to_find_no_of_terms_for_sum_of_AP()
                    printing_the_answers_to_find_no_of_terms()
                    break
                
                if to_find == 's':
                    sum_of_terms_of_ap()
                    printing_the_answers_of_sum()
                    break
                    
                elif to_find != 's' or to_find != 'n' or to_find != 'd' or to_find != 'a':
                    print("ERROR TRY AGAIN \n WRITE IN CORRECT FORMAT")
                    continue

        re_run()
    if asking != 'sum' or asking != 'nth term':
        print("ERROR TRY AGAIN\n WRITE IN CORRECT FORMAT")
        run_main_program()
run_main_program()





        
                

