from easygui import *
from Tkinter import *
import Tkinter as tk
import sys

z=ccbox("\t\t\n WELCOME TO HOUSEBOX99 \n\n\t\tthe place to find you an ideal home","HOUSEBOX99")

while 1:
    image="E:\phone1.png"
    msg="Hello!In which area would you like to search for your ideal home"
    title="HOUSEBOX99"
    choice=("Hadapsar(magarpatta city)","Kothrud" , "Chinchwad" , "Kondhwa")
    box=buttonbox(msg,title,choice)
    if box==str("Hadapsar(magarpatta city)"):
        msg1="What type of house would you like to choose"
        title="Housebox99"
        choice1=("Flats","Villa","Rowhouses")
        box1=buttonbox(msg1,title,choice1)
        if box1==str("Flats"):
            msg11=("How big do you want your flat to be?")
            title="Housebox99"
            choice11=("1BHK","2BHK","3+BHK")
            box11=buttonbox(msg11,title,choice11)
            if box11==str("1BHK"):
                msg111="Here are some 1BHK available flats for you"
                title="Housebox99"
                choice111=("One North appartments","Zinnia Appartments","Bhandari Greenfield Society")
                box111=buttonbox(msg111,title,choice111)
                if box111==str("One North appartments"):
                    msg1111=("Area=650 sqft\n\n\n Price starting from 56 Lac\n\n\nContact Person:\n\nSrushti Gosavi- 8756483985 ")
                    tit1e1="Features"
                    box1111=msgbox(msg1111,tit1e1)
                if box111==str("Bhandari Greenfield Society"):
                    msg1111=("Area=747 sqft\n\n\n Price starting from 41.5 Lac\n\n\nContact Person:\n\n Saumitra Bhandari-9876786782 ")
                    tit1e1="Features"
                    box1111=msgbox(msg1111,tit1e1)
                if box111==str("Zinnia Appartments"):
                    msg1111=("Area=658 sqft\n\n\n Price starting from 45 Lac\n\n\nContact Person:\n\n Ishaan Borulkar-7645375637 ")
                    tit1e1="Features"
                    box1111=msgbox(msg1111,tit1e1)
            if box11==str("2BHK"):
                msg112="Here are some available 2BHK flats for you"
                title="Housebox99"
                choice112=("Marvel Azure, Magarpatta","Magarpatta city Jasminium")
                box112=buttonbox(msg112,title,choice112)
                if box112==str("Marvel Azure, Magarpatta"):
                    msg1111=("Area=1265 sqft\n Price starting from 94 Lac\n \n\nContact Person:\n\n Jinshel George-9878765423")
                    tit1e1="Features"
                    box1111=msgbox(msg1111,tit1e1)
                if box112==str("Magarpatta city Jasminium"):
                    msg1111=("Area=1175 sqft\n\n\n Price starting from 84 Lac\n \n\nContact Person:\n\n Divya Sethi-7865456541")
                    tit1e1="Features"
                    box1111=msgbox(msg1111,tit1e1)      
            if box11==str("3+BHK"):
                msg113="Here are some available 3+BHK flats for you"
                title="Housebox99"
                choice113=("One North","Magarpatta Gravilen")
                box113=buttonbox(msg113,title,choice113)
                if box113==str("One North"):
                    msg1111=("Area=3850 sqft\n\n\n Price starting from 3.3Cr Lac\n \n\nContact Person:\n\n Zeeshant Aman-7656788654")
                    tit1e1="Features"
                    box1111=msgbox(msg1111,tit1e1)
                if box113==str("Magarpatta Gravilen"):
                    msg1111=("Area=1400 sqft\n\n\n Price starting from 1.1 Cr\n \n\nContact Person:\n\n Isha Pathak- 9878332443")
                    tit1e1="Features"
                    box1111=msgbox(msg1111,tit1e1)   
        if box1==str("Villa"): 
            msg12="Here are some villa available for you"
            choice12=("Avenue","Marvel Diva")
            box12=buttonbox(msg12,title,choice12)
            if box12==str("Avenue"):
                    msg1111=("Area=1400 sqft\n\n\n Price starting from 1.1 Cr\n\n\nContact Person:\n\n Marshall Wayne- +8766353621 ")
                    tit1e1="Features"
                    box1111=msgbox(msg1111,tit1e1)   
            if box12==str("Marvel Diva"):
                    msg1111=("Area=1400 sqft\n\n\n Price starting from 1.1 Cr\n \n\nContact Person:\n\n\ Ayesha Singh- 8797677666")
                    tit1e1="Features" 
                    box1111=msgbox(msg1111,tit1e1)
        if box1==str("Rowhouses"):
            msg13="Here are some rowhouses available for you"
            choice13=("Konark Bella Vista",)
            box13=buttonbox(msg,title,choice13)
            if box13==str("Konark Bella Vista"):
                msgbox(msg)
    if box==str("Kothrud"):
        msg2="What type of house would you like to choose"
        title="Housebox99"
        choice2=("Flats","Villa","Rowhouses","studio")
        box2=buttonbox(msg2,title,choice2)
        if box2==str("Flats"):
            msg21="How big do you want your flat to be"
            choice21=("1BHK","2BHK","3+BHK")
            box21=buttonbox(msg21,title,choice21)
            if box21==str("1BHK"):
                msg211="Here are some 1BHK flats available for you"
                choice211=("Madhuban Apartment","Gujrat Colony")
                box211=buttonbox(msg211,title,choice211)
                if box211==str("Madhuban Apartment"):
                    msg2111=("Area=683 sqft\n\n\n Price starting from 58 lac\n\n\nContact Person:\n\n Ashutosh Jadhav- 7654738984 ")
                    tit1e2="Features"
                    box1111=msgbox(msg2111,tit1e2)   
                if box211==str("Gujrat Colony"):
                    msg211=("Area=615 sqft\n\n\n Price starting from 50 lac\n \n\nContact Person:\n\n\ Vineet Kothari- 8746374363")
                    tit1e3="Features"
                    box1111=msgbox(msg211,tit1e3)   
            if box21==str("2BHK"):
                msg212="Here are some 2BHK flats available for you"
                choice212=("Madhuban Apartment","Gangotri Suhrud")
                box212=buttonbox(msg212,title,choice212)
                if box212==str("Madhuban Apartment"):
                    msg2121=("area=1200 sqft\n \n\nPrice starting from 95 lac\n \n\nContact Person: \n\n Ashutosh Jadhav- 7654738984")
                    tit1e3="Features"
                    box2121=msgbox(msg2121,tit1e3)
                if box212==str("Gangotri Suhrud"):
                    msg2122=("Area=1073-1290 sqft\n\n\n Price starting from 1.93-2.32 lac\n \n\nContact Person:\n\n Ninad Khan- 9878765445")
                    tit1e3="Features"
                    box2122=msgbox(msg2122,tit1e3)
            if box21==str("3+BHK"):
                msg213="Here are some 3BHK flats available for you"
                choice213=("Gangotri Suhrud","Bhagyashree Apartment" )
                box213=buttonbox(msg213,title,choice213)
                if box213==str("Gangotri Suhrud"):
                    msg2131=("Area=3654 sq ft \n\n\nPrices starting from 2.9 Cr \n\nContact Person:\n\n Soham Deshpande-9878654665")
                    title="Features"
                    box2131=msgbox(msg2131,title)
                if box213==str("Bhagyashree Apartment"):
                    msg2132=("Area=3724 sq ft \n\n\nPrices starting from 3.1 Cr \n\nContact Person:\n\n Rajaram Shinde- 8767997655")
                    title="Features"
                    box2132=msgbox(msg2132,title)    
        if box2==str("Villa"):
            msg22="Here are some villa available"
            choice22=("GPC","Amrut Runwal paradise")
            box22=buttonbox(msg22,title,choice22)
            if box22==str("GPC"):
                msg221=("Area=3600 \n\n\nPrices starting from 3.8 Cr.\n\nContact Person:\n\n Vaibhavi Rajput- 8796756476")
                title="Features"
                box221=msgbox(msg221,title)
            if box22==str("Amrut Runwal paradise"):
                msg222=("Area=2500 \n\n\nPrices starting from 1.56 Cr.\n\nContact Person:\n\n Vaibhavi Rajput-8796756476")
                title="Features"
                box221=msgbox(msg222,title)
        if box2==str("Rowhouses"):
            msg23="Here are some rowhouses available"
            choice23=("Tirupati Executive",)
            box23=buttonbox(msg23,title,choice23)
            if box23==str("Tirupati Executive"):
                msg231=("Area=1300sq.ft \n\n\nPrices starting from 1.5 Cr\n\nContact Person:\n\n Pranjal Dhawan- 8799997769.")
                title="Features"
                box221=msgbox(msg231,title)
        if box2==str("studio"):
            msg24="Here are some studio available for you"
            title="HOUSEBOX99"
            choice24=("Nirman Terraces",)
            box24=buttonbox(msg24,title,choice24)     
            if box24==str("Nirman Terraces"):
                msg241=("Area=240 \n\n\nPrices starting from 23 lakh\n\nContact Person:\n\n Rebecca Ferguson-9878765588.")
                title="Features"
                box221=msgbox(msg241,title)
    if box==str("Chinchwad"):
        msg3="What type of house would you like to choose"
        title="Housebox99"
        choice3=("Flats","Villa")
        box3=buttonbox(msg3,title,choice3)
        if box3==str("Flats"):
            msg31="How big do you want your flat to be"
            choice31=("1BHK","2BHK","3BHK")
            box31=buttonbox(msg31,title,choice31)
            if box31==str("1BHK"):
                msg311="Here are some 1BHK flats available for you"
                choice311=("Swiss Countey","Padumjee Greens")
                box311=buttonbox(msg311,title,choice311)
                if box311==str("Swiss Countey"):
                    msg3111=("Area=650 \n\n\nPrices starting from 43 lakh\n\nContact Person:\n\n Sasha Kapoor- 8799876655 ")
                    title="Features"
                    box3111=msgbox(msg3111,title)
                if box311==str("Padumjee Greens"):
                    msg3112=("Area=1605 \n\n\nPrices starting from 1.18 Cr\n\nContact Person:\n\n Raju Rastogi- 7673737873.")
                    title="Features"
                    box3112=msgbox(msg3112,title)
            if box31==str("2BHK"):
                msg312="Here are some 2BHK flats available for you"
                title="HOUSEBOX99"
                choice312=("Empire Square","Kunal Iconia")
                box312=buttonbox(msg312,title,choice312)
                if box312==str("Empire Square"):
                    msg3121=("Area=1192 \n\n\nPrices starting from 92 lakh\n\nContact Person:\n\n Kabir Thapar-8987788776.")
                    title="Features"
                    box3121=msgbox(msg3121,title)
                if box312==str("Kunal Iconia"):
                    msg3122=("Area=1132 \n\n\nPrices starting from 49 lakh\n\nContact Person:\n\n Aron Cooper- +6876657766")
                    title="Features"
                    box3122=msgbox(msg3122,title)
            if box31==str("3BHK"):
                msg313="Here are some 3BHK flats available for you"
                choice313=("Padumjee Greens",)
                box313=buttonbox(msg313,title,choice313)
                if box313==str("Padumjee Greens"):
                    msg3131=("Area=1605 \n\n\nPrices starting from 1.18 Cr\n\nContact Person:\n\n Vaani Singh- 8799776656.")
                    title="Features"
                    box3131=msgbox(msg3131,title)
        if box3==str("Villa"):
            msg32="Here are some Villa available"
            choice32=("Tarangan",)
            box32=buttonbox(msg32,title,choice32)
            if box32==str("Tarangan"):
                msg321=("Area=3000 \n\n\nPrices starting from 1.2Cr\n\nContact Person:\n\n Sameer Fuddi- 9876585745.")
                title="Features"
                box321=msgbox(msg321,title)
    if box==str("Kondhwa"):
        msg4="What type of house would you like to choose"
        title="Housebox99"
        choice4=("Flats","Villa")
        box4=buttonbox(msg4,title,choice4)
        if box4==str("Flats"):
            msg41="How big do you want your flat to be"
            choice41=("1BHK","2BHK")
            box41=buttonbox(msg41,title,choice41)
            if box41==str("1BHK"):
                msg411="Here are some 1BHK flats available for you"
                choice411=("Rajgruhi Residence","Sasha")
                box411=buttonbox(msg411,title,choice411)
                if box411==str("Rajgruhi Residence"):
                    msg4111=("Area=670 \n\n\nPrices starting from 31 lakh\n\nContact Person:\n\n Titu Mama- 9878746433.")
                    title="Features"
                    box4111=msgbox(msg4111,title)
                if box411==str("Sasha"):
                    msg4112=("Area=695 \n\n\nPrices starting from 31 lakh\n\nContact Person:\n\n Aakash Mehta- 9876788876.")
                    title="Features"
                    box4112=msgbox(msg4112,title)    
            if box41==str("2BHK"):
                msg412="Here are some 2BHK flats available for you"
                choice412=("Rajgruhi","Sasha bellisiom")
                box412=buttonbox(msg412,title,choice412)
                if box412==str("Rajgruhi"):
                    msg4121=("Area=1020 \n\n\nPrices starting from  42 lakh\n\nContact Person:\n\n Rimmy Agrawal-8788765676.")
                    title="Features"
                    box4121=msgbox(msg4121,title)
                if box412==str("Sasha Bellisiom"):
                    msg4122=("Area=1125 \n\n\nPrices starting from 43.5 lakh\n\nContact Person:\n\n Prakash Mehra- 987878666.")
                    title="Features"
                    box4122=msgbox(msg4122,title)
        if box4==str("Villa"):
            msg42="Here are some Villa available"
            choice42=("Ashirwad",)
            box32=buttonbox(msg42,title,choice42)
            if box32==str("Ashirwad"):
                msg321=("Area=3000 \n\n\nPrices starting from 4 Cr\n\nContact Person:\n\n Siddhi Johar- 9878655544.")
                title="Features"
                box321=msgbox(msg321,title)
                
    else:
     sys.exit()               
            