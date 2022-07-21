def arithmetic_arranger(v_lista,v_ok=False):
  lista=v_lista
  v_numerador=[]
  v_operador=[]
  v_denominador=[]

  v_final1=""
  v_final2="" 
  v_final3=""
  v_resultado=""
  v_espacio=" "
  c_error_operador =0
  c_error_len=0
  c_error_isnumeric=0
  v_error=""

  for num in v_lista:
    v_temp=num.split()
    v_numerador.append(v_temp[0])
    v_operador.append(v_temp[1])
    v_denominador.append(v_temp[2])

  for i in range(len(v_numerador)):

    if v_operador[i]=="/" and v_operador[i]=="*":
      c_error_operador += 2
     
      continue
    elif v_operador[i]=="/" or v_operador[i]=="*":
      c_error_operador += 1
   
      continue

    
    if len(v_numerador[i])>4 and len(v_denominador[i])>4 :
    
      c_error_len +=2
      continue
    elif len(v_numerador[i])>4 or len(v_denominador[i])>4 :
     
      c_error_len +=1
      continue


    if v_numerador[i].isnumeric() == False and v_denominador[i].isnumeric() == False:
     
      c_error_isnumeric +=2
      continue
    elif v_numerador[i].isnumeric() == False or v_denominador[i].isnumeric() == False:
     
      c_error_isnumeric +=1
      continue

    if len(v_numerador[i])>len(v_denominador[i]):
      
        v_final1 = v_final1 + "  " + v_numerador[i] + "    "
        v_cantidad=len(v_numerador[i])-len(v_denominador[i]) + 1
        v_final2 = v_final2 + v_operador[i]  +v_cantidad * v_espacio + v_denominador[i] + "    "
        v_final3 = v_final3 + (len(v_numerador[i]) + 2) * "-" + "    "
        
        if v_ok == True:
         
          if v_operador[i] == "+":
            
            if len(str(int(v_numerador[i]) + int(v_denominador[i]))) > len(v_numerador[i]):
              v_resultado = v_resultado +" " +str(int(v_numerador[i]) + int(v_denominador[i]))+"    "
            else:
              v_cantidad = len(v_numerador[i])-len(v_denominador[i])+1 
              v_resultado = v_resultado + v_cantidad * " "+str(int(v_numerador[i]) + int(v_denominador[i]))+"    "

          elif v_operador[i] == "-":
              v_resultado = v_resultado + 2 * " "+str(int(v_numerador[i]) - int(v_denominador[i]))+"    "

          else:
            c_error += 1

    elif len(v_numerador[i]) == len(v_denominador[i]):
        
        v_final1 = v_final1 + "  " + v_numerador[i] + "    "
        v_cantidad=len(v_numerador[i])-len(v_denominador[i]) + 1
        v_final2 = v_final2 + v_operador[i]  + v_espacio + v_denominador[i] + "    "
        v_final3 = v_final3 + (len(v_numerador[i]) + 2) * "-" + "    "

        if v_ok == True:
         
          if v_operador[i] == "+":
            
            if len(str(int(v_numerador[i]) + int(v_denominador[i]))) > len(v_numerador[i]):
              v_resultado = v_resultado +" "+ str(int(v_numerador[i]) + int(v_denominador[i]))+"    "
            else:
              v_resultado = v_resultado + 2 * " "+str(int(v_numerador[i]) + int(v_denominador[i]))+"    "

          elif v_operador[i] == "-":
            if len(str(int(v_numerador[i]) - int(v_denominador[i]))) >= len(v_numerador[i]):
              v_resultado = v_resultado + str(int(v_numerador[i]) - int(v_denominador[i]))+"    "
            else:
              v_cantidad = len(v_numerador[i]) +1 
              v_resultado = v_resultado + v_cantidad * " "+str(int(v_numerador[i]) - int(v_denominador[i]))+"    "

    elif len(v_numerador[i])<len(v_denominador[i]):
        v_cantidad=len(v_denominador[i])-len(v_numerador[i]) + 2
        v_final1 = v_final1 + v_cantidad * v_espacio + v_numerador[i] + "    "
        v_final2 = v_final2 + v_operador[i] + " " + v_denominador[i] + "    "
        v_final3 = v_final3 + (len(v_denominador[i])+2) * "-" + "    "
    
        if v_ok == True:
         
          if v_operador[i] == "+":

            if len(str(int(v_numerador[i]) + int(v_denominador[i]))) >= len(v_denominador[i]):
           
              v_resultado = v_resultado +(len(str(int(v_numerador[i]) + int(v_denominador[i])))-len(str(int(v_numerador[i]) + int(v_denominador[i])))+2)*" " + str(int(v_numerador[i]) + int(v_denominador[i]))+"    "

            else:
              v_cantidad = int(v_numerador[i]) + int(v_denominador[i])
              v_resultado = v_resultado + v_cantidad * " "+str(int(v_numerador[i]) + int(v_denominador[i]))+"    "

          elif v_operador[i] == "-":
                       
              v_resultado = v_resultado + 2 * " "+str(int(v_numerador[i]) - int(v_denominador[i]))+"    "

          else:
            c_error += 1

  if c_error_operador+c_error_isnumeric+ c_error_len >= 5:
    print("Error: Too many problems.")
  elif c_error_operador > 0:
     print("Error: Operator must be '+' or '-'.")
  elif c_error_isnumeric > 0:
     print("Error: Numbers must only contain digits.")
  elif c_error_len > 0:
     print("Error: Numbers cannot be more than four digits.")
  else:
    print(v_final1)
    print(v_final2)
    print(v_final3)
    print(v_resultado)
