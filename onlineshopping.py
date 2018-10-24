from easygui import *
import sys
while 1:
    msgbox("Hello, coustomer!")
    msg ="from which site do you want to purchase?"
    title = "shopping"
    choices = ["amazon", "flipkart"]
    choice = choicebox(msg, title, choices)
   # msgbox("You chose: " + str(choice), "Survey Result")
    if choice=="amazon":
        msg1 ="choose your preferrance"
        title1 = "shopping"
        choices1 = ["electronics","toys"]
        choice1 = choicebox(msg, title1, choices1)
       # msgbox("You chose: " + str(choice1), "Survey Result")
        if choice1=="electronics":
            msg ="choose your preferrance"
            title2 = "shopping"
            choices2 = ["mobiles","tv"]
            choice2 = choicebox(msg, title2, choices2)
           # msgbox("You chose: " + str(choice2), "Survey Result")
            if choice2=="mobiles":
                msg ="choose your preferrance"
                title3 = "shopping"
                choices3 = ["samsung"]
                choice3 = choicebox(msg, title3, choices3)
               # msgbox("You chose: " + str(choice3), "Survey Result")
                if choice3=="samsung":
                    msg ="choose your preferrance"
                    title4 = "shopping"
                    choices4 = ["j6"]
                    choice4 = choicebox(msg, title4, choices4)
                   # msgbox("You chose: " + str(choice4), "Survey Result")
                    if choice4=="j6":
                        msg ="choose your preferrance"
                        title5 = "shopping"
                        choices5 = ["N ELEC", "A ELEC"]
                        choice5 = choicebox(msg, title5, choices5)
                       # msgbox("You chose: " + str(choice5), "Survey Result")
                        if choice5=="N ELEC":
                           msgbox("You chose: " +str(choice5), "Rs.17000")
                        else:                  
                           msgbox("You chose: " +str(choice5), "Rs.17500")
           
            else:
                msg ="choose your preferrance"
                title8 = "shopping"
                choices8 = ["onida","LG"]
                choice8 = choicebox(msg, title8, choices8)
               # msgbox("You chose: " + str(choice8), "Survey Result")
                if choice8=="onida":
                     msg ="choose your preferrance"
                     title9 = "shopping"
                     choices9 = ["E tv","F tv"]
                     choice9 = choicebox(msg, title9, choices9)
                    # msgbox("You chose: " + str(choice9), "Survey Result")
                else:
                   if choice9=="E tv":
                      msgbox("You chose: " + str(choice9), "Rs.91500")
                   else:
                      msgbox("You chose: "+str(choice9), "Rs.71200")
        else:
            msg ="choose your preferrance"
            title6 = "shopping"
            choices6 = ["bike","robot"]
            choice6 = choicebox(msg, title6, choices6)
           # msgbox("You chose: " + str(choice6), "Survey Result")
            if choice6=="bike":
                msg ="choose your preferrance"
                title7 = "shopping"
                choices7 = ["C TOYS","D TOYS"]
                choice7 = choicebox(msg, title7, choices7)
               # msgbox("You chose: " + str(choice7), "Survey Result")
                if choice7=="C TOYS":
                      msgbox("You chose: " + str(choice7), "Rs.500")
                else:
                      msgbox("You chose: "+ str(choice7), "Rs.700")
            else:
                if choice7=="C TOYS":
                      msgbox("You chose: " + str(choice7), "Rs.1500")
                else:
                      msgbox("You chose: "+ str(choice7), "Rs.1200")
    elif choice=="flipkart":
        msg1 ="choose your preferrance"
        title1 = "shopping"
        choices1 = ["electronics","toys"]
        choice1 = choicebox(msg, title1, choices1)
       # msgbox("You chose: " + str(choice1), "Survey Result")
        if choice1=="electronics":
            msg ="choose your preferrance"
            title2 = "shopping"
            choices2 = ["mobiles","tv"]
            choice2 = choicebox(msg, title2, choices2)
           # msgbox("You chose: " + str(choice2), "Survey Result")
            if choice2=="mobiles":
                msg ="choose your preferrance"
                title3 = "shopping"
                choices3 = ["samsung"]
                choice3 = choicebox(msg, title3, choices3)
               # msgbox("You chose: " + str(choice3), "Survey Result")
                if choice3=="samsung":
                    msg ="choose your preferrance"
                    title4 = "shopping"
                    choices4 = ["j6"]
                    choice4 = choicebox(msg, title4, choices4)
                   # msgbox("You chose: " + str(choice4), "Survey Result")
                    if choice4=="j6":
                        msg ="choose your preferrance"
                        title5 = "shopping"
                        choices5 = ["N ELEC", "A ELEC"]
                        choice5 = choicebox(msg, title5, choices5)
                       # msgbox("You chose: " + str(choice5), "Survey Result")
                        if choice5=="N ELEC":
                           msgbox("You chose: " +str(choice5), "Rs.17000")
                        else:
                           msgbox("You chose: " +str(choice5), "Rs.17500")

            else:
                msg ="choose your preferrance"
                title8 = "shopping"
                choices8 = ["onida","LG"]
                choice8 = choicebox(msg, title8, choices8)
               # msgbox("You chose: " + str(choice8), "Survey Result")
                if choice8=="onida":
                     msg ="choose your preferrance"
                     title9 = "shopping"
                     choices9 = ["E tv","F tv"]
                     choice9 = choicebox(msg, title9, choices9)
                    # msgbox("You chose: " + str(choice9), "Survey Result")
                else:
                   if choice9=="E tv":
                      msgbox("You chose: " + str(choice9), "Rs.91500")
                   else:
                      msgbox("You chose: "+str(choice9), "Rs.71200")

        else:
            msg ="choose your preferrance"
            title6 = "shopping"
            choices6 = ["bike","robot"]
            choice6 = choicebox(msg, title6, choices6)
           # msgbox("You chose: " + str(choice7), "Survey Result")
            if choice6=="bike":
                msg ="choose your preferrance"
                title7 = "shopping"
                choices7 = ["C TOYS","D TOYS"]
                choice7 = choicebox(msg, title7, choices7)
               # msgbox("You chose: " + str(choice7), "Survey Result")
                if choice7=="C TOYS":
                      msgbox("You chose: " + str(choice7), "Rs.500")
                else:
                      msgbox("You chose: "+str(choice7), "Rs.700")
            else:
                msg ="choose your preferrance"
                title7 = "shopping"
                choices7 = ["C robot","D robot"]
                choice7 = choicebox(msg, title7, choices7)
                if choice7=="C TOYS":
                      msgbox("You chose: " + str(choice7), "Rs.1500")
                else:
                      msgbox("You chose: "+str(choice7), "Rs.1200")
if ccbox(msg, title):     # show a Continue/Cancel dialog
        pass  # user chose Continue
else:
        sys.exit(0)