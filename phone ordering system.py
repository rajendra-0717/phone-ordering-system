class Phones():
    
    def init(self):
     print(" Which phone Do you want ")
     n=1
     while n<=3:
      n+=1
        
    def brands(self):
        a='Iphone'
        b='Samsung'
        print(a)
        print(b)
  
    def varient(self):
        v1='128gb & 6gb'
        v2='256gb & 8gb'        
        v3='512gb & 12gb'
        print(v1)
        print(v2)
        print(v3)

    def color(self):
        c1='white'
        c2='red'
        c3='black'
    
        print(c1)
        print(c2)
        print(c3)

    def accessories(self):
        a1='charger'
        a2='earbuds'
        print(a1)
        print(a2)
     
class Iphone():

    def imodel(self):
       m1='Iphone13'
       m2='Iphone14'
       m3='Iphone15'
       print(m1)
       print(m2)
       print(m3)
    


class Samsung():

    def smodel(self):
        sm1='samsung s21'
        sm2='samsung s22'
        sm3='samsung s23'
        print(sm1)
        print(sm2)
        print(sm3)


class Final(Iphone,Samsung):
      def min(self):
        print("Do you want a phone")
      def call(self,d1,d2,d3,c1,c2,c3,b1,b2,b3,ps1,ps2,ps3,o1,o2,o3,pi1,pi2,pi3,ds1,ds2,ds3,cs1,cs2,cs3,bs1,bs2,bs3,p1,p2,p3,pr1,pr2,pr3,os1,os2,os3):
       n=1
       while n<=3:
        n+=1
        value=input("yes or no:-")
        ans=value.lower()
        print(ans)
        
        if ans=='yes' or (ans)=='1':
          Phones.init(self)
          Phones.brands(self)
          
          n=1
          while n<=3:
            n+=1
            value2=input("Select a phone  you want:-")
            ans1=value2.lower()
            if ans1=='iphone' or (ans1)=='1' :
              print(f"models for {ans1} are:-")
              Iphone.imodel(self)
              n=1
              while n<=3:
               n+=1
               ans2=input("Enter which model you want:-")
               print(ans2)
               if ans2=='Iphone13' or ans2=='13'  or ans2=='Iphone14' or ans2=='14' or ans2=='Iphone15' or ans2=='15':
                  print(f"The Varients for {ans2}  are:-")
                  Phones.varient(self)
                  n=1
                  while n<=3:
                   n+=1
                   ans3=input("Enter which varient do you want:-")
                   if ans3=='128gb & 6gb' or (ans3)=='1' or ans3=='256gb & 8gb' or (ans3)=='2' or ans3=='512gb & 12gb' or (ans3)=='3':
                    print(f"The colours for {ans2} are:-")
                    Phones.color(self)
                    n=1
                    while n<=3:
                     n+=1
                     value4=input("Enter which color do you want:-")
                     ans4=value4.lower()
                     if ans4=='white' or (ans4)=='1' or ans4=='red' or (ans4)=='1' or ans4=='black' or (ans4)=='3':
                       print(f"The display for {ans2} is:-") 
                       if ans2=='Iphone13'or (ans2)==13:
                        print(d1)
                        print(f'The camera for {ans2}:- {c1}')
                        print(f'the processor for {ans2}:- {pi1}')
                        print(f'The battery capacity for {ans2}:- {b1}')
                        print(f'The os {ans2}:- {o1}')
                        print('The Acessories in box are:- charger and earphones')
                        print(f'The price for  {ans2}:- {p1}')
                        return

                       elif ans2=='Iphone14' or (ans2)=='14': 
                        print(d2)
                        print(f'The camera for {ans2}:- {c2}')
                        print(f'the processor for {ans2}:- {pi2}')
                        print(f'The battery capacity for {ans2}:- {b1}')
                        print(f'The os {ans2}:- {o2}')
                        print('The Acessories in box are:- charger and earphones')
                        print(f'The price for {ans2}:- {p2}')
                        return

                       elif ans2=='Iphone15' or (ans2)=='15':
                        print(d3)
                        print(f'The camera for {ans2}:- {c3}')
                        print(f'the processor for {ans2}:- {pi3}')
                        print(f'The battery capacity for {ans2}:- {b3}')
                        print(f'The os {ans2}:- {o3}')
                        print('The Acessories in box are:- charger and earphones')
                        print(f'The price for {ans2}:- {p3}')

                       else:
                          print("Nope this not available !!!!")
                          print("Please select available one")
                     else:
                       print("Nope this not available !!!!")
                       print("Please select available one")
                   else: 
                     print("Nope this not available !!!!")
                     print("Please select available one")   
               else:
                print("Nope this not available !!!!")
                print("Please select available one")
            
            elif ans1=='samsung' or (ans1)=='2' : 
              print(f"models {ans1} are:-")
              Samsung.smodel(self)
              n=1
              while n<=3:
               n+=1
               ans2=input("Enter which model you want:-")
               if ans2=='samsung 21'or (ans2)=='21' or ans2=='samsung s22' or (ans2)=='22' or ans2=='samsung s23' or (ans2)=='23':
                  print(f"The Varients for {ans2}  are:-")
                  Phones.varient(self)
                  n=1
                  while n<=3:
                   n+=1
                   ans3=input("Enter which varient do you want:-")
                   if ans3=='128gb & 6gb' or (ans3)==1 or ans3=='256gb & 8gb' or (ans3)==2 or ans3=='512gb & 12gb' or (ans3)==3:
                      print(f"The colours for {ans2} are:-")
                      Phones.color(self)
                      n=1
                      while n<=3:
                       n+=1
                       ans4=input("Enter which color do you want:-")
                       if ans4=='white' or (ans4)=='1' or ans4=='red' or (ans4)=='2' or ans4=='black' or (ans4)=='3':
                        print(f"The display for {ans2} is:-")
                        if ans2=='samsung 21'or (ans2)=='21':
                          print(ds1)
                          print(f'The camera for {ans2}:- {cs1}')
                          print(f'the processor for {ans2}:- {ps1}')
                          print(f'The battery capacity for {ans2}:- {bs1}')
                          print(f'The os {ans2}:- {os1}')
                          print('The Acessories in box are:- charger and earphones')
                          print(f'The price for  {ans2}:- {pr1}')
                          return
                        elif ans2=='samsung 22' or (ans2)=='22': 
                          print(ds2)
                          print(f'The camera for {ans2}:- {cs2}')
                          print(f'the processor for {ans2}:- {ps2}')
                          print(f'The battery capacity for {ans2}:- {bs1}')
                          print(f'The os {ans2}:- {o2}')
                          print('The Acessories in box are:- charger and earphones')
                          print(f'The price for {ans2}:- {pr2}')
                          return 
                        elif ans2=='samsung 23' or (ans2)=='23':
                          print(ds3)
                          print(f'The camera for {ans2}:- {c3}')
                          print(f'the processor for {ans2}:- {ps3}')
                          print(f'The battery capacity for {ans2}:- {b3}')
                          print(f'The os for {ans2}:- {os3}')
                          print('The Acessories in box are:- charger and earphones')
                          print(f'The price for {ans2}:- {pr3}')

                        else:
                          print("Nope this not available !!!!")
                          print("Please select available one")
                       else:
                          print("Nope this not available !!!!")
                          print("Please select available one")
                   else: 
                     print("Nope this not available !!!!")
                     print("Please select available one")  
               else:
                print("Nope this not available !!!!")
                print("Please select available one")
            else:
               print("Nope this not available !!!!")
               print("Please select available one")
          
        elif ans=='no' or (ans)=='2':
            print("thank you visit again !!")
            if n==2:
             print("Two chance Left")
            elif n==3: 
              print("one chance Left")
            else:
              print("GO to assam!!!")

        else:
            if n==2:
             print("Two chance Left")
            elif n==3: 
              print("one chance Left")
            else:
              print("GO to assam!!!")
            # print("go to assam")
              

f1=Final()
f1.min()
f1.call(d1='oled',d2='Super Retina XDR display',d3='Super Retina XDR OLED display',c1='dual 12 mp',c2='48-megapixel sensor with an f/1.78 len',c3='48-megapixel image sensor, ƒ/1.6 aperture',
pi1='A15 Bionic chip',pi2='A13 Bionic chip',pi3='A16 Bionic chip',b1='4383mAh',b2= '4352mAh',b3= '4323mAh',o1='os7',o2='os8',o3='os9', p1='69,000/-' ,p2='80,000/-' ,p3='100,000/-',ds1='oled',ds2='Super Retina XDR display',ds3='Super Retina XDR OLED display',
cs1='64MP sensor',cs2='50MP sensor ',cs3='Samsung S5KGN3 1/1.57" sensor with 1.0µm pixels and a Tetracellfilter',ps1='Exynos 8 octa',ps2='Exynos 7 quad',ps3='Exynos 8 quad',bs1='4800mAh',bs2= '4352mAh',bs3= '4323mAh',os1='7.O Nougat',os2='8.O Oreo',os3='9.O pie',pr1='59,000/-',pr2='70,000/-',pr3='90,000)/-')
# f1.display(d1='oled',d2='Super Retina XDR display',sm1='samsung s21',sm2='samsung s22')